"""
Processes consolidated report text into normalized, parsable data.
"""
import re
from typing import Callable

from revo_tax.common import CsvReport

_HARD_SPACE = "\xa0"  # Used as a number separator in Poland
_POLISH_CURRENCY_SYMBOL = "PLN"


def _drop_hard_spaces(cell: str) -> str:
    """
    Iterates through a list of lists and removes '\xa0' (hard spaces) from all strings.
    """
    return cell.replace(_HARD_SPACE, "")


def _drop_currency_suffix(cell: str) -> str:
    # TODO this can't really drop the suffix everywhere, we need to know currency we've got.
    return cell.removesuffix(_POLISH_CURRENCY_SYMBOL)

def _normalize_polish_decimals(text: str) -> str:
    """
    Replaces a comma with a dot, but ONLY if it is surrounded by digits.
    Example: '21,37' -> '21.37'
    Example: 'To jest tekst, który pozostanie bez zmian' -> (Unchanged)
    """
    # Pattern explanation:
    # (?<=\d) : Lookbehind - asserts that what precedes is a digit
    # ,       : The actual comma we want to match
    # (?=\d)  : Lookahead - asserts that what follows is a digit
    return re.sub(r'(?<=\d),(?=\d)', '.', text)


_REPORT_NORMALIZATION_PROCESSORS: tuple[Callable[[str], str] ,...] = (
    _drop_hard_spaces,
    _drop_currency_suffix,
    _normalize_polish_decimals
)

def normalize_report(report: CsvReport) -> CsvReport:
    """
    Apply all the normalization functions to every CSV cell.
    """
    normalized_report = []

    for row in report:
        new_row = []
        for cell in row:
            for function in _REPORT_NORMALIZATION_PROCESSORS:
                cell = function(cell)
            new_row.append(cell)
        normalized_report.append(new_row)

    return normalized_report