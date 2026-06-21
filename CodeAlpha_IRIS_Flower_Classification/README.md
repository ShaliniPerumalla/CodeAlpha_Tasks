🌸 CodeAlpha IRIS Flower Classification 🧠 Overview

This project aims to classify iris flowers into three species — Setosa, Versicolor, and Virginica — using supervised machine learning techniques. The Iris dataset is one of the most well-known datasets in data science and is often used for testing classification algorithms.

The model analyzes four features of the iris flower:

Sepal Length

Sepal Width

Petal Length

Petal Width

and predicts which species the flower belongs to.

🎯 Objectives

Load and explore the Iris dataset.

Perform data preprocessing and visualization.

Train machine learning models to classify flower species.

Evaluate and compare model performance.

Build a simple prediction interface (optional Streamlit UI).

🛠️ Technologies Used

Python

Pandas – Data handling

NumPy – Numerical operations

Matplotlib / Seaborn – Visualization

Scikit-learn – Machine learning algorithms

Streamlit (optional) – Web-based interface for predictions

📂 Dataset

Source: Iris Dataset – UCI Machine Learning Repository

Attributes:

sepal_length (cm)

sepal_width (cm)

petal_length (cm)

petal_width (cm)

species — Target variable with 3 classes:

Iris-setosa

Iris-versicolor

Iris-virginica

🔍 Data Analysis & Preprocessing

Checked for missing values.

Visualized relationships using scatter plots and pair plots.

Encoded target labels into numerical values.

Split the dataset into training and testing sets (80/20).

🤖 Model Building

Trained and compared several models:

Logistic Regression

Decision Tree Classifier

Random Forest Classifier

Support Vector Machine (SVM)

K-Nearest Neighbors (KNN)

Evaluated models using accuracy, precision, recall, and confusion matrices.

📈 Results

The Random Forest and SVM models achieved the highest accuracy (~97–100%).

Confusion matrix showed minimal misclassification.

The model can reliably identify iris species based on petal and sepal features.

💻 Streamlit App (Optional)

You can create a simple web app to make live predictions using trained models.
