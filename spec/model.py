class ColumnSpec(object):
    def __init__(self, name, offset):
        self.name = name
        self.offset = offset

class FileSpec(object):
    def __init__(self, columns, include_header, input_encoding, output_encoding):
        self.columns = columns
        self.include_header = include_header
        self.input_encoding = input_encoding
        self.output_encoding = output_encoding
        self.column_names = [c.name for c in columns]


