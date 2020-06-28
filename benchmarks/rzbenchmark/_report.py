from typing import Any

from tabulate import tabulate

from ._defs import Report


def report_as_md_table(title: str,
                       report: Report,
                       summary: Any = None):  # or Summary
    content = f'## {title}\n\n'

    for data_name, group in report.items():
        content += f'### {data_name}\n\n'
        content += tabulate(group, headers='keys', tablefmt='pipe')
        content += '\n\n'

    if summary:
        content += '### Summary\n\n'
        content += tabulate(summary, headers='keys', tablefmt='pipe')
        content += '\n\n'

    return content