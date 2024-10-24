import pandas as pd

# Load data
melbourne_file_path = "data/melb_data.csv"
melbourne_data = pd.read_csv(melbourne_file_path) 
# print a summary of the data in Melbourne data
print(melbourne_data.describe())