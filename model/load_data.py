import pandas as pd

def load_and_clean_data(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)

    # Remove leading and trailing spaces in column names
    data.columns = data.columns.str.strip()

    # Convert 'close' to a float, after removing '$' symbol if present
    # Similarly update for other columns if they have a similar format
    if data['close'].dtype == object:
        data['close'] = data['close'].replace(r'[\$,]', '', regex=True).astype(float)

    # Convert 'date' to datetime and set as index
    data['date'] = pd.to_datetime(data['date'])
    data.set_index('date', inplace=True)

    # Additional cleaning steps...

    return data

if __name__ == "__main__":
    file_path = '/Users/fernandofranco/Desktop/sp/HistoricalQuotes.csv'  # Replace with your file path
    cleaned_data = load_and_clean_data(file_path)
