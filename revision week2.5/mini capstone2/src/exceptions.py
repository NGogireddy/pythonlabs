class InvalidContentError(Exception):

    def __init__(self):
        self.message = "Data in the file is not a valid JSON"
        super().__init__(self.message)
