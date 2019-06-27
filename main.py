from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

diabetes = pd.read_csv('diabetes.csv')
X_train, X_test, y_train, y_test = train_test_split(diabetes.loc[:, diabetes.columns != 'Outcome'], 
                                                    diabetes['Outcome'], 
                                                    stratify=diabetes['Outcome'], 
                                                    random_state=66)


mlp = MLPClassifier(random_state=42)
mlp.fit(X_train, y_train)

mlp.predict()