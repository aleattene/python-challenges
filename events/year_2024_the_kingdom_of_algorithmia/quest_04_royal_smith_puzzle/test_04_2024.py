import os
from dotenv import load_dotenv
from .solution_04_2024 import solve_04_2024

load_dotenv()
environment = os.getenv("ENVIRONMENT")

filename_demo = "input_demo.txt"
filename = "input.txt"
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_demo = os.path.join(current_dir, filename_demo)
file_path = os.path.join(current_dir, filename)


def test_04_2024():
    results_demo = solve_04_2024(file_path_demo)
    assert results_demo == (10, 110, 8)
    if environment == "development":
        expected_results = (int(os.getenv("SOLUTION_01_04_2024")),
                            int(os.getenv("SOLUTION_02_04_2024")),
                            int(os.getenv("SOLUTION_03_04_2024")))
        results = solve_04_2024(file_path)
        assert expected_results == results
