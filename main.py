import sys
import converter.text_converter as tc
import spec.parser as sp

if __name__ == '__main__':

    if len(sys.argv) != 4:
        sys.exit("SYNTAX: python3 main.py (spec.json file) (input file) (output file)")

    with open(sys.argv[1], "r") as spec_file:
        file_spec = sp.parse(spec_file.read())

        with open(sys.argv[2], "r", encoding = file_spec.input_encoding) as infile, open(sys.argv[3], "w", encoding = file_spec.output_encoding) as outfile:
            tc.convert_text(infile, outfile, file_spec)
