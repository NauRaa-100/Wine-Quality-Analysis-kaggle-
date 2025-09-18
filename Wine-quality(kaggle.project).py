import pandas as pd
import numpy as np

df=pd.read_csv(r'E:\Rev-DataScience\Wine.csv')
print(df.head())
print('------Seperate-------')
print(df.describe())
print('------Seperate-------')
print(df.columns)
print('------Seperate-------')
print(df.shape)
print('------Seperate-------')
'''
this dataset about wine quality ,
it has 1599 rows and 12 features 

'''

#=======================================
#Cleaning data
#=======================================
print(df.isnull().sum()) # 0 empty values
print(df.duplicated().sum()) #240
df=df.drop_duplicates(keep='first')
print(df.duplicated().sum())

"""
-- datset has no empty values 
-- but has duplicated values : 240 

*Action => removing those values and keep first one  

"""
#========================================
#Size 
#========================================
print(df.memory_usage(deep=True))
print('------Seperate-------')

df.index=df.index.astype('int32')
df['fixed acidity']=df['fixed acidity'].astype('float16')
df['volatile acidity']=df['volatile acidity'].astype('float16')
df['citric acid']=df['citric acid'].astype('float16')
df['residual sugar']=df['residual sugar'].astype('float16')
df['chlorides']=df['chlorides'].astype('float16')
df['free sulfur dioxide']=df['free sulfur dioxide'].astype('float16')
df['total sulfur dioxide']=df['total sulfur dioxide'].astype('float16')
df['density']=df['density'].astype('float16')
df['pH']=df['pH'].astype('float16')
df['sulphates']=df['sulphates'].astype('float16')
df['alcohol']=df['alcohol'].astype('float16')
df['quality']=df['quality'].astype('int32')

print(df.memory_usage(deep=True))
print('------Seperate-------')

#==========================================
#Relations with quality feature
#==========================================
print(df['quality'].describe())
print('------Seperate-------')
corr = df.corr(numeric_only=True)
print(corr)





