import csv
from io import StringIO

def get_variable_list(file_name):
    """
        Reads a text file, parses lines using ';' separator and '"' delimiter,
        and returns a list of dictionaries with 'variable_node' and 'variable_description' keys.
        """

    result_list = []

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            # Create a CSV reader object, specifying the parameters:
            # delimiter = ';' (the field separator)
            # quotechar = '"' (the character used to enclose values)
            csv_reader = csv.reader(file, delimiter=';', quotechar='"')

            for row in csv_reader:
                # The csv library returns a list of fields for each row.
                # If the row is empty or doesn't have exactly 2 fields, skip it.
                if len(row) != 2:
                    print(f"Warning: Invalid row skipped: {row}")
                    continue

                # Create the dictionary with the required key names
                row_dictionary = {
                    "variable_node": row[0].strip(),  # row[0] is the first value
                    "variable_description": row[1].strip()  # row[1] is the second value
                }

                result_list.append(row_dictionary)

            return result_list

    except FileNotFoundError:
        print(f"ERROR: The file '{file_name}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []

if __name__ == "__main__":

    # file_to_read = "opc_parameters/Real_R.txt"
    # variables = get_variable_list(file_to_read)
    #
    # if variables:
    #     print(f"File successfully read and cleaned. Number of variables: {len(variables)}")
    #     print(variables)

    # Assuming 'data.txt' contains lines like:
    # node1;"Description for node 1"
    # node2;"Description containing a ; semicolon"
    # node3;Description without quotes

    file_name = "opc_parameters/Real_R.txt"
    variable_list = get_variable_list(file_name)

    if variable_list:
        print("\nFile successfully processed:")
        for variable in variable_list:
            print(variable)
        print(f"\nTotal items in the list: {len(variable_list)}")