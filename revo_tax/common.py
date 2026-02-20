from typing import TypeAlias

BELKA_TAX = 0.19

CsvReport: TypeAlias = list[list[str]]

_NUMBER_OF_CURRENCY_FRACTION_PARTS = 2

def financial_round(number: float) -> float:
    return round(number, _NUMBER_OF_CURRENCY_FRACTION_PARTS)

