import os
import sys
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

from src.exception import CustomException
from src.logger import logging


@dataclass
class DataIngestionConfig:
    """
    Configuration for data ingestion paths
    """
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        """
        Reads the dataset, performs train-test split,
        and saves the files into artifacts folder.
        """
        logging.info("Entered the data ingestion method or component")
        try:
            # ✅ Read dataset
            df = pd.read_csv(r'notebook\data\stud.csv')
            logging.info("Read the dataset as dataframe")

            # ✅ Create artifacts directory if not exists
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # ✅ Save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Raw data saved successfully")

            # ✅ Split into train and test sets
            logging.info("Train-Test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # ✅ Save train and test files
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Data ingestion completed successfully")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    ingestion = DataIngestion()
    train_path, test_path = ingestion.initiate_data_ingestion()
    logging.info(f"Data Ingestion Completed. Train Path: {train_path}, Test Path: {test_path}")
