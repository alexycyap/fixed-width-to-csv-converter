# fixed-width-to-csv-converter
Parses fixed width file using a specified spec and converts it to output CSV file.

## DEPENDENCIES:
- python3

## USAGE:
### Main
- Syntax: python3 main.py (spec.json file) (input file) (output file)
- Example: python3 main.py fixed-width/spec.json test-input.txt test-output.csv

### Run tests

chmod a+x run-tests.sh

./run-tests.sh

### Docker

There's a Dockerfile that can be used to build an image that will run the code using a sample input file. After that, it will keep the container running so you can connect to it to see the results and run more manual tests. Commands:

docker build --tag=fixedwidth .

docker run -d fixedwidth

docker exec -it (container_id) /bin/bash

