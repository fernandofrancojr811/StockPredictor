import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
from model_utils import load_model

def evaluate_model(X_test, y_test, model_path):
    """
    Evaluate the performance of the machine learning model.

    Parameters:
    X_test (DataFrame): Test features.
    y_test (Series): True values for the test set.
    model_path (str): Path to the saved model.
    """
    # Load the trained model
    model = load_model(model_path)

    # Make predictions and evaluate the model
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    print(f"Mean Squared Error: {mse}")
    print(f"R^2 Score: {r2}")

if __name__ == "__main__":
    file_path = '/Users/fernandofranco/Desktop/sp/HistoricalQuotes.csv'
    model_path = 'stock_prediction_model.pkl'
    data = load_and_clean_data(file_path)
    featured_data = create_features(data)
    _, X_test, y_test = train_model(featured_data)
    evaluate_model(X_test, y_test, model_path)
