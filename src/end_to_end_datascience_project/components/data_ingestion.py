import os
import sys
from src.end_to_end_datascience_project.exception import CustomException
from src.end_to_end_datascience_project.logger import logging
from src.end_to_end_datascience_project.utils import load_data_from_database
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join("artifacts", "raw_data.csv")
    train_data_path: str = os.path.join("artifacts", "train_data.csv")
    test_data_path: str = os.path.join("artifacts", "test_data.csv")
class DataIngestion:
    def __init__(self):
        self.config = DataIngestionConfig()

    def initiate_data_ingestion(self,source_file_path: str, test_size: float = 0.2):
        logging.info("Starting data ingestion process.")
        try:
            # Read the dataset
            df = load_data_from_database(query="SELECT * FROM students")
            logging.info(f"Dataset read successfully from {source_file_path}.")

            # Create artifacts directory if it doesn't exist
            os.makedirs(os.path.dirname(self.config.raw_data_path), exist_ok=True)

            # Save raw data
            df.to_csv(self.config.raw_data_path, index=False)
            logging.info(f"Raw data saved at {self.config.raw_data_path}.")

            # Split the data into training and testing sets
            
            train_set, test_set = train_test_split(df, test_size=test_size, random_state=42)
            logging.info("Data split into training and testing sets.")

            # Save training and testing data
            train_set.to_csv(self.config.train_data_path, index=False)
            test_set.to_csv(self.config.test_data_path, index=False)
            logging.info(f"Training data saved at {self.config.train_data_path}.")
            logging.info(f"Testing data saved at {self.config.test_data_path}.")

            return self.config.train_data_path, self.config.test_data_path

        except Exception as e:
            logging.error("Error occurred during data ingestion.")
            raise CustomException("Data ingestion failed.", sys) from e