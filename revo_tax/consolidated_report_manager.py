"""
Manages the consolidated CSV report file.
"""
from pathlib import Path
import csv
from typing import TypeAlias

CsvReport: TypeAlias = list[list[str]]
_HARD_SPACE = "\xa0"  # Used as a number separator in Poland

class ConsolidatedReportManager:

    def __init__(self, file_path: str):
        self._file_path = file_path
        with open(file_path, mode="r") as csv_file:
            self._report: CsvReport = _drop_hard_spaces(list(csv.reader(csv_file, delimiter=",")))




def _drop_hard_spaces(report: CsvReport) -> CsvReport:
    """
    Iterates through a list of lists and removes '\xa0' (hard spaces) from all strings.
    """
    return [
        [
            item.replace(_HARD_SPACE, "")
            for item in row
        ]
        for row in report
    ]