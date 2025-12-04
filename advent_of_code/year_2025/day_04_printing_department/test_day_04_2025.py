import os
from dotenv import load_dotenv
from .solution_day_04_2025 import solve_day_04_2025

load_dotenv()
environment: str = os.getenv("ENVIRONMENT")

filename_demo: str = "input_demo.txt"
filename: str = "input.txt"
current_dir: str = os.path.dirname(os.path.abspath(__file__))
file_path_demo: str = os.path.join(current_dir, filename_demo)
file_path: str = os.path.join(current_dir, filename)


def test_day_04_2025():
    results_demo: tuple[int, int] = solve_day_04_2025(file_path_demo)
    assert results_demo == (13, 43)
    if environment == "development":
        expected_results = (int(os.getenv("SOLUTION_01_DAY_04_2025")),
                            int(os.getenv("SOLUTION_02_DAY_04_2025")))
        results: tuple[int, int] = solve_day_04_2025(file_path)
        assert expected_results == results
