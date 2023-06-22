import subprocess
import pandas as pd
import sqlite3
# List of required packages
required_packages = ['pandas', 'sqlite3']

# Function to check if a package is installed
def is_package_installed(package_name):
    try:
        __import__(package_name)
    except ImportError:
        return False
    return True

# Function to install a package using pip
def install_package(package_name):
    subprocess.check_call(['pip', 'install', package_name])

# Function to check and install required packages
def check_and_install_packages(packages):
    for package in packages:
        if not is_package_installed(package):
            print(f"Installing {package}...")
            install_package(package)
            print(f"{package} installed successfully.")
        else:
            print(f"{package} is already installed.")

def csv_to_sqlite(csv_file, db_file):
    # Check and install required packages
    check_and_install_packages(required_packages)
    
    # Rest of your code...
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
