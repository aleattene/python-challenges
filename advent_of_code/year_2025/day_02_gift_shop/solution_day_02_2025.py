from utils.aoc_utils import get_input_file_path, read_input_file, is_prime


def is_valid_id(id_string: str, id_length: int) -> bool:
    """
    Check if the given ID is valid based on specific criteria.
    :param id_string: The ID value to check.
    :param id_length: The length of ID.
    :return: True if the ID is valid, False otherwise.
    """
    # An ID is valid if it has an even number of digits and the first half matches the second half
    if id_length % 2 != 0: return False

    # Check if the first half matches the second half (123123 -> 123 and 123)
    i_mid: int = id_length // 2
    substring_start: str = id_string[:i_mid]
    return id_string.endswith(substring_start, i_mid)


def is_valid_substring_id(id_string: str, id_length: int) -> bool:
    """
    Check if the given ID can be divided into equal substrings.
    :param id_string: The ID value to check.
    :param id_length: The length of ID.
    :return: True if the ID can be divided into equal substrings, False otherwise.
    """
    # Check for prime length strings, which cannot be divided into equal substrings (except for all identical chars)
    if is_prime(id_length):
        return id_string == id_string[0] * id_length

    # Check each divisor to see if the string can be divided into equal substrings
    for divisor in range(2, id_length // 2 + 1):
        # Only consider divisors that evenly divide the length
        if id_length % divisor != 0: continue

        # Check if all substrings are identical
        substring_length: int = id_length // divisor
        substring: str = id_string[:substring_length]
        if substring * divisor == id_string: return True

    # If no valid id found, return False
    return False


def solve_day_02_2025(filename: str) -> tuple[int, int]:
    """
    Solution of the Advent of Code 2025 Day 02 - Gift Shop.
    :param filename: The name file containing the input data.
    :return: The results for part 1 and part 2.
    """
    try:
        # Create the absolute path of the input file
        input_file_path: str = get_input_file_path(__file__, filename)
        # Read the input file
        data: list[str] = read_input_file(input_file_path)[0].split(",")
    except Exception as error:
        raise RuntimeError(f"Error: {error}")

    # Initialize counters for invalid IDs (part 1 and part 2)
    invalid_ids_1: int = 0
    invalid_ids_2: int = 0

    # Process each ID range in the input data
    for id_sequence in data:
        start: int = int(id_sequence.split("-")[0])
        end: int = int(id_sequence.split("-")[1])

        # Iterate through each ID in the range
        for current_id in range(start, end + 1):
            # Part 1
            id_string: str = str(current_id)
            id_length: int = len(id_string)
            if is_valid_id(id_string, id_length): invalid_ids_1 += current_id
            # Part 2
            if is_valid_substring_id(id_string, id_length): invalid_ids_2 += current_id

    # Return the counts of invalid IDs for part 1 and part 2
    return invalid_ids_1, invalid_ids_2


if __name__ == "__main__":
    # Import function to print results
    import time
    from utils.aoc_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2 = solve_day_02_2025("input_demo.txt")
    start_time = time.time()
    solution_1, solution_2 = solve_day_02_2025("input.txt")
    end_time = time.time()

    # Calculate execution time in milliseconds
    execution_time: int = int((end_time - start_time) * 1000)

    # Print results in a formatted table (using rich)
    print_day_results(
        "2025", "02",
        str(demo_1), str(demo_2),
        str(solution_1), str(solution_2),
        execution_time
    )

