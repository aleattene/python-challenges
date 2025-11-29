from utils.aoc_utils import get_input_file_path, read_input_file

def solve_day_01_2025(filename: str) -> tuple[int, int]:
    """
    Solution of the Advent of Code 2025 Day 01 - ??????.
    :param filename: The name file containing the input data.
    :return:
    """
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        # Read the input file
        data = read_input_file(input_file_path)
    except Exception as error:
        raise RuntimeError(f"Error: {error}")

    # Solutions
    print("Day 01 - 2025:", data)

    return 0, 0



if __name__ == "__main__":
    # Import function to print results
    import time
    from utils.aoc_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2 = solve_day_01_2025("input_demo.txt")
    # start_time = time.time()
    # solution_1, solution_2 = solve_day_01_2025("input.txt")
    # end_time = time.time()
    #
    # # Calculate execution time in milliseconds
    # execution_time: int = int((end_time - start_time) * 1000)
    #
    # # Print results in a formatted table (using rich)
    # print_day_results(
    #     "2024", "01",
    #     str(demo_1), str(demo_2),
    #     str(solution_1), str(solution_2),
    #     execution_time
    # )

