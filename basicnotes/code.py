import pandas as pd

data = {
    "Name": ["Suraj", "Aman", "Rohit"],
    "Marks": [95, 70, 88]
}

df = pd.DataFrame(data)  #meaning -pd.dataframe👉 Converted the dictionary into a table.
print(df)

#output:   import pandas as pd
# 0 Suraj 95
# 1 Aman 70
# 2 Rohit 88


df = pd.read_csv("students.csv")
print(df)

print(df.head())

print(df.tail())

## df.info() :
print(df.info())

## df.describe()
print(df.describe())

print(df.loc[0])

# Extracting a specific value
print(df.loc[0, "Name"])

# .iloc[] is used for integer-location based indexing
print(df.iloc[0, 1])
print(df.iloc[: , [0, 3, 7]])


# Filtering Data 🔍
#Age > 20
print(df[df["Age"] > 20])

#City == Delhi
print(df["City"] == "Delhi")
print(df[df["City"] == "Delhi"])

#Multiple Conditions
print(df[(df["Age"] > 20) & (df["City"] == "Delhi")])

#8. Sorting Data 📈
#Age ascending
print(df.sort_values("Age"))

#Descending
print(df.sort_values("Age", ascending=False))

##9. Missing Values Handling
#Check Missing Values
print(df.isnull())

#Count Missing Values
print(df.isnull().sum())

#Fill Missing Values
df["Age"] = df["Age"].fillna(0)

#Remove Missing Rows
df = df.dropna()


##10. Real Analysis 🤖
#Average Age
print(df["Age"].mean())

#Maximum Marks
print(df["Marks"].max())

#Minimum Marks
print(df["Marks"].min())


#read.csv  --> Used to load CSV files into a Pandas DataFrame.
#Example:
data = pd.read_csv('students.csv')
print(data)

#type()  ---> This checks what type of object the data is. 🧠
print(type(data))

## shape
# Used to get the number of rows and columns in a DataFrame.
print(data.shape)    #Output: (rows, columns)


## Fetching Data

### Single . find a perticular row or coloumn with give name
print(data['City'])
#or Multiple columns or rows fetching
print(data[['City' , 'Email'  , 'Grade']])

# Multiple Conditions with Masks
mask1 = data['City'] == 'Delhi'
mask2 = data['Grade'] == 'A+'
print(data[mask1 & mask2])

### Specific Row
print(data.iloc[0])

### Specific Row and Column
print(data.loc[0, 'Name'])

### Index Based Fetching
print(data.iloc[0, 1])

## value_counts() 🔥
## Example
print(data['City'].value_counts())



## Find Count of Specific Value
### Using Filtering
data[data['City'] == 'Delhi'].shape[0]

#OR 

### Using value_counts()
print(data['City'].value_counts()['Delhi'])



## plot() Function

### Line Plot
import matplotlib.pyplot as plt
data['Marks'].plot(kind='line')

### Bar Plot and Barh plot
data['Marks'].plot(kind='bar')

### Pie Chart
data['Grade'].value_counts().plot(kind='pie')

### Important Functions
plt.title()
plt.xlabel()
plt.ylabel()
plt.show()


#Example:
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('students.csv')
data['Marks'].plot(kind='pie')
plt.title("Students Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

#OR you use if you want head 5 row only .. 
data['Marks'].head().plot(kind='line')



# unique()
print(data['City'].unique())
# nunique()
print(data['City'].nunique())

#types 😎
print(df.dtypes)


# Series Values
series = data['Course'].value_counts()

## Get Values
print(series.values)

## Get Index
print(series.index)

#Example:
series = data['Course'].value_counts()
print(series.values)
print(series.index)

# Access Specific Value from Series
series = data['Course'].value_counts()

## Example
series['BCA']

#Example:
s1 = pd.Series([10, 20, 30], index=['A', 'B', 'C'])
s2 = pd.Series([1, 2, 3], index=['B', 'C', 'D'])
print(s1 + s2)


#Example:
s1 = pd.Series([10, 20, 30], index=['A', 'B', 'C'])
s2 = pd.Series([2, 1, 3], index=['B', 'A', 'C'])
print(s1 + s2)


#Example:
s1 = pd.Series([10, 20, 30], index=['A', 'B', 'C'])
s2 = pd.Series([1, 2, 3], index=['X', 'Y', 'Z'])
print(s1 + s2)

#Example:
s1 = pd.Series([5, 6, 7], index=[1, 2, 3])
s2 = pd.Series([10, 20, 30], index=[2, 1, 4])
print(s1 + s2)


# drop_duplicates() with subset
data.drop_duplicates(subset=['City'])

#Example:


data = pd.DataFrame({
    'Name': ['Suraj', 'Aman', 'Riya', 'Karan' , 'Tina', 'Riya'],
    'City': ['Delhi', 'Delhi', 'Mumbai', 'goa', 'Chennai' , 'Delhi'],
    'Age': [20, 25, 21, 20, 22 , 20]
})

print("Original Data:\n")
print(data)
print(data.shape)


# WITHOUT inplace
new_data = data.drop_duplicates(subset=['City'])
print("\nNew Data:\n")
print(new_data)

print("\nShape After Removing Duplicates:\n")
print(data.drop_duplicates(subset=['City']).shape)
#or 
print(new_data.shape)


print("\nOriginal Data Still Same:\n")
print(data)
print(data.shape) 


# WITH inplace
new_data= data.drop_duplicates(subset=['City'], inplace=True)
print("\n no new data returned:\n")
print(new_data) 

print("\noriginal data after inplace=true:\n")
print(data)
print(data.shape)


print("\nNext step is multiple columns\n")


# WITHOUT inplace
new_data = data.drop_duplicates( subset=['City', 'Age'])
print("\nAfter Removing Duplicates:\n")
print(new_data)
print(new_data.shape)

# WITH inplace
new_data= data.drop_duplicates(subset=['City' , 'Age'], inplace=True)
print("\n no new data returned:\n")
print(new_data) 

print("\noriginal data after inplace=true:\n")
print(data)
print(data.shape)


print("\nKeep Last Duplicate:\n")
new_data=(data.drop_duplicates(subset=['City', 'Age'],keep='last'))
print()
print(new_data.shape)



