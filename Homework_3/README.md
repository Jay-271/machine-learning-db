# Homework 3

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
2. Open `Homework_3` Folder.
3. Download `HW_1.ipynb`
4. Run all cells and check tests

## Excersize 1 Graph:

![First_fig](https://github.com/ethanspivey/CSCI4120.Group20/blob/main/Homework_3/Fig_1.png)

## Excersize 2 Graph:

![Second_fig](https://github.com/ethanspivey/CSCI4120.Group20/blob/main/Homework_3/Fig_2.png)
