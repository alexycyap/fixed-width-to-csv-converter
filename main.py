import sys
import converter.text_converter as tc
import spec.parser as sp

class FixedWidthToCsvConverter(object):
    def __init__(self, spec_file_path):
        with open(spec_file_path, "r") as sf:
            self.file_spec = sp.parse(sf.read())

    def convert(self, input_file_path, output_file_path):
        with open(input_file_path, "r", encoding = self.file_spec.input_encoding) as infile, open(output_file_path, "w", encoding = self.file_spec.output_encoding) as outfile:
            tc.convert_text(infile, outfile, self.file_spec)




if __name__ == '__main__':

    if len(sys.argv) != 4:
        sys.exit("SYNTAX: python3 main.py (spec.json file) (input file) (output file)")

    spec_file_path = sys.argv[1]
    input_file_path = sys.argv[2]
    output_file_path = sys.argv[3]

    converter = FixedWidthToCsvConverter(spec_file_path)
    converter.convert(input_file_path, output_file_path)
