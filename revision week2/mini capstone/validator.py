from exceptions import InvalidSensorDataError, InvalidQuantumReadingError


def valid_schema(schema):
    """
    Validates if the schema is a valid quantum schema for correct keys
    :param schema:
    :return: bool
    :raises: InvalidSensorDataError
    """

    if "device_id" in schema and "backend" in schema and "readings" in schema:
        return True
    raise InvalidSensorDataError(schema)


def valid_reading(reading):
    """
    Validate if the reading is between 0 and 1
    :param reading: string
    :return: float(reading)
    :raises: InvalidQuantumReadingError
    """
    try:
        value = float(reading)
        if 0 <= value <= 1:
            return value**2
        return InvalidQuantumReadingError(f"Out of boundary")
    except (ValueError, TypeError):
        return InvalidQuantumReadingError("Invalid Value")
