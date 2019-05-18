import csv
import converter.generator as cg

def convert_text(textinput, textoutput, file_spec):
    writer = csv.DictWriter(textoutput, fieldnames = file_spec.column_names)
    if file_spec.include_header:
        writer.writeheader()

    for in_line in textinput:
        writer.writerow(cg.generate_row_dict(in_line, file_spec.columns))

    return textoutput    
