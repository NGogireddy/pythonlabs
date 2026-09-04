import ast
from pathlib import Path
from collections import Counter, namedtuple
from itertools import combinations, permutations


Result = namedtuple("Result", ["state", "count"])


class InvalidResultError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


def get_quantum_results():
    source_path = Path(__file__).resolve()
    file_path = source_path.parent / "results"
    content = ''
    if file_path.exists():
        with open(file_path, 'r') as file:
            content = file.read()
    return content


def is_valid_result(result):
    if "state" in result and "count" in result:
        if not isinstance(result["state"], str):
            raise InvalidResultError(f"State is not a string in {result}")
        if not isinstance(result["count"], int) or result["count"] < 0:
            raise InvalidResultError(f"Count is not a string in {result}")
    return True


def process_results(data):
    result_list = ast.literal_eval(data)
    state_counts = Counter()
    for result in result_list:
        try:
            if is_valid_result(result):
                res = Result(result["state"], result["count"])
                state_counts[res.state] += res.count
        except InvalidResultError as e:
            print(f'{result} is not a valid result')
    return(state_counts)


def run_app():
    print("App started")
    quantum_data = get_quantum_results()
    summary = {}
    if quantum_data:
        summary = process_results(quantum_data)
    print(summary)

    qubit_indices = list(range(2))
    qubit_combinations = list(combinations(qubit_indices, 2))
    print(f"\nPossible Qubit Pairs (combinations) for 2-qubit system:\n", qubit_combinations)

    qubit_permutations = list(permutations(qubit_indices, 2))
    print(f"\nPossible Qubit Pairs (permutations) for 2-qubit system:\n", qubit_permutations)


if __name__ == "__main__":
    run_app()
