# RevoTax

Helps you calculate the taxes for Revolut in Poland.

## Limitations

I'm ignoring crypto completely as I personally didn't have any transactions last year.
If needed, I can try to work something out.

## Legal information

This project is an independent open-source tool and is not affiliated with, endorsed by, or connected to
Revolut Ltd or any of its subsidiaries. "Revolut" is a trademark of Revolut Ltd.

This software is provided for informational and convenience purposes only.
It does not constitute financial, tax, or legal advice.

Tax laws vary by jurisdiction and are subject to change.
The maintainers of this repository cannot guarantee the accuracy of the calculations or the parsing logic.
You are solely responsible for verifying the output against your actual transaction data and consulting with a qualified tax professional before filing.

## Development

To run: `uv run main.py <path_to_report.csv>`

- Code style: `uv run prek`
- Typing: `uv run ty check`