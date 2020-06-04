import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import numpy.random as nr
import numpy.random as nr
import math
import scipy.stats as ss
import sklearn.preprocessing as pp
import sklearn.model_selection as ms
import sklearn.linear_model as lm
import sklearn.metrics as sklm
import datetime as DT
import io
## Reading CSV files

work_cuts_train = pd.read_csv('Data/AdvWorksCusts.csv')
month_spend = pd.read_csv('Data/AW_AveMonthSpend.csv')
bike_buyer = pd.read_csv('Data/AW_BikeBuyer.csv')
work_cuts_test = pd.read_csv('Data/AW_test.csv')


## drop Null columns
work_cuts_train.drop(['Title', 'MiddleName', 'Suffix', 'AddressLine2'], axis = 1, inplace = True)
work_cuts_test.drop(['Title', 'MiddleName', 'Suffix', 'AddressLine2'], axis = 1, inplace = True)

## identifying duplicates
work_cuts_train.shape
work_cuts_train['CustomerID'].unique().shape

## droping duplicates
work_cuts_train.drop_duplicates(subset = 'CustomerID', keep = 'first', inplace = True)
bike_buyer.drop_duplicates(subset = 'CustomerID', keep = 'first', inplace = True)
month_spend.drop_duplicates(subset = 'CustomerID', keep = 'first', inplace = True)

## joining Two or more pandas data Frame

work_cuts_train = pd.concat([work_cuts_train, bike_buyer.BikeBuyer, month_spend.AveMonthSpend], axis = 1)


## Converting Date of Birth to Age
work_cuts_train['Age'] = [(pd.to_datetime('1998-01-01').year-pd.to_datetime(date).year) for date in work_cuts_train['BirthDate']]
work_cuts_test['Age'] = [(pd.to_datetime('1998-01-01').year-pd.to_datetime(date).year) for date in work_cuts_test['BirthDate']]


labels = np.array(bike_buyer['BikeBuyer'])

## take log
#work_cuts_train['log_AveMonthSpend'] = np.log(work_cuts_train['AveMonthSpend'])
#hist_plot(work_cuts_train['log_AveMonthSpend'], 'log_AveMonthSpend')
month_spend['log_AveMonthSpend'] = np.log(month_spend['AveMonthSpend'])

## changing homeowner flag to categorical 
HomeOwnerFlag_dic = {1:'Yes',0:'No'}
work_cuts_train['HomeOwnerFlag_cat'] = [HomeOwnerFlag_dic[x] for x in work_cuts_train['HomeOwnerFlag']]
work_cuts_test['HomeOwnerFlag_cat'] = [HomeOwnerFlag_dic[x] for x in work_cuts_test['HomeOwnerFlag']]


## Create dummy variables from categorical features

Features_train = work_cuts_train['CountryRegionName']
Features_test = work_cuts_test['CountryRegionName']
enc = pp.LabelEncoder()
enc.fit(Features_train)
enc.fit(Features_test)
Features_train = enc.transform(Features_train)
Features_test = enc.transform(Features_test)


ohe = pp.OneHotEncoder()
encoded = ohe.fit(Features_train.reshape(-1,1))
encoded = ohe.fit(Features_test.reshape(-1,1))
Features_train = encoded.transform(Features_train.reshape(-1,1)).toarray()
Features_test = encoded.transform(Features_test.reshape(-1,1)).toarray()

def encode_string(cat_feature):
    ## First encode the strings to numeric categories
    enc = pp.LabelEncoder()
    enc.fit(cat_feature)
    enc_cat_feature = enc.transform(cat_feature)
    ## Now, apply one hot encoding
    ohe = pp.OneHotEncoder()
    encoded = ohe.fit(enc_cat_feature.reshape(-1,1))
    return encoded.transform(enc_cat_feature.reshape(-1,1)).toarray()
    

categorical_columns = ['Education','Occupation','Gender', 'MaritalStatus','HomeOwnerFlag_cat']#,'BikeBuyer_cat']

for col in categorical_columns:
    temp_train = encode_string(work_cuts_train[col])
    temp_test = encode_string(work_cuts_test[col])
    Features_train = np.concatenate([Features_train, temp_train], axis = 1)
    Features_test = np.concatenate([Features_test, temp_test], axis = 1)

Features_train = np.concatenate([Features_train, np.array(work_cuts_train[['NumberCarsOwned','NumberChildrenAtHome','TotalChildren','YearlyIncome','Age']])], axis = 1)
Features_test = np.concatenate([Features_test, np.array(work_cuts_test[['NumberCarsOwned','NumberChildrenAtHome','TotalChildren', 'YearlyIncome','Age']])], axis = 1)


## Randomly sample cases to create independent training and test data
nr.seed(9988)
x_train = Features_train
y_train = np.ravel(labels)
x_test = Features_test 

scaler = pp.StandardScaler().fit(x_train[:,22:])
x_train[:,22:] = scaler.transform(x_train[:,22:])
x_test[:,22:] = scaler.transform(x_test[:,22:])


### Constract logistic regression model
logistic_mod = lm.LogisticRegression()
logistic_mod.fit(x_train, y_train)

probabilities = logistic_mod.predict_proba(x_test)

def score_model(probs, threshold):
    return np.array([1 if x > threshold else 0 for x in probs[:,1]])
scores = score_model(probabilities, 0.5)


score_csv = pd.DataFrame(scores)
score_csv.to_csv('BikeBuy_predicted.csv', index = False,sep=',', header = True)
