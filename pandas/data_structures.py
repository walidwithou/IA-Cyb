import numpy as np 
import pandas as pd 

# Series : A one dimensional labeled array holding 
# data of any type 

# Dataframe : a two-dimensional data structure that holds data like a two dismension array or table
# with rows and columns 


# Creating a Series
s = pd.Series([1,2,3,4])

print( s.shape , s.dtype)
print(s)

# changing the indexes 

a = pd.Series([1,2,3,4,5] , index = ['A','B','C','D','E'])
print(a)

# Creating a dataframe 

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print(df)

# Creating dataframes from lists
print("\n\n")
df2 = pd.DataFrame([[1,2,3,4],[22,44,22,44]])
print(df2)

# From dicionaries 

data= {
    'ID' : [1,2,3] ,
    'Name' : ['Alice' , 'Bob' , 'Jeffery']
}

print("\n\n")
df3 = pd.DataFrame(data)
print(df3)

print("\n\n")

#From CSV files 
df4 = pd.read_csv('enterprise_data.csv')
print(df4.head(10))

#basic operations 
print(df4.head()) # First five rows
print("\n\n")

print(df4.tail()) # Last five rows 
print("\n\n")

print(df4.info()) # Summary of DataFrame
print("\n\n")

print(df4.describe()) # Statistics of numerical columns 


# Data Selecting 

# Selecting columns 

print(df3['Name'])

# Selecting Rows 
print("SELECTING ROWS \n\n")

print(df3)

print(df3.iloc[1])
print(df3.loc[1])

#filtering 

filtered_df = df4[df4['Units'] != "Percentage"]

print(df4.head())
print(filtered_df.head())

#Data aggregation and Grouping 

classes = np.array(["A" , "B" , "C"])
marks = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
rng = np.random.default_rng()


grades = [{'Name': "Mark" , 'class': rng.choice(classes) , "mark" : rng.choice(marks)  } , 
        {'Name': "jeff" , 'class': rng.choice(classes) , "mark" : rng.choice(marks) } ,
        {'Name': "Robert" , 'class': rng.choice(classes) , "mark" : rng.choice(marks) } ,
        {'Name': "Tim" , 'class': rng.choice(classes)  , "mark" : rng.choice(marks)  } ,
        {'Name': "Hannah" , 'class': rng.choice(classes) , "mark" : rng.choice(marks) } ,
        {'Name': "Sarah" , 'class': rng.choice(classes) , "mark" : rng.choice(marks) } ,
        {'Name': "Mohamed" , 'class': rng.choice(classes) , "mark" : rng.choice(marks) } ,
        {'Name': "Jeorge" , 'class': rng.choice(classes) , "mark" : rng.choice(marks) } ,
        {'Name': "Peter" , 'class':rng.choice(classes) , "mark" : rng.choice(marks) } ,
        {'Name': "Melissa" , 'class': rng.choice(classes)  , "mark" : rng.choice(marks)  } ,
        {'Name': "Alex" , 'class':  rng.choice(classes) , "mark" : rng.choice(marks) } ,
        {'Name': "Peter" , 'class': rng.choice(classes)  , "mark" : rng.choice(marks) } ,
        {'Name': "frank" , 'class': rng.choice(classes) , "mark" :rng.choice(marks) } ,
        
        ]

df5 = pd.DataFrame(grades)
grouped = df5.groupby('class')['mark'].mean()

print(df5)
print("\n\n")
print(grouped)