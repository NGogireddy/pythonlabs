import json
from pathlib import Path

data_dir = Path.cwd()/"data"
print(data_dir)

input_file = data_dir/"sensor_data.json"

with open(input_file, "r") as file:
    data = json.load(file)
print(data)

# challenge 1: Investigating data
print(f'Device ID : {data["device_id"]}')
print(f'Location  : {data["location"]}')
print(f'Readings  : {data["readings"]}')


# challenge 2: Cleansing data
def process_sensor_reading(readings) -> list[float]:
    output = []
    for reading in readings:
        try:
            number = float(reading)
        except (ValueError, TypeError):
            pass
        else:
            if 0 <= number <= 1:
                output.append(number**2)
    return output


print(process_sensor_reading(data["readings"]))

# challenge 3: Handling Key error
try:
    print(data["device_name"])
except KeyError:
    print('device_name not found')

# challenge 4: Handling invalid json
invalid_file = data_dir/"invalid_json.json"
with open(invalid_file, 'r') as file:
    try:
        invalid_data = json.load(file)
    except json.JSONDecodeError as e:
        print(f'json.decoder.JSONDecodeError: {e}')
    else:
        print(invalid_data)
