from utils.aoc_utils import get_input_file_path, read_input_file, get_max_k_digits_number_str


def solve_day_03_2025(filename: str) -> tuple[int, int]:
    """
    Solution of the Advent of Code 2025 Day 03 - Lobby.
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

    # Initialize total joules for part 1 and part 2
    total_joules_1 = total_joules_2 = 0

    # Process each line of the input data only once to improve efficiency
    for batteries in data:
        # The function called use greedy algorithm to get the maximum k-digits number from the string
        total_joules_1 += get_max_k_digits_number_str(batteries, 2)
        total_joules_2 += get_max_k_digits_number_str(batteries, 12)

    # Return the results for part 1 and part 2
    return total_joules_1, total_joules_2


if __name__ == "__main__":
    # Import function to print results
    import time
    from utils.aoc_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2 = solve_day_03_2025("input_demo.txt")
    start_time = time.time()
    solution_1, solution_2 = solve_day_03_2025("input.txt")
    end_time = time.time()

    # Calculate execution time in milliseconds
    execution_time: int = int((end_time - start_time) * 1000)

    # Print results in a formatted table (using rich)
    print_day_results(
        "2025", "03",
        str(demo_1), str(demo_2),
        str(solution_1), str(solution_2),
        execution_time
    )
