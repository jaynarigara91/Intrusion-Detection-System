import sys
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from src.exception import CustomException
from sklearn.metrics import accuracy_score
from dataclasses import dataclass

@dataclass
class ModelEvaluation:
    def evaluate_models(X_train, y_train, X_test, y_test, models, param):
        """
        Evaluates multiple classification models using GridSearchCV and returns their performance.
        """
        try:
            report = {}

            for i in range(len(list(models))):
                model = list(models.values())[i]
                para = param[list(models.keys())[i]]

                # Perform GridSearchCV to find the best parameters
                gs = GridSearchCV(model, para)
                gs.fit(X_train, y_train)

                # Set the best parameters to the model
                model.set_params(**gs.best_params_)
                model.fit(X_train, y_train)

                # Predict on train and test data
                # y_train_pred = model.predict(X_train)
                y_test_pred = model.predict(X_test)

                # Calculate evaluation metrics
                test_accuracy = accuracy_score(y_test, y_test_pred)

                # Log metrics
                report[list(models.keys())[i]] = test_accuracy

            return report
        
        except Exception as e:
            raise CustomException(e, sys)