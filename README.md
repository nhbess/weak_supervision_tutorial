# Weak Supervision Workshop

[![Python Version](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-360/)

This repo contains the material for the practical part of the one-day workshop on weak supervision to be hold in Aalborg University Copenhagen, at 29.09.2023. 

---
## Content 

In our workshop, we are going to go through 3 different tutorials: 
1. `part_2_spam_clf` - In this part, we will build a spam detection classifier using weakly supervised data. 
We will work with a dataset of YouTube comments and use a weak supervision approach to annotate it. 
In particular, we will create labeling functions, explore different label models (e.g., majority vote, FABLE), and train a basic classifier. 
Finally, we will also run an end-to-end weakly supervised model SepLL. 
All the experiments will be conducted using Wrench - one of the most popular and comprehensive frameworks for weak supervision.
2. `part_3_eng_pos_tags`- In this part, we will experiment with weak supervision for part-of-speech (POS) tagging. 
We will create labeling functions (LFs) based on syntactic and grammatical rules, in order to obtain weak labels. 
Moreover we will add LFs that employ rule-based and pre-trained taggers. 
Then, the results of the labeling functions and the models trained on the weak labels will be discussed and we will perform an analysis of their results in relation to different types of rules, different training sizes, etc.
3. `part_4_global_pos_tags` - This part, again, involves POS tagging. However, a language of your choice is selected from the Universal Dependencies (https://universaldependencies.org/ )
The key objective of this part is to apply the knowledge you've acquired so far in a completely new and unfamiliar setting.

---
## Installation

In order to be able to work on the tutorials, you need to have all the necessary libraries installed. 
We recommend to use Conda environment. 
For that, please do the following: 

1. Clone/download this GitHub repo
2. Create a new Conda environment:

```
# go to the tutorials directory 
cd weak_supervision_workshop
```

Install the Conda library with pip:
```
pip3 install conda       
```
or download it online: https://www.anaconda.com/download

Create a new Conda environment and **specify the Python version (3.8)**:  
```
conda create --name <the name of your environment> python=3.8
```

4. Install the required libraries using the `requirements.txt` file:

Enter the virtual environment:
```
conda activate <the name of your environment>
```

Install `pip` package (if it is not installed on a user level):
```
conda install pip
```

Install the requirements in the current virtual environment: 
```
pip3 install -r requirements.txt
```
5. launch the jupyter notebook from the activated virtual environment
```
jupyter notebook 
```







Now you can access all jupyter notebooks that we are going to use today. Have fun!

---
## Created by

- [Benjamin Roth](http://benjaminroth.net/)
- [Vasiliki Kougia](https://dm.cs.univie.ac.at/team/person/117900/)
- [Anastasiia Sedova](https://anasedova.github.io)
- [Andreas Stephan](https://andst.github.io)

<img src="img/Uni_Logo_2016.jpg" width="300"/>





