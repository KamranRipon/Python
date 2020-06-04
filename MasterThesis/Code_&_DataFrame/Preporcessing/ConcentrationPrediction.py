import pandas as pd
from skimage.io import imread, imshow
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from skimage.feature import match_template
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
import math
from sklearn import linear_model
import sklearn.metrics as sklm
import scipy.stats as ss
import re
import sklearn.model_selection as ms
import numpy.random as nr
import scipy.stats as ss

#from sklearn.model_selection import cross_val_score
#from sklearn.model_selection import KFold
#from sklearn.model_selection import ShuffleSplit
#from sklearn.model_selection import RepeatedKFold
#from sklearn.model_selection import GridSearchCV
#from sklearn.ensemble import RandomForestRegressor

#nr.seed(7854)

################################################################
pd.set_option('display.max_columns',None)
################################################################

data_dir = 'ML_data/'

def getNumbers(str): 
    array = re.findall(r'[0-9]+', str) 
    return array 


img_name = list()

roi1_mean = list()
roi1_median = list()
roi1_std = list()

roi2_mean = list()
roi2_median = list()
roi2_std = list()
img_ratio = list()
concentration = list()

### Ratio

Ratio_of_mean = list()
Ratio_of_median = list()
Ratio_of_std = list()



for i, roi in enumerate(os.listdir(data_dir)):

        
    indexlist = list() 
    ig = imread(data_dir+roi)
    img = imread(data_dir+roi)
#    plt.figure()
#    imshow(img)
#    plt.title(roi)
    for jj, ii in enumerate(img):
        if np.mean(ii) == 255:
            pass
        else:
            indexlist.append(jj)
            
    listlist=list()
    for x in indexlist:
        try:
            if x+1 == indexlist[indexlist.index(x) +1]:
                listlist.append(x)
            
        except:
            pass 
       
    img = img[listlist[3]:listlist[-12],55:622]
#    plt.figure()
#    imshow(img)
#    plt.title(roi)
    #print(img.shape)
    
    try:
        if roi.split('.')[0].split()[-1] == 'ROI_1':
            ReOI1 = img.shape[0]
            #print('ReOI1',ReOI1)
        else:
            ReOI2 = img.shape[0]
            #print('ReOI2',ReOI2)
            img_ratio.append(ReOI1/ReOI2)
    except:
        pass
    
    
    
#####################################################################
#    print(i,' ',roi)
#    print()
#    print(np.mean(img))
#    print(np.median(img))
#    print(np.std(img))
#    print()
    
#####################################################################
  
    
########################   Index    ################################
    images = os.listdir(data_dir)        
#    for name in images:
    imgname_1 = roi
    
    try:
        imgname_2 = images[images.index(imgname_1)+1]
        
        if imgname_1.split()[:-1] == imgname_2.split()[:-1]:
            img_name.append(roi.split('.')[0])
    except:
        pass

##################### ROI 1 #############################
    if roi.split()[-1].split('.')[0] == 'ROI_1':
        roi1_mean.append(np.mean(img))
#        roi1_mean.append(np.log(np.mean(img)))
        roi1_median.append(np.median(img))
        roi1_std.append(np.std(img))
#        roi1_std.append(np.log(np.std(img)))
        ######################################
        roi1_Mean = np.mean(img)
        roi1_Median = np.median(img)
        roi1_Std = np.std(img)
        ######################################


##################### ROI 2 #############################
    if roi.split()[-1].split('.')[0] == 'ROI_2':
        roi2_mean.append(np.mean(img))
        roi2_median.append(np.median(img))
        roi2_std.append(np.std(img))
        ###########################
        roi2_Mean = np.mean(img)
        roi2_Median = np.median(img)
        roi2_Std = np.std(img)
        ###########################
        
        ##########################
        Ratio_of_mean.append(roi1_Mean/roi2_Mean)
        Ratio_of_median.append(roi1_Median/roi2_Median)
        Ratio_of_std.append(roi1_Std/roi2_Std)
        ############################
        
##################### Concentra column ##################
    name=roi
    
    try:
        name2 = images[images.index(name)+1]
        
        if name.split()[:-1] == name2.split()[:-1]:
            arr = getNumbers(name)
            try:
                concentration.append(np.int(arr[0]))
            except:
                pass
        
    except:
        pass

'''Creating ration list '''

#for i in range(126):
#    Ratio_of_mean.append(roi1_mean[i]/roi2_mean[i])
#    Ratio_of_median.append(roi1_median[i]/roi2_median[i])
#    Ratio_of_std.append(roi1_std[i]/roi2_std[i])



#roi1_mean = np.log(roi1_mean)
#roi1_std = np.log(roi1_std)
#roi1_median = np.log(roi1_median)
#roi1_median = np.sqrt(roi1_median)
#
#roi2_mean = np.log(roi2_mean)
##roi2_std = np.sqrt(roi2_std)
#roi2_std = np.sqrt(roi2_std)
#roi2_median = np.log(roi2_median)
#
#img_ratio = np.log(img_ratio)*-1
#
#Ratio_of_mean = np.sqrt(Ratio_of_mean)
#Ratio_of_median = np.sqrt(Ratio_of_median)
#Ratio_of_std = np.sqrt(Ratio_of_std)



#zippedList =  list(zip(img_name, roi1_mean, roi1_median, roi1_std, 
#                       roi2_mean, roi2_median,roi2_std, img_ratio,concentration))
zippedList =  list(zip(img_name, roi1_mean, roi1_median, roi1_std, roi2_mean, 
                       roi2_median,roi2_std, img_ratio,Ratio_of_mean, Ratio_of_median,
                       Ratio_of_std, concentration))


df = pd.DataFrame(zippedList, columns = ['img_name', 'roi1_mean', 'roi1_median','roi1_std',
                                         'roi2_mean', 'roi2_median','roi2_std', 'img_ratio',
                                         'Ratio_of_mean', 'Ratio_of_median', 'Ratio_of_std','concentration'])

df.columns = ['ImageName', 'ControlLine_mean', 'ControlLine_median','ControlLine_std', 'TestLine_mean','TestLine_median',
             'TestLine_std','Ratio_of_CL_to_TL','Ratio_of_mean', 'Ratio_of_median', 'Ratio_of_std', 'Concentration']    

    
    
    
#for x in df.columns[1:-1]:
#    plt.figure()
#    sns.distplot(df[x])
#    plt.title(x)
    

for x in df.columns[1:-1]:
    f, [ax1,ax2,ax3] = plt.subplots(1,3)
    sns.distplot(df[x],ax=ax1)
    sns.distplot(np.sqrt(df[x]), ax=ax2)
    sns.distplot(np.log(df[x]), ax=ax3)
    ax1.set_title(x, fontsize = 15)
    ax2.set_title('Square root of '+ x, fontsize=15)
    ax3.set_title('Log of ' + x, fontsize=15)

#for x in df.columns[1:-1]:
#    f, [ax1,ax2] = plt.subplots(1,2)
#    sns.distplot(df[x],ax=ax1)
#    sns.distplot(np.log(df[x]), ax=ax2)
#    ax1.set_title(x)
#    ax2.set_title('Log of '+x)


#df.to_csv('CropImage_Data2.csv')
#df.to_csv('ConcentrationPrediction_DataFrame.csv')
#zippedList =  list(zip(roi1_mean, roi1_median, roi1_std, 
#                       roi2_mean, roi2_median,roi2_std,concentration))
#
#df = pd.DataFrame(zippedList, columns = ['roi1_mean', 'roi1_median','roi1_std',
#                                      'roi2_mean', 'roi2_median','roi2_std', 'concentration'])
#    


#scaler = StandardScaler()
##
#scaler.fit(df.drop(['img_name','concentration'],axis=1))
#scaled_features = scaler.transform(df.drop(['img_name','concentration'],axis=1))
#df1 = pd.DataFrame(scaled_features,columns=df.columns[1:-1])


#X = df[['roi1_mean', 'roi1_median','roi1_std', 'roi2_mean', 'roi2_median','roi2_std']]
X = df[['ControlLine_mean', 'ControlLine_median','ControlLine_std', 'TestLine_mean','TestLine_median',
             'TestLine_std','Ratio_of_CL_to_TL','Ratio_of_mean', 'Ratio_of_median', 'Ratio_of_std',]]
    
y = df['Concentration']

#X_train, X_test, y_train, y_test = train_test_split(scaled_features, df['concentration'], test_size=0.3, random_state=101)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

#lm = LinearRegression()
lm = LinearRegression(fit_intercept=False)

lm.fit(X_train,y_train)

# print the intercept
print(lm.intercept_)
print(lm.coef_)

#coeff_df = pd.DataFrame(lm.coef_,X.columns,columns=['Coefficient'])
#print(coeff_df)

predictions = lm.predict(X_test)

#print('MAE:', metrics.mean_absolute_error(y_test, predictions))
#print('MSE:', metrics.mean_squared_error(y_test, predictions))
#print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))


def print_metrics(y_true, y_predicted, n_parameters):
    ## First compute R^2 and the adjusted R^2
    r2 = sklm.r2_score(y_true, y_predicted)
    r2_adj = r2 - (n_parameters - 1)/(y_true.shape[0] - n_parameters) * (1 - r2)

    ## Print the usual metrics and the R^2 values
    print('Mean Square Error      = ' + str(sklm.mean_squared_error(y_true, y_predicted)))
    print('Root Mean Square Error = ' + str(math.sqrt(sklm.mean_squared_error(y_true, y_predicted))))
    print('Mean Absolute Error    = ' + str(sklm.mean_absolute_error(y_true, y_predicted)))
    print('Median Absolute Error  = ' + str(sklm.median_absolute_error(y_true, y_predicted)))
    print('R^2                    = ' + str(r2))
    print('Adjusted R^2           = ' + str(r2_adj))

y_score = lm.predict(X_test) 
print_metrics(y_test, y_score, 28)


predictions = predictions.round()

def hist_resids(y_test, y_score):
    ## first compute vector of residuals. 
    resids = np.subtract(y_test, y_score)
    ## now make the residual plots
    plt.figure()
    sns.distplot(resids)
    plt.title('Histogram of residuals')
    plt.xlabel('Residual value')
    plt.ylabel('count')
    
hist_resids(y_test, y_score) 

def resid_qq(y_test, y_score):
    ## first compute vector of residuals. 
    resids = np.subtract(y_test, y_score)
    ## now make the residual plots
#    ss.probplot(resids.flatten(), plot = plt)
    plt.figure()
    ss.probplot(resids, plot = plt)
    plt.title('Residuals vs. predicted values')
    plt.xlabel('Predicted values')
    plt.ylabel('Residual')
    
resid_qq(y_test, y_score)  

def resid_plot(y_test, y_score):
    ## first compute vector of residuals. 
    resids = np.subtract(y_test, y_score)
    ## now make the residual plots
    plt.figure()
    sns.regplot(y_score, resids, fit_reg=False)
    plt.title('Residuals vs. predicted values')
    plt.xlabel('Predicted values')
    plt.ylabel('Residual')

resid_plot(y_test, y_score) 
#df.to_csv('CropImage_Data.csv')

#df.to_excel('Concentration_Prediction_DataFrame.xlsx')

#def distribution(num_col):
#    plt.figure()
#    sns.distplot(X[num_col], color='g')
#    plt.title(num_col)
#
#for num_col in X.columns:
#    distribution(num_col)
