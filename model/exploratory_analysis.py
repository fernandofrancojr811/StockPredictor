import pandas as pd
import matplotlib.pyplot as plt
from load_data import load_and_clean_data

def perform_eda(data):
    """
    Perform exploratory data analysis on the dataset.

    Parameters:
    data (DataFrame): The cleaned dataset.
    """
    # Plotting the closing price
    plt.figure(figsize=(10, 6))
    plt.plot(data['Close/Last'], label='Closing Price')
    plt.title('Stock Closing Prices Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    file_path = '/Users/fernandofranco/Desktop/sp/HistoricalQuotes.csv'
    data = load_and_clean_data(file_path)
    perform_eda(data)
