import pandas as pd

# Load Excel file
df = pd.read_excel("student_data.xlsx")

# Display column names
print("Columns in the file:")
print(df.columns)

# Display data types of each column
print("\nData types of each column:")
print(df.dtypes)