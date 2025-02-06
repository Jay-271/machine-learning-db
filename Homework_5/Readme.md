# Homework 5 - RF Accuracy Improvement

## Team Members
-Ethan Spivey spiveye22@students.ecu.edu
-Jason Avila-Soria avilasoriaj22@students.ecu.edu

## Installing and making environment...

### Installing ubuntu

#### For Windows users:

-Install Virtualbox: https://www.virtualbox.org/wiki/Downloads (Links to an external site.)

-Download Ubuntu 20.04 LTS:  https://releases.ubuntu.com/20.04/Links (Links to an external site.) (22.04 may not work…)

-Install Jupyter notebook: https://linuxhint.com/install-jupyter-notebook-on-ubuntu-20-04/

-If you want to increase your VM performance:

-http://www.rawinfopages.com/tips/2017/07/speed-up-virtualbox-in-windows/Links to an external site.

#### For Mac users:

check this tutorial:
https://www.youtube.com/watch?v=Hzji7w882OY&t=33sLinks to an external site.

### Creating a Virtual Environment + Dependencies

```bash
sudo apt update
sudo apt install python3
sudo apt install python3-venv
python3 -m venv env_name
source env_name/bin/activate
```
**Once activated:**
```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter scipy tensorflow keras yellowbrick
pip install torch torchvision torchaudio
```

### Access File:
1. Go to: https://github.com/ethanspivey/CSCI4120.Group20/tree/main
2. Open `Homework_5` Folder.
3. Download `HW6.ipynb`
4. Run all cells or simply see outputs from cells!
5. If any dependcy issues please install what's needed based off imports missing inside cells

## The TODO's:

* ✅ TODO Select some features (X), hint: based on the connections with our Y (importance? correlation?) 
* ✅ TODO need 5 fold cross validation
* ✅ TODO Tune parameters for RandomForestClassifier
* ✅ TODO Calculate Average accuracy score
* ✅ TODO Calculate Average (accuracy score/number of features)
* ✅ Your accuracy should be more than 0.92 and (Accuracy/number of features) should be more than 0.45.
* ✅ Hyperparameters used.
* ✅ Accuracy and (accuracy/number of features)

### Code breakdown

#### Init data
```py
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load the breast cancer dataset
data = load_breast_cancer()
X, y = data.data, data.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

forest_pipe = RandomForestClassifier(random_state = 0)

param_dist = {
    'n_estimators': np.unique(np.round(np.logspace(0, 3, num=1000)).astype(int)),
    'max_depth': [3, 5, 10, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Use RandomizedSearchCV for faster hyperparameter tuning
random_search = RandomizedSearchCV(
    estimator=forest_pipe,
    param_distributions=param_dist,
    n_iter=70,  # Number of random samples
    cv=5,
    scoring='accuracy',
    random_state=0,
    n_jobs=-1
)
random_search.fit(X_train, y_train)

# Evaluate the best model on the test set
best_model = random_search.best_estimator_
feature_importances = best_model.feature_importances_
```
![First_fig](https://github.com/ethanspivey/CSCI4120.Group20/blob/main/Homework_5/hw6_1.png)

#### Retrain with 2 best features gotten from first CV search

```py
#Show in plot best features:
importances_df = pd.DataFrame({
    'Feature': data.feature_names,
    'Importance': feature_importances
}).sort_values(by='Importance', ascending=False)
plt.figure(figsize=(10, 6))
plt.barh(importances_df['Feature'], importances_df['Importance'])
plt.xlabel('Feature Importance')
plt.title('Feature Importances in Random Forest')
plt.show()

# Select the top 5% most important features
threshold = np.percentile(feature_importances, 95)
selected_features = np.where(feature_importances >= threshold)[0]
X_selected = X[:, selected_features]

# Split data into training and testing sets using only best features
X_train, X_test, y_train, y_test = train_test_split(X_selected, y, test_size=0.2, random_state=0)

#Find best model again using only those features:
random_search = RandomizedSearchCV(
    estimator=forest_pipe,
    param_distributions=param_dist,
    n_iter=70,  # Number of random samples
    cv=5,
    scoring='accuracy',
    random_state=0,
    n_jobs=-1
)
random_search.fit(X_train, y_train)
best_model = random_search.best_estimator_
```
![Second_fig](https://github.com/ethanspivey/CSCI4120.Group20/blob/main/Homework_5/hw6_2.png)

#### Get accuracy

```py
#get accuracy
y_pred = best_model.predict(X_test)
test_accuracy = accuracy_score(ytest, y_pred)
# Calculate the accuracy per feature
ratio = test_accuracy / X_selected.shape[1]
print("Test Accuracy:", test_accuracy)
print("Test Accuracy/Number of Features:", ratio)
print("Number of Selected Features:", X_selected.shape[1])
print("Selected Feature Indices:", selected_features)
### OUTPUT:
# Test Accuracy: 0.9649122807017544
# Test Accuracy/Number of Features: 0.4824561403508772
# Number of Selected Features: 2
# Selected Feature Indices: [22 27]
###
```
![Third_fig](https://github.com/ethanspivey/CSCI4120.Group20/blob/main/Homework_5/hw6_3.png)

#### Model params

```py
#Specific attributes of model:
params = best_model.get_params()
for param in params.items():
    print(param)

### OUTPUT:
# ('bootstrap' = True)
# ('ccp_alpha' = 0.0)
# ('class_weight' = None)
# ('criterion' = 'gini')
# ('max_depth' = 5)
# ('max_features' = 'sqrt')
# ('max_leaf_nodes' = None)
# ('max_samples' = None)
# ('min_impurity_decrease' = 0.0)
# ('min_samples_leaf' = 2)
# ('min_samples_split' = 10)
# ('min_weight_fraction_leaf' = 0.0)
# ('n_estimators' = 101)
# ('n_jobs' = None)
# ('oob_score' = False)
# ('random_state' = 0)
# ('verbose' = 0)
# ('warm_start' = False)
###
```

![Fourth_fig](https://github.com/ethanspivey/CSCI4120.Group20/blob/main/Homework_5/hw6_4.png)


