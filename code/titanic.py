import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import seaborn as sns
plt.style.use('default')


def prediction(row):
    sex = row['Sex']
    pclass = row['Pclass']
    p = 0
    if pclass == 1:
        if sex == 'female':
            p = 0.968085
        elif sex == 'male':
            p = 0.368852
    elif pclass == 2:
        if sex == 'female':
            p = 0.921053
        elif sex == 'male':
            p = 0.157407
    elif pclass == 3:
        if sex == 'female':
            p = 0.500000
        elif sex == 'male':
            p = 0.135447

    return bernoulli.rvs(p) 


def add_interval(row):
    fare = row['Fare']
    interval = ''
    if 0 <= fare <= 9:
        interval = '[0, 9]'
    elif 10 <= fare <= 19:
        interval = '[10, 19]'
    elif 20 <= fare <= 29:
        interval = '[20, 29]'
    elif 30 <= fare <= 39:
        interval = '[30, 39]'
    else:
        interval = '[40, +['

    return interval



train = pd.read_csv('../data/titanic-train.csv')
test = pd.read_csv('../data/titanic-test.csv')
test_survived = pd.read_csv('../data/gendermodel.csv')

test = pd.concat([test, test_survived], axis=1)
print(test.head())


