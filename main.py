import datetime

import arguably

from revo_tax.consolidated_report_manager import ConsolidatedReportManager
from revo_tax.currency import convert, Currency

@arguably.command
def main(path_to_consolidated_statement: str) -> None:
    """
    Calculate your taxes for Revolut in Poland
    by providing the path to your CSV consolidated statement for taxable year.

    Args:
        path_to_consolidated_statement: path to your CSV report generated in Revolut
    """
    val = convert(
        amount=100.0,
        currency=Currency.EUR,
        conversion_date=datetime.date(year=2025, month=1, day=13),
    )
    print(val)

    # report = ConsolidatedReportManager('data/consolidated-statement_2025-01-01_2025-12-31_pl-pl_a1aa72.csv')
    report = ConsolidatedReportManager(path_to_consolidated_statement)
    print(report)


if __name__ == "__main__":
    arguably.run()