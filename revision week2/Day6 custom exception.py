import json
from pathlib import Path


class InvalidQuantumReadingError(Exception):
    """Raised when the reading sent is not a valid quantum reading"""

    def __init__(self, reading, device_id):
        self.reading = reading
        self.device_id = device_id
        self.message = f"Error in reading: {reading} from the device: {device_id}"
        super().__init__(self.message)


class InvalidSensorDataError(Exception):
    """Raised when the sensor data structure is invalid."""

    def __init__(self, data):
        self.data = data
        self.message = f'{data} is not a valid (json) sensor data'
        super().__init__(self.message)


# challenge 1 and challenge 2
def validate_reading(value, device_id):
    try:
        output = float(value)
    except (ValueError, TypeError):
        raise InvalidQuantumReadingError(value, device_id)

    if 0 <= output <= 1:
        return output
    raise InvalidQuantumReadingError(value, device_id)


def process_line(data):
    try:
        for value in data["readings"]:
            try:
                print(validate_reading(value, data["device_id"]))
            except InvalidQuantumReadingError as e:
                print(e.message)
    except KeyError as e:
        print(f'readings/device_id key is missing from data')



# challenge 3
sensor_file = Path.cwd()/"data/sensor_data.json"
with open(sensor_file, 'r') as file:
    data = json.load(file)
    print(data)

for reading in data["readings"]:
    try:
        print(validate_reading(reading, data["device_id"]))
    except InvalidQuantumReadingError as e:
        print(e.message)

# challenge 4
sensor_lines_file = Path.cwd()/"data/sensor_stream.jsonl"
with open(sensor_lines_file, 'r') as file:
    lines = file.readlines()

for line in lines:
    try:
        process_line(json.loads(line.strip()))
    except json.JSONDecodeError as e:
        error_context = InvalidSensorDataError(line.strip())
        print(f'Warning: {error_context}')
