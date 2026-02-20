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
    report = ConsolidatedReportManager(path_to_consolidated_statement)

    print("Goodbye!")


if __name__ == "__main__":
    arguably.run()