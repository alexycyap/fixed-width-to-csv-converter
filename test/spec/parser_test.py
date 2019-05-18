import unittest
import spec.parser as sp

class SpecParserTest(unittest.TestCase):

    def test_parse_success(self):
        spec = """
            {
                "ColumnNames":"f1, f2, f3, f4, f5, f6, f7, f8, f9, f10",
                "Offsets":"3,12,3,2,13,1,10,13,3,13",
                "InputEncoding":"windows-1252",
                "IncludeHeader":"True",
                "OutputEncoding":"utf-8"
            }
        """

        file_spec = sp.parse(spec)

        self.assertEqual(file_spec.include_header, True)
        self.assertEqual(file_spec.input_encoding, "windows-1252")
        self.assertEqual(file_spec.output_encoding, "utf-8")
        columns = file_spec.columns
        self.assertEqual(len(columns), 10)
        self.assertEqual(file_spec.column_names, ["f1","f2","f3","f4","f5","f6","f7","f8","f9","f10"] )
        self.assert_column_spec(columns[0], "f1", 3)
        self.assert_column_spec(columns[1], "f2", 12)
        self.assert_column_spec(columns[2], "f3", 3)
        self.assert_column_spec(columns[3], "f4", 2)
        self.assert_column_spec(columns[4], "f5", 13)
        self.assert_column_spec(columns[5], "f6", 1)
        self.assert_column_spec(columns[6], "f7", 10)
        self.assert_column_spec(columns[7], "f8", 13)
        self.assert_column_spec(columns[8], "f9", 3)
        self.assert_column_spec(columns[9], "f10", 13)


    def assert_column_spec(self, column_spec, name, offset):
        self.assertEqual(column_spec.name, name)
        self.assertEqual(column_spec.offset, offset)

 
if __name__ == '__main__':
    unittest.main()