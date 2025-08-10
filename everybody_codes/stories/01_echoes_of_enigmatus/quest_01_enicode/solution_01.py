import os
from dotenv import load_dotenv
from utils.ec_utils import get_input_file_path, read_input_file

load_dotenv()
environment = os.getenv("ENVIRONMENT")


def get_enicode_remainders_sum(multiplier: int, iterations: int, module: int, score: int = 1) -> int:
    """
    This function calculates the sum of remainders for the Enicode operation.
    For optimization, it detects cycles in the progressive remainders (previous scores plus the current score)
    and uses them to reduce the number of iterations.
    :param multiplier: the number to be multiplied by the initial score
    :param iterations: the number of iterations to be executed
    :param module: the module to apply after each iteration
    :param score: the initial score to start with
    :return: the sum of progressive remainders after all iterations
    """
    # Initialize variables (scores to keep track of the progressive remainders, cycle_reminders_found to keep track of
    # cycle found, and iterations_sum to store the sum of iterations in cycles)
    scores: list[int] = []
    cycle_reminders_found: bool = False
    iterations_sum: int = 0

    # Loop until all iterations are completed
    while iterations > 0:
        # Calculate the new score and append it to the scores list
        score: int = (score * multiplier) % module
        scores.append(score)
        # If a cycle is not found yet, check if the current score is in the scores list, because if it is, it means
        # a cycle has been found.
        # So, we need to calculate the cycle length, the number of cycles that can be executed considering the remaining
        # iterations, and the sum of reminders in the cycle than can be used to calculate the iterations sum.
        # After that, we can normalize the iterations to the cycle length to optimize the calculation.
        if not cycle_reminders_found and score in scores[:-1]:
            prev_index: int = scores.index(score)
            cycle_length: int = len(scores) - prev_index - 1
            num_cycles: int = iterations // cycle_length
            # If the cycle length is 1, it means that the score is always the same, so we can just return the sum of
            # scores avoiding all remaining iterations, because they will not change the result.
            if cycle_length == 1:
                return sum(scores) + score * (iterations - 1)
            iterations %= cycle_length
            cycle_sum: int = sum(scores[prev_index: -1])
            iterations_sum: int = num_cycles * cycle_sum
            cycle_reminders_found: bool = True
        iterations -= 1
    # Return the sum of scores plus the iterations sum if a cycle was found, otherwise just return the sum of scores.
    return sum(scores) + iterations_sum


def get_enicode_remainders_list(multiplier: int, iterations: int, module: int, limit: int = 0, score: int = 1) -> int:
    """
    This function calculate the Enicode operation and returns the joined string of remainders (with or without limit).
    :param multiplier: the number to be multiplied by the initial score
    :param iterations: the number of iterations to be executed
    :param module: the module to apply after each iteration
    :param limit: the limit of remainders to keep in the list (0 means no limit)
    :param score: the initial score to start with
    :return: the final result after all iterations
    """
    # Initialize variables (reminders_list to keep track of the remainders, and a dictionary to keep track of the
    # reminders strings and their iterations to consider in the next step of the algorithm for cycle detection)
    remainders_list: list[int] = []
    reminders_string_to_iteration: dict[str, int] = {}

    # Loop until all iterations are completed
    while iterations > 0:
        # Create a string from the current remainders list insert it at the beginning of the remainders list
        score: int = (score * multiplier) % module
        remainders_list.insert(0, score)

        # If the limit is set and the remainders list is longer than the limit, remove the last element
        if limit and len(remainders_list) == limit + 1:
            remainders_list.pop()
            # Create a candidate string from the remainders list
            current_reminders_string: str = "".join(map(str, remainders_list))

            # If the current reminders string is already in the dictionary, it means that a cycle has been found, than
            # we can calculate the cycle length and reduce the iterations to the cycle length.
            if current_reminders_string in reminders_string_to_iteration:
                prev_iterations: int = reminders_string_to_iteration[current_reminders_string]
                cycle_length: int = prev_iterations - iterations
                iterations: int = iterations % cycle_length
            # Add the current reminders string to the dictionary with the current iterations
            reminders_string_to_iteration[current_reminders_string] = iterations
        iterations -= 1
    # Join the remainders list into a string and return it as an integer
    return int("".join(map(str, remainders_list)))


def create_variables_value_dict(line: str) -> dict[str, int]:
    """
    This function creates a dictionary with the variable names as keys and their values as integers.
    :param line: a string containing the variables and their values ("A=1 B=2 C=3")
    :return: a dictionary with the variable names as keys and their values as integers ({"A": 1, "B": 2, "C": 3})
    """
    variables: dict = {}
    for variable in line.replace("=", "").split(' '):
        variables[variable[0]] = int(variable[1:])
    return variables


def solve_01(filename: str) -> tuple[int, int, int]:
    """
    Solution of the Everybody Codes Stories: Echoes of Enigmatus - Quest 01: Enicode.
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

    # Solution Part 1
    highest_remainder_1 = 0
    for line in data_1:
        variables_1 = create_variables_value_dict(line)
        eni_ops = get_enicode_remainders_list(variables_1['A'],variables_1['X'], variables_1['M'])
        eni_ops += get_enicode_remainders_list(variables_1['B'],variables_1['Y'], variables_1['M'])
        eni_ops += get_enicode_remainders_list(variables_1['C'],variables_1['Z'], variables_1['M'])
        if eni_ops > highest_remainder_1: highest_remainder_1 = eni_ops

    # Solution Part 2
    highest_remainder_2 = 0
    for line in data_2:
        variables_2 = create_variables_value_dict(line)
        eni_ops = get_enicode_remainders_list(variables_2['A'], variables_2['X'], variables_2['M'], 5)
        eni_ops += get_enicode_remainders_list(variables_2['B'], variables_2['Y'], variables_2['M'], 5)
        eni_ops += get_enicode_remainders_list(variables_2['C'], variables_2['Z'], variables_2['M'], 5)
        if eni_ops > highest_remainder_2: highest_remainder_2 = eni_ops

    # Solution Part 3
    highest_remainder_3 = 0
    for n, line in enumerate(data_3):
        # Only print progress in development environment (every 50 lines)
        if environment == "development" and n % 49 == 0:
                print(f"Processing line {n + 1}/{len(data_3)}")
        variables_3 = create_variables_value_dict(line)
        eni_ops = get_enicode_remainders_sum(variables_3['A'], variables_3['X'], variables_3['M'])
        eni_ops += get_enicode_remainders_sum(variables_3['B'], variables_3['Y'], variables_3['M'])
        eni_ops += get_enicode_remainders_sum(variables_3['C'], variables_3['Z'], variables_3['M'])
        if eni_ops > highest_remainder_3: highest_remainder_3 = eni_ops

    # Return the highest remainders for each part of the quest
    return highest_remainder_1, highest_remainder_2, highest_remainder_3


if __name__ == "__main__":
    # Import function to print results
    import time
    from utils.ec_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2, demo_3 = solve_01("input_demo.txt")
    start_time: float = time.time()
    solution_1, solution_2, solution_3 = solve_01("input.txt")
    end_time: float = time.time()

    # Calculate execution time in milliseconds
    execution_time: int = int((end_time - start_time) * 1000)

    # Print results in a formatted table (using rich)
    print_day_results(
        "Stories", "01",
        str(demo_1), str(demo_2), str(demo_3),
        str(solution_1), str(solution_2), str(solution_3),
        execution_time
    )