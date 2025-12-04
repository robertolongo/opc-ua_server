

def get_variable_list(file_name):
    """
        Reads a text file and returns a list containing the file's lines,
        removing the newline character (\n) from each line.
        """
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            # List comprehension to read the lines and clean them
            # strip() removes leading/trailing whitespace and the newline character
            variable_list = [line.strip() for line in file]
            return variable_list
    except FileNotFoundError:
        print(f"ERROR: The file '{file_name}' was not found.")
        return []

if __name__ == "__main__":

    file_to_read = "opc_parameters/Real_R.txt"
    variables = get_variable_list(file_to_read)

    if variables:
        print(f"File successfully read and cleaned. Number of variables: {len(variables)}")
        print(variables)