from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_traine import ModelTrainer

if __name__ == "__main__":
    try:
        # Data Ingestion: Load the dataset
        print("Initializing data ingestion...")
        obj = DataIngestion()
        train_path, test_path, data_path = obj.initialize_data_ingestion()

        # Data Transformation: Clean and preprocess the data
        print("Initializing data transformation...")
        data_transform = DataTransformation()
        train_data_arr,test_data_arr = data_transform.get_initialize_data_transformation(train_path,test_path)

        # Model Training: Train the model with the preprocessed data
        print("Initializing model training...")
        train_model = ModelTrainer()
        train_model.get_initiate_model_trainer(train_data_arr,test_data_arr)
        
        print("Training pipeline completed successfully!")

    except Exception as e:
        print(f"An error occurred in the pipeline: {e}")
