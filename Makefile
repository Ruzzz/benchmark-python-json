run:
	python -m benchmarks.benchmark

check:
	pylint benchmarks

-include Makefile.local
