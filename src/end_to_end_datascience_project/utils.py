import os
import sys
from src.end_to_end_datascience_project.exception import CustomException
from src.end_to_end_datascience_project.logger import logging
import mysql.connector
import pandas as pd
from dotenv import load_dotenv




def load_data_from_database(query: str) -> pd.DataFrame:
    """
    Load data from a MySQL database into a pandas DataFrame.

    Parameters:
    query (str): SQL query to fetch data.
    database (str): Name of the database.

    Returns:
    pd.DataFrame: DataFrame containing the fetched data.

    """
    load_dotenv()
    host = os.getenv("host")
    user = os.getenv("user")
    password = os.getenv("password")
    database = os.getenv("database")
    try:
        # Establish the database connection
        connection=mysql.connector.connect(
            
            host="localhost",user="root",password="Lucky$2021",database="college",use_pure=True
            
        )
        logging.info("Database connection established successfully.")

        # Execute the query and fetch data into a DataFrame
        df = pd.read_sql(query, con=connection)
        logging.info("Data fetched successfully from the database.")

        return df

    except Exception as e:
        logging.error("Error occurred while loading data from the database.")
        raise CustomException("Failed to load data from database.", sys) from e

    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            logging.info("Database connection closed.")