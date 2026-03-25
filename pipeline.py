import pandas as pd
import sqlite3


print("Extracting data...")
print("Transforming data...")
print("Loading data...")

# Extract
def extract():
    df = pd.read_csv('data/movies.csv')
    return df

# Transform
def transform(df):
    df = df.dropna()  # remove missing values
    df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')
    df = df[df['release_year'] > 2000]  # filter recent movies
    return df

# Load
def load(df):
    conn = sqlite3.connect('db.sqlite')
    df.to_sql('movies', conn, if_exists='replace', index=False)
    conn.close()

# Pipeline
def run_pipeline():
    df = extract()
    df = transform(df)
    load(df)
    print("Pipeline executed successfully!")

if __name__ == "__main__":
    run_pipeline()

def run_pipeline():
    print("Starting pipeline...")
    
    df = extract()
    print("Data extracted")
    
    df = transform(df)
    print("Data transformed")
    
    load(df)
    print("Data loaded into database")

    print("Pipeline executed successfully!")
