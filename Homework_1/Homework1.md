# Homework 1

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
pip install pandas numpy matplotlib seaborn scikit-learn jupyter scipy tensorflow keras
pip install torch torchvision torchaudio
```

### Access File:
1. Go to: https://github.com/ethanspivey/CSCI4120.Group20/tree/main
2. Open `Homework_1` Folder.
3. Download `Homework1_KNN.ipynb`
4. Simply run cell 1 & 2

## Data preperation:
- These lines of code seperate the X values (features) and the Y-values (targets)
	```python
	    url = 'https://raw.githubusercontent.com/ruiwu1990/CSCI_4120/master/KNN/iris.data'
	    df = pd.read_csv(url, header=None)
	    data = df.iloc[:, :-1].values
	    labels = df.iloc[:, -1].values
	```
- This list stores accuracy for batches
	```python
	final_predict = []
	```
- We then use train_test_split from import to seperate into x_train, x_test, etc:
	```python
	from sklearn.model_selection import train_test_split
	```
- Inside each batch loop, we do the following:
	```python
	for k in range(1, 21):
            accuracy = 0
            neighbors = clfr(n_neighbors=k)
            neighbors.fit(X_train, y_train)
            predictions = neighbors.predict(X_test)
	```
	- This simply fits and returns prediction according to 1-20 K-neighbors since last index is n-1. 
- To check if the prediction is correct we go into this loop:
	```python
	#evaluate the precision
            for i, prediction in enumerate(predictions):
                if prediction == y_test[i]:
                    accuracy += 1
	```
- Then we get the correct accuracy score based off of how many K's were testd:
	```python
	accuracy /= len(predictions)
            #append to current batch list
            predictions_batch.append(accuracy)
        #Append all batches to list
        final_predict.append(predictions_batch)
	```
	- Remember the predictions batch was simply a 2-D array storing K-values 1-20 for 5 total batches.
- The rest of the code simply does the average and prints to screen:
	```python
	#convert data to np array for easy mean calculation:
    pred_arr = np.array(final_predict)
    #print(pred_arr)
    average_per_k = np.mean(pred_arr, axis=0)
    for k in range(0,20):
        print(f"K-value: {k+1} | Score: {average_per_k[k]}")
    return average_per_k
	```
- Output already averaged:
```text
K-value: 1 | Score: 0.9400000000000001
K-value: 2 | Score: 0.932
K-value: 3 | Score: 0.952
K-value: 4 | Score: 0.944
K-value: 5 | Score: 0.9559999999999998
K-value: 6 | Score: 0.9480000000000001
K-value: 7 | Score: 0.9480000000000001
K-value: 8 | Score: 0.9399999999999998
K-value: 9 | Score: 0.944
K-value: 10 | Score: 0.9559999999999998
K-value: 11 | Score: 0.944
K-value: 12 | Score: 0.9480000000000001
K-value: 13 | Score: 0.9480000000000001
K-value: 14 | Score: 0.9480000000000001
K-value: 15 | Score: 0.944
K-value: 16 | Score: 0.9359999999999999
K-value: 17 | Score: 0.9359999999999999
K-value: 18 | Score: 0.9239999999999998
K-value: 19 | Score: 0.9199999999999999
K-value: 20 | Score: 0.9199999999999999
```
There are similar results because the larger the k the less noise there is but the classification boundaries is bad when k increases.
## Findings

- Modifying the following:
```python
        X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=.33, random_state=i+1, shuffle=True)
```
- It was decided that random state = i+1 (basically 1-5 based off current batch)
	- This was done to test different shuffling of data that could lead to better K-neighbors.
	- We can see this in effect moreso in the indiviudal batches for K's 1-20:
```python
[
	[0.98 0.98 0.98 0.98 0.98 0.98 0.98 0.98 0.98 0.98 0.98 0.98 0.98 0.98
	  0.98 0.98 0.98 0.98 0.98 0.98] # Random state = 1

	 [1.   0.98 1.   1.   1.   1.   0.98 0.96 0.98 0.98 0.98 1.   0.98 0.98
	  0.98 0.98 0.98 0.98 0.98 0.98] # Random state = 2

	 [0.96 0.96 0.94 0.94 0.94 0.94 0.94 0.96 0.96 0.92 0.96 0.94 0.94 0.96
	  0.96 0.96 0.96 0.94 0.96 0.94] # Random state = 3

	 [0.96 0.96 0.98 0.98 0.98 0.98 0.98 0.98 0.98 0.98 0.98 0.98 0.98 0.98
	  0.98 0.98 0.98 0.98 0.98 0.98] # Random state = 4

	 [0.94 0.94 0.96 0.96 0.98 0.98 1.   1.   0.98 1.   1.   1.   1.   1.
	  1.   1.   1.   1.   1.   0.98] # Random state = 5
]
```
- As we can see, better random-states offer better K-neighbors due to better data sampling. 
