run:
	python -m benchmarks.benchmark_json

charts:
	python -m benchmarks.benchmark_json_charts

all:
	python -m benchmarks.benchmark_json && python -m benchmarks.benchmark_json_charts

check:
	pylint benchmarks && mypy benchmarks

test:
	pytest --disable-pytest-warnings --cov=benchmarks/rzbenchmark benchmarks/rzbenchmark/tests

-include Makefile.local
