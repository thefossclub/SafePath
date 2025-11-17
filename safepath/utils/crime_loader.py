# safepath/utils/crime_loader.py
import pandas as pd
import os

def load_crime_data():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    csv_path = os.path.join(BASE_DIR, "data/delhi_crime_data.csv")

    df = pd.read_csv(csv_path)
    return df

