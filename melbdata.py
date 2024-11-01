import pandas as pd

# Load data
melbourne_file_path = "data/melb_data.csv"
melbourne_data = pd.read_csv(melbourne_file_path) 
# print a summary of the data in Melbourne data
# print(melbourne_data.describe())
# print(melbourne_data.columns)

predicate_y = melbourne_data.Price

# melbourne_data = melbourne_data.dropna(axis=0)
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]
print(X.describe())
print(X.head())