import json
from exceptions import InvalidSensorDataError, InvalidQuantumReadingError
from validator import valid_schema, valid_reading


def process_readings(sensor_readings):
    """
    Square the readings and return
    :param sensor_readings:
    :return: A list of squared readings if valid value otherwise reason for invalid value
    """
    output = []
    for reading in sensor_readings:
        try:
            output.append(valid_reading(reading))
        except InvalidQuantumReadingError as e:
            output.append(e.message)
    return output


def process_data(data):
    """
    Receives sensor data in JSON format, validates and prints a report
    :param data: Valid sensor data
    :return: report as a dictionary
    """
    results = {
        "device_id": "",
        "backend": "",
        "total_readings": "",
        "valid_readings": [],
        "invalid_readings": []
    }
    try:
        if valid_schema(data):
            results["device_id"] = data["device_id"]
            results["backend"] = data["backend"]
            results["total_readings"] = len(data["readings"])
            for reading, result in zip(data["readings"], process_readings(data["readings"])):
                if isinstance(result, float):
                    results["valid_readings"].append((reading, result))
                else:
                    results["invalid_readings"].append((reading, result.message))
    except InvalidSensorDataError as e:
        print(e.message)

    return results


def process_file(data_file):
    """
    Reads the file and returns the results
    :return:
    """
    with open(data_file, 'r') as file:
        try:
            data = json.load(file)
            return process_data(data)
        except json.JSONDecodeError:
            print('Data in sensor_data.json is not a valid JSON')
