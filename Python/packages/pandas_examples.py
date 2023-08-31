import pandas as pd

'''
This Python file contains five functions demonstrating different functionalities of the pandas package for Excel operations:

read_excel_file(): Reads an Excel file and prints its contents.
write_to_excel(): Writes a DataFrame to an Excel file.
filter_rows(): Filters rows based on a condition and prints the filtered DataFrame.
update_cell(): Updates the value of a specific cell in the DataFrame.
apply_function_to_column(): Applies a function to a DataFrame column to update its values.
'''

def read_excel_file():
    """Read an Excel file and display its contents"""
    df = pd.read_excel("example.xlsx")
    print("=== Reading Excel File ===")
    print(df)
    print("\n")

def write_to_excel():
    """Write a DataFrame to a new Excel file"""
    data = {'Name': ['John', 'Alice', 'Bob'],
            'Age': [28, 24, 22]}
    df = pd.DataFrame(data)
    df.to_excel("output.xlsx", index=False)
    print("=== Writing to Excel File ===")
    print("DataFrame has been written to 'output.xlsx'")
    print("\n")

def filter_rows():
    """Filter rows based on a condition"""
    df = pd.read_excel("example.xlsx")
    filtered_df = df[df['Age'] > 25]
    print("=== Filtering Rows ===")
    print(filtered_df)
    print("\n")

def update_cell():
    """Update the value of a specific cell"""
    df = pd.read_excel("example.xlsx")
    df.at[0, 'Name'] = 'John Doe'
    print("=== Updating a Cell ===")
    print(df)
    print("\n")

def apply_function_to_column():
    """Apply a function to a DataFrame column"""
    df = pd.read_excel("example.xlsx")
    df['Age'] = df['Age'].apply(lambda x: x + 1)
    print("=== Applying Function to Column ===")
    print(df)
    print("\n")

if __name__ == "__main__":
    read_excel_file()
    write_to_excel()
    filter_rows()
    update_cell()
    apply_function_to_column()
