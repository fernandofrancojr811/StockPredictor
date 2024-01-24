import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from joblib import dump  # Using joblib directly for clarity
from feature_engineering import create_features
from load_data import load_and_clean_data

def train_model(data):
    """
    Train a machine learning model on the data.

    Parameters:
    data (DataFrame): The dataset with features and target.

    Returns:
    model: Trained machine learning model.
    """
    # Assuming 'Close/Last' as the target variable
    # Ensure that the feature columns match your dataset and are correctly prepared for training
    X = data.drop('Close/Last', axis=1)
    y = data['Close/Last']

    # Splitting the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Save the model for later use
    dump(model, 'stock_prediction_model.pkl')

    return model, X_test, y_test

if __name__ == "__main__":
    file_path = '/Users/fernandofranco/Desktop/sp/HistoricalQuotes.csv'
    data = load_and_clean_data(file_path)
    featured_data = create_features(data)
    model, X_test, y_test = train_model(featured_data)
