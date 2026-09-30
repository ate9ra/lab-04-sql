import os
import logging
import mysql.connector
import pandas as pd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DBHOST = os.environ.get("DBHOST")
DBUSER = os.environ.get("DBUSER")
DBPASS = os.environ.get("DBPASS")
DBNAME = os.environ.get("DBNAME")

def read_data(filename):
    """Loads and reads the data csv."""
    # reads the CSV file's contents into a pandas DataFrame
    df = pd.read_csv(filename)
    logger.info(f"Loaded {len(df)} rows from {filename}")
    return df

def clean_data(data):
    """It removes the rows with any missing values from the DataFrame"""
    data["game_date"] = pd.to_datetime(data["game_date"]) # convert game_date from text to a real datetime
    cleaned = data.dropna()#method to remove any blank values
    logger.info(f"Cleaned data: {len(data)} rows: {len(cleaned)} rows after dropping missing values") #f string to show data and amt of rows dropped
    return cleaned    cleaned = data.dropna()#method to remove any blank values

def load_data(data, table):
    """ Connects to the MySQL databas and creates the target table if it doesn't already exist. It also uploads the DataFrame row by row using INSERT statements."""
    create_table_sql = f"""
    CREATE TABLE IF NOT EXISTS {table} (
        id BIGINT,
        `group` VARCHAR(255),
        teams VARCHAR(255),
        game_date DATETIME,
        location VARCHAR(255),
        attendance BIGINT)"""

    # INSERT statement using %s placeholders to avoid SQL injection
    insert_sql = f"""
    INSERT INTO {table} (id, `group`, teams, game_date, location, attendance)
    VALUES (%s, %s, %s, %s, %s, %s) """

    connection = None
    try:
        # opens the database connection
        connection = mysql.connector.connect(
            host=DBHOST,
            user=DBUSER,
            password=DBPASS,
            database=DBNAME
        )
        cursor = connection.cursor()

        # create the table if it doesn't exist
        cursor.execute(create_table_sql)
        logger.info(f"Ensured table '{table}' exists")

        # loop over each row of the DataFrame and insert it
        for _, row in data.iterrows():
            values = (
                row["id"],
                row["group"],
                row["teams"],
                row["game_date"],
                row["location"],
                row["attendance"],
            )
            cursor.execute(insert_sql, values)

        # commit all inserts to the database
        connection.commit()
        logger.info(f"Uploaded {len(data)} rows into '{table}'")

    except mysql.connector.Error as er:
        logger.error(f"Database error: {er}")

def main():
    """Runs the full pipeline: reads the mock CSV, cleans it, and uploads the cleaned data into the MySQL 'mock' table."""
    # load the CSV data
    raw_data = read_data("MOCK_DATA.csv")

    # clean the data
    cleaned_data = clean_data(raw_data)

    #uploads to the database
    load_data(cleaned_data, "mock")

if __name__ == "__main__":
    main()
