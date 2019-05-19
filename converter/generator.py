
def generate_row_dict(input, columns_spec):
    '''
    Generates a dictionary of column names to values, representing the values of a single row of fixed-width input data parsed using the specified columns specifications.
    If the input row data has less data than what the columns_spec expects, it will parse till the last column that has a value and skip the other columns.
    If there is not enough data for even the first column, it will return an empty dict. 

    :param str input: A single row of fixed-width input data
    :param list[ColumnSpec] columns_spec: A list of ColumnSpec objects with which to parse the input
    :return: dict of column names to values
    :rtype: dict[str, str]
    '''

    output_dict = {}
    index = 0
    for col_spec in columns_spec:
        to_index = index+col_spec.offset
        if len(input) >= to_index:
            output_dict[col_spec.name] = input[index:to_index]
            index = to_index
        else:
            break
    return output_dict

