# Loading the modules and packages(Dependencies).
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Data collection and analysis
data = pd.read_csv("C:\\Users\\prakh\\Downloads\\Practice DataSet\\insurance.csv")

# Print 5 rows of dataset.
print(data.head())

# Checking the number of rows and columns
print("Rows:", data.shape[0], "\nColumns:", data.shape[1])

# Fetching some information of dataset
print(data.info())

# Checking the missing value
print(data.isnull().sum())

# Data Analysis Part

# Statical Measures of dataset
print(data.describe())

# Distribution of age value
sns.set()
plt.figure(figsize=(6, 6))
sns.distplot(data["age"])
plt.title("Age Distribution")
plt.show()

# Gender Column evaluation
plt.figure(figsize=(6, 6))
sns.countplot(x="sex", data=data)
plt.title("Gender Evaluation")
plt.show()

print(data["sex"].value_counts())

# BMI distribution Evaluation
plt.figure(figsize=(6, 6))
sns.distplot(data["bmi"])
plt.title("BMI Distribution")
plt.show()

# Children columns evaluation
plt.figure(figsize=(6, 6))
sns.countplot(x="children", data=data)
plt.title("Children Evaluation")
plt.show()
print(data["children"].value_counts())

# Smoker column Evaluation
plt.figure(figsize=(6, 6))
sns.countplot(x="smoker", data=data)
plt.title("Smoker Evaluation")
plt.show()
print(data["smoker"].value_counts())

# Region column Evaluation
plt.figure(figsize=(6, 6))
sns.countplot(x="region", data=data)
plt.title("Region Evaluation")
plt.show()
print(data["region"].value_counts())

# Distribution of charges value
plt.figure(figsize=(6, 6))
sns.distplot(data["charges"])
plt.title("Charges Distribution")
plt.show()


# Data Pre-Processing
# Encoding the categorical feature

# Encoding sex column
data.replace({'sex': {'male': 0, "female": 1}}, inplace=True)

# Encoding smoker column
data.replace({'smoker': {'yes': 0, "no": 1}}, inplace=True)

# Encoding region column
data.replace({'region': {'southeast': 0, "southwest": 1, "northeast": 2, "northwest": 3}}, inplace=True)

print(data.head())

# Positioning the X and Y for model
X = data.drop(columns="charges", axis=1)
Y = data["charges"]

# Splitting the data into training and testing data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.2, random_state=2)
print("X's rows:", X.shape[0],"\nX's columns:", X.shape[1])
print("X's rows:", X_train.shape[0], "\nX's columns:", X_train.shape[1])
print("X's rows:", X_test.shape[0], "\nX's columns:", X_test.shape[1])

# Model Training
# Loading the linear Regression Model using sklearn
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

# Model Evaluation
# Prediction on training data

training_data_prediction = regressor.predict(X_train)

# R Square Value
r2_train = metrics.r2_score(Y_train, training_data_prediction)
print("R square value:", r2_train)

# Prediction on testing data

testing_data_prediction = regressor.predict(X_test)

# R Square Value
r2_test = metrics.r2_score(Y_test, testing_data_prediction)
print("R square value:", r2_test)


# Building a Predective system

age = int(input('Enter the age:'))
sex = int(input("Press 0 for male and 1 for Female:"))
bmi = float(input('Enter the BMI value:'))
children = int(input('Enter the number of children:'))
smoker = int(input("Press 0 if you smoke and 1 if you don't :"))
region = int(input("Press 0 for Southeast, 1 for Southwest, 2 for Northeast, 3 for Northwest:"))

input_data = (age, sex, bmi, children, smoker, region)
# Changing input_data into numpy array
input_data_as_numpy_array = np.asarray(input_data)

# Reshape the array
input_data_reshape = input_data_as_numpy_array.reshape(1, -1)

predicting_value = regressor.predict(input_data_reshape)

print("Predicting cost of given data is:", predicting_value, "dollar")



