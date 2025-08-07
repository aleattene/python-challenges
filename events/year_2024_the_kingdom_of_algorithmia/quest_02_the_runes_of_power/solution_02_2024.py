import re
from utils.file_utils import (
    get_input_file_path, read_input_file,
    from_linear_to_circular_string,
    transpose_matrix_of_strings
)

def get_words_with_words_reversed(words: list[str]) -> set[str]:
    """
    This function takes a list of strings and returns a set that contains
    the original string and their reversed versions.
    :param words: list of strings
    :return: set of original strings with their reversed versions
    """
    if not words: return set()
    reversed_words: list[str] = [word[::-1] for word in words]
    reversed_words.extend(words)
    return set(reversed_words)

def get_covered_indexes(text: str, words_to_search: set[str]) -> set[int]:
    """
    This function takes a text and a set of words to search for, and returns a set of indexes
    that are covered by the occurrences of those words in the text.
    :param text: a string in which to search for words
    :param words_to_search: a list of string words to search for in the text
    :return: a set of indexes that are covered by the occurrences of the words in the text
    """
    covered_indexes: set[int] = set()
    for word in words_to_search:
        pattern_with_overlap: str = f'(?={re.escape(word)})'
        occurrences = re.finditer(pattern_with_overlap, text)

        if not occurrences: continue
        for occurrence in occurrences:
            start_index: int = occurrence.start()
            end_index: int = start_index + len(word)
            covered_indexes.update(range(start_index, end_index))
    return covered_indexes


def solve_02_2024(filename: str) -> tuple[int, int, int]:
    """
    Solution of the Everybody Codes 2024/02.
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
    words_1: list[str] = data_1[0].split(":")[1].split(",")
    text_1: str = data_1[1]
    # Count occurrences of each word in the text
    occurrences_1: int = sum(text_1.count(word) for word in words_1)

    # Solution Part 2
    words_2: list[str] = data_2[0].split(":")[1].split(",")
    words_2: set[str] = get_words_with_words_reversed(words_2)
    text_2: list[str] = data_2[1:]
    # Count lines_indexes (symbols) covered by words in the text
    symbols_2: int = 0
    for text in text_2:
        covered_indexes_2: set[int] = get_covered_indexes(text, words_2)
        symbols_2 += len(covered_indexes_2)

    # Solution Part 3
    words_3: list[str] = data_3[0].split(":")[1].split(",")
    # Get words with their reversed versions to check words occurrences in all directions (left, right, up, down)
    words_3: set[str] = get_words_with_words_reversed(words_3)
    text_3: list[str] = data_3[1:]
    lines_normalizer: int = len(text_3[0])
    # Initialize a set to store all cols_indexes (symbols) covered by words in the text
    covered_indexes: set[int] = set()

    # Convert each line to a circular string and create a new matrix (to check words in circular horizontal lines
    matrix_3: list[str] = []
    for line in text_3:
        line_circular: str = from_linear_to_circular_string(line)
        matrix_3.append(line_circular)

    # Find lines_indexes (symbols) covered by words in the circular text and append them to the set covered_indexes
    counter: int = 0
    for text in matrix_3:
        covered_indexes_3_by_lines: set[int] = get_covered_indexes(text, words_3)
        # Normalize the indexes from circular lines to unique row with unique indexes
        covered_indexes_3_by_lines: set[int] = {
            (index % lines_normalizer) + (counter * lines_normalizer) for index in covered_indexes_3_by_lines
        }
        # Add the normalized indexes to the covered_indexes set
        for index in covered_indexes_3_by_lines:
            covered_indexes.add(index)
        counter += 1

    # After processing all lines, we need to transpose the matrix to check vertical words (no circular effect)
    matrix_3_transposed: list[str] = transpose_matrix_of_strings(text_3)
    counter: int =  0
    for text in matrix_3_transposed:
        covered_indexes_3_by_columns: set[int] = get_covered_indexes(text, words_3)
        # Normalize the indexes from transposed columns to unique row with unique indexes
        covered_indexes_3_by_columns: set[int]  = {
            (index * lines_normalizer) + counter for index in covered_indexes_3_by_columns
        }
        for index in covered_indexes_3_by_columns:
            covered_indexes.add(index)
        counter += 1
    # Count the unique symbols covered by words in the text
    symbols_3: int = len(covered_indexes)

    # Return the results for all three parts
    return occurrences_1, symbols_2, symbols_3


if __name__ == "__main__":
    # Import function to print results
    import time
    from utils.file_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2, demo_3 = solve_02_2024("input_demo.txt")
    start_time: float = time.time()
    solution_1, solution_2, solution_3 = solve_02_2024("input.txt")
    end_time: float = time.time()

    # Calculate execution time in milliseconds
    execution_time: int = int((end_time - start_time) * 1000)

    # Print results in a formatted table (using rich)
    print_day_results(
        "2024", "02",
        str(demo_1), str(demo_2), str(demo_3),
        str(solution_1), str(solution_2), str(solution_3),
        execution_time
    )