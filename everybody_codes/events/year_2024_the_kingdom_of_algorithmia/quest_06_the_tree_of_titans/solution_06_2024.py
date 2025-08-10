from utils.ec_utils import (get_input_file_path, read_input_file)
import pprint as pp

def create_tree(data_tree: dict, node: str, current_tree: dict) -> dict:
    """
    Create a tree structure from the input data.
    :param data_tree: List of strings representing the tree nodes and their children.
    :param node: The current node to process.
    :param current_tree: The current state of the tree being built.
    :return: A dictionary representing the tree structure.
    """
    # Take the sub-nodes for the current node
    sub_nodes: list[str] = data_tree.get(node, [])
    # If the node is not in the current tree, add it
    if node not in current_tree:
        current_tree[node] = {}
    # Iterate through the sub-nodes and create the tree recursively
    for sub_node in sub_nodes:
        # If the sub-node is @, it indicates a leaf node (end of branch/path)
        if sub_node == '@':
            current_tree[node]['@'] = {}
        # If the sub-node is not a leaf node and not already in the current tree, add it
        if sub_node not in current_tree[node]:
            current_tree[node][sub_node] = {}
        # Recursively create the tree for each sub-node
        create_tree(data_tree, sub_node, current_tree[node])
    # At the end of the recursion, return the created tree structure
    return current_tree

def count_path_nodes(tree: dict, path: list[str], length_paths_to_paths: dict) -> dict:
    """
    Count the paths in the tree and store them in a dictionary based on their lengths.
    :param tree: The tree structure as a dictionary.
    :param path: The current path being traversed in the tree.
    :param length_paths_to_paths: A dictionary to store paths based on their lengths.
    :return: A dictionary with path lengths as keys and lists of paths as values.
    """
    for node, sub_nodes in tree.items():
        new_path: list[str] = path + [node]
        # If the node is a leaf node (indicated by '@'), store the path in results
        if node == '@':
            path_length = len(new_path)
            # If the path length is not in results, initialize it with the new path
            if path_length not in length_paths_to_paths: length_paths_to_paths[path_length] = [new_path]
            # Otherwise, append the new path to the existing list for that length
            else: length_paths_to_paths[path_length].append(new_path)
        else:
            # If the node is not a leaf, continue traversing the tree recursively
            for subnode, nephews in sub_nodes.items():
                count_path_nodes({subnode:nephews}, new_path, length_paths_to_paths)
    # After traversing all nodes, return the dictionary containing paths grouped by their lengths
    return length_paths_to_paths

def from_tree_list_to_tree_dict(tree_list: list[str], bugs_ants: set[str]) -> dict:
    """
    Convert a list of strings representing a tree into a dictionary structure.
    :param tree_list: List of strings where each string represents a node and its children (subnodes).
    :param bugs_ants: A set of nodes that should be ignored ('BUG', 'ANT', ...).
    :return: A dictionary representing the tree structure.
    """
    # Initialize an empty dictionary to hold the tree structure
    tree_dict: dict = {}
    # Iterate through each line in the tree_list
    for line in tree_list:
        node = line.split(":")[0]
        # If the node is a bug or an ant, skip it because they are a fake branches/nodes
        if node in bugs_ants: continue
        sub_nodes = line.split(":")[1].split(",")
        # Add the node and its sub-nodes to the tree_dict
        tree_dict[node] = sub_nodes
    # Return the constructed tree dictionary
    return tree_dict

def get_unique_path(tree: dict, char_node:int = 0) -> str:
    """
    Get the unique path from the root node to a leaf node in the tree.
    :param tree: The tree structure as a dictionary.
    :param char_node: The number of characters to consider for the unique path (default is 0 and indicates all chars).
    :return: A string representing the unique path from the root to a leaf node.
    """
    empty_path = ""
    # Iterate through the tree to find the unique path
    for length_path, path in tree.items():
        if len(path) == 1:
            # If char_node is specified, return the sliced path to get only the specified char_node characters
            if char_node: return empty_path.join([node[char_node-1] for node in path[0]])
            # Otherwise, return the full path as a string
            return empty_path.join(path[0])
    # If no unique path is found, return an empty string
    return empty_path

def solve_part(data: list[str], root_node: str, bugs_ants: set[str], char_node:int = 0) -> str:
    """
    Solve a part of the quest by creating a tree and finding the unique path.
    :param data: List of strings representing the tree structure.
    :param root_node: The root node of the tree.
    :param bugs_ants: A set of nodes that should be ignored (bugs and ants).
    :param char_node: The number of characters to consider for the unique path (default is 0 and indicates all chars).
    :return: The unique path as a string.
    """
    # Convert the list of strings to a dictionary structure representing the tree
    data_tree = from_tree_list_to_tree_dict(data, bugs_ants)
    # Create the tree structure from the dictionary
    tree = create_tree(data_tree, root_node, {})
    # Count the paths in the tree and store them in a dictionary based on their lengths
    length_paths_to_paths = count_path_nodes(tree, [], {})
    # Return the unique path from the root node to a leaf node, considering the specified number of chars required
    return get_unique_path(length_paths_to_paths, char_node)


def solve_06_2024(filename: str) -> tuple[str, str, str]:
    """
    Solution of the Everybody Codes 2024/06.
    :param filename: filename that contains the input data
    :return: solution for each part of the quest (1, 2, and 3)
    """
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        # Read the input files
        data_1: list[str] = read_input_file(input_file_path.replace('.txt', '_01.txt'))
        data_2: list[str] = read_input_file(input_file_path.replace('.txt', '_02.txt'))
        data_3: list[str] = read_input_file(input_file_path.replace('.txt', '_03.txt'))
    except Exception as error:
        raise RuntimeError(f"Error: {error}")

    # Identify the root node from the first line of data_1 (always RR)
    root_node = data_1[0].split(":")[0]
    # Define a set of nodes that should be ignored (bugs and ants)
    bugs_ants: set[str] = {'BUG', 'ANT'}

    # Solution Part 1, 2, and 3
    unique_path_1: str = solve_part(data_1, root_node, bugs_ants)
    unique_path_2: str = solve_part(data_2, root_node, bugs_ants, 1)
    unique_path_3: str = solve_part(data_3, root_node, bugs_ants, 1)

    # Return the unique paths for each part of the quest
    return unique_path_1, unique_path_2, unique_path_3


if __name__ == "__main__":
    # Import function to print results
    import time
    from utils.ec_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2, demo_3 = solve_06_2024("input_demo.txt")
    start_time: float = time.time()
    solution_1, solution_2, solution_3 = solve_06_2024("input.txt")
    end_time: float = time.time()

    # Calculate execution time in milliseconds
    execution_time: int = int((end_time - start_time) * 1000)

    # Print results in a formatted table (using rich)
    print_day_results(
        "2024", "06",
        str(demo_1), str(demo_2), str(demo_3),
        str(solution_1), str(solution_2), str(solution_3),
        execution_time
    )