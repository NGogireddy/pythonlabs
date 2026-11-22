import pytest
from bell_state_explorer import explore_bell_state, generate_summary


@pytest.mark.parametrize("state, shots, expected_result", [
    ('phi_plus', 1000, {'00', '11'}),
    ('phi_minus', 1200, {'00', '11'}),
    ('psi_plus', 900, {'01', '10'}),
    ('psi_minus', 500, {'01', '10'}),
])
def test_positive_cases(state, shots, expected_result):
    result = explore_bell_state(state, shots)
    assert set(result["measurement_counts"].keys()) == expected_result
    assert sum(result["measurement_counts"].values()) == shots


def test_negative_case():
    with pytest.raises(ValueError, match="Unknown Bell state"):
        explore_bell_state("invalid_state")


def test_generate_summary_valid_input():
    outcome = {
            "bell_state": "phi_plus",
            "measurement_counts": {
                "00": 498,
                "11": 502
            }
        }
    expected_result = [
        "Bell State: phi_plus",
        "Total count:  1000",
        "Outcome 00: 498 (49.8%)",
        "Outcome 11: 502 (50.2%)",
    ]
    result = generate_summary(outcome)
    assert result == expected_result


def test_generate_summary_empty_input():
    with pytest.raises(ValueError, match="Empty result, no summary produced"):
        generate_summary({})


def test_generate_summary_invalid_total():
    outcome = {
            "bell_state": "phi_plus",
            "measurement_counts": {
                "00": -10,
                "11": 10
            }
        }
    with pytest.raises(ValueError, match="Total shots = 0, no summary produced"):
        generate_summary(outcome)


def test_generate_summary_invalid_count():
    outcome = {
            "bell_state": "phi_plus",
            "measurement_counts": {
                "00": -10,
                "11": 110
            }
        }
    with pytest.raises(ValueError, match="Invalid shot count, no summary generated"):
        generate_summary(outcome)
