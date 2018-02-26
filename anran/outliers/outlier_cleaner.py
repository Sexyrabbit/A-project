#!/usr/bin/python

import pandas as pd
import math 

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    diff = [math.fabs(i-j) for i,j in zip(predictions,net_worths)]

    data_frame = pd.DataFrame({
        'pred':predictions,
        'age':ages,
        'net':net_worths,
        'diff':diff
        })

    print len(data_frame['age'])
    for i in range(8):
        print i
        data_frame = data_frame.drop(data_frame['diff'].idxmax())
    print len(data_frame['age'])
    data_frame = data_frame.reset_index(drop=True)
    print data_frame.loc[0,'diff']
    cleaned_data = []

    ### your code goes here
    #for i in len(predictions):
    for i in range(len(data_frame['age'])):
        cleaned_data.append((data_frame.loc[i,'age'],data_frame.loc[i,'net'],data_frame.loc[i,'diff']))
    print cleaned_data
    
    return cleaned_data



import random
import numpy
import matplotlib.pyplot as plt
import pickle

from outlier_cleaner import outlierCleaner


### load up some practice data with outliers in it
ages = pickle.load( open("practice_outliers_ages.pkl", "r") )
net_worths = pickle.load( open("practice_outliers_net_worths.pkl", "r") )



### ages and net_worths need to be reshaped into 2D numpy arrays
### second argument of reshape command is a tuple of integers: (n_rows, n_columns)
### by convention, n_rows is the number of data points
### and n_columns is the number of features
ages       = numpy.reshape( numpy.array(ages), (len(ages), 1))
net_worths = numpy.reshape( numpy.array(net_worths), (len(net_worths), 1))
print "after reshape()"

from sklearn.cross_validation import train_test_split
ages_train, ages_test, net_worths_train, net_worths_test = train_test_split(ages, net_worths, test_size=0.1, random_state=42)

### fill in a regression here!  Name the regression object reg so that
### the plotting code below works, and you can see what your regression looks like


from sklearn.linear_model import LinearRegression

reg = LinearRegression()
reg.fit(ages_train, net_worths_train)


print reg.coef_
print reg.score(ages_test,net_worths_test)


try:
    plt.plot(ages, reg.predict(ages), color="blue")
except NameError:
    pass
plt.scatter(ages, net_worths)
#plt.show()


### identify and remove the most outlier-y points
cleaned_data = []
try:
    print "calling outlier_cleaner()"
    predictions = reg.predict(ages_train)
    print predictions,net_worths_train
    predictions = [item for sublist in predictions for item in sublist]
    net_worths_train = [item for sublist in net_worths_train for item in sublist]
    ages_train = [item for sublist in ages_train for item in sublist]
    print "to list"
    print predictions
    print net_worths_train
    cleaned_data = outlierCleaner( predictions, ages_train, net_worths_train )
except NameError:
    print "your regression object doesn't exist, or isn't name reg"
    print "can't make predictions to use in identifying outliers"



