#******************************NILESH RAMAN **********************************
#-----------------------CAR SELLING PRICE PREDICTION-----------------------------

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
df=pd.read_csv("Car.csv")#IMPORTING CSV FILE FROM DIRECTORY
from joblib import dump,load

#Finding out DATA TYPES.
print(df.dtypes)

print(df.index)

# Checking for missing value.
print(df.isnull().sum()) 

#Dropping null(missing value) column.
df = df.drop(columns=["torque"])
df=df.drop(columns=["name"])
df=df.dropna()


#--------------------------PREPROCESSING---------------------------------------
#for removing kmpl and km/kg from mileage.
df['mileage']=df['mileage'].replace(' kmpl','',regex=True).str.replace(',', '')
df['mileage']=df['mileage'].replace(' km/kg','',regex=True).str.replace(',', '')
#for removing  and cc from engine.
df['engine']=df['engine'].replace(' CC','',regex=True).str.replace(',', '')
#for removing  and bhp from max_power.
df['max_power']=df['max_power'].replace(' bhp','',regex=True).str.replace(',', '')

#converting string into numeric
df['mileage'] = pd.to_numeric(df['mileage'])
df['engine'] = pd.to_numeric(df['engine'])
df['max_power'] = pd.to_numeric(df['max_power'])

#to remove the null value from 
df=df.dropna()


#***************Sperating Independent and Dependent data*******************

#Independent      
x=df.iloc[:,:]
x=x.drop(columns=["selling_price"])
#Dependent
y=df["selling_price"]


#----------------Encoding data-------------------------
from sklearn.preprocessing import LabelEncoder

la=LabelEncoder()
x['fuel']=la.fit_transform(x['fuel'])

lb=LabelEncoder()
x['seller_type']=lb.fit_transform(x['seller_type'])

lt=LabelEncoder()
x['transmission']=lt.fit_transform(x['transmission'])

lo=LabelEncoder()
x['owner']=lo.fit_transform(x['owner'])



#-------------scaling on Independent data.-----------------------
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x=sc.fit_transform(x)

#-----------------training and testing data----------------------
# Splitting of training and testing data  
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)



#Applying--------- (RandomForestRegressor)----------------------
from sklearn.ensemble import RandomForestRegressor
  
reg=RandomForestRegressor()
reg.fit(x_train,y_train)


#-------------------prediction of data-----------------------------
y_pred=reg.predict(x_test)

#-----------------Checking accuracy using r2_score-------------------
from sklearn.metrics import r2_score
print(r2_score(y_test,y_pred))

#----------------Saving the data using joblib----------------------

dump(la,"fuel.joblib")
dump(lb,"seller_type.joblib")
dump(lt,"transmission.joblib")
dump(lo,"owner.joblib")
dump(sc,"scaling.joblib")
dump(reg,"regressor.joblib")














