import time
import random
from contract_review import updated_process_reading, generate_report


def generate_mock_sensor_data(sample_size):
    """
    Generates a mock sensor schema with the sample size requested
    :param sample_size: integer
    :return: sensor schema
    """
    sample_readings = [1, 0.5, 0, 1.5, "abc", None, -0.3, 2.4, 0.88]

    return {
        "device_id": "device1",
        "backend": "simulator",
        "readings": [random.choice(sample_readings) for _ in range(sample_size)]
    }


for sample in [100, 10_000, 100_000]:
    mock_payload = generate_mock_sensor_data(sample)

    start_time = time.perf_counter()
    report = updated_process_reading(mock_payload)
    end_time = time.perf_counter()

    print(f'Run time for sample size {sample}: {end_time - start_time}')
