import os
from dotenv import load_dotenv
from .solution_01 import solve_01

load_dotenv()
environment = os.getenv("ENVIRONMENT")

filename_demo = "input_demo.txt"
filename = "input.txt"
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_demo = os.path.join(current_dir, filename_demo)
file_path = os.path.join(current_dir, filename)


def test_01():
    results_demo = solve_01(file_path_demo)
    assert results_demo == (11611972920, 11051340, 3279640)
    if environment == "development":
        expected_results = (int(os.getenv("SOLUTION_01_01")),
                            int(os.getenv("SOLUTION_02_01")),
                            int(os.getenv("SOLUTION_03_01")))
        results = solve_01(file_path)
        assert expected_results == results