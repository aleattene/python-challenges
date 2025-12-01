from utils.aoc_utils import get_input_file_path, read_input_file

def get_direction_from_rotation(rotation: str) -> str:
    """
    Extract direction from rotation instruction.
    :param rotation: The rotation instruction.
    :return: A direction 'L', 'R', or error message.
    """
    direction: str = rotation[0]
    if direction not in ('L', 'R'):
        raise NameError("Invalid direction in rotation instruction. The direction must be 'L' or 'R'.")
    return direction


def get_password(rotations: list[str], position: int = 50) -> tuple[int, int] | str:
    """
    Calculate the password based on the current position and mode.
    :param rotations: List of rotation instructions.
    :param position: The current position on the dial.
    :return: The calculated passwords.
    """
    # Initialize passwords
    password_1: int = 0
    password_2: int = 0

    # Iterate through each rotation instruction and through each step
    for rotation in rotations:
        # Identify direction and steps from the rotation instruction
        direction = get_direction_from_rotation(rotation)
        steps = int(rotation[1:])
        for _ in range(steps):
            # Increment or decrement position based on direction
            position += 1 if direction == 'R' else -1
            position %= 100
            # For part 2 check if position is 0
            if position == 0: password_2 += 1
        # For part 1 check if position is 0
        if position == 0: password_1 += 1

    # Return the calculated passwords
    return password_1, password_2

def solve_day_01_2025(filename: str) -> tuple[int, int]:
    """
    Solution of the Advent of Code 2025 Day 01 - Secret Entrance.
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
    # Initial position on the dial
    position: int = 50

    # Calculate the passwords for part 1 and part 2
    try:
        password_1, password_2 = get_password(data, position)
    except NameError as error:
        raise RuntimeError (f"Error: {error}")
    except ValueError:
        raise RuntimeError("Error: Invalid step value in rotation instruction. Steps must be integers.")
    except Exception as error:
        raise RuntimeError(f"Error: Something went wrong during password calculation. {error}")

    # Return the calculated passwords
    return password_1, password_2


if __name__ == "__main__":
    # Import function to print results
    import time
    from utils.aoc_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2 = solve_day_01_2025("input_demo.txt")
    start_time = time.time()
    solution_1, solution_2 = solve_day_01_2025("input.txt")
    end_time = time.time()

    # Calculate execution time in milliseconds
    execution_time: int = int((end_time - start_time) * 1000)

    # Print results in a formatted table (using rich)
    print_day_results(
        "2025", "01",
        str(demo_1), str(demo_2),
        str(solution_1), str(solution_2),
        execution_time
    )

