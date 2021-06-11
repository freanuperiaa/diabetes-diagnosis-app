import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


class LinearRegressionModel():

    def __init__(self):
        dataset = pd.read_csv('diabetes.csv')

        # retrieve independent and dependent variables from dataset
        X = np.array(
            dataset[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 
            'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']]
        )
        y = np.array(dataset['Outcome'])

        # split data to train and test data, with ratio 0.8:0.2
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.20, random_state=42
        )
 
        """
        instantiate LogisticRegression class, solver='lbfgs', max_iter=1000 is needed because it says
            'STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.'
        if without these parameters.
        """

        self.model = LogisticRegression(solver='lbfgs', max_iter=1000)
        # use data to train the model
        self.model.fit(X_train, y_train)

    def predict(
            self, pregnancies, glucose, bp, skin_thickness, insulin, bmi,
            diabetes_pedigree, age
        ):
        """
        input the following:
        'Pregnancies',
        'Glucose', 
        'BloodPressure', 
        'SkinThickness', 
        'Insulin', 
        'BMI', 
        'DiabetesPedigreeFunction', 
        'Age'

        to get the predicted outcome (0 or 1) using the trained Logistic Regression Model
        """

        return self.model.predict([[
            pregnancies, glucose, bp, skin_thickness, insulin, bmi,
            diabetes_pedigree, age
        ]])


lr_model = LinearRegressionModel()
print(lr_model.predict(1, 85, 66, 29, 0, 26.6, 0.351, 31))