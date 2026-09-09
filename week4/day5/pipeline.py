import inspect
import json
from pathlib import Path
from datetime import datetime


"""
## Drill — Trace the Pipeline

Consider:

numbers = range(10)

pipeline = (
    number * 2
    for number in numbers
    if number % 2 == 0
)

print(next(pipeline))
print(next(pipeline))

Answers: Before executing the code
1. What values are produced?
0 alone is produced

2. When does multiplication happen?
It happens only when number is even.

3. Are all values processed before the first `next()`?
No, they are processed one after the other.

4. What happens if the consumer stops after two values?
The pipeline generator will be in PAUSED state.
"""

numbers = range(10)

pipeline = (
    number * 2
    for number in numbers
    if number % 2 == 0
)

print(next(pipeline))
print(next(pipeline))
print(inspect.getgeneratorstate(pipeline))
"""
Answers: After executing the code
1. What values are produced?
0 and 4 are produced, the generator expression loops through the numbers until an output is generated.

2. When does multiplication happen?
It happens only when number is even.

3. Are all values processed before the first `next()`?
No, they are processed one after the other.

4. What happens if the consumer stops after two values?
The pipeline generator will be in SUSPENDED state.
"""

"""
Study:
- chaining generators : It is similar to the example above range yeilds numbers one after the other and for each number
pipeline does the processing one after the other. 

- generator pipelines : Once the generators are chained it becomes a generator pipeline. 

- lazy filtering : Filtering done and returns only one item when required.
 
- lazy transformation : Transformation is done on the object and returned lazily. 

- consumers such as `sum()`, `list()`, `any()`, `all()` : sum, any and all are lazy operations and list is the 
materialization operation.

"""


def is_valid_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def get_experiment_data():
    data_file_name = Path(__file__).resolve().parent / "experiment_results"
    with open(data_file_name, 'r') as file:
        for line in file:
            yield line


def validate_results(raw_lines):
    result = {}
    for file_content in raw_lines:
        try:
            file_content = file_content.strip().rstrip(',')
            result = json.loads(file_content)
        except json.JSONDecodeError:
            print(f"Invalid experiment result: {file_content}")
        if "status" in result and "sensor_reading" in result:
            if result["status"] == 'OK':
                try:
                    if is_valid_float(result["sensor_reading"]) and result["status"] == "OK":
                        yield result
                except ValueError:
                    print(f"Invalid sensor_reading: {result['sensor_reading']}")


def transform_result(validated_results):
    result = {}
    for valid_result in validated_results:
        result["experiment_id"] = valid_result["experiment_id"]
        result["sensor_reading"] = float(valid_result["sensor_reading"])
        result["timestamp"] = datetime.strptime(valid_result["timestamp"], "%Y-%m-%d %H:%M:%S")
        yield result

raw_stream = get_experiment_data()
validated_stream = validate_results(raw_stream)
transformed_stream = transform_result(validated_stream)
print(next(transformed_stream))
print(next(transformed_stream))
print(next(transformed_stream))

"""
Reflection: 
I have struggled today to understand the assignment and implement it. I have got ideas on how to use counter for this 
project but finding hard on how to implement it. I took some help from google and finished the work today. 
I couldn't continue with the test cases today. I will resume tomorrow. 
"""
