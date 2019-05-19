
def generate_row_dict(input, columns_spec):
    '''
    Generates a dictionary of column names to values, representing the values of a single row of fixed-width input data parsed using the specified columns specifications.

    :param str input: A single row of fixed-width input data
    :param list[ColumnSpec] columns_spec: A list of ColumnSpec objects with which to parse the input
    :return: dict of column names to values
    :rtype: dict[str, str]
    :raises AssertionError: If the input row data has less data than what the columns_spec expects
    '''

    output_dict = {}
    index = 0
    for col_spec in columns_spec:
        to_index = index+col_spec.offset
        assert (len(input) >= to_index), "Expecting to read until length {}, but data line only has length of {}.".format(to_index, len(input))
        output_dict[col_spec.name] = input[index:to_index]
        index = to_index
    return output_dict

