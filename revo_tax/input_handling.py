

class CsvFileCannotBeParsedError(Exception):
    def __init__(self, message: str):
        super().__init__(f"Could not parse the CSV file. Reason: {message}")
