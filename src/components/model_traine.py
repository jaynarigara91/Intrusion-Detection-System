import os
import sys
from dataclasses import dataclass

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier,GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier

from src.components.model_evaluation import ModelEvaluation
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()


    def get_initiate_model_trainer(self,train_data_arr,test_data_arr):
        """
            - Spliting data into train ans test
            - Giving  diffrent model and hyper perameter to model_evaluate.py
            - Getting hight accuracy model and strore that train model in aftifact folder
        """
        try:
            logging.info("Split training and test input data")
            
            X_train,y_train=(train_data_arr[:,:-1],train_data_arr[:,-1])
            X_test,y_test=(test_data_arr[:,:-1],test_data_arr[:,-1])
            
            logging.info("Spliting Data Into Train and test.")
            
            models = {
                        "Logistic Regression": LogisticRegression(),
                        "Decision Tree": DecisionTreeClassifier(),
                        "Random Forest Classifier": RandomForestClassifier()
                        # "Gradien Bossting Classifier": GradientBoostingClassifier(),
                        # "XGBClassifier": XGBClassifier(),
                        # "K-Neighbors Classifier": KNeighborsClassifier(),
                        # "Super Vector Machine" : SVC(),
                        # "AdaBoost Classifier": AdaBoostClassifier()
                    }
            params={
                "Decision Tree": {
                    'criterion':['gini'],
                    # 'splitter':['best','random'],
                    # 'max_features':['sqrt'],
                },
                "Random Forest Classifier":{
                    'criterion':['gini'],
                    # 'max_depth' : [None,3,5,6,7],
                    # 'max_features':['sqrt','log2',None],
                    'n_estimators': [128]
                },
                # "K-Neighbors Classifier":{
                #     'n_neighbors' : [3],
                    
                # },
                # "Gradien Bossting Classifier":{
                #     # 'loss':['log_loss', 'deviance', 'exponential'],
                #     'learning_rate':[0.1],
                #     # 'criterion':['squared_error', 'friedman_mse'],
                #     # 'max_features':['auto','sqrt','log2'],
                #     'n_estimators': [128]
                # },
                "Logistic Regression":{}
                # "XGBClassifier":{
                #     'learning_rate':[0.1],
                #     'n_estimators': [100],
                #     'max_depth': [6]
                # },
                # "Super Vector Machine":{},
                # "AdaBoost Classifier":{
                #     'learning_rate':[0.1],
                #     'n_estimators': [128]
                # }
                
            }
            
            logging.info("Model Training started on diffrent diffrent models.")

            model_report:dict=ModelEvaluation.evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,
                                             models=models,param=params)
            
            logging.info("Model Trained On Diffrenet diffrent models.")
            
            ## To get best model score from dict
            best_model_score = max(model_report.values())

            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model = models[best_model_name]

            if best_model_score<0.6:
                raise CustomException("No best model found")
            logging.info(f"Best found model on both training and testing dataset")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )
            
            logging.info("Taking model that give height accuracy than other.")
            
            predicted=best_model.predict(X_test)

            accuracy = accuracy_score(y_test, predicted)
            confusion = confusion_matrix(y_test, predicted)
            print(model_report)
            print(best_model_name)
            print(accuracy)
            print(confusion)
            return accuracy
            
        except Exception as e:
            raise CustomException(e,sys)