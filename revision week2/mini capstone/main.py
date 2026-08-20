import json
from pathlib import Path
from processor import process_data


def run_app():
    """
    Main application orchestrating module
    :return: None
    """
    data_file = Path.cwd() / "data" / "sensor_data.json"

    if data_file.exists():
        with open(data_file, 'r') as file:
            try:
                data = json.load(file)
                final_report = process_data(data)
                print(final_report)
            except json.JSONDecodeError:
                print('Data in sensor_data.json is not a valid JSON')
    else:
        print(f'Sensor_data file "{data_file}" does not exist ')


if __name__ == "__main__":
    run_app()
