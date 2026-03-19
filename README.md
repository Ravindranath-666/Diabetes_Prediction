# Diabetes Prediction Web App (Machine Learning + Streamlit)

An end-to-end Machine Learning project that predicts the likelihood of diabetes based on patient health data.  
The project includes model training, evaluation, threshold-based prediction logic, and an interactive Streamlit web interface with probability-based results.

---

## Features

- Logistic Regression model for diabetes prediction (achieving ~73% accuracy)
- StandardScaler for feature normalization
- Interactive Streamlit web UI
- Probability-based prediction output
- Clean project structure suitable for production-level demos
- Logo & banner images included for better UI

##  Machine Learning Pipeline

- Data loading & exploration
- Feature-target separation
- Train-test split with stratification
- Feature scaling using StandardScaler
- Model training using LogisticRegression
- Probability-based predictions
- Model evaluation using confusion matrix
- Model & scaler serialization using Pickle

## Tech Stack

- Python 3.10
- Pandas
- Scikit-learn
- Streamlit
- Pickle

## Project Structure

DIABETIES_PREDICTION/
│
├── dataset/
│   └── diabetes.csv
│
├── model/
│   ├── model.pkl
│   └── scaler.pkl
│
├── Pictures/
│   ├── logo.png        # Web app logo
│   └── baner.png       # Banner image displayed in Streamlit
│
├── Demo_screenshots/
│   ├── demo1.png       # Output screenshot demo 1
│   └── demo2.png       # Output screenshot demo 2
│
├── app.py              # Streamlit web application
├── train_model.py      # Model training script
├── requirements.txt
├── README.md
└── .gitignore


## ▶How to Run the Project
  streamlit run app.py 
### 1️⃣ Clone the repository
```bash
git clone https://github.com/Sangam-555/Diabetes_prediction.git
cd Diabetes_prediction

2️⃣ Create virtual environment (recommended)

python -m venv .pre
.pre\Scripts\activate   # Windows
# source .venv/bin/activate   # Mac/Linux

3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Train the model

python train_model.py

5️⃣ Run Streamlit app

streamlit run app.py

📊 Model Decision Logic

    Model outputs probability using predict_proba

    Default threshold = 0.5

    Prediction rule:

        Probability ≥ 0.5 → Diabetes

        Probability < 0.5 → No Diabetes

Motivation

This project was built to demonstrate practical Machine Learning skills with a focus on:

    Real-world healthcare data

    Explainable predictions

    Industry-relevant ML workflows

👤 Author

** Bala Venkata Naga Ravindranath Sangam **  
🎓 MSc Artificial Intelligence and Robotics  
🏛️ University of Hertfordshire