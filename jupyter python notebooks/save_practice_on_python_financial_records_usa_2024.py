
import pandas as pd
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

print("Imports are working correctly!")

print("Welcome to our banking activation practice for the Python modules and Machine Learning procedures for values and predictions.")

# Load the dataset
file_path = r'C:\Users\Walte\OneDrive\Documents\Datasets from Kaggle\archive\US_Stock_Data.csv'
df = pd.read_csv(file_path)

# Drop unnamed columns if they exist
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
print("Dropped unnamed columns.")

# Display the first few rows and general info
print(df.head())
print(df.info())

# Handle NaN values
print(f"Rows before dropping NaNs: {df.shape[0]}")
df.dropna(inplace=True)
print(f"Rows after dropping NaNs: {df.shape[0]}")

# Display the cleaned DataFrame (optional)
print(df.head())

import os

# Define the folder and file paths
output_folder = r'C:\Users\Walte\OneDrive\Documents\Cleansed Data CSV Files Coded Python or R'
output_file_path = os.path.join(output_folder, 'cleaned_US_Stock_Data.csv')

# Create the folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Save the DataFrame to the CSV file
df.to_csv(output_file_path, index=False)

print(f"Cleaned dataset saved to {output_file_path}")

####################################################################
###USAGE OF LINEAR REGRESSION FOR SPECIFIC VALUES
####################################################################

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load your dataset
df = pd.read_csv(r'C:\Users\Walte\OneDrive\Documents\Cleansed Data CSV Files Coded Python or R\cleaned_US_Stock_Data.csv')

# Inspect the dataset
print(df.info())

# Identify numeric columns
numeric_columns = df.select_dtypes(include=[float, int]).columns
print("Numeric Columns:", numeric_columns)

# Function to convert columns to numeric
def convert_columns_to_numeric(df, columns):
    for column in columns:
        # Remove commas and convert to float
        df[column] = pd.to_numeric(df[column].str.replace(',', ''), errors='coerce')
    return df

# List of columns that might contain comma-separated values
problematic_columns = ['Bitcoin_Price', 'Platinum_Price', 'Ethereum_Price', 
                       'S&P_500_Price', 'Nasdaq_100_Price', 'Berkshire_Price', 'Gold_Price']

# Apply conversion
df = convert_columns_to_numeric(df, problematic_columns)

# Check the data types after conversion
print(df.dtypes)

# Check for any NaN values after conversion
print("Missing values after conversion:\n", df.isnull().sum())

# Drop rows with NaN values in numeric columns
df = df.dropna(subset=numeric_columns)

# Define your features (X) and target (y)
X = df[['Gold_Vol.','Ethereum_Vol.','Bitcoin_Vol.']]  # Feature columns
y = df['Gold_Price']  # Target column

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create the Linear Regression model and fit it to the data
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)

# Output results
print("Predicted Values:", y_pred)

# Evaluate the model performance
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Mean Squared Error:", mse)
print("R^2 Score:", r2)


