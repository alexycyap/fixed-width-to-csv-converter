
def generate_row_dict(input, columns_spec):
    output_dict = {}
    index = 0
    for col_spec in columns_spec:
        to_index = index+col_spec.offset
        assert (len(input) >= to_index), "Expecting to read until length {}, but data line only has length of {}.".format(to_index, len(input))
        output_dict[col_spec.name] = input[index:to_index]
        index = to_index
    return output_dict

