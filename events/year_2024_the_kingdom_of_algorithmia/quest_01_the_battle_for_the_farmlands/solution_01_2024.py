from utils.file_utils import get_input_file_path, read_input_file


def get_potions_from_enemies(enemies: str, chunk: int = 1) -> int:
    """
    Calculate the needed potions based on the enemies and the chunk size.
    :param enemies: a string representing the enemies.
    :param chunk: the size of the chunk to process (default is 1).
    :return: total number of potions needed.
    """
    # Validate the chunk size (if not in range 1 to 3, set it to 1)
    if not 1 <= chunk <= 3: chunk = 1
    # Define the potions for each enemy type
    enemy_potions: dict[str, int] = {'A': 0, 'B': 1, 'C': 3, 'D': 5, 'x': 0}
    # Initialize the total number of potions and process the enemies in chunks
    potions = 0

    # Split the enemies string into chunks of the specified size and calculate the potions needed for each chunk
    for i in range(0, len(enemies), chunk):
        enemy: list[str] = [enemies[i]]
        if chunk >= 2: enemy.append(enemies[i+1])
        if chunk == 3: enemy.append(enemies[i+2])

        # Count the number of 'x' characters in the chunk
        x_count: int = "".join(enemy).count('x')

        # Calculate the extra potions needed based on the number of 'x' characters
        extra_potions = 0
        if len(enemy) - x_count == 2: extra_potions = 2
        elif len(enemy) - x_count == 3: extra_potions = 6

        # Sum the potions needed for the current chunk
        potions += sum(enemy_potions[char] for char in enemy) + extra_potions

    # Return the total number of potions needed for enemies
    return potions

def solve_01_2024(filename: str) -> tuple[int, int, int]:
    """
    Solution of the Everybody Codes 2024/01.
    :param filename: filename that contains the input data
    :return: tuple with the number of potions for each part of the quest (1,2, and 3)
    """
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        # Read the input file
        data = read_input_file(input_file_path)
    except Exception as error:
        raise RuntimeError(f"Error: {error}")

    # Split the data into three parts
    data_1, data_2, data_3 = data[0], data[1], data[2]

    # Calculate the total number of potions for each part
    potions_1 = get_potions_from_enemies(data_1)
    potions_2 = get_potions_from_enemies(data_2, 2)
    potions_3 = get_potions_from_enemies(data_3, 3)

    # Return the total number of potions for each part (1, 2, and 3)
    return potions_1, potions_2, potions_3

if __name__ == "__main__":
    # Import function to print results
    import time
    from utils.file_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2, demo_3 = solve_01_2024("input_demo.txt")
    start_time = time.time()
    solution_1, solution_2, solution_3 = solve_01_2024("input.txt")
    end_time = time.time()

    # Calculate execution time in milliseconds
    execution_time: int = int((end_time - start_time) * 1000)

    # Print results in a formatted table (using rich)
    print_day_results(
        "2024", "01",
        str(demo_1), str(demo_2), str(demo_3),
        str(solution_1), str(solution_2), str(solution_3),
        execution_time
    )