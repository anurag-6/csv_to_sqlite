import pandas as pd
import sqlite3

def csv_to_sqlite(csv_file, db_file):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)
    
    # Create a SQLite database connection
    conn = sqlite3.connect(db_file)
    
    # Save the DataFrame to a SQLite database table
    df.to_sql('sales', conn, if_exists='replace', index=False)
    
    # Close the database connection
    conn.close()
    
    print("CSV data successfully converted to SQLite database.")

# Specify the input CSV file path and output SQLite database file path
csv_file = 'sample.csv'
db_file = 'output.db'

# Call the function to convert the CSV file to SQLite
csv_to_sqlite(csv_file, db_file)
