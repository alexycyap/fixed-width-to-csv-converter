import json
from spec.model import ColumnSpec, FileSpec

def parse(spec_str):

	spec_json = json.loads(spec_str)

	col_names_csv = spec_json['ColumnNames']
	col_names = __split_csv(col_names_csv)

	offsets_csv = spec_json['Offsets']
	offsets = __split_csv(offsets_csv)

	input_enc = spec_json['InputEncoding']
	output_enc = spec_json['OutputEncoding']
	include_header = spec_json['IncludeHeader'] == 'True'

	assert (len(offsets) >= len(col_names)), "There are {} column names, but only {} offset values".format(len(col_names), len(offsets))

	columns = [ ColumnSpec(col_names[i], int(offsets[i])) for i in range(0, len(col_names)) ]
	return FileSpec(columns, include_header, input_enc, output_enc)


def __split_csv(csv_line):
	return [ x.strip() for x in csv_line.split(',') ]
