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
2. Open `Homework_6` Folder.
3. Download `HW5.ipynb`
4. Run all cells or simply see outputs from cells!
5. If any dependcy issues please install what's needed based off imports missing inside cells

## Requirements

---

You are required to classify digits with SVM models.
Compare the performance of linear, radial, and polynomial kernels (classification score).
Tune kernel parameters using RandomizedSearchCV method.
Use PCA to reduce data dimensionality (80% of information remain).
After you apply PCA, use 5-fold Cross-Validation to get the final accuracy.
README.MD file
Team member names and email addresses
Parameters selected for linear, radial, polynomial kernels.
Results comparison between linear, radial, polynomial kernels

---


### Tune kernel parameters using RandomizedSearchCV method.

This was accomplished in this line of code:
```py
search = RandomizedSearchCV(svc, param_distributions=param_grid, n_iter=50, cv=5, scoring='accuracy', random_state=0) # Has the 5-Cross-Fold Validation
```

### Use PCA to reduce data dimensionality (80% of information remain).

This was done here:
```py
pca = PCA(n_components=0.8, random_state=0)  # Retain 80% variance
```

### Parameters selected for linear, radial, polynomial kernels.

The paramaters used were from the `RandomSearchCV` and were as such:
```txt
Best parameters for linear kernel: {'C': 0.30218397440325717, 'degree': 3, 'gamma': 'scale'}

Best parameters for rbf kernel: {'C': 8.389400292173631, 'degree': 3, 'gamma': 0.014695476192547066}

Best parameters for poly kernel: {'C': 5.588135039273247, 'degree': 3, 'gamma': 0.8542657485810173}
```
### After you apply PCA, use 5-fold Cross-Validation to get the final accuracy

This requirement was a little confusing. We weren't sure to go with regular scoring since the code shown above in `Tune kernel...` requirement kind of already has 5-Cross-Fold validation. Therefore, we went out of our way and did the following:
> This does regular scoring for best accuracy
```py
# Step 5: Compare model performances
for kernel, model in best_models.items():
    print(f"\nEvaluating SVM with {kernel} kernel")
    y_pred = model.predict(X_test_pca)
    acc = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {acc:.4f}")
```

> This does CV for getting best accuracy
```py
# Step 5: Compare model performances
from sklearn.model_selection import cross_val_score
for kernel, model in best_models.items():
    print(f"\nEvaluating SVM with {kernel} kernel")
    scores = cross_val_score(model, X_test_pca, y_test, cv=5)
    tot_score = 0
    for score in scores:
        tot_score += score
    tot_score = tot_score/len(scores)
    print(f"{tot_score:.4f}") 
```
As such we have two different scores BUT the results at the end still hold no matter the scoring...
#### Compare the performance of linear, radial, and polynomial kernels (classification score).

> Using regular scoring accuracy method:

```text
Evaluating SVM with linear kernel
Accuracy: 0.9556

Evaluating SVM with rbf kernel
Accuracy: 0.9204

Evaluating SVM with poly kernel
Accuracy: 0.9833
```

> Using CV for scoring accuracy again:

```text
Evaluating SVM with linear kernel
0.9315

Evaluating SVM with rbf kernel
0.7148

Evaluating SVM with poly kernel
0.9574
```

### Results comparison between linear, radial, polynomial kernels

Overall, we can see that the best SVC model was the `poly` kernel model. The `linear` kernel one was close behind but ultimately did not do as well. Last place was the `rbf` kernel model. Doing the CV scoring method really dropped the accuracy a ton on it which kind of makes sense because this kernel is the circle one which kind of feels weird to even use for this digits data. 

Once again, the best models, ranked, were:
1. `Poly` kernel model
2. `Linear` kernel model
3. `rbf` kernel model
