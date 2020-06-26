import json
from pathlib import Path

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

ROOT_PATH = Path(__file__).resolve().parents[1]
REPORT_DATE = '2020-06-27'


def save_chart(data, title, fname):
    plt.rcParams.update({'font.size': 8})
    plt.figure(figsize=(5, 3))

    df = pd.DataFrame(sorted(data, key=lambda x: x['callee']))
    ax = sns.barplot(x='callee', y='elapsed', palette='pastel', data=df)
    ax.set_title(title)
    ax.set_xlabel('')
    ax.set_ylabel('')
    Path(fname).parent.mkdir(parents=True, exist_ok=True)
    ax.figure.savefig(fname, dpi=100)
    plt.close(ax.figure)


def save_charts(report_name: str, report: dict):
    ret = ''
    for data_name, data_report in report.items():
        title = f'{report_name} | {data_name}'
        fname = f'reports/charts/{report_name}-{data_name}.png'
        save_chart(data_report, title, ROOT_PATH / fname)

        ret += f'![{data_name}]({fname})\n'
    return ret


def main():
    markdown = '# Charts\n\n'
    data = json.load(open(ROOT_PATH / f'reports/json-dumps-{REPORT_DATE}.json'))
    md = save_charts('dumps', data['report'])
    markdown += '## JSON dumps\n\n' + md

    data = json.load(open(ROOT_PATH / f'reports/json-loads-{REPORT_DATE}.json'))
    md = save_charts('loads', data['report'])
    markdown += '\n## JSON loads\n\n' + md
    with open(ROOT_PATH / f'charts-{REPORT_DATE}.md', 'w') as f:
        f.write(markdown)


if __name__ == '__main__':
    main()
