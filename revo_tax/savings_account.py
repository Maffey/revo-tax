from functools import cached_property

from revo_tax.common import CsvReport, BELKA_TAX, financial_round
from revo_tax.input_handling import CsvFileCannotBeParsedError

_SAVINGS_HEADER = "Summary for Savings Accounts"
_TOTAL_EARNINGS_HEADER = "Łączna kwota zarobionych odsetek"

class SavingsView:

    def __init__(self, report: CsvReport) -> None:
        self._view = find_savings(report)

    @cached_property
    def total_earnings(self) -> float:
        for row in self._view:
            if _TOTAL_EARNINGS_HEADER in row[0]:
                return float(row[1].strip())
        raise CsvFileCannotBeParsedError("Couldn't find total earnings for the Savings Account.")

    @property
    def tax(self) -> float:
        # TODO keep returns as values, but at the end create a summary class that attaches currency as well.
        return financial_round(self.total_earnings * BELKA_TAX)


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
