from pathlib import Path
from exceptions import InvalidContentError
from utilities import get_experiment_data, validate_experiment, process_experiment_data
DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def run_app():
    """
    Orchestrator module to control the flow
    :return: None
    """
    file_path = DATA_DIR / "quantum_results.json"
    if file_path.exists():
        try:
            experiment_data = get_experiment_data(file_path)
            if validate_experiment(experiment_data):
                print(process_experiment_data(experiment_data))
        except InvalidContentError as e:
            print(e.message)


if __name__ == "__main__":
    run_app()
