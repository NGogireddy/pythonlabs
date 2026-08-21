from pathlib import Path
from processor import process_file


DIVIDER_LINE = '========================================'
HEADING = ' Quantum Sensor Processing Report '
UNDER_LINE = '-------------'
COMPLETED_STATUS = 'Processing Status: COMPLETED'


def run_app():
    """
    Main application orchestrating module
    :return: None
    """
    data_file = Path.cwd() / "data" / "sensor_data.json"

    if data_file.exists():
        report = process_file(data_file)
        if report is not None:
            print(DIVIDER_LINE)
            print(HEADING)
            print(DIVIDER_LINE+"\n")
            print(f'{"Device ID":16}: {report["device_id"]}')
            print(f'{"Backend":16}: {report["backend"]} \n')
            print(f'{"Total readings":16}: {report["total_readings"]}')
            print(f'{"Valid readings":16}: {len(report["valid_readings"])}')
            print(f'{"Invalid readings":16}: {len(report["invalid_readings"])}\n')
            print('Valid results')
            print(UNDER_LINE)
            for value, output in report["valid_readings"]:
                print(f'{str(value):6} -> {output}')
            print("")
            print('Invalid results')
            print(UNDER_LINE)
            for value, output in report["invalid_readings"]:
                print(f'{str(value):6} -> {output}')
            print("")
            print(COMPLETED_STATUS)
            print(DIVIDER_LINE)
    else:
        print(f'Sensor_data file "{data_file}" does not exist ')


if __name__ == "__main__":
    run_app()
