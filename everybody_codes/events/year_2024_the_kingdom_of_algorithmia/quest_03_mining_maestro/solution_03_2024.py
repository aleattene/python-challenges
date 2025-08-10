from utils.ec_utils import (get_input_file_path, read_input_file)
import pprint as pp


def is_adjacent_neighbors(grid: list[str], current_position: tuple[int, int], cross_neighbors: bool = False) -> bool:
    """
    Check if the neighbors of a given position are not adjacent by a specified distance.
    :param grid: list of strings representing the grid
    :param current_position: tuple containing the x and y coordinates of the position
    :param cross_neighbors: boolean indicating if diagonal neighbors should be considered or not
    :return: True if neighbors are not adjacent, False otherwise
    """
    # Identify the current value in the grid at the given position
    row, col = current_position
    current_value = grid[row][col]
    # Define the directions for neighbors based on whether cross neighbors are considered or not
    neighbors_directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    if not cross_neighbors: neighbors_directions += [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    # Iterate through the neighbors' directions and check if their values are the same as the current value
    for direction in neighbors_directions:
        neighbor_row, neighbor_col = row+direction[0], col+direction[1]
        # Check if the neighbor is within the grid bounds otherwise return False
        if not (0 <= neighbor_row < len(grid) and 0 <= neighbor_col < len(grid[0])): return False
        neighbor_value = grid[neighbor_row][neighbor_col]
        # If the neighbor value is '.', it means it does not represent a valid neighbor so return False
        if neighbor_value == '.': return False
        # if the neighbor value is different from the current value, return False
        if current_value != neighbor_value: return False
    # The neighbors are all the same as the current value, so the current block is considered valid to be updated
    return True

def remove_block(grid: list[str], counter: int, cross_neighbors: bool) -> int:
    """
    Remove a block at the specified position in the grid.
    :param grid: list of strings representing the grid
    :param counter: current counter value to modify the cell values in the grid
    :param cross_neighbors: boolean indicating if diagonal neighbors should be considered or not
    :return: total number of blocks modified in the grid
    """
    # If the counter is greater than 9, reset it to 0
    counter = counter % 9
    # Initialize a list to store the positions of cells that can be changed for the current iteration
    cells_to_change: list[tuple[int, int]] = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # If the current value is '.', it means it does not represent a valid block to check
            current_value = grid[row][col]
            if current_value == '.': continue
            # Check if there are cells/blocks that can be changed
            is_position_to_change = is_adjacent_neighbors(grid, (row, col), cross_neighbors)
            # If there are a cells/blocks that can be changed, store them position
            if is_position_to_change: cells_to_change.append((row, col))

    # If no cells to change, the grid is stable and no more blocks can be removed
    if not cells_to_change: return 0

    # Otherwise, change the cells in the grid
    for row, col in cells_to_change:
        grid[row] = grid[row][:col] + str(counter + 1) + grid[row][col + 1:]
    # pp.pprint(grid)
    # Recall the function to remove blocks recursively
    return len(cells_to_change) + remove_block(grid, counter + 1, cross_neighbors)

def modify_secure_grid(grid: list[str], block_from: str = '#', block_to: str = '1', block_removed: int = 0) -> int:
    """
    Thi function modifies the secure grid, only during the first iteration, by replacing all occurrences of a specific
    block with another block.
    """
    for row in range (len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == block_from:
                block_removed += 1
                grid[row] = grid[row][:col] + block_to + grid[row][col+1:]
    return block_removed

def solve_03_2024(filename: str) -> tuple[int, int, int]:
    """
    Solution of the Everybody Codes 2024/03.
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

    # Solution part 1
    block_removed_1 = modify_secure_grid(data_1)
    block_removed_1 += remove_block(data_1, 1, True)

    # Solution part 2
    block_removed_2 = modify_secure_grid(data_2)
    block_removed_2 += remove_block(data_2, 1, True)

    # Solution part 3
    block_removed_3 = modify_secure_grid(data_3)
    block_removed_3 += remove_block(data_3, 1, False)

    # Return the results for each part of the quest
    return block_removed_1, block_removed_2, block_removed_3


if __name__ == "__main__":
    # Import function to print results
    import time
    from utils.ec_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2, demo_3 = solve_03_2024("input_demo.txt")
    start_time: float = time.time()
    solution_1, solution_2, solution_3 = solve_03_2024("input.txt")
    end_time: float = time.time()

    # Calculate execution time in milliseconds
    execution_time: int = int((end_time - start_time) * 1000)

    # Print results in a formatted table (using rich)
    print_day_results(
        "2024", "03",
        str(demo_1), str(demo_2), str(demo_3),
        str(solution_1), str(solution_2), str(solution_3),
        execution_time
    )