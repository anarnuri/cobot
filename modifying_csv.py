import pandas as pd

# Load the CSV file
input_file = 'joints_values.csv'  # Change this to your file path

# Read the CSV file into a DataFrame
df = pd.read_csv(input_file)

# Remove the first 5 rows
df = df.iloc[5:]  # iloc slices the DataFrame from the 6th row onward

# Save the modified DataFrame to a new CSV file
df.to_csv(input_file, index=False)

print(f"First 5 rows removed. Modified file saved as '{input_file}'.")