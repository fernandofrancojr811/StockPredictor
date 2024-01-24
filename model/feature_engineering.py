import pandas as pd
from load_data import load_and_clean_data

def create_features(data):
    """
    Create new features from the dataset.

    Parameters:
    data (DataFrame): The cleaned dataset.

    Returns:
    DataFrame: Dataset with new features.
    """
    # Currently, this adds 'MA_10'. You can comment it out or remove it.
    # data['MA_10'] = data['Close/Last'].rolling(window=10).mean()

    # Add other feature engineering steps as required

    return data

if __name__ == "__main__":
    file_path = '/Users/fernandofranco/Desktop/sp/HistoricalQuotes.csv'
    data = load_and_clean_data(file_path)
    featured_data = create_features(data)
