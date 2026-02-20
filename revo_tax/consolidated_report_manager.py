"""
Manages the consolidated CSV report file.
"""
import csv

from revo_tax.common import CsvReport
from revo_tax.report_sanitizer import normalize_report


class ConsolidatedReportManager:

    def __init__(self, file_path: str):
        self._file_path = file_path
        with open(file_path, mode="r") as csv_file:
            report = list(csv.reader(csv_file, delimiter=","))
            self._report: CsvReport = normalize_report(report)
