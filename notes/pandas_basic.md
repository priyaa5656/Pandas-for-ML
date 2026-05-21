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
print(df["City"] == "Delhi")
print(df[df["City"] == "Delhi"])
```
Meaning:“Show only those rows where the city is Delhi.”

### Multiple Conditions
```python
print(df[(df["Age"] > 20) & (df["City"] == "Delhi")])
```
Meaning: “Show only those rows where the age is greater than 20 AND the city is Delhi.”

# Function with Filtering
## Example
```python
data = pd.read_csv('students.csv')

def get_city_match_count(city):
    mask = data['City'] == city
    return data[mask].shape[0]

print(get_city_match_count('Delhi'))
```
## Explanation
- `mask` stores True/False values.
- `data[mask]` filters matching rows.
- `.shape[0]` returns the number of rows.

## Multiple Conditions with Masks

### Creating Masks

mask1 = data['City'] == 'Delhi'

mask2 = data['Grade'] == 'A+'

### Using Multiple Conditions

data[mask1 & mask2]

### Explanation

- `mask1` checks rows where City is Delhi.
- `mask2` checks rows where Grade is A+.
- `&` means AND condition.
- Only rows matching both conditions are returned.




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


## value_counts() 🔥
Usage of value_counts():
It is used to count how many times each value appears in a specific column. 😄

## Example
```python
data['City'].value_counts()
```
## Output Example

Delhi     2
Mumbai    1
Meerut    1

## Find Count of Specific Value
### Using Filtering
```python
data[data['City'] == 'Delhi'].shape[0]
```

OR 

### Using value_counts()
```python
data['City'].value_counts()['Delhi']
```


## plot() Function
```python
Used for data visualization.
```

### Line Plot
```python
data['Marks'].plot(kind='line')
```

### Bar Plot and Barh plot
```python
data['Marks'].plot(kind='bar')
```

### Pie Chart
```python
data['Grade'].value_counts().plot(kind='pie')
```

### Important Functions
```python
plt.title()
plt.xlabel()
plt.ylabel()
plt.show()
```


Example:
```python
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
```

# Series Values
```python
series = data['Course'].value_counts()
```

## Get Values
This will only return the count values! 😄🔥
```python
print(series.values)
#important function 
print(series.head)
print(series.tail)
```

## Get Index
This will only return the count index! 😄🔥
```python
print(series.index)
```

Example:
```python
data = pd.read_csv('students.csv')
series = data['Course'].value_counts()
print(series.values)
print(series.index)
```

# Access Specific Value from Series
Purpose :Returns count of a specific value from the Series.

```python
series = data['Course'].value_counts()
series['BCA']

```

## Example
```python
import pandas as pd
data = pd.read_csv('students.csv')
series = data['Course'].value_counts()
print(series['BCA'])
```











