# Homework 4

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
2. Open `Homework_4` Folder.
3. Download `HW_4.ipynb`
4. Run all cells and check tests
> 💡NOTE: It's okay to see red **"warnings"** in the final 2 cells, just scroll to the bottom.  

### Results
```text
Linear regression MAX 10-fold score:
Best Cross-Validation Score: 
0.8453827595922794

Ridge MAX 10-fold score and alpha:
Best Alpha: 74.623029
Best Cross-Validation Score: 0.7735374215292923

Lasso MAX 10-fold score and alpha:
Best Alpha: 19.377033
Best Cross-Validation Score: 0.8203098101932735
```

- From here we can conclude that the **Linear Regression Model** was the best with a CV of ~84%
> 💡NOTE: It's okay to see red **"warnings"** in the final 2 cells, just scroll to the bottom.  

### Additional Notes

We used the `MakePipeline` function with `StandardScalar` and `Lasso`/`Ridge` models in order to squeeze out the best performance.
- Note* `Linear Regression` did not use the ***StandardScalar*** because weird test results due to un-normalized data. Instead, only used regular data **without** `StandardScalar`.

