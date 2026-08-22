from pathlib import Path
from contract_review import load_sensor_data, generate_report, updated_process_reading, valid_schema
from exceptions import InvalidSensorDataError, InvalidQuantumReadingError


def run_app():
    """
    Main application orchestrating module
    :return: None
    """
    data_file = Path.cwd() / "data" / "sensor_data.json"
    try:
        input_data = load_sensor_data(data_file)
        if valid_schema(input_data):
            output = updated_process_reading(input_data)
            generate_report(output)
    except (InvalidSensorDataError, InvalidQuantumReadingError, FileNotFoundError) as e:
        print(str(e))


if __name__ == "__main__":
    run_app()
