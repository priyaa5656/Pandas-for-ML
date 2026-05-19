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
type(data)

## shape
# Used to get the number of rows and columns in a DataFrame.
print(data.shape)    #Output: (rows, columns)


## Fetching Data

### Single . find a perticular row or coloumn with give name
print(data['City'])
#or Multiple columns or rows fetching
print(data[['City' , 'Email'  , 'Grade']])


### Specific Row
print(data.iloc[0])

### Specific Row and Column
print(data.loc[0, 'Name'])

### Index Based Fetching
print(data.iloc[0, 1])



