import os
import re

# -------------------------------
# Utility Functions
# -------------------------------

def sanitize_name(raw_name: str) -> str:
    """
    Replace spaces with underscores and remove invalid characters.
    Keeps naming filesystem-safe and consistent.
    """
    cleaned = re.sub(r'[^\w\s\-]', '', raw_name)   # remove special characters
    return cleaned.strip().replace(" ", "_")


def create_markdown_file(file_path: str):
    """
    Create an empty markdown file if it does not exist.
    """
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(f"# {os.path.basename(file_path).replace('_', ' ').replace('.md','')}\n")


# -------------------------------
# Core Tree Creation Logic
# -------------------------------

def process_unit(unit_path: str, topics: list):
    """
    Process a unit and create topic/subtopic structure.
    
    Rule:
    - If ANY topic has subtopics → all topics become folders
    - Else → topics become markdown files directly
    """
    
    # Check if any topic has subtopics
    has_subtopics = any(isinstance(topic[1], list) and topic[1] for topic in topics)

    for topic_index, (topic_name, subtopics) in enumerate(topics, start=1):
        topic_prefix = f"{topic_index:02d}_"
        topic_clean = topic_prefix + sanitize_name(topic_name)

        if has_subtopics:
            # Create topic folder
            topic_folder_path = os.path.join(unit_path, topic_clean)
            os.makedirs(topic_folder_path, exist_ok=True)

            # If topic has subtopics → create them
            if isinstance(subtopics, list) and subtopics:
                for sub_index, subtopic in enumerate(subtopics, start=1):
                    sub_prefix = f"{sub_index:02d}_"
                    sub_clean = sub_prefix + sanitize_name(subtopic) + ".md"
                    sub_path = os.path.join(topic_folder_path, sub_clean)
                    create_markdown_file(sub_path)
            else:
                # No subtopics → create topic.md inside folder
                topic_md_path = os.path.join(topic_folder_path, f"{topic_clean}.md")
                create_markdown_file(topic_md_path)

        else:
            # No subtopics in entire unit → direct topic.md
            topic_md_path = os.path.join(unit_path, f"{topic_clean}.md")
            create_markdown_file(topic_md_path)


def create_structure(base_path: str, syllabus: dict):
    """
    Main function to create full folder structure.
    """
    os.makedirs(base_path, exist_ok=True)

    for subject_name, units in syllabus.items():
        subject_folder = os.path.join(base_path, sanitize_name(subject_name))
        os.makedirs(subject_folder, exist_ok=True)

        for unit_name, topics in units.items():
            unit_folder = os.path.join(subject_folder, sanitize_name(unit_name))
            os.makedirs(unit_folder, exist_ok=True)

            process_unit(unit_folder, topics)


# -------------------------------
# Full Syllabus Data (4 subjects)
# -------------------------------

syllabus_data = {
    "Engineering Economics & Project Management": {
        "Unit I (Group A): Introduction, Theory of Demand & Supply": [
            ("Engineering Economics", ["Relationship between Engineering and Economics"]),
            ("Resources", ["Scarcity of resources", "Efficient utilization of resources"]),
            ("Opportunity cost", []),
            ("Rational Choice Theory", []),
            ("Theory of Demand", [
                "Law of demand",
                "Types of demand (Individual demand & Market demand)",
                "Determinants of demand",
                "Demand function",
                "Change in demand (Shift of demand curve) vs. change in quantity demanded"
            ]),
            ("Elasticity of demand", [
                "Types (price, income & cross price elasticity) with mathematical derivation",
                "Elastic and inelastic goods",
                "Measurement of price elasticity (Point elasticity and Arc elasticity)",
                "Variation of price elasticity on a linear demand curve (zero to infinity)",
                "Relationship between price, total revenue and price elasticity of demand (mathematical derivation)"
            ]),
            ("Theory of Supply", [
                "Definition of supply",
                "Determinants of supply",
                "Supply function",
                "Supply curve and shift of supply curve"
            ]),
            ("Market mechanism", [
                "Definition of Market",
                "Price mechanism: determination of equilibrium price and quantity (Numerical examples with graphical illustration)",
                "Stability of equilibrium",
                "Basic comparative static analysis: Change in equilibrium due to shift of demand & supply curve (Numerical problems with graphical illustration)"
            ])
        ],
        "Unit II (Group A): Theory of Production & Costs": [
            ("Theory of Production", [
                "Concept of production (goods & services)",
                "Factors of production (fixed and variable factors)",
                "Short-run production function (Graphical illustration)",
                "Law of return (graphical and mathematical derivation)",
                "Long-run production function (returns to scale)"
            ]),
            ("Theory of Cost", [
                "Short-run and long-run cost curves (graphical illustration)",
                "Total cost, fixed cost, variable cost, marginal cost, average cost (diagrammatic concept)",
                "Relationship between AC and MC"
            ]),
            ("Economic concept of profit", [
                "Profit maximization (numerical problems)"
            ])
        ],
        "Unit III (Group A): Different Types of Market and Role of Government": [
            ("Perfect Competition: Features of Perfectly Competitive Market", []),
            ("Imperfect Competition: Monopoly, Monopolistic Competition, Oligopoly", []),
            ("Role of government in Socialist, Capitalist and Mixed Economy structure with example", [])
        ],
        "Unit I (Group B): Concept of Project": [
            ("Definition and classification of projects", []),
            ("Importance of Project Management", []),
            ("Project life Cycle (Conceptualization–Planning–Execution–Termination)", [])
        ],
        "Unit II (Group B): Feasibility Analysis of a Project": [
            ("Economic and Market analysis", []),
            ("Financial analysis: Basic techniques in capital budgeting", [
                "Payback period method",
                "Net Present Value method",
                "Internal Rate of Return method"
            ]),
            ("Environmental impact study: adverse impact of the project on the environment", []),
            ("Project risk and uncertainty: Technical, economical, socio-political, environmental risks", []),
            ("Evaluation of the financial health of a project", [
                "Fixed & Working Capital, Debt & Equity, Shares, Debentures",
                "Financial ratios: Liquidity Ratios, Activity Ratios, Debt-equity ratio, Profitability Ratio"
            ])
        ],
        "Unit III (Group B): Project Administration": [
            ("Gantt Chart: system of bar charts for scheduling and reporting project progress", []),
            ("PERT and CPM: basic concept and application with real-life examples", [])
        ]
    },

    "Cloud Computing": {
        "Unit 1: Cloud Computing Fundamentals": [
            ("Origins of Cloud computing", []),
            ("Fundamental concepts and models", []),
            ("Roles and boundaries", []),
            ("Cloud components", []),
            ("On-demand self-service", []),
            ("Broad network access", []),
            ("Location independent resource pooling", []),
            ("Rapid elasticity", []),
            ("Measured service", []),
            ("Comparing cloud providers with traditional IT service providers", []),
            ("Roots of cloud computing", []),
            ("Migrating to clouds", [])
        ],
        "Unit 2: Cloud Delivery Model": [
            ("Cloud Delivery Models, The SPI Framework", []),
            ("Cloud Service Models", []),
            ("Cloud Deployment Models", []),
            ("Alternative Deployment models", []),
            ("Expected benefits of the models", [])
        ],
        "Unit 3: Virtualization": [
            ("Characteristics & Taxonomy of virtualization", []),
            ("Virtualization vs Private Cloud", []),
            ("Desktop Virtualization", []),
            ("Hardware Virtual Machine (HVM)", []),
            ("Virtual Servers", []),
            ("Logical Network Perimeter", []),
            ("Network Virtualization", []),
            ("Data Center virtualization", []),
            ("Cloud Storage Device", []),
            ("Cloud usage monitor", []),
            ("Resource replication", [])
        ],
        "Unit 4: Fundamental Cloud Security": [
            ("Cloud Information Security Objectives", []),
            ("Cloud Security Services & Relevant Cloud Security Design Principles", []),
            ("Secure Cloud Software Requirements", []),
            ("Secure Development practices", []),
            ("Approaches to Cloud Software Requirement Engineering", []),
            ("Privacy and Compliance Risks", []),
            ("Threats to Infrastructure", []),
            ("Data and Access Control", []),
            ("Cloud Service Provider Risks", []),
            ("Cloud Security Policy Implementation", [])
        ],
        "Unit 5: Cloud Tools and applications": [
            ("Cloud Performance Monitoring tools", []),
            ("General model for Application platform", []),
            ("Apache Virtual Computing Lab", []),
            ("VMware", []),
            ("CloudSim", []),
            ("Microsoft Cloud Services (Azure)", []),
            ("Google Cloud Applications", []),
            ("Amazon cloud services", [])
        ]
    },

    "Machine Learning": {
        "Unit 1: Supervised Learning (Regression & Classification)": [
            ("Basic methods", [
                "Distance-based methods",
                "Nearest-Neighbours",
                "Decision Trees",
                "Naive Bayes"
            ]),
            ("Linear models", [
                "Linear Regression",
                "Logistic Regression",
                "Generalized Linear Models"
            ]),
            ("Support Vector Machines", [
                "Nonlinearity",
                "Kernel Methods"
            ])
        ],
        "Unit 2: Unsupervised Learning": [
            ("Clustering: K-means/Kernel K-means", []),
            ("Dimensionality Reduction: PCA and kernel PCA", []),
            ("Matrix Factorization and Matrix Completion", [])
        ],
        "Unit 3: Artificial Neural Network": [
            ("Neural network representation", []),
            ("Perceptron", []),
            ("Multilayer Network and Back Propagation Algorithm", []),
            ("Illustrative Example: Face recognition", [])
        ],
        "Unit 4: Genetic Algorithm": [
            ("Representing Hypotheses", []),
            ("Genetic Operators", []),
            ("Fitness Function and Selection", []),
            ("Hypothesis space search", []),
            ("Genetic Programming", [])
        ],
        "Unit 5: Reinforcement Learning": [
            ("The Learning Task", []),
            ("Q Learning", []),
            ("Temporal Difference Learning", [])
        ]
    },

    "Entrepreneurship and Start-ups": {
        "Unit 1: Entrepreneurship – Introduction and Process": [
            ("Concept, Competencies, Functions and Risks of entrepreneurship", []),
            ("Entrepreneurial Values & Attitudes and Skills", []),
            ("Mindset of an employee/manager and an entrepreneur", []),
            ("Types of Ownership for Small Businesses", [
                "Sole proprietorship",
                "Partnerships",
                "Joint Stock company (public limited and private limited)"
            ]),
            ("Difference between entrepreneur and Intrapreneur", [])
        ],
        "Unit 2: Preparation for Entrepreneurial Ventures": [
            ("Business Idea", [
                "Concept",
                "Characteristics of a Promising Business Idea",
                "Uniqueness of the product or service and its competitive advantage over peers"
            ]),
            ("Feasibility Study", [
                "Concept",
                "Locational, Economic, Technical and Environmental Feasibility",
                "Structure and Contents of a standard Feasibility Study Report"
            ]),
            ("Business Plan", [
                "Concept",
                "Rationale for developing a Business Plan",
                "Structure and Contents of a typical Business Plan"
            ]),
            ("Project Report", [
                "Concept",
                "Features and components"
            ]),
            ("Financial Statements (Basic components)", [
                "Revenue",
                "Expenses (Revenue & capital Exp)",
                "Gross Profit",
                "Net Profit",
                "Asset",
                "Liability",
                "Cash Flow",
                "Working capital",
                "Inventory",
                "Funding Methods (Equity or Debt)"
            ])
        ],
        "Unit 3: Establishing Small Enterprises": [
            ("Legal Requirements and Compliances for establishing a New Unit", [
                "NOC from Local body",
                "Registration of business in DIC",
                "Statutory license or clearance",
                "Tax compliances"
            ])
        ],
        "Unit 4: Start-up Ventures": [
            ("Concept & Features", []),
            ("Mobilisation of resources by start-ups: Financial, Human, Intellectual and Physical", []),
            ("Problems and challenges faced by start-ups", []),
            ("Start-up Ventures in India (Contemporary Success Stories and Case Studies)", [])
        ],
        "Unit 5: Financing Start-up Ventures in India": [
            ("Communication of ideas to potential investors – Investor Pitch", []),
            ("Equity Funding, Debt funding – Angel Investors, Venture Capital Funds, Bank loans to start-ups", []),
            ("Govt Initiatives including incubation centre to boost start-up ventures", []),
            ("MSME Registration for Start-ups – its benefits", [])
        ],
        "Unit 6: Exit Strategies for Entrepreneurs": [
            ("Merger and acquisition exit", []),
            ("Initial Public Offering (IPO)", []),
            ("Liquidation", []),
            ("Bankruptcy", [])
        ]
    }
}


# -------------------------------
# Execution Entry Point
# -------------------------------

if __name__ == "__main__":
    root_directory = "onGit"
    create_structure(root_directory, syllabus_data)

    print("Folder structure successfully created under 'onGit/'")