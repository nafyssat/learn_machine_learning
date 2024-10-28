import pandas as pd
from sklearn.tree import DecisionTreeRegressor


# Load data
melbourne_file_path = "data/melb_data.csv"
melbourne_data = pd.read_csv(melbourne_file_path) 


y = melbourne_data.Price

# melbourne_data = melbourne_data.dropna(axis=0)
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]

melbourne_model=DecisionTreeRegressor(random_state=1)
melbourne_model.fit(X,y)

print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))