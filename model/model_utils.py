import joblib

def save_model(model, file_name):
    """
    Save the machine learning model to a file.

    Parameters:
    model: Trained machine learning model.
    file_name (str): File name to save the model.
    """
    joblib.dump(model, file_name)

def load_model(file_name):
    """
    Load a machine learning model from a file.

    Parameters:
    file_name (str): File name from which to load the model.

    Returns:
    model: Loaded machine learning model.
    """
    return joblib.load(file_name)
