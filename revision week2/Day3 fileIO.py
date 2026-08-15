# Muscle memory practice
with open("data.txt", 'r') as file:
    content = file.read()
print(content)

lines = list(content.split('\n'))
print(lines)
print("------------\n")

with open("data.txt", 'r') as file:
    lines = file.readlines()
print(lines)
for line in lines:
    print(line.strip())
print("------------\n")

with open("data.txt", 'r') as file:
    print(type(file))
    for line in file:
        print(line.strip())
print("------------\n")


# Validation function
def sensor_data_validation(value: str) -> float | None:
    """
    Validates if the input can be converted into a non-negative float.
    returns a floatvalue if valid, otherwise None
    :param value: string
    :return: FloatValue | None
    """
    try:
        sensor_reading = float(value)
        return sensor_reading if sensor_reading >= 0 else None
    except ValueError:
        return None


# Read file contents and create a list
try:
    with open("quantum_sensor_data.txt", 'r') as file:
        readings = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    print("File quantum_sensor_data.txt is not found")
else:
    valid_readings = list(filter(sensor_data_validation, readings))
    invalid_reading = [reading for reading in readings if sensor_data_validation(reading) is None]
    print(valid_readings)
    print(invalid_reading)
    print("Summary report of the sensor readings")
    print(f"Total number of records : {len(readings)}")
    print(f"Count of valid readings : {len(valid_readings)}")
    print(f"Count of invalid reading: {len(invalid_reading)}")

# Reading an empty file
try:
    with open("empty_file.txt", "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    print("empty_file.txt not found")
else:
    print(lines)
