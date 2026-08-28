import json
from exceptions import InvalidContentError


DIVIDER_LINE = "-----------------------------------------------------------"
HEADER_LINE = "               Summary of the experiment                  "


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
        raise InvalidContentError("Not a valid JSON")


def validate_experiment(experiment_data):
    """
    Validates if all keys are present and their values are of correct data type.
    :param experiment_data:
    :return: bool
    """
    if not ('experiment_id' in experiment_data and isinstance(experiment_data['experiment_id'], str) and experiment_data['experiment_id'] != ""):
        raise InvalidContentError("experiment_id is missing or not a string or is empty")
    if not ('backend' in experiment_data and isinstance(experiment_data['backend'], str) and experiment_data['backend'] != ""):
        raise InvalidContentError('backend is missing or not a string or is empty')
    if not ('shots' in experiment_data and isinstance(experiment_data['shots'], int) and experiment_data['shots'] > 0):
        raise InvalidContentError('shots is missing or not a positive integer')
    if not ('results' in experiment_data and isinstance(experiment_data['results'], list) and len(experiment_data['results']) > 0):
        raise InvalidContentError('results is missing or not a list or is empty')
    return True


def is_valid_result(result):
    """
    Validates if all keys are present and their values are of correct data type.
    :param result:
    :return: bool
    """
    if not('state' in result and isinstance(result['state'], str) and result['state'] != ""):
        raise InvalidContentError('state is missing or is not a non-empty string')
    if not('count' in result and isinstance(result['count'], int) and result['count'] > 0):
        raise InvalidContentError('count is missing or is not a positive Integer')
    return True


def process_experiment_data(experiment_data):
    """
    Process the experiments results and create a summary that can be reported
    :param experiment_data:
    :return: dictionary of experiment summary
    """
    summary = {
        "experiment_id": experiment_data['experiment_id'],
        "total_shots": experiment_data['shots'],
        "valid_shots": 0,
        "unique_states": [],
        "probabilities": [],
        "most_probable_state": "",
        "invalid_results": []
    }
    max_shots = 0
    for result in experiment_data['results']:
        try:
            if is_valid_result(result):
                summary['valid_shots'] += result['count']
                summary['unique_states'].append(result['state'])
                summary['probabilities'].append({result['state']: result['count']/summary['total_shots']})
                if max_shots < result['count']:
                    summary['most_probable_state'] = result['state']
                    max_shots = result['count']
        except InvalidContentError as e:
            summary['invalid_results'].append((result, str(e)))
    return summary


def generate_report(summary):
    """
    Generates a report of the summary created.
    :param summary:
    :return: None
    """
    if summary:
        print(DIVIDER_LINE)
        print(HEADER_LINE)
        print(DIVIDER_LINE + "\n")
        print(f'{"Experiment ID":18} : {summary["experiment_id"]}')
        print(f'{"Total shots":18} : {summary["total_shots"]}')
        print(f'{"Valid shots":18} : {summary["valid_shots"]}')
        print(f'{"Unique states":18} : {summary["unique_states"]}')
        print(f'{"Most likely state":18} : {summary["most_probable_state"]}')
        probabilities_formatted = [f'{key} -> {value}' for d in summary["probabilities"] for key, value in d.items()]
        print(f'{"Probabilities":18} :')
        for line in probabilities_formatted:
            print('\t\t'+line)
        invalid_results_formatted = [f'{result} --> {reason}' for result, reason in summary["invalid_results"]]
        print(f'{"Invalid results":18} :')
        for line in invalid_results_formatted:
            print('\t\t'+line)
        print(DIVIDER_LINE + "\n")
