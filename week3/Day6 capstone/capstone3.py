import ast
from pathlib import Path
from collections import Counter, namedtuple, defaultdict


"""
Use Counter to get the total count of each state
Use `defaultdict` for at least one meaningful grouping operation.
Use `namedtuple` for one appropriate internal record.

results = [
    {"state": "00", "count": 482},
    {"state": "11", "count": 498},
    {"state": "01", "count": 12},
    {"state": "10", "count": 8},
    {"state": "00", "count": 485},
    {"state": "11", "count": 495},
    {"state": "01", "count": 15},
    {"state": "10", "count": 5},
]
"""


class InvalidResultError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


counter1 = Counter([(2, 2), (3, 1), (2, 2), (3, 5)])
print(counter1)

Result = namedtuple("Result", ["state", "count"])
summary = defaultdict(int)


def get_file_path():
    source_path = Path(__file__).resolve()
    return source_path.parent / "results"


def get_results(file_location):
    with open(file_location, 'r') as file:
        data = file.read()
    return data


def is_valid_result(result):
    if "state" in result and "count" in result:
        if isinstance(result["state"], str) and isinstance(result["count"], int):
            return True
    raise InvalidResultError("Not a valid result")


def process_result(result):
    result_tup = Result(**result)
    summary[result_tup.state] += result_tup.count


file_path = get_file_path()
results = get_results(file_path)
result_list = ast.literal_eval(results)
for result in result_list:
    try:
        if is_valid_result(result):
            process_result(result)
    except InvalidResultError:
        print(f'result: {result} is not valid')
print(summary)
