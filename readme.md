# Diabetes Prediction using Decision Tree Classifier

This repository demonstrates a basic machine learning workflow using a **Decision Tree Classifier** to predict diabetes outcomes from a structured medical dataset.  
The project is intended for **learning and demonstration purposes**, focusing on data loading, visualization, model training, and decision tree interpretation.

---

## Overview

The program performs the following steps:

1. Loads a diabetes dataset from a CSV file
2. Performs basic exploratory analysis
3. Visualizes aggregated pregnancy counts by age
4. Trains a Decision Tree classifier
5. Generates a visual representation of the trained decision tree

---

## Dataset

- **File:** `diabetes.csv`
- **Target Variable:** `Outcome`
- **Features:**  
  - Pregnancies  
  - Glucose  
  - BloodPressure  
  - SkinThickness  
  - Insulin  
  - BMI  
  - DiabetesPedigreeFunction  
  - Age  

> Note: The dataset path is currently hardcoded and must be updated to match your local environment.

---

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Matplotlib
- Graphviz

---

## How It Works

### 1. Data Loading
The dataset is read using Pandas and basic information about the data structure is displayed.

### 2. Visualization
A bar chart is generated showing the total number of pregnancies grouped by age.

### 3. Model Training
- The dataset is split into training and testing sets.
- A Decision Tree classifier is trained using Scikit-learn.
- Predictions are made on the test set.

### 4. Model Visualization
The trained decision tree is exported and visualized using Graphviz to understand feature splits and decision paths.

