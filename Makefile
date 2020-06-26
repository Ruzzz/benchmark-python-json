run:
	python -m benchmarks.benchmark

check:
	pylint benchmarks

charts:
	python -m benchmarks.gen_charts

all:
	python -m benchmarks.benchmark && python -m benchmarks.gen_charts

-include Makefile.local
