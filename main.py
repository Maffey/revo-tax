import datetime

from revo_tax.currency import convert, Currency


def main() -> None:
    val = convert(
        amount=100.0,
        currency=Currency.EUR,
        conversion_date=datetime.date(year=2025, month=1, day=13),
    )
    print(val)


if __name__ == "__main__":
    main()
