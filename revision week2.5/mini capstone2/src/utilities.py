import json
from exceptions import InvalidContentError


def get_experiment_data(file_path):
    """
    Reads the data from the file path and returns it.
    :param file_path: Quantum experiment results folder
    :return: read data and return the json.
    """

    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        raise InvalidContentError()
