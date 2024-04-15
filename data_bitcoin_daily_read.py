import csv

def get_column_values(csv_file, column_index):
    """
    Reads a CSV file and returns the values of a specified column as an array of floats.
    
    Args:
        csv_file (str): Path to the CSV file.
        column_index (int): Index of the column to extract (0-indexed).
        
    Returns:
        list: Array containing the values of the specified column as floats.
    """
    column_values = []  # Initialize an empty list to store column values
    
    # Open the CSV file
    with open(csv_file, 'r') as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file, delimiter=',')

        # Skip the header row
        next(csv_reader)

        # Iterate through each row in the CSV file
        for row in csv_reader:
            # Convert the value of the specified column to float and append to the list
            value = float(row[column_index].strip("'"))  # Convert to float and remove quotes
            column_values.append(value)

    return column_values

# Example usage:
csv_file_path = '../data/csv/bitcoin-daily.csv'
column_index_to_extract = 1  # Index of the "Open" column (0-indexed)
open_column_values = get_column_values(csv_file_path, column_index_to_extract)

# Print the array of values obtained from the "Open" column as floats
print(open_column_values)

