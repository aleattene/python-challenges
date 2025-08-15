import os
from dotenv import load_dotenv
from .solution_03 import solve_03

load_dotenv()
environment = os.getenv("ENVIRONMENT")

filename_demo: str = "input_demo.txt"
filename: str = "input.txt"
current_dir: str = os.path.dirname(os.path.abspath(__file__))
file_path_demo: str = os.path.join(current_dir, filename_demo)
file_path: str = os.path.join(current_dir, filename)


def test_03() -> None:
    results_demo: tuple[int, int, int] = solve_03(file_path_demo)
    assert results_demo == (1310, 14, 13659)
    if environment == "development":
        expected_results = (int(os.getenv("SOLUTION_01_03")),
                            int(os.getenv("SOLUTION_02_03")),
                            int(os.getenv("SOLUTION_03_03")))
        results: tuple[int, int, int] = solve_03(file_path)
        assert expected_results == results