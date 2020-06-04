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
bike_buyer_predicted = pd.read_csv('Data/BikeBuy_predicted.csv')
work_cuts_test = pd.read_csv('Data/AW_test.csv')

bike_buyer_predicted.columns = ['bikebuyer_predicted']

## Checking Null Values
work_cuts_train.isnull().sum()

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
work_cuts_train = pd.concat([work_cuts_train,bike_buyer.BikeBuyer, month_spend.AveMonthSpend], axis = 1)
work_cuts_test = pd.concat([work_cuts_test, bike_buyer_predicted.bikebuyer_predicted], axis = 1)
#work_cuts_test = work_cuts_test.dropna()
#work_cuts_test = work_cuts_test[:500]
#work_cuts_test.replace(np.NaN, 1, inplace=True)

''' Solutions to Replace empty / null values '''

## Solution: 1, replace with space

# work_cuts_train.fillna(" ")

## Solution: 2, Remove rows
# work_cuts_train.dropna()


#def box_plot_occupation(work_cuts_train, col, col_y='YearlyIncome'):
#    for col in cols:
#        plt.figure()
#        sns.set_style("whitegrid")
#        sns.boxplot(col, col_y, data = work_cuts_train)
#        plt.xlabel(col)
#        plt.ylabel(col_y)
#        plt.show()
#
#cols = ['Occupation', 'Education', 'Gender','MaritalStatus','HomeOwnerFlag','NumberCarsOwned','NumberChildrenAtHome']
#box_plot_occupation(work_cuts_train, 'Occupation')

## Converting Date of Birth to Age
work_cuts_train['Age'] = [(pd.to_datetime('1998-01-01').year-pd.to_datetime(date).year) for date in work_cuts_train['BirthDate']]
work_cuts_test['Age'] = [(pd.to_datetime('1998-01-01').year-pd.to_datetime(date).year) for date in work_cuts_test['BirthDate']]



#def plot_scatter_shape(work_cuts_train, cols, shape_col = 'Gender', col_y = 'AveMonthSpend', alpha = 0.2):
#    shapes = ['+', 'o', 's', 'x', '^'] # pick distinctive shapes
#    unique_cats = work_cuts_train[shape_col].unique()
#    for col in cols: # loop over the columns to plot
#        plt.figure()
#        sns.set_style("whitegrid")
#        for i, cat in enumerate(unique_cats): # loop over the unique categories
#            temp = work_cuts_train[work_cuts_train[shape_col] == cat]
#            sns.regplot(col, col_y, data=temp, marker = shapes[i], label = cat,
#                        scatter_kws={"alpha":alpha}, fit_reg = False, color = 'blue')
#        plt.title('Scatter plot of ' + col_y + ' vs. ' + col) # Give the plot a main title
#        plt.xlabel(col) # Set text for the x axis
#        plt.ylabel(col_y)# Set text for y axis
#        plt.legend()
#        plt.show()
#            
#num_cols = ['Age']
#plot_scatter_shape(work_cuts_train, num_cols)   

#def box_plot(work_cuts_tain, cols, col_y = 'AveMonthSpend'):
#    for col in cols:
#        plt.figure()
#        sns.set_style('whitegrid')
#        sns.boxplot(col, col_y, data = work_cuts_train)
#        plt.xlabel(col)
#        plt.ylabel(col_y)
#        plt.show()
#    
#cols = ['Gender', 'MaritalStatus','NumberCarsOwned','NumberChildrenAtHome']
#box_plot(work_cuts_train, cols)

#def box_plot2(work_cuts_tain, cols, col_x = 'BikeBuyer'):
#    for col in cols:
#        plt.figure()
#        sns.set_style('whitegrid')
#        sns.boxplot(col_x, col, data = work_cuts_train)
#        plt.xlabel(col_x)
#        plt.ylabel(col)
#        plt.show()
#    
#cols = ['AveMonthSpend', 'YearlyIncome','NumberChildrenAtHome','NumberCarsOwned']
#box_plot2(work_cuts_train, cols)


#cat_cols = ['StateProvinceName', 'CountryRegionName', 
#       'Education', 'Occupation', 'Gender', 'MaritalStatus']
#
#work_cuts_train['dummy'] = np.ones(shape = work_cuts_train.shape[0])
#
#for col in cat_cols:
#    count = work_cuts_train[['dummy', 'BikeBuyer', col]].groupby(['BikeBuyer', col], as_index = False).count()
#    temp = count[count['BikeBuyer'] == 0][[col, 'dummy']]
#    plt.figure()
#    plt.subplot(1,2,1)
#    plt.bar(temp[col], temp.dummy)
#    plt.xticks(rotation = 90)
#    plt.title('Counts for ' + col + '\n did not buy')
#    plt.ylabel('count')
#    plt.subplot(1, 2, 2)
#    temp = count[count['BikeBuyer'] == 1][[col, 'dummy']]
#    plt.bar(temp[col], temp.dummy)
#    plt.xticks(rotation=90)
#    plt.title('Counts for ' + col + '\n Bought')
#    plt.ylabel('count')
#    plt.xlabel(col)
#    plt.show()

## plot Density plot
#def hist_plot(vals, lab):
#    ## Distribution plot of values
#    plt.figure()
#    sns.distplot(vals)
#    plt.title('Histogram of ' + lab)
#    plt.xlabel('Value')
#    plt.ylabel('Density')
#    
##labels = np.array(auto_prices['price'])
#hist_plot(work_cuts_train['AveMonthSpend'], 'AveMonthSpend')

## take log
#work_cuts_train['log_AveMonthSpend'] = np.log(work_cuts_train['AveMonthSpend'])
#hist_plot(work_cuts_train['log_AveMonthSpend'], 'log_AveMonthSpend')
month_spend['log_AveMonthSpend'] = np.log(month_spend['AveMonthSpend'])

## changing homeowner flag to categorical 
HomeOwnerFlag_dic = {1:'Yes',0:'No'}
work_cuts_train['HomeOwnerFlag_cat'] = [HomeOwnerFlag_dic[x] for x in work_cuts_train['HomeOwnerFlag']]
work_cuts_test['HomeOwnerFlag_cat'] = [HomeOwnerFlag_dic[x] for x in work_cuts_test['HomeOwnerFlag']]

##BikeBuyer
BikeBuyer_dic = {1:'Yes',0:'No'}
work_cuts_train['bikebuy_cat'] = [BikeBuyer_dic[x] for x in work_cuts_train['BikeBuyer']]
work_cuts_test['bikebuy_cat'] = [BikeBuyer_dic[x] for x in work_cuts_test['bikebuyer_predicted']]

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
    

categorical_columns = ['Education','Occupation','Gender', 'MaritalStatus','HomeOwnerFlag_cat','bikebuy_cat']

for col in categorical_columns:
    temp_train = encode_string(work_cuts_train[col])
    temp_test = encode_string(work_cuts_test[col])
    Features_train = np.concatenate([Features_train, temp_train], axis = 1)
    Features_test = np.concatenate([Features_test, temp_test], axis = 1)

Features_train = np.concatenate([Features_train, np.array(work_cuts_train[['NumberCarsOwned','NumberChildrenAtHome','TotalChildren','YearlyIncome','Age']])], axis = 1)
Features_test = np.concatenate([Features_test, np.array(work_cuts_test[['NumberCarsOwned','NumberChildrenAtHome','TotalChildren', 'YearlyIncome','Age']])], axis = 1)

## Randomly sample cases to create independent training and test data
nr.seed(9988)
labels = np.array(month_spend['log_AveMonthSpend'])
indx = range(Features_train.shape[0])
indx = ms.train_test_split(indx, test_size = 500)

#x_train = Features_train[indx[0], :]
#y_train = np.ravel(labels[indx[0]])
##x_test = Features_train[indx[1],:]
#x_test = Features_test
#y_test = np.ravel(labels[indx[1]])

x_train = Features_train
y_train = np.ravel(labels)
x_test = Features_test
y_test = np.ravel(labels[indx[1]])

## define and fit the linear regression model
lin_mod = lm.LinearRegression()
lin_mod.fit(x_train, y_train)

def print_metrics(y_true, y_predicted):
    ## First compute R^2 and the adjusted R^2
    r2 = sklm.r2_score(y_true, y_predicted)
    
    ## Print the usual metrics and the R^2 values
    print('Mean Square Error      = ' + str(sklm.mean_squared_error(y_true, y_predicted)))
    print('Root Mean Square Error = ' + str(math.sqrt(sklm.mean_squared_error(y_true, y_predicted))))
    print('Mean Absolute Error    = ' + str(sklm.mean_absolute_error(y_true, y_predicted)))
    print('Median Absolute Error  = ' + str(sklm.median_absolute_error(y_true, y_predicted)))
    print('R^2                    = ' + str(r2))
    
def resid_plot(y_test, y_score):
    ## first compute vector of residuals. 
    resids = np.subtract(y_test.reshape(-1,1), y_score.reshape(-1,1))
    ## now make the residual plots
    plt.figure()
    sns.regplot(y_score, resids, fit_reg=False)
    plt.title('Residuals vs. predicted values')
    plt.xlabel('Predicted values')
    plt.ylabel('Residual')
    plt.show()

def hist_resids(y_test, y_score):
    ## first compute vector of residuals. 
    resids = np.subtract(y_test.reshape(-1,1), y_score.reshape(-1,1))
    ## now make the residual plots
    sns.distplot(resids)
    plt.title('Histogram of residuals')
    plt.xlabel('Residual value')
    plt.ylabel('count')
    plt.show()
    
def resid_qq(y_test, y_score):
    ## first compute vector of residuals. 
    resids = np.subtract(y_test, y_score)
    ## now make the residual plots
    plt.figure()
    ss.probplot(resids.flatten(), plot = plt)
    plt.title('Residuals vs. predicted values')
    plt.xlabel('Predicted values')
    plt.ylabel('Residual')
    plt.show()
  

y_score = lin_mod.predict(x_test) 
print_metrics(y_test, y_score) 
hist_resids(y_test, y_score)  
resid_qq(y_test, y_score) 
resid_plot(y_test, y_score)


#scaler = pp.StandardScaler().fit(x_train[:,24:])
#x_train[:,24:] = scaler.transform(x_train[:,24:])
#x_test[:,24:] = scaler.transform(x_test[:,24:])

def plot_regularization(l, train_RMSE, test_RMSE, coefs, min_idx, title):
    plt.figure()
    plt.plot(l, test_RMSE, color = 'red', label = 'Test RMSE')
    plt.plot(l, train_RMSE, label = 'Train RMSE')    
    plt.axvline(min_idx, color = 'black', linestyle = '--')
    plt.legend()
    plt.xlabel('Regularization parameter')
    plt.ylabel('Root Mean Square Error')
    plt.title(title)
    plt.show()
    
    plt.figure()
    plt.plot(l, coefs)
    plt.axvline(min_idx, color = 'black', linestyle = '--')
    plt.title('Model coefficient values \n vs. regularizaton parameter')
    plt.xlabel('Regularization parameter')
    plt.ylabel('Model coefficient value')
    plt.show()

def test_regularization_l2(x_train, y_train, x_test, y_test, l2):
    train_RMSE = []
    test_RMSE = []
    coefs = []
    for reg in l2:
        lin_mod = lm.Ridge(alpha = reg)
        lin_mod.fit(x_train, y_train)
        coefs.append(lin_mod.coef_)
        y_score_train = lin_mod.predict(x_train)
        train_RMSE.append(sklm.mean_squared_error(y_train, y_score_train))
        y_score = lin_mod.predict(x_test)
        test_RMSE.append(sklm.mean_squared_error(y_test, y_score))
    min_idx = np.argmin(test_RMSE)
    min_l2 = l2[min_idx]
    min_RMSE = test_RMSE[min_idx]
    
    title = 'Train and test root mean square error \n vs. regularization parameter'
    plot_regularization(l2, train_RMSE, test_RMSE, coefs, min_l2, title)
    return min_l2, min_RMSE
     
l2 = [x for x in range(1,101)]
out_l2 = test_regularization_l2(x_train, y_train, x_test, y_test, l2)
print(out_l2)

lin_mod_l2 = lm.Ridge(alpha = out_l2[0])
lin_mod_l2.fit(x_train, y_train)
y_score_l2 = lin_mod_l2.predict(x_test)


def test_regularization_l1(x_train, y_train, x_test, y_test, l1):
    train_RMSE = []
    test_RMSE = []
    coefs = []
    for reg in l1:
        lin_mod = lm.Lasso(alpha = reg)
        lin_mod.fit(x_train, y_train)
        coefs.append(lin_mod.coef_)
        y_score_train = lin_mod.predict(x_train)
        train_RMSE.append(sklm.mean_squared_error(y_train, y_score_train))
        y_score = lin_mod.predict(x_test)
        test_RMSE.append(sklm.mean_squared_error(y_test, y_score))
    min_idx = np.argmin(test_RMSE)
    min_l1 = l1[min_idx]
    min_RMSE = test_RMSE[min_idx]
    
    title = 'Train and test root mean square error \n vs. regularization parameter'
    plot_regularization(l1, train_RMSE, test_RMSE, coefs, min_l1, title)
    return min_l1, min_RMSE
    
l1 = [x/5000 for x in range(1,101)]
out_l1 = test_regularization_l1(x_train, y_train, x_test, y_test, l1)
print(out_l1)


lin_mod_l1 = lm.Lasso(alpha = 0.000001)
lin_mod_l1.fit(x_train, y_train)
y_score_l1 = lin_mod_l1.predict(x_test)


y_score_untransform = np.exp(y_score_l1)
y_score_csv = pd.DataFrame(y_score_untransform)
y_score_csv.to_csv('AveMonthSpend_predicted.csv', index = True, header = False)
