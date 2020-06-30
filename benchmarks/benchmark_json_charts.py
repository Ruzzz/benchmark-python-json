import json
from pathlib import Path

from penchmark.charts import save_charts_and_get_markdown

ROOT_PATH = Path(__file__).resolve().parents[1]
REPORT_DATE = '2020-06-30'


markdown_template = '''# Charts

## JSON dumps

{dumps_charts_markdown}

## JSON loads

{loads_charts_markdown}
'''


def _save_charts_and_get_markdown(op_title: str) -> str:
    report = json.load(open(ROOT_PATH / f'reports/json-{op_title}-{REPORT_DATE}.json'))['report']
    relative_path = 'reports/charts/json-' + op_title + '-{data_name}.png'
    charts_markdown = save_charts_and_get_markdown(
        report,
        title_template=op_title + ' | {data_name}',
        fname_template=str(ROOT_PATH) + '/' + relative_path,
        link_template=relative_path
    )
    return charts_markdown


def main():
    dumps_charts_markdown = _save_charts_and_get_markdown('dumps')
    loads_charts_markdown = _save_charts_and_get_markdown('loads')
    markdown = markdown_template.format(
        dumps_charts_markdown=dumps_charts_markdown,
        loads_charts_markdown=loads_charts_markdown
    )

    with open(ROOT_PATH / f'json-charts-{REPORT_DATE}.md', 'w') as f:
        f.write(markdown)


if __name__ == '__main__':
    main()
