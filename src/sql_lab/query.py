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


def get_data_by_group(value):
    """Returns all rows from the 'mock' table where the `group` column matches the given value. Filters on the `group` column."""
    query = "SELECT * FROM mock WHERE `group` = %s;"

    try:
        # opens the database connection
        connection = mysql.connector.connect(
            host=DBHOST,
            user=DBUSER,
            password=DBPASS,
            database=DBNAME
        )
        cursor = connection.cursor()

        # runs the queryn
        cursor.execute(query, (value,))
        results = cursor.fetchall()
        logger.info(f"Found {len(results)} rows where group = '{value}'")
        connection.close()
        return results

    except mysql.connector.Error as er:
        logger.error(f"Database error: {er}")
        return None


def plot_counts(groupby):
    """Counts rows in the 'mock' table grouped by the given column, and prints the counts. The `groupby` argument is a column name, so it's inserted into the query text directly """
    query = f"SELECT `{groupby}`, COUNT(*) FROM mock GROUP BY `{groupby}`;"

    try:
        # opens the database connection
        connection = mysql.connector.connect(
            host=DBHOST,
            user=DBUSER,
            password=DBPASS,
            database=DBNAME
        )
        cursor = connection.cursor()

        # runs the group-by count query
        cursor.execute(query)
        results = cursor.fetchall()
        logger.info(f"Counted rows grouped by '{groupby}'")
        connection.close()

        df = pd.DataFrame(results, columns=[groupby, "count"])
        return df

    except mysql.connector.Error as er:
        logger.error(f"Database error: {er}")
        return None


def main():
    """Runs the demo queries and grabs  rows for one group then it  prints counts of rows."""
    print("=== rows where group = 'Soccer' ===")
    print(get_data_by_group("Soccer"))

    print("=== counts by group ===")
    print(plot_counts("group"))


if __name__ == "__main__":
    main()
