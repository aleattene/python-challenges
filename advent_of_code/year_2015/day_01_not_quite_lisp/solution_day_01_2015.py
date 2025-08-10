import os
from dotenv import load_dotenv
from utils.ec_utils import get_input_file_path, read_input_file

load_dotenv()
environment = os.getenv("ENVIRONMENT")


def solve_01_2015(filename: str) -> tuple[int, int]:
    """
    Solution of the Advent of Code 2015, Day 01: Not Quite Lisp.
    :param filename: filename that contains the input data
    :return: solution for each part (1, 2)
    """
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        # Read the input files
        data: str = read_input_file(input_file_path)[0]
    except Exception as error:
        raise RuntimeError(f"Error: {error}")

    # Solution Part 1
    num_positions = data.count('(') - data.count(')')

    # Solution Part 2
    floor = 0
    elevator_map = {
        "(": 1,
        ")": -1
    }
    num_position = 0
    for position, symbol in enumerate(data, start=1):
        if symbol in elevator_map:
            floor += elevator_map[symbol]
        if floor < 0:
            num_position = position
            break
    #
    return num_positions, num_position




if __name__ == "__main__":
    # Import function to print results
    import time
    from utils.aoc_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2 = solve_01_2015("input_demo.txt")
    start_time: float = time.time()
    solution_1, solution_2 = solve_01_2015("input.txt")
    end_time: float = time.time()

    # Calculate execution time in milliseconds
    execution_time: int = int((end_time - start_time) * 1000)

    # Print results in a formatted table (using rich)
    print_day_results(
        "2015", "01",
        str(demo_1), str(demo_2),
        str(solution_1), str(solution_2),
        execution_time
    )