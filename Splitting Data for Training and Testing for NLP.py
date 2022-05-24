#Starting a Practical use case of Natural Text Processing (NLP)

import numpy as np

import pandas as pd

import sklearn as skl

skl.show_versions()
from sklearn.model_selection import train_test_split

df=pd.read_csv('moviereviews5.csv')

overview=df['overview']

print(overview)

vote_average=df['vote_average']

print(vote_average)

Overview_train,Overview_test, vote_average_train, vote_average_test=train_test_split(overview,vote_average, test_size=0.25)

print (Overview_train)

print (Overview_test)
