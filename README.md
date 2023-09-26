# Weak Supervision workshop

[![Python Version](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-360/)

This repo contains the material for the practical part of the one-day workshop on weak supervision to be hold in Aalborg University Copenhagen, at 29.09.2023. 

---
## Content 

In our workshop, we are going to go through 3 different tutorials: 
1. `01_ws_baseics.ipynb` - we will train a spam detection classifier. 
For that, we will first collect the training data, then annotate it in a weakly supervised fashion 
(i.e., with help of labeling functions),
aggregate the annotations into weak labels (with two different models),
and train a simple MLP. 
Additionally, we will train a more sophisticated end-to-end SepLL model. 
2. 
3.
 
---
## Installation

In order to be able to work on the tutorials, you need to have all the necessary libraries installed. 
For that, please do the following: 

0. install python 3.8
1. clone/download this GitHub repo
2. create a virtual environment using the `requirements.txt` file:
```
# go to the tutorials directory 
cd WS_tutorial

# install the virtualenv library if you don't already have it
pip3 install virtualenv       

# create a new virtual environment  
virtualenv <the name of your environment>  

# enter the virtual environment         
source <the name of your environment>/bin/activate

# install the requirements in the current virtual environment 
pip3 install -r requirements.txt
```
3. launch the jupyter notebook from the activated virtual environment
```
jupyter notebook 
```

Now you can access all jupyter notebooks that we are going to use today. Have fun!

---
## Created by

- [Benjamin Roth](http://benjaminroth.net/)
- [Anastasiia Sedova](https://anasedova.github.io)
- [Andreas Stephan](https://andst.github.io)
- Vasiliki Kougia

<img src="img/Uni_Logo_2016.jpg" width="300"/>





