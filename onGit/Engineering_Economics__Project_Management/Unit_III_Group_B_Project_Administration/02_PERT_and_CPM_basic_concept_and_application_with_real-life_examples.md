# PERT and CPM basic concept and application with real life examples

## Video Explanation

* [https://www.youtube.com/watch?v=ZKOL-rZ79gs](https://www.youtube.com/watch?v=ZKOL-rZ79gs)

## Visual Aids

![Image](https://images.openai.com/static-rsc-4/GecCvTElZ6uSTAApPhleyVgAMKzYBDJyfhOQkQv4T2rl_GWnJ0iHuL4HwlJKkbC0kr4DZqKEFpN2i_-WZCbKx1dCJADX2-nS8bedKQB6dI95_CIQmhhAqVAFC4Q_T0N1cIy35ZxXU25Cs7s_J9i7nOiaOX61Ond3Iv6sxreHw9jEKR5sdzRBgg2RCNsE9Hw7?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/ZcItWagXpFjMNLkdCYZby8jhkXg555Vhf1_S-4QejM7_GVObPYtHhee1lAExGBkcFV5HUZdRami2kfj0dlGjGk5bC8MyJ_uzOTyYqRyv-IfMR2dLfjQoedD0lvk9RrjQFjCVE-h8yBajuVAr5wBtvKJg20s8ppKUUJ26C1lyOeDUrJmM2AekVwOZA9rdy_Dj?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/Sgtbg1JdosbylBhnbn5N0j0CRq2CE5GtntPysl2Pv7T4pFECDi9IP_CQPB7-EunKKjtnhWhXyJ9n4yhrg__SCnCWsdKv875N-RCZXBIXQbA3LsbRCpUyPIptl8TPpmsYSnyQquqeo4womPJVcx7sea1PhvngTGGbszkN-efvgpbtiuhTX2y3o6yeZGMSbGY2?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/5x4EeS6oWWQFc13IWoMgMWGvNyARiWI_btlqHOK5iVD97YpzHZ7X_LXVbbKVuTC-DCh_3RppwMFdqSzFtTwVI8gBSxJHH__5rNLe32n3ejlQ7QowYfkl4RCxPMe5U_iVkXmBrXCGu8k9hxob-TGWCzM4wk-CHeWUn7oGruSGi2CA50WuqLvFhUbu5BP6AX7I?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/gzXr6YoCFkMoKZY4Nu9H7e2OSWcVeQILIdhQxvz5hXkVI6g350QOIV8xxJm-IhtwqWpkPJDz0T_McLmgdlfXcu1mPhSCj_RZSflJww9i7kSk9iC1GwAxU4FNI0XErbgYTvr29MUtL8lOu2Wx85ZaZPToG05DM66EnrX5o8UoFKcXFrhfOEwzK5mEegP0F0Rm?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/QM7lda9gtC5WwcyqDq_NYJ2VevruYuD_nAuVAP1kOYCYvU0hp5piO0aljwDkFjV-n-Vx7eXOhPRVeYdU2JGbaDtrJkHtZnaXrm5PFn8VyLbg_la2JtjmFQ4w9s6EiVT6TPteKb-q9HRmZ2Ol645h6B3KC8ymMJZVjOajzs8RB1I2NAyL1oakfY8JEr_GQ06V?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/DPOmOO6DCNbJ3KczmOU336rH9N9gjdR8Ki6m5OBBDjGSnyxAjOyoSxjNoIetGRY4iBGR443YVYdkqKMse8Rrn3msH991qqCOtxZq3uxPiIr0YEMD-TbaWpL65Vvl3OsXal9QpJML4XbCZk3CuA_OtzmaixDNjYbRtPsx4LMvZBiPIerJj4a6IymFB9fQI78a?purpose=fullsize)

## 1. Definition

PERT (Program Evaluation and Review Technique) and CPM (Critical Path Method) are network-based project management tools used to plan, schedule, and control complex projects. PERT deals with uncertain activity durations using probabilistic time estimates, while CPM uses fixed, deterministic durations. Both methods identify the critical path – the longest sequence of dependent activities that determines the project’s shortest possible completion time.

---

## 2. Concept Explanation

The basic idea is to break a large project into smaller, manageable activities and arrange them in a logical order. A network diagram is drawn showing activities as arrows or nodes and their dependencies. Then, the time required for each activity is estimated. By calculating the earliest and latest possible start and finish times, we determine how much delay each activity can absorb without affecting the overall project deadline. The activities that cannot be delayed even by one day form the critical path.

How it works: In CPM, we use one fixed time estimate per activity. In PERT, we use three time estimates – optimistic, most likely, and pessimistic – to compute an expected time and its variance, reflecting uncertainty. For both methods, we perform a forward pass to compute early times and a backward pass for late times. Total float (slack) for each activity is then found. Activities with zero total float lie on the critical path. This path dictates the project’s minimum duration. We can also estimate the probability of completing a project by a target date using PERT.

Why it is important: These techniques bring discipline to planning. They reveal which activities must be carefully managed to meet deadlines. Managers can allocate resources effectively, anticipate bottlenecks, and evaluate the impact of delays. PERT is extremely useful for new, non-repetitive projects like research and development, while CPM is ideal for routine construction and engineering projects. Both improve communication, coordination, and control.

---

## 3. Key Characteristics / Features

- **Network logic:** All activities are linked by predecessor–successor relationships, showing the exact sequence of work.
- **Critical path identification:** Both methods pinpoint activities that are critical for on-time project completion.
- **Float or slack calculation:** They compute the amount of time an activity can be delayed without affecting the project finish date.
- **Time focus:** CPM emphasises time–cost trade-off, while PERT concentrates on time estimation under uncertainty.
- **Graphical representation:** A network diagram provides a clear visual of project structure and flow.
- **Deterministic vs. probabilistic:** CPM assumes known, fixed activity times; PERT uses probabilistic estimates and calculates expected duration and variance.
- **Applicability:** CPM suits repetitive, well-defined projects (like construction); PERT suits unique, uncertain projects (like R&D).
- **Management tool:** Both are indispensable for project scheduling, monitoring, and controlling large-scale undertakings.

---

## 4. Types / Classification (of Network Techniques and Diagrams)

PERT and CPM are the two main network-based scheduling techniques. Additionally, networks can be drawn using different conventions:

- **Activity-on-Arrow (AOA) or Arrow Diagramming Method (ADM):** Activities are represented by arrows, and nodes represent events (start/finish of activities). This traditional form is often used for PERT/CPM.
- **Activity-on-Node (AON) or Precedence Diagramming Method (PDM):** Activities are shown as nodes (boxes), and arrows indicate dependencies. This is common in modern project management software.

Depending on the timing approach:

- **Deterministic networks (CPM):** One definite time per activity.
- **Probabilistic networks (PERT):** Three time estimates per activity, with statistical analysis.

---

## 5. Working / Mechanism (Step-by-Step)

1. Identify all activities required to complete the project.
2. Determine the logical sequence: which activities must precede and which can follow.
3. Draw the network diagram using nodes and arrows, showing all dependencies. Number events (AOA) or label nodes (AON).
4. For CPM, assign a single duration to each activity. For PERT, obtain three time estimates per activity:
   - Optimistic time (tₒ)
   - Most likely time (tₘ)
   - Pessimistic time (tₚ)
5. For PERT, compute the expected time (tₑ) for each activity using the formula:
   tₑ = (tₒ + 4tₘ + tₚ) / 6. Also compute variance: σ² = ((tₚ – tₒ) / 6)².
6. Perform a forward pass to determine the Earliest Start (ES) and Earliest Finish (EF) times for all activities, moving from start to finish. The EF of the last activity gives the project duration.
7. Perform a backward pass to determine the Latest Finish (LF) and Latest Start (LS) times, starting from the project end date and moving backward.
8. Calculate Total Float (TF) for each activity: TF = LS – ES or LF – EF.
9. Identify the critical path: the sequence of activities with zero total float. This is the longest path through the network.
10. For PERT, calculate the project standard deviation (σ_project) as the square root of the sum of variances of activities on the critical path. Then use the normal distribution to find the probability of completing by a given deadline using Z = (D – Tₑ) / σ_project, where D is the deadline and Tₑ is the expected project duration.

---

## 6. Diagram

Below is a simplified network diagram for a small project. Activities A, B, C, and D with durations; A is followed by B and C; B and C both must finish before D can start.

```mermaid
graph LR
    Start((Start)) --> A[ Activity A (3 days) ]
    A --> B[ Activity B (2 days) ]
    A --> C[ Activity C (4 days) ]
    B --> D[ Activity D (1 day) ]
    C --> D
    D --> Finish((Finish))
```

*Critical path calculation:*  
Path A–B–D = 3 + 2 + 1 = 6 days.  
Path A–C–D = 3 + 4 + 1 = 8 days.  
Thus, **A–C–D is the critical path**, and the project duration is 8 days. Activities A, C, D are critical (zero float). Activity B has a total float of 2 days.

---

## 7. Mathematical Formulation

### PERT Expected Time and Variance

$$
t_e = \frac{t_o + 4t_m + t_p}{6}
$$

$$
\sigma^2 = \left( \frac{t_p - t_o}{6} \right)^2
$$

Where:  
- \( t_o \) = Optimistic time (shortest possible)  
- \( t_m \) = Most likely time  
- \( t_p \) = Pessimistic time (longest possible)  
- \( t_e \) = Expected activity duration  
- \( \sigma^2 \) = Activity time variance

### Project Duration and Probability

Expected project duration \( T_E \) = sum of \( t_e \) of critical activities.  
Project variance \( \sigma_p^2 \) = sum of variances of critical activities.  
Project standard deviation \( \sigma_p = \sqrt{\sigma_p^2} \).

Probability of meeting a target deadline \( D \):

$$
Z = \frac{D - T_E}{\sigma_p}
$$

Value of \( Z \) is used to find probability from standard normal distribution table.

### CPM Float (Slack)

Total Float for an activity:

$$
TF = LS - ES \quad \text{or} \quad TF = LF - EF
$$

Activities with \( TF = 0 \) are on the critical path.

---

## 8. Example (Real-life Application)

**CPM Example – Construction of a Boundary Wall:**  
Activities and estimated (deterministic) durations:

| Activity | Description | Predecessor | Duration (days) |
|----------|-------------|-------------|-----------------|
| A | Site clearing | – | 2 |
| B | Foundation excavation | A | 3 |
| C | Concrete footing | B | 2 |
| D | Brick masonry | C | 5 |
| E | Plastering and painting | D | 3 |

– Network: A → B → C → D → E, a simple linear sequence. The critical path is A–B–C–D–E with total duration 15 days.

If activity C is delayed by 1 day, the entire project is delayed. The critical path tells the supervisor to focus especially on concrete supply for footing.

**PERT Example – Development of a New Mobile App Feature:**  
Activity “User Interface Coding” has uncertain duration. Estimates:  
- Optimistic (tₒ) = 4 days  
- Most likely (tₘ) = 7 days  
- Pessimistic (tₚ) = 12 days  

Expected time: \( t_e = (4 + 4×7 + 12) / 6 = (4 + 28 + 12) / 6 = 44 / 6 ≈ 7.33 \) days.  
Variance: \( ((12 – 4) / 6)² = (8/6)² = (1.333)² ≈ 1.78 \).

The project has three critical activities with variances 1.78, 2.00, and 0.50. Expected project duration \( T_E \) = 25 days, \(\sigma_p^2\) = 1.78+2.00+0.50=4.28, \(\sigma_p\) ≈ 2.07 days.  
Probability of finishing within 28 days: Z = (28-25)/2.07 ≈ 1.45; from Z-table, probability ≈ 92.6%. Management can be fairly confident of meeting the deadline.

---

## 9. Analogy

Think of preparing a big family dinner. Some tasks have fixed times: roasting a chicken takes exactly 90 minutes (like a CPM activity). Others are uncertain: making a new dessert you haven’t tried before could take anywhere from 30 to 60 minutes (like PERT). You list all dishes, decide which must finish before others (gravy after chicken is cooked), and find the chain of tasks that determines when dinner can be served. That chain is your critical path. If the chicken roaster breaks down (a delay on the critical path), dinner is late; but a delay in setting the table (a non‑critical task with float) doesn’t push dinner time.

---

## 10. Comparison (PERT vs. CPM)

| Feature | PERT | CPM |
|--------|------|-----|
| Meaning | Probabilistic; handles uncertainty in activity times | Deterministic; assumes fixed, known activity times |
| Time estimates | Three time estimates (optimistic, most likely, pessimistic) | Single time estimate |
| Focus | Time analysis and probability of completion | Time–cost trade-off and optimal resource utilization |
| Suitability | Research, development, and non-repetitive projects | Construction, maintenance, and repetitive projects |
| Critical path | Identified using expected times | Identified using fixed durations |
| Variance calculation | Computes activity and project variance | No variance concept |
| Cost optimization | Not a primary concern | Crashing techniques used to reduce duration at minimum cost |

---

## 11. Advantages

- Both methods force detailed project planning, breaking work into manageable activities.
- They clearly reveal dependencies and the impact of delays, enabling proactive management.
- The critical path highlights tasks that must be closely monitored and accelerated if needed.
- Float information prevents unnecessary panic over non‑critical delays and guides resource shifting.
- PERT allows realistic handling of uncertainty, giving probability estimates for meeting deadlines.
- CPM facilitates crashing analysis to shorten project duration at the lowest extra cost.
- They improve communication among stakeholders through a standard, visual representation.
- Decision-making becomes data-driven, reducing reliance on guesswork.

---

## 12. Disadvantages / Limitations

- For large, complex projects, network diagrams become huge and difficult to manage without software.
- Estimating activity durations accurately is still challenging, especially in PERT when subjective probability inputs can be biased.
- CPM assumes durations are fixed; real construction projects face unforeseen delays, making schedule adjustments necessary.
- PERT’s underlying assumption of beta distribution and the weighted average formula (1:4:1) may not always hold.
- Both methods require that activities be clearly defined with logical relationships, which may be difficult in early project stages.
- They focus primarily on time; resources and manpower are not directly considered unless additional tracking is overlaid.
- The deterministic CPM critical path may shift if activity times vary, a limitation that PERT partly addresses but still requires a stable network.

---

## 13. Important Points / Exam Notes

- PERT is probabilistic (three time estimates); CPM is deterministic (one time estimate).
- Expected time formula: \( t_e = \frac{t_o + 4t_m + t_p}{6} \).
- Variance: \( \sigma^2 = \left( \frac{t_p - t_o}{6} \right)^2 \).
- Critical path = longest path in the network; activities on it have zero total float.
- Total Float (TF) = LS – ES; Free Float = next ES – current EF (if no delay to successors).
- Forward pass gives early times; backward pass gives late times.
- For probability of meeting deadline in PERT, use Z = (D – T_E) / σ_p.
- CPM crashing: reducing activity duration by adding resources, at a cost.
- PERT originated from the US Navy’s Polaris missile project; CPM from DuPont and Remington Rand.
- Network diagrams can be AOA (Activity on Arrow) or AON (Activity on Node).

---

## 14. Applications / Use Cases

- **Construction of a highway bridge:** CPM schedules excavation, piling, pier construction, deck casting, and finishing. Critical path ensures timely opening.
- **Organising a large industrial exhibition:** PERT used because many activities (venue modification, stall erection, VIP invitations) have uncertain durations; probability of being ready by inauguration day is calculated.
- **Software implementation project:** Blended use – CPM for phases with fixed effort (data migration), PERT for innovative coding modules with uncertain durations.
- **Shipbuilding:** CPM schedules hull fabrication, outfitting, and commissioning; crashing used to accelerate launch dates.
- **Pharmaceutical drug development:** PERT networks map clinical trial phases, with probability analysis for filing new drug application deadlines.

---

## 15. MCQs

**Q1. PERT stands for:**  
A. Project Evaluation and Review Technique  
B. Program Evaluation and Review Technique  
C. Program Estimation and Reporting Tool  
D. Project Estimation and Resource Technique  
**Answer:** B  
**Explanation:** PERT stands for Program Evaluation and Review Technique, a probabilistic scheduling tool.

**Q2. Which of the following is true about CPM?**  
A. It uses three time estimates  
B. It is probabilistic  
C. It assumes fixed activity durations  
D. It does not identify the critical path  
**Answer:** C  
**Explanation:** CPM (Critical Path Method) uses deterministic, known activity durations and identifies the critical path.

**Q3. The formula for expected time in PERT is:**  
A. \( t_e = \frac{t_o + t_m + t_p}{3} \)  
B. \( t_e = \frac{t_o + 2t_m + t_p}{4} \)  
C. \( t_e = \frac{t_o + 4t_m + t_p}{6} \)  
D. \( t_e = \frac{2t_o + 3t_m + t_p}{6} \)  
**Answer:** C  
**Explanation:** The PERT weighted average formula gives the expected time as (t_o + 4t_m + t_p)/6.

**Q4. In a project network, the critical path is the:**  
A. Shortest path from start to finish  
B. Path with the most activities  
C. Longest path in terms of duration  
D. Path with the highest cost  
**Answer:** C  
**Explanation:** The critical path is the sequence of activities that determines the minimum project duration; it is the longest path.

**Q5. Total float of an activity is calculated as:**  
A. ES – LS  
B. LS – ES or LF – EF  
C. EF – ES  
D. LF – LS  
**Answer:** B  
**Explanation:** Total float = Latest Start – Earliest Start (or Latest Finish – Earliest Finish). It indicates how much an activity can be delayed without affecting the project end date.

**Q6. An activity on the critical path has a total float of:**  
A. One  
B. Negative  
C. Zero  
D. Infinite  
**Answer:** C  
**Explanation:** Activities on the critical path have zero total float; any delay directly delays the project.

**Q7. The variance of an activity in PERT is given by:**  
A. \( \frac{t_p - t_o}{6} \)  
B. \( \left( \frac{t_p + t_o}{6} \right)^2 \)  
C. \( \left( \frac{t_p - t_o}{6} \right)^2 \)  
D. \( \frac{t_p + t_o}{6} \)  
**Answer:** C  
**Explanation:** Activity variance = ((t_p – t_o) / 6)², measuring the spread of possible durations.

**Q8. Which technique is more suitable for a research project with highly uncertain activity times?**  
A. CPM  
B. Gantt chart  
C. PERT  
D. Break-even analysis  
**Answer:** C  
**Explanation:** PERT is designed for projects with uncertainty, using probabilistic time estimates.

**Q9. In the forward pass of a CPM/PERT network, we calculate:**  
A. Latest start and latest finish times  
B. Earliest start and earliest finish times  
C. Total float and free float  
D. Activity variances  
**Answer:** B  
**Explanation:** The forward pass computes the earliest times (ES and EF) an activity can start and finish, moving from start to end.

**Q10. If a project’s expected duration is 30 weeks and the standard deviation of the critical path is 2 weeks, the Z‑value for a deadline of 33 weeks is:**  
A. 1.5  
B. 3  
C. 1.0  
D. 0.5  
**Answer:** A  
**Explanation:** Z = (33 – 30)/2 = 1.5. This Z‑value is used to find the probability of completing within 33 weeks.