from src.end_to_end_datascience_project.logger import logging
from src.end_to_end_datascience_project.exception import CustomException
from src.end_to_end_datascience_project.components.data_ingestion import DataIngestionConfig
from src.end_to_end_datascience_project.components.data_ingestion import DataIngestion



import sys


if __name__ == "__main__":
    logging.info("Starting the end-to-end data science project application.")
    logging.info("Application is running...")
    try:
        data_ingestion_config=DataIngestionConfig()
        print(data_ingestion_config)
        data_ingestion_component = DataIngestion()
        data_ingestion_component.initiate_data_ingestion(source_file_path="student_sample_data.xlsx")
        ##data_ingestion_component.initiate_data_ingestion(config=data_ingestion_config,source_file_path="student_sample_data.xlsx")

    except Exception as e:
        logging.info("An error occurred in the application.")
        raise CustomException("An error occurred during application execution.", sys) from e
    
