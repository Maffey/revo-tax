import datetime
from enum import StrEnum

from currency_converter import CurrencyConverter


class Currency(StrEnum):
    USD = "USD"
    EUR = "EUR"
    PLN = "PLN"


currency_converter = CurrencyConverter()

def yesterday(given_date: datetime.date) -> datetime.date:
    return given_date - datetime.timedelta(days=1)


def convert(
    amount: float, currency: Currency, conversion_date: datetime.date | None = None
) -> float:
    # TODO not all days are collected... fml
    return currency_converter.convert(
        amount,
        currency=currency.value,
        new_currency=Currency.PLN.value,
        date=conversion_date,
    )
