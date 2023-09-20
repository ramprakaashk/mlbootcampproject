import os
import sys
import pandas as pd
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split

class DataIngestionConfig():
    train_data_path = os.path.join("artifact","train.csv")
    test_data_path = os.path.join("artifact","test.csv")
    raw_data_path = os.path.join("artifact","raw.csv")

class DataIngestion():
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("starting data ingestion")
        try:
            df = pd.read_csv(os.join.path("notebook/cleandata.csv"))
            
            os.makedir(os.path.dirname(self.ingestion_config.train_data_path),exist_ok = True)
            df.to_csv(self.ingestion_config.raw_data_path)
            
            
            train_set, test_set = train_test_split(df, test_size=0.25, random_state=42)
            logging.info("splitting csv data into train and test")
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("Data ingetsion completed. Data is written into train and test files")
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
                
            )
            
        except Exception as e:
            raise Exception
            
    
    




