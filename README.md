﻿
# Intrusion Detection System (IDS) Using Machine Learning  

## 📄 Overview  
This project implements a comprehensive **Intrusion Detection System (IDS)** that detects and classifies network traffic into normal or malicious categories. By leveraging **Random Forest**, which delivered exceptional accuracy (99%), this system effectively identifies intrusions with high precision. The project integrates an **ETL pipeline** and a **Streamlit-based interface**, ensuring an intuitive user experience and real-time predictions.  

---

## ✨ Key Features  
- **ETL Pipeline**: Handles **data ingestion**, **transformation**, and model **training** workflows.  
- **High Performance**: Achieved **99% accuracy** using Random Forest after evaluating multiple machine learning models.  
- **Modular Design**: Well-structured components, including reusable modules for data processing, logging, and error handling.  
- **Streamlit Interface**: Real-time prediction and visualization of network traffic data.  

---

## 📂 Project Structure  

```plaintext
├── artifacts/           # Stores intermediate and final results (e.g., models, datasets)
├── build/               # Build files for packaging
├── dist/                # Distribution files
├── Intrusion_Detection_System/ # Python package files
├── logs/                # Logging outputs
├── myenv/               # Python virtual environment
├── Notebook/            # Jupyter notebooks for exploratory analysis
├── src/                 # Source code for pipelines and components
│   ├── components/      # Reusable components for data ingestion, transformation, etc.
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_evaluation.py
│   │   ├── model_training.py
│   ├── pipeline/        # Training and prediction pipelines
│   │   ├── train_pipeline.py
│   │   ├── predict_pipeline.py
│   ├── exception.py     # Custom exception handling
│   ├── logger.py        # Logging module
│   ├── utils.py         # Utility functions
├── .dockerfile          # Docker configuration file
├── .dockerignore        # Files to ignore in Docker builds
├── .gitignore           # Files to ignore in Git repository
├── app.py               # Streamlit app
├── README.md            # Project documentation
```

## Confusion Metrix and ROC Curve

![Screenshot 2025-01-11 192256](https://github.com/user-attachments/assets/71bfe534-6ca7-4cc3-b872-4894d84540be)

![Screenshot 2025-01-11 192313](https://github.com/user-attachments/assets/cabd1f40-3d0f-47b4-b3ec-f5300dd12294)

---

## 🚀 Workflow  
### 1. Data Processing  
- **Data Ingestion**: Loads and validates the dataset.  
- **Data Transformation**: Handles encoding, scaling, and feature engineering.  

### 2. Model Training  
- **Random Forest**: Outperformed other models, achieving **99% accuracy**.  
- **Evaluation**: Models were evaluated using metrics such as Precision, Recall, and F1-Score.  

### 3. Streamlit Application  
- Upload data or provide inputs via an intuitive interface.  
- Get real-time predictions: **Normal Traffic** or **Malicious Traffic**.  

---

## 🛠️ Technologies Used  
- **Python**: Core programming language  
- **Scikit-learn**: Machine learning library  
- **Streamlit**: Web interface framework  
- **Docker**: Containerization for deployment  
- **Pandas & NumPy**: Data processing and analysis  
- **Matplotlib & Seaborn**: Data visualization  

---

## 📊 Results  
- **Model Performance**:  
  - **Accuracy**: 99%  
  - **Precision, Recall, F1-Score**: Optimized for intrusion detection.  
 

## 📌 Future Enhancements  
- Add support for live traffic monitoring.  
- Integrate deep learning models for complex patterns.  
- Enhance multi-class attack classification.  

---

## 🤝 Contributing  
Contributions are welcome! Please open issues or submit pull requests for any improvements.  

---

## 🙋‍♂️ Author  
**[Jay Narigara]**  
- [LinkedIn](https://www.linkedin.com/in/jaynarigara/)  
- [GitHub](https://github.com/jaynarigara91)  

---
