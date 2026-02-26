import datetime

import arguably

from revo_tax.consolidated_report_manager import ConsolidatedReportManager
from revo_tax.currency import convert_to_pln, Currency


@arguably.command
def main(path_to_consolidated_statement: str) -> None:
    """
    Calculate your taxes for Revolut in Poland
    by providing the path to your CSV consolidated statement for taxable year.

    Args:
        path_to_consolidated_statement: path to your CSV report generated in Revolut
    """
    report = ConsolidatedReportManager(path_to_consolidated_statement)
    savings = report.savings
    print(f"{savings.total_earnings = }")
    print(f"{savings.tax = }")

    acquired_date = datetime.date(year=2024, month=4, day=15)
    acquired_pln = convert_to_pln(149.02, currency=Currency.USD, conversion_date=acquired_date)

    print(acquired_pln)


    print("Goodbye!")


if __name__ == "__main__":
    arguably.run()