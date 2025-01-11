import os
import sys
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    """
    Configuration for data transformation paths.
    """
    preprocessor_path_config : str = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.prerocessor_path = DataTransformationConfig()

    def get_initialize_data_transformer_obj(self):
        """
        Creates a preprocessing object using pipelines for numeric and categorical columns.
        """
        try:
            # Define numeric and categorical columns
            numeric_columns = ['duration', 'src_bytes', 'dst_bytes', 'land', 'wrong_fragment',
                                'urgent', 'hot', 'num_failed_logins', 'logged_in', 'num_compromised',
                                'root_shell', 'su_attempted', 'num_root', 'num_file_creations',
                                'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login',
                                'is_guest_login', 'count', 'srv_count', 'serror_rate',
                                'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate',
                                'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count',
                                'dst_host_srv_count', 'dst_host_same_srv_rate',
                                'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
                                'dst_host_srv_diff_host_rate', 'dst_host_serror_rate',
                                'dst_host_srv_serror_rate', 'dst_host_rerror_rate',
                                'dst_host_srv_rerror_rate']
            
            categorical_columns = ['protocol_type', 'service', 'flag']

            # Define numerical pipeline
            num_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='median')),
                ('scaler', StandardScaler())
            ])

            # Define categorical pipeline
            cat_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='most_frequent')),
                ('onehot', OneHotEncoder(handle_unknown='ignore'))
            ])

            # Combine pipelines into a ColumnTransformer
            preprocessor = ColumnTransformer([
                ('num_pipeline', num_pipeline, numeric_columns),
                ('cat_pipeline', cat_pipeline, categorical_columns)
            ])

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    def get_initialize_data_transformation(self,train_path,test_path):
        """
        Transforms training and testing data with augmentation (SMOTE).
        """
        try:
            
            train_data = pd.read_csv(train_path)
            test_data = pd.read_csv(test_path)

            logging.info("Load data from artifacts folder")

            preprocessing_obj = self.get_initialize_data_transformer_obj()
            
            logging.info("Preprocessing data with pipeline.")

            target_column_name = "labels"
            

            train_X = train_data.drop(columns=[target_column_name],axis=1)
            train_y = train_data[target_column_name]
            
            test_X = test_data.drop(columns=[target_column_name],axis=1)
            test_y = test_data[target_column_name]
            
            
            train_X = preprocessing_obj.fit_transform(train_X)
            test_X = preprocessing_obj.transform(test_X)
            
            
            mapping = {'normal':0, 'attack':1}
            train_y = train_y.map(mapping)
            test_y = test_y.map(mapping)
            
            
            logging.info("Data Encoding Completed")

            train_data_arr = np.c_[train_X,train_y]
            test_data_arr = np.c_[test_X,test_y]

            os.makedirs(os.path.dirname(self.prerocessor_path.preprocessor_path_config), exist_ok=True)
            
            logging.info("Storing preprocess.pkl in artifacts folder")
            
            save_object(
                file_path=self.prerocessor_path.preprocessor_path_config,
                obj=preprocessing_obj
            )
            
            logging.info(f"Preprocessing object saved at {self.prerocessor_path.preprocessor_path_config}.")

            return train_data_arr,test_data_arr

        except Exception as e:
            raise CustomException(e, sys)
