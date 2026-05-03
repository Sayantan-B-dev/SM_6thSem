"""
Purpose:
--------
Generate a folder tree structure and export it into a .txt file
instead of printing it to the console.

Design Decisions:
-----------------
- Uses recursion for deep traversal of directories.
- Accumulates output lines in a list before writing to file.
- Ensures deterministic ordering using sorted listing.
- Handles permission errors gracefully without stopping execution.
"""

import os


def build_folder_tree_lines(root_directory_path: str, indent_prefix: str = "", output_lines=None):
    """
    Recursively builds folder tree lines.

    Parameters:
    -----------
    root_directory_path : str
        Path of the directory to scan.

    indent_prefix : str
        Prefix for indentation formatting.

    output_lines : list
        List to accumulate output lines.
    """

    if output_lines is None:
        output_lines = []

    try:
        directory_contents = sorted(os.listdir(root_directory_path))
    except PermissionError:
        output_lines.append(indent_prefix + "└── [Permission Denied]")
        return output_lines

    total_items = len(directory_contents)

    for index, item_name in enumerate(directory_contents):
        item_full_path = os.path.join(root_directory_path, item_name)

        is_last_item = (index == total_items - 1)
        connector_symbol = "└── " if is_last_item else "├── "

        # Append current line
        output_lines.append(indent_prefix + connector_symbol + item_name)

        # Recurse into directories
        if os.path.isdir(item_full_path):
            next_indent = "    " if is_last_item else "│   "
            build_folder_tree_lines(item_full_path, indent_prefix + next_indent, output_lines)

    return output_lines


# Entry Point
if __name__ == "__main__":
    root_path = input("Enter directory path: ").strip()
    output_file_path = "folder_tree_output.txt"

    # Generate tree lines
    tree_lines = build_folder_tree_lines(root_path)

    # Write to file
    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write(f"Folder Tree for: {root_path}\n\n")
        file.write("\n".join(tree_lines))

    print(f"Folder tree exported to: {output_file_path}")