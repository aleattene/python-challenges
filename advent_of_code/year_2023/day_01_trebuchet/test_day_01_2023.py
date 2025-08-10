import os
from dotenv import load_dotenv
from .solution_one_day_01_2023 import solve_day_01_2023_one
from .solution_two_day_01_2023 import solve_day_01_2023_two


load_dotenv()
environment = os.getenv("ENVIRONMENT")

filename_demo_one = "input_demo_one.txt"
filename_demo_two = "input_demo_two.txt"
filename = "input.txt"
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_demo_one = os.path.join(current_dir, filename_demo_one)
file_path_demo_two = os.path.join(current_dir, filename_demo_two)
file_path = os.path.join(current_dir, filename)


def test_day_01_2023():
    result_demo_1 = solve_day_01_2023_one(file_path_demo_one)
    assert result_demo_1 == 142
    result_demo_2 = solve_day_01_2023_two(file_path_demo_two)
    assert result_demo_2 == 281
    if environment == "development":
        expected_result_1 = int(os.getenv("SOLUTION_01_DAY_01_2023"))
        result_1 = solve_day_01_2023_one(file_path)
        assert expected_result_1 == result_1
        expected_result_2 = int(os.getenv("SOLUTION_02_DAY_01_2023"))
        result_2 = solve_day_01_2023_two(file_path)
        assert expected_result_2 == result_2