# 💰 Insurance Price Prediction

A Machine Learning regression project that predicts medical insurance charges based on personal and demographic information such as age, BMI, number of children, smoking status, sex, and region.

The project was built from scratch to understand and implement an end-to-end Machine Learning workflow, including exploratory data analysis, feature engineering, model training, evaluation, regularization, hyperparameter tuning, model saving, web application development, GitHub, and deployment.

## 🚀 Live Demo

**Streamlit Application:**  
👉 [Open Insurance Price Prediction App](https://insurance-price-predictiongit-hh6wxbqb5knryfcqzch5qx.streamlit.app/)

## 📌 Project Overview

The objective of this project is to predict medical insurance charges using regression techniques.

Three regression models were trained and evaluated:

- Linear Regression
- Ridge Regression
- Lasso Regression

The models were compared using multiple regression metrics. Hyperparameter tuning with cross-validation was then performed for regularized models.

The trained model and preprocessing scaler were saved using Joblib and integrated into a Streamlit application for real-time predictions.

---

## 🔄 Machine Learning Workflow

```text
Dataset
   ↓
Exploratory Data Analysis
   ↓
Feature Engineering
   ↓
Train-Test Split
   ↓
Feature Scaling
   ↓
Linear Regression
   ↓
Ridge Regression
   ↓
Lasso Regression
   ↓
Model Comparison
   ↓
Hyperparameter Tuning
   ↓
Save Model & Scaler
   ↓
Streamlit Application
   ↓
GitHub
   ↓
Deployment
```

---

## 📊 Models Used

### 1. Linear Regression

Linear Regression was used as the baseline model for predicting insurance charges.

### 2. Ridge Regression

Ridge Regression applies L2 regularization to reduce the magnitude of model coefficients and help control overfitting.

### 3. Lasso Regression

Lasso Regression applies L1 regularization. It can shrink some feature coefficients to zero, which can also perform feature selection.

---

## 📈 Model Evaluation

The models were evaluated using:

- **MAE** - Mean Absolute Error
- **MSE** - Mean Squared Error
- **RMSE** - Root Mean Squared Error
- **R²** - Coefficient of Determination

### Model Comparison

| Model | MAE | MSE | RMSE | Train R² | Test R² |
|---|---:|---:|---:|---:|---:|
| Linear Regression | 4181.19 | 3.3597e+07 | 5796.28 | 0.7417 | **0.7836** |
| Ridge Regression | 4182.39 | 3.3602e+07 | 5796.68 | 0.7417 | **0.7836** |
| Lasso Regression | 4248.49 | 3.4266e+07 | 5853.72 | 0.7405 | 0.7700 |

Hyperparameter tuning was performed using cross-validation to select an appropriate regularization strength for the regularized models.

---

## 🛠️ Feature Engineering

Categorical variables were converted into numerical features using one-hot encoding.

The final model uses the following features:

```text
age
sex
bmi
children
smoker
region_northwest
region_southeast
region_southwest
```

`region_northeast` acts as the reference category because `drop_first=True` was used during one-hot encoding.

### Feature Scaling

The numerical features:

```text
age
bmi
children
```

were standardized using `StandardScaler`.

The fitted scaler was saved using Joblib and reused during prediction so that new user inputs are transformed consistently with the training data.

---

## 💻 Streamlit Application

The trained model was integrated into a Streamlit web application.

Users can provide:

- Age
- Sex
- BMI
- Number of children
- Smoking status
- Region

The application performs the required preprocessing and generates an estimated insurance charge.

### Prediction Flow

```text
User Input
    ↓
Categorical Encoding
    ↓
Feature DataFrame
    ↓
StandardScaler Transformation
    ↓
Trained Regression Model
    ↓
Predicted Insurance Charge
```

---

## 📁 Project Structure

```text
insurance-price-prediction/
│
├── data/
│
├── models/
│   ├── linear_regression_model.pkl
│   └── scaler.pkl
│
├── notebooks/
│   ├── 03_Linear_Regression.ipynb
│   ├── 06_Model_Comparison.ipynb
│   └── 07_Hyperparameter_Tuning.ipynb
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Technologies Used

### Programming Language
- Python

### Data Analysis & Visualization
- Pandas
- NumPy
- Matplotlib
- Seaborn

### Machine Learning
- Scikit-learn
- Linear Regression
- Ridge Regression
- Lasso Regression
- StandardScaler
- Cross-Validation

### Deployment & Development
- Streamlit
- Joblib
- Git
- GitHub

---

## ▶️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/adityasagar1125-lgtm/insurance-price-prediction.git
```

### 2. Navigate to the project directory

```bash
cd insurance-price-prediction
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🌐 Deployment

The Streamlit application has been deployed using Streamlit Community Cloud.

👉 **[Launch the Live Application](https://insurance-price-predictiongit-hh6wxbqb5knryfcqzch5qx.streamlit.app/)**

---

## 📚 Project Progress

The project was developed through the following stages:

- ✅ Exploratory Data Analysis
- ✅ Feature Engineering
- ✅ Linear Regression
- ✅ Ridge Regression
- ✅ Lasso Regression
- ✅ Model Comparison
- ✅ Hyperparameter Tuning
- ✅ Model Saving
- ✅ Streamlit Application
- ✅ GitHub Repository
- ✅ Deployment

---

## 🔮 Future Improvements

Potential improvements include:

- Experimenting with additional regression algorithms
- More extensive hyperparameter optimization
- Improving the Streamlit user interface
- Adding prediction visualizations
- Adding model monitoring
- Exploring additional feature engineering techniques
- Improving predictive performance

---

## 👨‍💻 Author

### Aditya Sagar

This project was built as part of my Machine Learning learning journey to gain practical experience in developing and deploying an end-to-end Machine Learning application.

**GitHub:**  
https://github.com/adityasagar1125-lgtm
