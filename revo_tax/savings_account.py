from functools import cached_property

from revo_tax.common import CsvReport
from revo_tax.input_handling import CsvFileCannotBeParsedError

_SAVINGS_HEADER = "Summary for Savings Accounts"

class SavingsView:

    def __init__(self, report: CsvReport) -> None:
        self._view = find_savings(report)

    @cached_property
    def total_earnings(self):
        for row in self._view:
            if "Łączna kwota zarobionych odsetek" in row[0]:
                return row[1]


def find_savings(report: CsvReport) -> CsvReport:
    savings_view: CsvReport = []
    is_in_view = False
    # TODO this probably needs some meaningful testing
    for row in report:
        if _SAVINGS_HEADER in " ".join(row):
            is_in_view = True
        if row == [] and is_in_view is True:
            return savings_view

        if is_in_view:
            savings_view.append(row)

    raise CsvFileCannotBeParsedError("Couldn't find the Savings report.")
