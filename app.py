from src.end_to_end_datascience_project.logger import logging
from src.end_to_end_datascience_project.exception import CustomException
import sys


if __name__ == "__main__":
    logging.info("Starting the end-to-end data science project application.")
    logging.info("Application is running...")
    try:
        # Simulate some operations
        result = 10 / 0  # This will raise an exception
    except Exception as e:
        logging.info("An error occurred in the application.")
        raise CustomException("An error occurred during application execution.", sys) from e
    
