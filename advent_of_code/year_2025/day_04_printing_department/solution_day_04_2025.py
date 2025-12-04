from utils.aoc_utils import get_input_file_path, read_input_file, get_neighbors_positions_with_symbol


def find_available_rolls(data: list[str], neighbors_limit: int = 4) -> tuple[int, list[tuple[int, int]]]:
    """
    Find available paper rolls that have less than 4 neighboring rolls.
    :param data: The grid representing the printing department.
    :param neighbors_limit: The maximum number of neighboring rolls to consider a roll as available.
    :return: A tuple containing the number of available rolls and their positions.
    """
    # Get the dimensions of the grid (rows and columns)
    rows: int = len(data)
    cols: int = len(data[0]) if rows > 0 else 0

    # Initialize the count of available rolls and their positions
    available_rolls: int = 0
    rolls_to_replace: list[tuple[int, int]] = []

    # Iterate through each cell in the grid
    for x in range(rows):
        for y in range(cols):
            # Check if the current cell contains a paper roll ('@') otherwise skip it
            if data[x][y] != '@': continue
            # Get the neighboring positions that contain a paper roll ('@')
            paper_rolls: list[tuple[int, int]] = get_neighbors_positions_with_symbol(data, x, y, '@')
            # If there are less than 4 neighboring rolls, count it as available and store its position
            if len(paper_rolls) < neighbors_limit:
                available_rolls += 1
                rolls_to_replace.append((x, y))

    # Return the count of available rolls and their positions
    return available_rolls, rolls_to_replace


def solve_day_04_2025(filename: str) -> tuple[int, int]:
    """
    Solution of the Advent of Code 2025 Day 04 - Printing Department.
    :param filename: The name file containing the input data.
    :return: The results for part 1 and part 2.
    """
    try:
        # Create the absolute path of the input file
        input_file_path: str = get_input_file_path(__file__, filename)
        # Read the input file
        data: list[str] = read_input_file(input_file_path)
    except Exception as error:
        raise RuntimeError(f"Error: {error}")

    # Solution for part 1
    available_rolls_1: int = find_available_rolls(data)[0]

    # Solution for part 2
    available_rolls_2: int = 0
    while True:
        available_rolls, rolls_to_replace = find_available_rolls(data)
        # If there are no more rolls to replace, break the loop because we're completed the process
        if not rolls_to_replace: break

        # Accumulate the number of available rolls found in this iteration and replace them with '.'
        available_rolls_2 += available_rolls
        for x, y in rolls_to_replace:
            data[x] = data[x][:y] + '.' + data[x][y+1:]

    # Return the results for part 1 and part 2
    return available_rolls_1, available_rolls_2


if __name__ == "__main__":
    # Import function to print results
    import time
    from utils.aoc_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2 = solve_day_04_2025("input_demo.txt")
    start_time = time.time()
    solution_1, solution_2 = solve_day_04_2025("input.txt")
    end_time = time.time()

    # Calculate execution time in milliseconds
    execution_time: int = int((end_time - start_time) * 1000)

    # Print results in a formatted table (using rich)
    print_day_results(
        "2025", "04",
        str(demo_1), str(demo_2),
        str(solution_1), str(solution_2),
        execution_time
    )
