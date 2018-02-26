#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop( 'TOTAL', 0 )
#features = ["salary", "bonus"]
features = ["bonus", "salary"]
data = featureFormat(data_dict, features)


### your code below
from sklearn.linear_model import LinearRegression
target_train, features_train = targetFeatureSplit(data)
print "watch out !!!"
print features_train
print target_train
reg = LinearRegression()
reg.fit(features_train,target_train)


for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )


matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")

# my plot
matplotlib.pyplot.plot(features_train,reg.predict(features_train),color='red')

matplotlib.pyplot.show()
