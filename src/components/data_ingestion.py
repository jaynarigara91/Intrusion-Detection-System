import os
import sys
import pandas as pd
import numpy as np
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

from src.components.data_transformation import DataTransformation
from src.components.model_traine import ModelTrainer
import warnings
warnings.filterwarnings("ignore")


@dataclass
class DataIngestionConfig:
    """
        setting train_path ,test_path, data_path
    """
    train_path_config : str = os.path.join('artifacts','train.csv')
    test_path_config: str = os.path.join('artifacts','test.csv')
    Rawdata_path_config: str = os.path.join('artifacts','data.csv')
    
class DataIngestion:
    def __init__(self):
        # Initialize the data ingestion process with configuration paths
        self.data_config_path = DataIngestionConfig()
        
    def initialize_data_ingestion(self):
        """
        This method handles the data ingestion process:
        - Loads the dataset.
        - Data Cleaning
        - Saves the processed data into train and test datasets.
        """
        try:
            
            data = pd.read_csv(os.path.join('Notebook\Data','kdd_data.csv'))
            logging.info('Data Load From Folder Successfully.')
            
            data['labels'] = data['labels'].apply(lambda x: "attack" if x != "normal" else x)
            
            data.replace(["","null"],np.nan,inplace=True)
            data.dropna(inplace=True)
            data.drop_duplicates(inplace=True)
            
            logging.info("Data Cleaning Successfull")
           
            os.makedirs(os.path.dirname(self.data_config_path.Rawdata_path_config), exist_ok=True)
            
            logging.info("artifacts folder created.")
        
            data.to_csv(self.data_config_path.Rawdata_path_config, index=False, header=True)
            
            # Split the data into training and testing sets
            train_set, test_set = train_test_split(data, test_size=0.2, random_state=42)
            
            logging.info("Splited Data Into Train And test.")
            
            train_set.to_csv(self.data_config_path.train_path_config, index=False, header=True)
           
            test_set.to_csv(self.data_config_path.test_path_config, index=False, header=True)
            
            logging.info('Saved train_data, test_data and Raw_data into artifacts folder.')

            return (
                self.data_config_path.train_path_config,  #train_path
                self.data_config_path.test_path_config, #test_path
                self.data_config_path.Rawdata_path_config
            )
        
        except Exception as e:
            raise CustomException(e, sys)
        
