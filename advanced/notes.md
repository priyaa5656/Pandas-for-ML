# What is groupby()? 🤔
groupby() is used to divide data into groups based on similar values.

Simple Meaning 😄
Same type ki rows ko group mein divide karna

## Real-Life Example 🧠
Name	City	Marks
Suraj	Delhi	90
Aman	Delhi	80
Riya	Mumbai	95
Tina	Mumbai	85

If we group by City:
Delhi Group           Mumbai Group
Suraj                 Riya
Aman                   Tina

## we have Dataset Fortune100.csv like this Example 🧠
Rank	Title	Sector	    Revenue
1	    Walmart	Retail	    648
2	    Amazon	Technology	574
3	    Apple	Technology	383
4	    Exxon	Energy	    344
....


## Step 1 
Read Fortune100.csv and store it in the 'company' variable.
```python
company = pd.read_csv('Fortune100.csv')
```

## Step 2 🔥:
Create groups according to the Sector column
```python
company.groupby('Sector')
```
Meaning: Create groups based on the 'Sector'.

Example Groups 😄
Technology Group --> Amazon , Apple
Retail Group-->  Walmart

## IMPORTANT 😄:
groupby() : It only creates groups. It does not perform calculations. 😄

## types()
Meaning: Check what type of object the company is.
```python
print(type(company))
#Output Example : <class 'pandas.core.frame.DataFrame'>
```

## len():
Meaning 🔥: Total rows count
```python
print(len(company))
```

Example Output: 100
Meaning: Dataset mein 100 rows hain


## size():
Meaning 😄:How many companies are there in every sector?
```python
print(sector.size())
```
Example Output 🚀
Energy 10
Retail 5
Technology 8

Meaning:
Energy sector → 10 companies
Retail sector → 5 companies
Technology sector → 8 companies

## company.groupby('Sector') :
Meaning 🧠: By creating Sector wise groups.
```python
print(company.groupby('Sector'))
# output: <pandas.api.typing.DataFrameGroupBy object at 0x0000 001705F9AA3050>>
```
Meaning: Group object has been created

## company.groupby('Sector').size()
Meaning 😎: How many companies are there in each sector?
```python
print(company.groupby('Sector').size())
```
Example Output 🚀
Energy         5
Finance        8
Retail        12
Technology    15


## sort_values()
Which sector has the maximum number of companies?
```python
print(sector.size().sort_values(ascending=False))
```

###  Step-by-Step 🔥
Step 1: sector.size()
Find: How many companies are there in every sector?
Step 2: sort_values(ascending=False)
Meaning: bring the biggest value to the top

Example Output 🚀
Technology 20
Retail 15
Finance 12
Energy 8


## first() : 
Meaning 😄 : Har group ki first row dikhao
```python 
print(sector.first())
```
Example 🧠
Technology Group:
Amazon
Apple
Microsoft

Output 🚀
Sector	    First Company
Technology	Amazon


## last():
Meaning 🔥: Har group ki last row dikhao
```python 
print(sector.last())
```
Example 🧠
Technology Group:
Amazon
Apple
Microsoft

Output 🚀
Sector	    Last Company
Technology	Microsoft

## sector.groups
it give us all indexes of different groups 
```python
print(sector.groups)
```
OUTPUT :{'Aerospace': [28 ], 'Automotive': [11, 12, 20, 55, 56, 57, 58, 59, 60, 94], 'Consumer Goods': [22, 23, 26, 77, 78, 79, 80, 81, 82, 83, 84], 'Energy': [5, 13, 61, 62, 63], 'Entertainment': [85, 86, 87, 88], 'Financials': [3, 10, 36, 37, 38, 39, 40, 41], 'Healthcare': [4, 7, 8, 14, 18, 42, 43, 44, 45, 46, 47, 48, 49], 'Industrial': [64, 65, 66, 67, 68], 'Logistics': [69, 70, 71], 'Retail': [0, 9, 16, 17, 27, 72, 73, 74, 75, 76], 'Technology': [1, 2, 6, 15, 21, 24, 25, 29, 30, 31, 32, 33, 34, 35, 50, 51, 52, 53, 54, 89, 90, 91, 92, 93, 95, 96, 97, 98, 99], 'Telecom': [19 ]}

Meaning : 
Sector Row :  Indexes
Aerospace':   [28 ]
Telecom':     [19 ]

## NOW THIS 😄🔥
Meaning 🧠:fetch Index 1 row 
```python
print(company.iloc[1, :])
```
OUTPUT 🚀
Rank	Title	 Sector
2,      Amazon,  Technology


## sector.get_group('Energy')
Meaning: Bring all the rows of Energy sector
SIMPLE LANGUAGE 😄groupby() created Sector-wise groups.
so now 

```python 
print(sector.get_group('Energy'))
```
means:Energy basket wala kholo

Example 😊Suppose:
Index   Title   Sector
5       Exxon   Energy
13      Chevron Energy

Output: 
Index   Rank Title  Sector
5       6    Exxon  Energy
13     14   Chevron Energy

### To view the full data 🚀use it
```python 
pd.set_option('display.max_columns', None)
print(sector.get_group('Energy'))
```
### Specific columns can be seen:
```python
print(sector.get_group('Energy')[['Title', 'Revenue_Billion_USD']])
```

## IMPORTANT🏆
Code Meaning
groupby() -create groups
groups - show indexes
get_group()- show actual rows

## print(sector.groups.keys())  or print(company['Sector'].unique())
View all groups
```python
print(sector.groups.keys())

#OR

print(company['Sector'].unique())
```
Output 😎
dict_keys(['Technology','Retail','Energy'])


## sector.get_group('Technology').shape
How many rows and columns are there in the Technology Group?
```python
print(sector.get_group('Technology').shape)
```

Output 🚀
(29, 9),  29- total rows , 9-total columns

Step 1: Bring all the rows of Technology sector 🚀
get_group('Technology sector')

Step 2: Tell rows and columns count
.shape


```python
print(sector.get_group('Technology').shape[0])
print(sector.get_group('Technology').shape)
print(sector.get_group('Technology').shape[1])
```

IMPORTANT 🏆
Code	Meaning
.shape[0]	rows count
.shape[1]	columns count
.shpae  	rows + columns


## sector.sum()
Meaning 🔥: Calculate the total of the numerical columns for each sector.
IMPORTANT 🧠 sum(): Works only on numeric columns! 😄🔥
Examples: Employees, Revenue, Profit

```python
print(sector.sum())
```
output like this 
Index  Rank  ... Revenue_Billion_USD  Profit_Billion_USD
Sector                       ...                                        
Aerospace          28    29  ...                77.8                -2.2
Automotive        482   492  ...              1768.5               126.7
Consumer Goods    715   726  ...               586.3                73.8

### perticular coloumn sum. Only Revenue Sum. 
Meaning 🧠Total revenue of each sector

```python
print(sector['Revenue_Billion_USD'].sum())
```
output: 
Sector           Revenue_Billion_USD
Aerospace           77.8
Automotive        1768.5
Consumer Goods     586.3
Energy            1318.8
Entertainment      173.9


## sector.mean()
Meaning 🧠🚀Calculate the average of numerical columns of every sector.
```python
print(sector.mean())
```
Example output :
Sector                Index  Rank  ... Revenue_Billion_USD  Profit_Billion_USD
Aerospace          28    29  ...                77.8                -2.2
Automotive        482   492  ...              1768.5               126.7
Consumer Goods    715   726  ...               586.3                73.8
Energy            204   209  ...              1318.8               107.7
Entertainment     346   350  ...               173.9                 2.6

### perticular coloumn mean. Only Revenue mean. 
👇Average revenue of each sector
```python
print(sector['Revenue_Billion_USD'].mean())
```

output:
Sector           Revenue_Billion_USD
Aerospace          77.800000
Automotive        176.850000
Consumer Goods     53.300000
Energy            263.760000
Entertainment      43.475000

## Difference:company['Revenue_Billion_USD'].mean() VS sector['Revenue_Billion_USD'].mean()
Code	Meaning	Output
company['Revenue_Billion_USD'].mean()|	Pure dataset average|	single value
sector['Revenue_Billion_USD'].mean()|	Sector-wise average|	    many values


## sector['Revenue_Billion_USD'].mean().sort_values(ascending=False)
Calculate the average revenue for each sector, then sort from highest to lowest.
```python
print(sector['Revenue_Billion_USD'].mean().sort_values(ascending=False))
```
Exaple output:
Sector           Revenue_Billion_USD
Energy            263.760000
Automotive        176.850000
Healthcare        172.576923
Retail            148.850000
Telecom           134.000000
Financials        106.537500
Technology         98.420690

## TOTAL PROFIT TOP 5 SECTORS 🚀
```python
print(sector['Profit_Billion_USD'] .sum() .sort_values(ascending=False) .head(5))
```
Meaning 😄🔥
Find out the total profit of every sector then sort from highest to lowest first show top 5


## AVERAGE PROFIT TOP 5 SECTORS 😊
```python
print( sector['Profit_Billion_USD'] .mean() .sort_values(ascending=False) .head(5))
```
Meaning 🧠🔥
Find out the average profit of every sectorthen sort from highest to lowestfirst show top 5

🚀

IMPORTANT 🏆
Function	Meaning
size()	count
sum()	total
mean()	average
max()	highest
min()	lowest

## Question based .:

### 1️⃣ Sabse jyada revenue wali top 5 companies 😎
```python
print(company.sort_values('Revenue_Billion_USD',ascending=False)[['Title', 'Revenue_Billion_USD']].head(5))
```

### 2️⃣ Sabse jyada profit wali top 10 companies 🚀
```python
print(company.sort_values('Profit_Billion_USD',ascending=False)[['Title', 'Profit_Billion_USD']].head(10))
```

### 3️⃣ Kis sector mein sabse jyada companies hain 😄🔥
```python
print(sector.size().sort_values(ascending=False).head(1))
```

### 4️⃣ Har sector ki average revenue 🧠
```python
print(sector['Revenue_Billion_USD'].mean().sort_values(ascending=False))
```

### 5️⃣ Har sector ka total profit 😎🔥
```python
print(sector['Profit_Billion_USD'].sum().sort_values(ascending=False))
```

### 6️⃣ Sabse jyada employees wali company 🚀
```python
print(company.sort_values('Employees',ascending=False)[['Title', 'Employees']].head(1))
```

### 7️⃣ Loss mein chal rahi companies 😄
```python
print(company[company['Profit_Billion_USD'] < 0])
```

### 8️⃣ Technology sector ki companies 😎🔥
```python
print(sector.get_group('Technology'))
```

### 9️⃣ Har sector ki average employees 🧠🚀
```python
print(sector['Employees'].mean().sort_values(ascending=False))
```

### 🔟 Top 5 profitable sectors 😄🔥
```python
print(sector['Profit_Billion_USD'].sum().sort_values(ascending=False).head(5))
```

### 1️⃣1️⃣ Sabse kam revenue wali companies 😎
```python
print(company.sort_values('Revenue_Billion_USD')[['Title', 'Revenue_Billion_USD']].head(5))
```

### 1️⃣2️⃣ Har sector mein total employees 🚀
```python
print(sector['Employees'].sum().sort_values(ascending=False))
```

## MOST IMPORTANT PATTERN 🏆
Goal|	Function
Create Group|	groupby()
Total|	sum()
Average|	mean()
Ranking|	sort_values()
Top rows|	head()
Filtering|	[]


## Now we use new dataset delivery.csv 

First Step 😎🔥
Load CSV
```python 
import pandas as pd
ipl = pd.read_csv('deliveries.csv')
print(ipl.head())
```

IMPORTANT IPL QUESTIONS 🚀🏏

### 1️⃣ Sabse jyada runs kis batsman ne banaye 😄
Meaning 🧠🔥Total runs for each batsman, followed by the players with the highest runs.
```python
print(ipl.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10))
```


### 2️⃣ Sabse jyada fours 😎
```python
print(ipl[ipl['batsman_runs'] == 4].groupby('batsman').size().sort_values(ascending=False).head(10))
Meaning 🚀Jab batsman_runs = 4 tabhi count karo
```

### 3️⃣ Sabse jyada sixes 🏏🔥
```python
print(ipl[ipl['batsman_runs'] == 6].groupby('batsman').size().sort_values(ascending=False).head(10))
```

### 4️⃣ Sabse jyada wickets 😎
```python
print(ipl['bowler'].value_counts().head(10))

⚠️ Ye exact wickets nahi 😄Bas appearances count karta hai.
Better wicket calculation 🚀
print(ipl['player_dismissed'].value_counts().head(10))
```


### 5️⃣ Kis team ne sabse jyada runs banaye 😄🔥
```python
print(ipl.groupby('batting_team')['total_runs'].sum().sort_values(ascending=False))
```

### 6️⃣ Virat Kohli total runs 😎
```python
print(ipl[ipl['batsman'] == 'V Kohli']['batsman_runs'].sum())
```

### 7️⃣ MS Dhoni total sixes 🚀
```python
print(ipl[(ipl['batsman'] == 'MS Dhoni') &(ipl['batsman_runs'] == 6)].shape[0])








