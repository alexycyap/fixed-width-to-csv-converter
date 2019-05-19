#!/bin/sh

echo Running unit tests...
./run-tests.sh

echo Converting test-input.txt to test-output.csv
python3 main.py fixed-width/spec.json test-input.txt test-output.csv