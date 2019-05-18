import unittest
import io
from spec.model import FileSpec, ColumnSpec
import converter.text_converter as tc


class TextConverterTest(unittest.TestCase):
    def test_convert_text_without_header(self):
        text_input = io.StringIO(
"""1112233333
aaabbccccc""")
        text_output = io.StringIO()

        columns = [ ColumnSpec("f1",3), ColumnSpec("f2",2), ColumnSpec("f3",5) ]
        file_spec = FileSpec(columns = columns, include_header = False, input_encoding="utf-8", output_encoding="utf-8")

        tc.convert_text(text_input, text_output, file_spec)

        expected_output = "111,22,33333\r\naaa,bb,ccccc\r\n"
        self.assertEqual(text_output.getvalue(), expected_output)

    def test_convert_text_with_header(self):
        text_input = io.StringIO(
"""1112233333
aaabbccccc""")
        text_output = io.StringIO()

        columns = [ ColumnSpec("f1",3), ColumnSpec("f2",2), ColumnSpec("f3",5) ]
        file_spec = FileSpec(columns = columns, include_header = True, input_encoding="utf-8", output_encoding="utf-8")

        tc.convert_text(text_input, text_output, file_spec)

        expected_output = "f1,f2,f3\r\n111,22,33333\r\naaa,bb,ccccc\r\n"
        self.assertEqual(text_output.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()

