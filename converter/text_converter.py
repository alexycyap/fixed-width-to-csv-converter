import csv
import converter.generator as cg

def convert_text(text_input, csv_output, file_spec):
    '''
    Converts the input text content to output csv content, based on the specified file specifications.

    :param file text_input: File-like object, such as file handle or StringIO, that provides the input text content
    :param file csv_output: File-like object, such as file handle or StringIO, to which the csv output content will be written
    :return: The csv_output file-like object
    '''
    writer = csv.DictWriter(csv_output, fieldnames = file_spec.column_names)
    if file_spec.include_header:
        writer.writeheader()

    for in_line in text_input:
        writer.writerow(cg.generate_row_dict(in_line, file_spec.columns))

    return csv_output    
