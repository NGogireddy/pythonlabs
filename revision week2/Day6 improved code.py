import json
from pathlib import Path


class InvalidQuantumReadingError(Exception):
    """Raised when a quantum sensor reading is invalid."""

    def __init__(self, reading, device_id):
        self.reading = reading
        self.device_id = device_id
        self.message = f'{device_id} sent invalid reading: {reading}'
        super().__init__(self.message)


class InvalidSensorDataError(Exception):
    """Raised when the format of the sensor data is invalid"""

    def __init__(self, data):
        self.data = data
        self.message = f'{data} is not in the valid format'
        super().__init__(self.message)


# challenge 1 & 2
def validate_reading(value, device):
    """Validates the reading from the device and returns it if valid"""
    try:
        output = float(value)
    except (ValueError, TypeError):
        raise InvalidQuantumReadingError(value, device)

    if 0 <= output <= 1:
        return output
    raise InvalidQuantumReadingError(value, device)


def process_json(data):
    """Validates the sensor data"""
    if "device_id" not in data or  "readings" not in data:
        raise KeyError("device_id/readings key is missing")

    for reading in data["readings"]:
        try:
            print(validate_reading(reading, data["device_id"]))
        except InvalidQuantumReadingError as e:
            print(e.message)


# challenge 3
sensor_file = Path.cwd() / "data" / "sensor_data.json"
data = ""
if sensor_file.exists():
    try:
        with open(sensor_file, 'r') as file:
            data = json.load(file)
            process_json(data)
    except (json.JSONDecodeError, KeyError) as e:
        error_context = InvalidSensorDataError(data)
        print(error_context)
else:
    print('Sensor file doesn\'t exist')

# challenge 4
sensor_file2 = Path.cwd() / "data" / "sensor_stream.jsonl"
if sensor_file2.exists():
    # process it
    with open(sensor_file2, 'r') as file:
        lines = file.readlines()
    for line_no, data in enumerate(lines, start=1):
        try:
            sensor_data = json.loads(data.strip())
            process_json(sensor_data)
        except (json.JSONDecodeError, KeyError) as e:
            error_context = InvalidSensorDataError(data)
            print(f'json {data} in line number: {line_no} is not a valid schema. {error_context}')
else:
    print("Sensor stream file doesn't exist")

# empty file check
empty_file = Path.cwd() / "empty_file.txt"
if empty_file.exists():
    empty_data = ""
    try:
        with open(empty_file, 'r') as file2:
            empty_data = json.load(file2)
            process_json(empty_data)
    except (json.JSONDecodeError, KeyError) as e:
        print("Exception handle of empty file: ")
        error_context = InvalidSensorDataError(empty_data)
        print(error_context)
else:
    print('Empty file doesn\'t exist')
