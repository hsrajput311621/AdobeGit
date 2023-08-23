import numpy as np # for Arrays
import pandas as pd # for data frame tables
import matplotlib.pyplot as plt # charts and visualization
import matplotlib_inline
import seaborn as sns

df = pd.read_csv('Diwali Sales Data.csv', encoding='unicode_escape' )
print(df.shape)  # to check the csv file total rows and column
#print(df.head())  # it will print the first 5 rows of the file
#print(df.head(10)) # showing first 10 values from the csv file
print(df.info()) # give the information of the csv file
print(df.index) # give the rangeIndev

#drop unrelated/blank columns

#df.drop(['Status', 'unnamed1'], axis = 1 , inplace=True)
#it will remove the unwanted column from the file,
# so 'status' and 'unnamed1' column will be removed.

# print(df.info())

# print(pd.isnull(df).sum())  # it will display sum of all null values in rows.
#
# print(df.shape)
#
# print(df.dropna(inplace=True))
#
# print(df.shape)
#
# print(pd.isnull(df).sum())

#initilize list of lists

# data_test = [['madhav', 11],['Gopi', 15],['Hitesh', ], ['keshav', 25]]
# #create the pandas dataframe using list
# df_test = pd.DataFrame(data_test, columns=['Name', 'Age'])
# print(df_test)
# #df_test.dropna(inplace=True)  drop the row completely which has null value.
# print(df_test)

# df['Amount'] = df['Amount'].astype('int')
#print(df['Amount'].dtypes)  #it tell the datatype of Index
#print(df.columns) # print all the column names.

#rename of the column
#df.rename(columns= {'Marital_Status' : 'Shaadi'})
#print(df.columns)

# print(df.describe())
#print(df[['Age','Orders','Amount']].describe()) # descripion of columns.



### Exploratory Data Analysis ###

# Gender
print(df.columns)

ax = sns.countplot(x = 'Gender' , data = df)

for bars in ax.containers:
    ax.bar_label(bars)

print(ax)

graph = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
print(sns.barplot(x = 'Gender',y='Amount' ,data= graph))
