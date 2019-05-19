import unittest
from spec.model import ColumnSpec
import converter.generator as cg

class DictGeneratorTest(unittest.TestCase):
    def test_generate_dict(self):
        input = "aaabbbbbcc"
        columns_spec = [ColumnSpec("f1",3), ColumnSpec("f2",5), ColumnSpec("f3",2)]

        row_dict = cg.generate_row_dict(input, columns_spec)
        self.assertEqual(row_dict, { "f1":"aaa", "f2":"bbbbb", "f3":"cc" } )

    def test_generate_dict_ignoring_extra_input(self):
        input = "aaabbbbbccdddeeee"
        columns_spec = [ColumnSpec("f1",3), ColumnSpec("f2",5), ColumnSpec("f3",2)]

        row_dict = cg.generate_row_dict(input, columns_spec)
        self.assertEqual(row_dict, { "f1":"aaa", "f2":"bbbbb", "f3":"cc" } )


    def test_generate_dict_skipping_missing_column(self):
        input = "aaabbbbb"
        columns_spec = [ColumnSpec("f1",3), ColumnSpec("f2",5), ColumnSpec("f3",2)]

        row_dict = cg.generate_row_dict(input, columns_spec)
        self.assertEqual(row_dict, { "f1":"aaa", "f2":"bbbbb" } )

    def test_generate_dict_skipping_incomplete_column(self):
        input = "aaabbbbbc"
        columns_spec = [ColumnSpec("f1",3), ColumnSpec("f2",5), ColumnSpec("f3",2)]

        row_dict = cg.generate_row_dict(input, columns_spec)
        self.assertEqual(row_dict, { "f1":"aaa", "f2":"bbbbb" } )

    def test_generate_empty_dict_if_less_than_one_column_data(self):
        input = "aa"
        columns_spec = [ColumnSpec("f1",3), ColumnSpec("f2",5), ColumnSpec("f3",2)]

        row_dict = cg.generate_row_dict(input, columns_spec)
        self.assertEqual(row_dict, {} )


if __name__ == '__main__':
    unittest.main()

