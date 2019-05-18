#!/bin/sh

python3 -m unittest discover -s test/spec -p "*_test.py"
python3 -m unittest discover -s test/converter -p "*_test.py"