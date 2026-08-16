from pathlib import Path

data_file = Path.cwd()/"quantum_sensor_data.txt"

print(data_file)
print(data_file.name)
print(data_file.suffix)
print(data_file.exists())

curr_wd = Path.cwd()
print(curr_wd)

home_dir = Path.home()
print(home_dir)

parent_dir = curr_wd.parent
print(parent_dir)

print(type(data_file))
print(type(parent_dir))

data_dir = curr_wd/"data"
data_dir.mkdir(parents=True, exist_ok=True)

# Writing file.
sensor_file = data_dir/"quantum_sensor_data.txt"
sensor_file.write_text("0.81")
# write_text overwrites the content that is already present.
sensor_file.write_text("0.25")

with open(sensor_file, 'r') as file:
    print(file.readlines())

sensor_data = ["0.25", '0.81', "invalid", "None", "-1.2", "0.64"]
sensor_text = "\n".join(sensor_data)
sensor_file.write_text(sensor_text)

with open(sensor_file, 'r') as file:
    print(file.readlines())

# Creating random files in the directory
sensor_week1 = data_dir/"sensor_week1_data.txt"
sensor_week2 = data_dir/"sensor_week2_data.txt"
sensor_week3 = data_dir/"sensor_week3_data.txt"
sensor_week4_log = data_dir/"sensor_week4_log"

sensor_week1.write_text("0.25\n1.22\nNone\n-0.04\n\n1.0\nabc")
sensor_week2.write_text("0.04\n1.00\n0.81")
sensor_week3.write_text("")
sensor_week4_log.write_text("No logs available for week4")


def filter_data(sensor_data_list) -> list:
    """
    Reads the list of sensor readings and returns valid sensor data in the range of [0,1]
    :param sensor_data_list: list of readings
    :return: list of valid readings
    """
    valid_values = []

    for reading in sensor_data_list:
        try:
            output = float(reading)
            if 0 <= output <= 1:
                valid_values.append(output)
        except (ValueError, TypeError):
            # Catching TypeError too, just in case a None value gets passed
            pass

    return valid_values


valid_readings = []
# Listing all the text files in the directory
text_files = data_dir.glob("*.txt")
for textfile in sorted(text_files):
    print(textfile.name)
    # Reading file and processing data
    try:
        with open(data_dir/textfile, 'r') as file:
            for output in filter_data(file.readlines()):
                valid_readings.append(output)
    except FileNotFoundError:
        print(f'File {data_dir/textfile} not found')
print(valid_readings)

# trying glob on non existing directory
not_a_dir = curr_wd/"non_existent_dir"

if not_a_dir.exists():
    print(f'{not_a_dir} exist')
else:
    print("Directory not found")

if not_a_dir.is_dir():
    print(f'{not_a_dir} is a directory')
else:
    print(f'{not_a_dir} is not a directory')

if not_a_dir.is_file():
    print(f'{not_a_dir} is a file')
else:
    print(f'{not_a_dir} is not a file')

# creating empty directory and running glob on it.
empty_dir = curr_wd/"empty_dir"
empty_dir.mkdir(parents=True, exist_ok=True)

if empty_dir.is_dir():
    print("Fetching files from empty directory")
    for filenames in empty_dir.glob("*"):
        print(filenames)

# glob returning empty
filtered_files = data_dir.glob("*")
print(len(list(filtered_files)))
