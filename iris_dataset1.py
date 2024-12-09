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
iris = load_iris()  # Loads the Iris dataset from Scikit-learn
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)  # Creates a DataFrame for the feature data
iris_df['species'] = iris.target  # Adds the target (species) column to the DataFrame
iris_df['species'] = iris_df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})  # Maps target numbers to species names

# Prepare the Data
X = iris.data  # Features (inputs) of the dataset
y = iris.target  # Labels (species) of the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)  # Splits data into training and testing sets (70% train, 30% test)

# Train the Model
model = LogisticRegression(max_iter=200)  # Creates a Logistic Regression model (used for classification)
model.fit(X_train, y_train)  # Trains the model using the training data

# Make Predictions
predictions = model.predict(X_test)  # Predicts the species using the test data

# Create a Confusion Matrix
cm = confusion_matrix(y_test, predictions)  # Generates a confusion matrix comparing actual vs predicted labels
plt.figure(figsize=(8, 6))  # Creates a figure with specific size (8x6 inches)

# Define a light lotus-like tone for the squares in the confusion matrix
lotus_cmap = sns.light_palette("#D84B6C", as_cmap=True)  # Defines a soft pink lotus color palette for the heatmap

# Create the heatmap with a white background and lotus-colored squares
sns.heatmap(cm, annot=True, fmt='d', cmap=lotus_cmap, xticklabels=iris.target_names,  # Creates the heatmap with annotations, using lotus color
            yticklabels=iris.target_names, cbar=False, linewidths=1, linecolor='white',  # Removes colorbar, adds white lines between squares
            square=True, annot_kws={"size": 16})  # Ensures squares are uniform and adjusts annotation size

plt.title('Confusion Matrix for Model Predictions')  # Sets the title for the heatmap
plt.xlabel('Predicted')  # Sets label for x-axis (Predicted species)
plt.ylabel('Actual')  # Sets label for y-axis (Actual species)
plt.show()  # Displays the heatmap plot

# Save and Load the Model (Optional)
joblib.dump(model, 'iris_classifier.pkl')  # Saves the trained model as a .pkl file
loaded_model = joblib.load('iris_classifier.pkl')  # Loads the saved model
print("Loaded Model Accuracy:", loaded_model.score(X_test, y_test))  # Prints the accuracy of the loaded model on the test data
