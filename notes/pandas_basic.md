# What is Pandas? 🐼
Pandas is a Python library used to organize, clean, analyze, and manipulate data. 🚀

In simple terms 👇
Pandas = The "superpowered" version of Excel, right inside Python! 😎

Real-Life Example 🧠
Imagine you have data on students:
Name	|Marks	|Hours
Suraj	|95	|8
Aman	|70	|4

If you need to:
Calculate averages
Identify students with low scores
Clean up missing data
Feed data into an ML model
...then Pandas is the tool to use! 👍

## With this, you can:
Read CSV files
Manage tables
Clean data
Prepare AI/ML datasets
Perform analysis and visualization

## Pandas primarily utilizes two key structures: 📦
### 1️⃣ Series: Single-column data
Example: [10, 20, 30]
### 2️⃣ DataFrame ⭐: A table consisting of rows and columns
Example:
Name    Marks
Suraj   95
Aman    70

DataFrame is the most important Pandas structure because most real-world datasets are stored in tabular form.

## First Code 🐼

Install (optional if local setup)
pip install pandas
Import Pandas
import pandas as pd    # pd is shortcut😄


## example: Create First DataFrame 🔥
```python
import pandas as pd
data = {"Name": ["Suraj", "Aman", "Rohit"],
        "Marks": [95, 70, 88]}
df = pd.DataFrame(data)
print(df)
```

## Reading a CSV File 📂
Let's assume the file name is: students.csv
```python
df = pd.read_csv("students.csv")
print(df)
```

Meaning:
Part	Meaning
import-	Import a library
pandas-	Library name
as-	Nickname
pd-	Short name
Simple: “We will use the Pandas library under the name ‘pd’.”


df	Variable name
=	Store
pd	Pandas
read_csv()	Read a CSV file
"students.csv"	File name
Simple language: “Read the ‘students.csv’ file and store it in the ‘df’ variable.”

What is df? 🤔
df = DataFrame
In other words, a table.

print(df)
Meaning: “Display the entire table on the screen.”

## 3. head() 🔥
```python
print(df.head())
```
Displays the first 5 rows or what you want.

### df.info() :
Data information is given:
columns
data type
null values
```python
print(df.info())
```

### df.describe()
Numerical summary is given 📊
meaning
min
max
count
```python
print(df.describe())
```


## 4. tail()
```python
print(df.tail())
```
Displays the last rows.

## 5. .loc[]
```python
print(df.loc[0])
```
Meaning
Part	Meaning
loc	label based access
[0]	row number 0

## Extracting a specific value- Specific row + column
```python
print(df.loc[0, "Name"])
```
Meaning: “Give the name of the first row.”


## 6. .iloc[] — Extracting data by position
```python
print(df.iloc[0, 1])
```
Meaning
Part	Meaning
iloc	position based
0	first row
1	second column

And 
```python
print(df.iloc[: , [0, 3, 7]])
```



## Row + column position
```python
print(df.iloc[0, 1])
```

### Note: Difference 🔥
Method	Uses
.loc[]	Name
.iloc[]	Number position


## 7. Filtering Data 🔍
### Age > 
```python
print(df[df["Age"] > 20])
```
Meaning: “Show only those rows where the age is greater than 20.”

### City == Delhi
```python
print(df[df["City"] == "Delhi"])
```
Meaning:“Show only those rows where the city is Delhi.”

### Multiple Conditions
```python
print(df[(df["Age"] > 20) & (df["City"] == "Delhi")])
```
Meaning: “Show only those rows where the age is greater than 20 AND the city is Delhi.”


## 8. Sorting Data 📈
### Age ascending
```python
print(df.sort_values("Age"))
```
Meaning:“Arrange by age.”

### Descending
```python
print(df.sort_values("Age", ascending=False))
```
Meaning:The oldest at the top.


## 9. Handling Missing Values ​​🚨

Empty values ​​are very common in datasets.
Example:
| Name | Age |
|---|---|
| Suraj | 20 |
| Aman | NaN |

### Check for Missing Values
```python
print(df.isnull())
```
Meaning: Check where data is missing.

### Count Missing Values
```python
print(df.isnull().sum())
```
Meaning: Count how many missing values ​​exist.


### Fill Missing Values
```python
df["Age"] = df["Age"].fillna(0)
```
Meaning: Insert 0 into the empty spaces.

## Remove Rows with Missing Values
```python
df = df.dropna()
```
Meaning: Remove any row that contains a missing value.

## 10. Real Analysis🤖
### Mean -
```python
print(df["Age"].mean())
```
Meaning: Find the average age.


### Max-
```python
print(df["Marks"].max())
```
Meaning: Highest marks.


### Min-
```python
print(df["Marks"].min())
```
Meaning: Lowest marks.


# read_csv()
Used to load CSV files into a Pandas DataFrame.
Example:
```python
data = pd.read_csv('students.csv')
print(data)
```


## type()
This checks what type of object the data is. 🧠
```python
type(data)   #Output: <class 'pandas.core.frame.DataFrame'>
```

Example 🧠
```python
x = 10
print(type(x))     # Output: <class 'int'>
```

## shape
Used to get the number of rows and columns in a DataFrame.
```python
print(data.shape)    #Output: (rows, columns)
```

Example :
```python
🔥 If data:
Name	Marks
Suraj	95
Aman	80
Riya	90
print(data.shape)
```
Output: (3, 2)  -->  beacause:- 3 rows ,  2 columns

## Fetching Data

### Single 
```python
data['Name']
```
### Multiple columns or rows
```python
print(data[['City' , 'Email'  , 'Grade']])
```

### Specific Row
```python
data.iloc[0]
```

### Specific Row and Column
```python
data.loc[0, 'Name']
```

### Index Based Fetching
```python
data.iloc[0, 1]
```











