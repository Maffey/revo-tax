import datetime

from revo_tax.consolidated_report_manager import ConsolidatedReportManager
from revo_tax.currency import convert, Currency


def main() -> None:
    val = convert(
        amount=100.0,
        currency=Currency.EUR,
        conversion_date=datetime.date(year=2025, month=1, day=13),
    )
    print(val)

    report = ConsolidatedReportManager('data/consolidated-statement_2025-01-01_2025-12-31_pl-pl_a1aa72.csv')
    print(report)


if __name__ == "__main__":
    main()
