class InvalidSensorDataError(Exception):
    """
    Exception raised when the schema of the sensor data is invalid
    """

    def __init__(self, data):
        self.data = data
        self.message = f'{data} is not a valid schema for sensor data'
        super().__init__(self.message)


class InvalidQuantumReadingError(Exception):
    """
    Exception raised when the reading is not a valid quantum reading
    """

    def __init__(self, reading):
        self.reading = reading
        self.message = f'{reading}'
        super().__init__(self.message)
