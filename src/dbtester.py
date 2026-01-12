#create a main function to run the data ingestion component
from src.end_to_end_datascience_project.logger import logging
from src.end_to_end_datascience_project.exception import CustomException
import mysql.connector
import sys
import os
from dotenv import load_dotenv

load_dotenv()
host="localhost"
user=os.getenv("user")
password=os.getenv("password")
database=os.getenv("database")


if __name__ == "__main__":
    logging.info("Starting the end-to-end data science project application.")
    logging.info("Application is running...")
    try:
         mysql.connector.connect(
            
            host="localhost",user="root",password="Lucky$2021",use_pure=True
            
        )
         logging.info("Successfully connected to the database.")


    except Exception as e:
        logging.info("An error occurred in the application.")
        raise CustomException("An error occurred during application execution.", sys) from e