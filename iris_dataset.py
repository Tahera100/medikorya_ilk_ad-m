# Importing required libraries
import pandas as pd  # Importing Pandas to handle data in DataFrame format
import seaborn as sns  # Importing Seaborn for easy plotting
import matplotlib.pyplot as plt  # Importing Matplotlib for general plotting
from sklearn.datasets import load_iris  # Importing Iris dataset from Scikit-learn
from sklearn.model_selection import train_test_split  # For splitting the data into training and testing sets
from sklearn.linear_model import LogisticRegression  # Importing Logistic Regression model
from sklearn.metrics import confusion_matrix  # Importing function to calculate confusion matrix
import joblib  # For saving and loading the trained model

# Load the Iris dataset
iris = load_iris()  
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)  
iris_df['species'] = iris.target  
iris_df['species'] = iris_df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})  

# Prepare the Data
X = iris.data  
y = iris.target  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) 

# Train the Model
model = LogisticRegression(max_iter=100) 
model.fit(X_train, y_train) 

# Make Predictions
predictions = model.predict(X_test)  

# Create a Confusion Matrix
cm = confusion_matrix(y_test, predictions) 
plt.figure(figsize=(6, 6))  

# Define a light lotus-like tone for the squares in the confusion matrix
lotus_cmap = sns.light_palette("#D84B6C", as_cmap=True) 

# Create the heatmap with a white background and lotus-colored squares
sns.heatmap(cm, annot=True, fmt='d', cmap=lotus_cmap, xticklabels=iris.target_names, yticklabels=iris.target_names, cbar=False, linewidths=1, linecolor='white', square=True, annot_kws={"size": 16}) 

# Design the graph
plt.title('Confusion Matrix for Model Predictions')  
plt.xlabel('Predicted')  
plt.ylabel('Actual')  
plt.show()  

