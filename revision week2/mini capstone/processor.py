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
    return[output]


def process_data(data):
    """
    Receives sensor data in JSON format, validates and prints a report
    :param data: Valid sensor data
    :return: report as a dictionary
    """
    report = dict()
    try:
        if valid_schema(data):
            report["total_readings"] = len(data["readings"])
            print(process_readings(data["readings"]))
    except InvalidSensorDataError as e:
        print(e.message)

    return report
