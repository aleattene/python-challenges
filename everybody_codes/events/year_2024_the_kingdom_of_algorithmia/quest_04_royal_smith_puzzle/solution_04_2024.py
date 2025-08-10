from utils.ec_utils import (
    get_input_file_path, read_input_file,
    from_list_strings_to_list_integers,
    get_median_from_list_integers
)

def get_strikes_needed(nails: list[int], nail_height: int) -> int:
    """
    Calculate the number of strikes needed to make all nails the same height.
    :param nails: A list of integers representing the heights of the nails.
    :param nail_height: The target height for all nails.
    :return: The total number of strikes needed.
    """
    if not nails: return 0
    return sum(abs(nail - nail_height) for nail in nails)


def solve_04_2024(filename: str) -> tuple[int, int, int]:
    """
    Solution of the Everybody Codes 2024/04.
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

    # Solution Part 1 and Part 2
    data_1: list[int] = from_list_strings_to_list_integers(data_1)
    strikes_needed_1: int = get_strikes_needed(data_1, min(data_1))
    data_2: list[int] = from_list_strings_to_list_integers(data_2)
    strikes_needed_2: int = get_strikes_needed(data_2, min(data_2))

    # Solution Part 3
    data_3: list[int] = from_list_strings_to_list_integers(data_3)
    # Calculate the median nail height (using numpy for efficiency) to minimize the total strikes needed
    median_nail: int = get_median_from_list_integers(data_3)
    best_strikes_3: int = get_strikes_needed(data_3, median_nail)

    # Return the results for all three parts
    return strikes_needed_1, strikes_needed_2, best_strikes_3


if __name__ == "__main__":
    # Import function to print results
    import time
    from utils.ec_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2, demo_3 = solve_04_2024("input_demo.txt")
    start_time: float = time.time()
    solution_1, solution_2, solution_3 = solve_04_2024("input.txt")
    end_time: float = time.time()

    # Calculate execution time in milliseconds
    execution_time: int = int((end_time - start_time) * 1000)

    # Print results in a formatted table (using rich)
    print_day_results(
        "2024", "04",
        str(demo_1), str(demo_2), str(demo_3),
        str(solution_1), str(solution_2), str(solution_3),
        execution_time
    )