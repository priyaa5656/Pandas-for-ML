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
print(delivery['player_dismissed'].value_counts().head(10))

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
```

## delivery.groupby
Meaning :🧠🔥Create a separate group for each batsman.
BUT output does not look useful 😄🔥 That's why usually after groupby:
Function| Meaning
.sum()  |total
.mean() | average
.size() |count
.first()| first row
.last() | last row


Example: Total runs per batsman
```python 
print(delivery.groupby('batsman')['batsman_runs'].sum())
```
Example Output 🚀
V Kohli |7263
MS Dhoni| 5082
RG Sharma| 6211

## .get_group  (Fetching a specific group)
Bring only Virat Kohli's rows
```python
runs = delivery.groupby('batsman')
print(runs.get_group('V Kohli'))
```

## .shape
```python
runs = delivery.groupby('batsman')
runs.get_group('V Kohli').shape        # (3494, 21)
```

output explain: 
Step 1 Create every batsman's group 😄🏏
groupby('batsman')

Step 2 🚀👇Sirf:Virat Kohli's rows came out 🔥🔥
get_group('V Kohli')


Step 3 🧠How many rows and columns are there in the Virat Kohli group?
.shape
output:(rows, columns)


## runs['batsman_runs'].sum()
Meaning :Find out the total runs of each batsman
```python
runs = delivery.groupby('batsman')
runs['batsman_runs'].sum()    # or group_name['column'].sum()
```

STEP-BY-STEP 🚀
Step 1 😄Create a group of every batsman 🔥
runs = delivery.groupby('batsman')

Step 2 🚀Only runs column selected 😄🔥
runs['batsman_runs']


Step 3 👉Add runs of every batsman 🚀
.sum()

## Which batsman has scored the most runs?
Calculate the total runs for all batsmen, then sort them from highest to lowest.
Next, display the top 5 batsmen.

```python
print(
runs['batsman_runs']
.sum()
.sort_values(ascending=False)
.head()
)
```
Output:
batsman
SK Raina    | 4548
V Kohli     | 4423
RG Sharma   | 4207
G Gambhir   | 4132
DA Warner   | 4014



## Which batsman hit the most fours?
Only take that ball on which the four is hit., then create Batsman-wise groups 🚀.How many fours did it take.then sort them from highest to lowest.Next, display the top 5 batsmen.

```python
print(
ipl[ipl['batsman_runs'] == 4]
.groupby('batsman')
.size()
.sort_values(ascending=False)
.head(10)
)
```

STEP-BY-STEP
Step 1. Only take that ball on which the four is hit.
ipl['batsman_runs'] == 4

Step 2.Batsman-wise groups 🚀
.groupby('batsman')

Step 3. How many fours did it take 😄🔥
.size()
means:rows count

Example 🏏
batsman batsman_runs
Virat |4
Virat |4
Rohit |4

Output 🚀
Virat |2
Rohit |1
IMPORTANT🧠

## how many 4-run shots of every batsman. 
```python
new_delivery = delivery[delivery['batsman_runs'] == 4]

print(new_delivery.groupby('batsman')['batsman_runs'].count().sort_values(ascending=False).head(10))
```

## Top 10 fours hitters:
```python
print(delivery.groupby('batsman')['batsman_runs'] ).count().sort_values(ascending=False) .head(10)
```

STEP-BY-STEP 🚀
1️⃣only 4-run balls
new_delivery
👇

2️⃣all batsman's group 😄🏏
.groupby('batsman')

3️⃣Runs column select 🚀
['batsman_runs']

4️⃣How many fours to kill?
.count()

Example 🧠
Virat Group
batsman_runs
4
4
4
count() = 3

5️⃣Highest fours → lowest 😄
.sort_values(ascending=False)

6️⃣Top 10 batsmen 🚀
.head(10)



## 🆚 IMPORTANT DIFFERENCE (MOST IMP) 🔥
.count() vs .size()
Function|What does it count?
.count()| only valid (non-null) values
.size()| total rows (null also included)

## we have to find Against which three teams has Virat Kohli scored the most runs?
```python
print(
delivery[delivery['batsman'] == 'V Kohli']
.groupby('bowling_team')['batsman_runs']
.sum()
.sort_values(ascending=False)
.head(3)
)
```

Explain:
STEP-BY-STEP
1️⃣only Virat Kohli rows 🔥
delivery['batsman'] == 'V Kohli'

2️⃣Opponent team-wise groups 🚀
.groupby('bowling_team')

Example 😄
MI group
CSK group
KKR group

3️⃣against total runs of all team
['batsman_runs']
.sum()

4️⃣Highest runs → lowest 😊
.sort_values(ascending=False)

5️⃣Top 3 teams 🚀
.head(3)


## We create a function where we provide a batsman's name and, in return, receive information about the teams against which that batsman has scored the most runs.
```python
def run_scored(batsman_name):
   vk = delivery[delivery['batsman'] == batsman_name]
   return vk.groupby('bowling_team')['batsman_runs'] .sum() .sort_values(ascending=False) .index
print(run_scored('V Kohli'))
```

STEP-BY-STEP 😄🔥
1️⃣ Function: ➡Dynamic function 🚀Any batsman can use
def run_scored(batsman_name):

2️⃣ Filtering: Only us batsman's rows 🚀
delivery['batsman'] == batsman_name

3️⃣ Groupby : Opponent team-wise groups 😄
.groupby('bowling_team')


4️⃣ Sum :Total runs 🏏
['batsman_runs'].sum()

5️⃣ Sorting 🔥Highest → lowest 🚀
.sort_values(ascending=False)

6️⃣ .index 😄only team names 😊
.index


## 📘 Difference
Function	Meaning
groupby()	|groups create
.get_group() |	specific group fetch
.sum()|	total
.count()	|non-null values count
.size()|	total rows count


## What is isin() ? 🤔
it is a method in pandas that checks if each element in a Series is contained in a specified list of values. It returns a boolean Series where True indicates that the element is in the list and False indicates that it is not.

### Simple Example😄
data.csv
Name| | city
Suraj | Delhi
Aman| mumbai
Riya| Pune

```python
import pandas as pd
df = pd.read_csv('data.csv')
df['City'].isin(['Delhi', 'Pune'])
```
Output 😊
0 - True
1 -False
2 -True

Meaning 🚀
City In List?
Delhi| ✅
Mumbai| ❌
Pune | ✅

## MOST IMPORTANT 🧠🔥
### == ->only ONE value check 😄
company['Sector'] == 'Technology'

### isin() ->MULTIPLE values check 🚀
company['Sector'].isin(['Technology', 'Retail'])

### Fortune100 Example ->Technology + Retail Companies
Meaning 🧠Sir bring rows of Technology and Retail sector
```python
print(company[company['Sector'].isin(['Technology', 'Retail'])])
```

### IPL Example -> Virat + Rohit Rows 😄
Meaning 🚀Just bring the rows where the vlaue is Virat and Rohit
```python
print(delivery[delivery['batsman'].isin(['V Kohli', 'RG Sharma'])])
```

STEP 1 : delivery
Meaning 😄complete IPL dataset

STEP 2 🧠 delivery['batsman']
Meaning: Just find batsman column

Example 😄
batsman
V Kohli
RG Sharma
MS Dhoni

STEP 3 🚀🔥 .isin( ['V Kohli', 'RG Sharma'])
Meaning Check whether the batsman is V Kohli or RG Sharma?

OUTPUT😄🔥
True
False
True
False

## With groupby 😎🔥Virat + Rohit Total Runs
```python
print(delivery[delivery['batsman'].isin(['V Kohli', 'RG Sharma'])].groupby('batsman')['batsman_runs'].sum())
```

Output Example 🏏
V Kohli      7263
RG Sharma    6211

Explain: step 1,2,3 are same as above then 

STEP 4 🧠🚀: -> delivery[delivery['batsman'].isin(['V Kohli', 'RG Sharma']    )]
Meaning 😎🔥: Bring only those rows where the value is Kohli or Rohit Sharma.

Example Output 😄🏏
batsman	batsman_runs
V Kohli-	4
RG Sharma	-6
V Kohli	-1

STEP 5 🧠😎 .groupby('batsman')
Meaning 😄🔥: Create batsman-wise groups

Groups 🚀=> 
V Kohli Group 😎batsman_runs
4
1
RG Sharma Group 😄batsman_runs
6

STEP 6 🧠🔥['batsman_runs']
Meaning 😎: select only  runs column 

STEP 7  .sum()
Meaning: add all batsman total runs.

FINAL OUTPUT:
batsman
V Kohli      5
RG Sharma    6


## NOT isin() ❌
Opposite of isin. Technology aur Retail ko hata do
```python
~company['Sector'].isin(['Technology', 'Retail'])
```
Example 😄🔥
```python
print(company[~company['Sector'].isin(['Technology', 'Retail'])])
```

### Notes
| Code      | Meaning         |
| --------- | --------------- |
| `==`      | single value    |
| `isin()`  | multiple values |
| `~isin()` | opposite filter |

### Question:Find the most destructive death-over batsman in IPL history
Meaning :Death overs means= Over 16 → 20
         Most destructive = highest strike rate

## Strike Rate Formula 🚀
Strike Rate =Balls/Runs ​× 100

Condition😄🔥
Minimum 200 balls played in overs 16-20


```python
death_over = delivery[
    delivery['over'] > 15
]

runs = death_over.groupby('batsman')[
    'batsman_runs'
].sum()

balls = death_over.groupby('batsman')[
    'batsman_runs'
].count()

sr = (runs / balls) * 100

mask = balls >= 200

print(
    sr[mask]
    .sort_values(ascending=False)
    .head(10)
)
```


## STEP-BY-STEP 🧠🏏
1️⃣ Death overs filter
death_over = delivery[
    delivery['over'] > 15]

Meaning : Only overs 16-20

2️⃣ Group by batsman 🚀
death_over.groupby('batsman')
Meaning: group of all batsman 


3️⃣ Calculate Strike Rate 🔥
runs = death_over.groupby('batsman')['batsman_runs'].sum()
balls = death_over.groupby('batsman')['batsman_runs'].count()

Why count()? 🧠
1 row = 1 ball

4️⃣ Strike Rate Formula 🚀
sr = (runs / balls) * 100

5️⃣ Minimum 200 balls 😄🔥
mask = balls >= 200
Meaning: Only those batsmen who played 200+ balls

OUTPUT Meaning : Top death-over hitters with best strike rate (minimum 200 balls)


IMPORTANT CONCEPTS 🧠🔥
Code-	Meaning
over > 15-	death overs
groupby('batsman')-	batsman groups
.sum()-	total runs
.count()	-total balls
(runs/balls)*100	-strike rate
balls >= 200	-minimum balls condition


# IMPORTANT CONCEPTS 🧠🔥

| Code | Meaning |
|---|---|
| over > 15 | death overs |
| groupby('batsman') | batsman groups |
| sum() | total runs |
| count() | total balls |
| (runs/balls)*100 | strike rate |
| balls >= 200 | minimum balls condition |


Example
```python
print(delivery[delivery['batsman'].isin(['V Kohli', 'RG Sharma'])].groupby('batsman')['batsman_runs'].sum())
```


STEP 1 🚀
delivery
Meaning :complete IPL dataset


STEP 2 🧠
delivery['batsman']
Meaning : fetch only batsman column 

Example :
batsman
V Kohli
RG Sharma
MS Dhoni


STEP 3 🚀🔥
.isin(['V Kohli', 'RG Sharma'])
Meaning : Check: Is the batsman Kohli or Rohit Sharma?

OUTPUT 😄🔥
True
False
True
False


STEP 4 🧠🚀
delivery[delivery['batsman'].isin(['V Kohli', 'RG Sharma'])]
Meaning :Retrieve only those rows where the batsman is V Kohli or RG Sharma.

Example Output 😄🏏
batsman	-batsman_runs
V Kohli	-4
RG Sharma	-6
V Kohli	-1


STEP 5 🧠😎
.groupby('batsman')
Meaning : Now creating batsman-wise groups 

STEP 6 🧠🔥
['batsman_runs']
Meaning : only select runs column.

STEP 7 🚀🔥
.sum()
Meaning : add all batsman total runs.

FINAL OUTPUT 🏏🔥
batsman
V Kohli      5
RG Sharma    6

## FLOW UNDERSTANDING 🧠🚀
Dataset
↓
Filter players
↓
Create groups
↓
Select runs column
↓
Add runs


## What is merge()? 🤔
join the 2 DataFrames.

### Real-Life Example 😄🔥
Suppose:
Table 1 → Students
id	 → name
1	→  suraj
2	→  Aman

Table 2 → Marks
id→marks
1→	90
2→ 80

Goal 🧠🔥
Importing Names and Marks into a Table

```python
students = pd.DataFrame({'id': [1, 2],'name': ['Suraj', 'Aman']})
marks = pd.DataFrame({'id': [1, 2],'marks': [90, 80]})
print(pd.merge(students, marks, on='id'))
```

OUTPUT 🚀
id	name	marks
1	Suraj	90
2	Aman	80


## TYPES OF MERGE 😎🔥
Type	Meaning
inner	common rows only
left	left table full
right	right table full
outer	all rows


### INNER MERGE 
Meaning : only matching rows

```python
pd.merge(students,marks,on='id',how='inner')
```

### LEFT MERGE 🧠🔥
Meaning :all rows of Left table 

```python
pd.merge(students,marks,on='id',how='left')
```

### RIGHT MERGE 🚀

```python
pd.merge(students,marks,on='id',how='right')
```

### OUTER MERGE 😄🔥
Meaning: all rows of both tables.

```python
pd.merge(students,marks,on='id',how='outer')
```

📘 Notes 😎🔥
Code	Meaning
merge()	join DataFrames
on=''	common column
how='inner'	matching rows
how='left'	left full
how='right'	right full
how='outer'	all rows


1️⃣ Virat Kohli ne kis city me sabse jyada runs banaye 😎🔥
```python
merge_df = pd.merge(delivery,matches,left_on='match_id', right_on='id')
print(merge_df[ merge_df['batsman'] == 'V Kohli'].groupby('city')['batsman_runs'].sum().sort_values(ascending=False).head())
```
expain: 
### PART 1 😎pd.merge()
pd:here pd is nickname of pandas 
import pandas as pd

merge()
Meaning:add two DataFrames.

### PART 2 🚀delivery
First DataFrame

Example:
match_id  |	batsman	batsman_runs
1  |	V Kohli	4
1  |	V Kohli	1

### PART 3 🔥matches
Second DataFrame

Example:
id |	city
1  |	Hyderabad

### PART 4 🧠left_on='match_id'
Meaning: In Delivery table use match_id column  


### PART 5 🚀 right_on='id'
Meaning:In Matches table use id column 

#### VISUAL UNDERSTANDING 🏏
Delivery:
match_id |batsman
1  |	V Kohli
↓

Matches:
id  |	city
1	|Hyderabad
↓

Merge:
match_id  |	batsman	| city
1	| V Kohli  |	Hyderabad


### PART 6: merge_df
Meaning:New merged dataframe

### PART 7 🚀: merge_df['batsman']
Meaning: fetch only batsman column 
Example:
V Kohli
MS Dhoni
RG Sharma

### PART 8 🔥
merge_df['batsman'] == 'V Kohli'
Meaning:Check batsman is Virat or not?
Output:
True
False
True
False

### PART 9 🧠 : merge_df[merge_df['batsman'] == 'V Kohli']
Meaning: fetch only Virat Kohli's rows 
Example:
batsman	city|	batsman_runs
V Kohli	Delhi|	4
V Kohli	Mumbai|	1

### PART 10 🚀 :  .groupby('city')
Meaning: create group according to city.
Example:
Delhi Group
batsman_runs
4
6

Mumbai Group
batsman_runs
1
2

### PART 11 🔥: ['batsman_runs']
Meaning: only take runs column.

### PART 12 🧠: .sum()
Meaning: add all city runs.
Example:
Delhi -> 4 + 6 = 10
Mumbai -> 1 + 2 = 3

Output:
Delhi     10
Mumbai     3


### PART 13 🚀:  .sort_values(ascending=False)
sort_values()
Meaning: Sorting

ascending=False
Meaning:Big → small

Output:
Delhi     10
Mumbai     3

### PART 14 🔥.head(5)
Meaning: show Top 5 rows 



Example 2️⃣: Kis player ne Hyderabad me sabse jyada runs banaye 😄🔥
```python
print(merge_df[    merge_df['city'] == 'Hyderabad'].groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10))
```

3️⃣ Har season me total matches 😎🚀
```python
print(matches.groupby('season').size())
```


4️⃣ Virat Kohli ka har season total runs 🏏🔥
```python
print(merge_df[    merge_df['batsman'] == 'V Kohli'].groupby('season')['batsman_runs'].sum().sort_values(ascending=False)).drop_duplicate(subset='season',keep='first')
```


Example :
```python
new = delivery.merge(match,left_on='match_id',right_on='id')
new.groupby(['season', 'batsman'])['batsman_runs'] .sum() .sort_values(ascending=False) .reset_index()
```
Explain:
### STEP 1 🚀: delivery.merge()
Meaning: join delivery dataframe with another dataframe.

### STEP 2 😎: match
Second dataframe
Example:
id|	season
1|	2017
2|	2017

### STEP 3 🔥:left_on='match_id'
Meaning: use match_id of delivery dataframe 

### STEP 4 🧠: right_on='id'
Meaning: use id of match dataframe.
RESULT :

before->

delivery
match_id|	batsman|	batsman_runs
1|	V Kohli||	4

match
id|	season
1|	2017

after Merge ->
match_id |	batsman|batsman_runs|	season
1	     | V Kohli |     4      |   2017


### STEP 5 🏏: new.groupby(['season','batsman'])
Meaning: Season + create groups according to Batsman 

Example:
Group 1
2017 + V Kohli
Group 2
2018 + V Kohli
Group 3
2017 + MS Dhoni


### STEP 6 🔥['batsman_runs']
Meaning: take only runs  column

### STEP 7 🚀 .sum()
Meaning:Add total runs of group

Example:
2017 + V Kohli
4
6
2
1
↓
13

Output:
season | batsman  | total run
2017   | V Kohli  |    973
2017   | DA Warner  |  641


### STEP 8 😎 : .sort_values(ascending=False)
Meaning: runs big -> small

Example:
V Kohli      973
DA Warner    641
MS Dhoni     590

### STEP 9 🔥: .reset_index()
Seasons and batsmen become index.

Before:
season | batsman   |  run 
2017   | V Kohli  |    973
2018   | V Kohli |     530

this is MultiIndex .

After:
season  | batsman  | batsman_runs
2017    | V Kohli  |  973
2018    |V Kohli   |   530

### STEP 10 : drop_duplicates(subset='season', keep='first')
thsi is very important part.

Before Data
season|	batsman	|runs
2016|	V Kohli	|973
2016|	AB de Villiers|	687
2016|	DA Warner	|848
2017|	DA Warner	|641
2017	|G Gambhir	|498

subset='season'
Meaning: check Season column

keep='first'
Meaning:Keep the first row you received.

Since data is already sorted according highest runs then 
2016 first row: V Kohli 973

The first row stays ✅. Remove the remaining rows from 2016 ❌.

2017 : DA Warner 641 ✅

FINAL OUTPUT 😎🏏
season	|batsman	|runs
2016	|V Kohli	|973
2017	|DA Warner	|641
2018	|KS Williamson	|735
2019	|DA Warner	|692

and: groupby(['season','batsman'])  =  Multi-Level Grouping 

## now we have new dataframe name is food.csv

### What is the average amount spent on each food item in every city?
```python
print(food.pivot_table(index='City',columns='Item',values='Spends',aggfunc='mean'))
```

Word-by-Word 🧠

index='City'
👉 Each city will form a row

columns='Item'
👉 Each food item will form a column

values='Spends'
👉 calculate the spends

aggfunc='mean'
👉 find the average spend

Example Data 😄
Name	|City	  |Item	    |Spends
Anu	    |Kolkata  |Burger	|11
Riya	|Delhi	  |Pizza	|25
Amit	|Kolkata  |Pizza	|20

Output 🚀
City	|Burger |Pizza
Delhi	|NaN	|25
Kolkata	|11	    |20

Meaning 😎
Average spend on Burger in Kolkata = 11
Average spend on Pizza in Kolkata = 20
Average spend on Pizza in Delhi = 25


Notes 📝
Parameter|	Meaning
index	|Rows
columns	|Columns
values	|Column on which calculation is to be performed
aggfunc	|Type of calculation to be performed


Example 
```python
print(food.pivot_table(index=['City'],columns=['Item'],values='Spends',aggfunc='mean'))
```

Word-by-Word 🧠🔥

### index='City'
👉 Each city will form a row

###  columns='Item'
👉 Every food item will create a column.

### values='Spends'
👉 Expenses have to be calculated

### aggfunc='mean'
👉 Average spend is calculated

### Example Data 😄
Name	City	Item	Spends
Anu	Kolkata	Burger	11
Riya	Delhi	Pizza	25
Amit	Kolkata	Pizza	20

Output 🚀
City	Burger	Pizza
Delhi	NaN	25
Kolkata	11	20

###  Meaning 😎
Average spend of Burger in Kolkata = 11
Average spend of Pizza in Kolkata = 20
Average spend of Pizza in Delhi = 25

Notes 📝
Parameter	Meaning
index	Rows
columns	Columns
values	​​On which column is the calculation done?
aggfunc Which calculation is being performed?


```python
print(food.pivot_table(index=['City', 'Gender'],columns=['Item', 'Frequency'],values='Spends',aggfunc='mean'))
```

Word-by-Word

index=['City', 'Gender']
👉 creating Rows-
Delhi    F
Delhi    M
Kolkata  F
Kolkata  M


columns=['Item', 'Frequency']
👉 Create Columns :
Burger Weekly
Burger Monthly
Pizza Weekly
Pizza Monthly


values='Spends'
👉calculation on Spends column.

aggfunc='mean'
👉 find Average spend.

Example Output 🚀
City	|Gender	|Burger |weekly 	|Pizza Monthly
Delhi	|F	           |15	      | 25
Kolkata	|M	          | 11       |	20

Pivot Table Formula 🏆
```python
df.pivot_table(index=[row_groups],columns=[column_groups],values='numeric_column',aggfunc='mean')
```

😎 Remember the Rule:
index   → rows
columns → columns
values  → On which the calculation is to be performed
aggfunc → Which calculation?


```python
import pandas as pd
delivery=pd.read_csv('delivery.csv')
mask = delivery['batsman_runs'] == 6
six = delivery[mask]
pt = six.pivot_table(index='over',columns='batting_team',values='batsman_runs',aggfunc='count')
import seaborn as sns
sns.heatmap(pt)
```
Meaning: How many successful hits did each team achieve in each over?

Word-by-Word 🧠🔥
### Step 1: mask = delivery['batsman_runs'] == 6
Meaning: Find only six balls

### Step 2: six = delivery[mask]
Meaning: Get the 'six' row out.

### Step 3: pivot_table()
Meaning:create Summary table

### Step 4: index='over'
Meaning: Rows = Over Number


### Step 5:columns='batting_team'
 Meaning:Columns = Teams

### Step 6: values='batsman_runs'
Meaning:Calculations based on 'sixer' lines


### Step 7: aggfunc='count'
Meaning: How many sixes were hit?

Output Table Example 😎
over	CSK	MI	RCB
1	0	1	0
2	2	0	1
20	15	12	18


### Heatmap 🔥
sns.heatmap(pt)

Dark color = more sixes 🏏💥
Light color = less sixes

Example :
```python 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

delivery=pd.read_csv('delivery.csv')
mask = delivery['batsman_runs'] == 6
six = delivery[mask]

pt = six.pivot_table(index='over',columns='batting_team',values='batsman_runs'aggfunc='count')
sns.heatmap(pt, annot=True)
plt.show()
```
Using `(annot=True)`, the count of sixes will also be visible inside each cell.



## match.corr()
It means: Calculating the correlation between numerical columns.

What is correlation? 🤔
It indicates how closely two columns are related to each other.

The value always ranges from -1 to +1.

Example 😎
Value	Meaning
+1	Perfect Positive Relation
0	No Relation
-1	Perfect Negative Relation

Example 🚀
Hours Studied	Marks
1	20
2	40
3	60

Output: 1.0
Meaning: The more you study, the higher the marks.


### Example
```python
import pandas as pd
match=pd.read_csv('match.csv')
print(match.corr(numeric_only=True))
```
Output
index                  id    season  dl_applied  win_by_runs  win_by_wickets  umpire3
id             | 1.000000 | 0.471087  |  0.024281  |  -0.010263   |    -0.015510   |   NaN
season         |0.471087  |1.000000   | 0.004170   | -0.016815    |   -0.000708    |  NaN
dl_applied     | 0.024281 | 0.004170  |  1.000000  |  -0.010893   |    -0.011640   |   NaN
win_by_runs    |-0.010263 |-0.016815  | -0.010893  |   1.000000   |    -0.565181   |   NaN
win_by_wickets |-0.015510 |-0.000708  | -0.011640  |  -0.565181   |     1.000000   |   NaN
umpire3        |     NaN  |    NaN    |     NaN    |      NaN     |        NaN     | NaN

Word-by-Word 🧠🔥

match
↓
Match dataframe

.corr()
↓
Correlation matrix


## Heatmap:
```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.heatmap(match.corr(numeric_only=True),annot=True)
plt.show()
```

Word-by-Word 🧠🔥
### Step 1: match.corr(numeric_only=True)
Meaning: find only numerical columns correlation.

Example:
id
season
dl_applied
win_by_runs
win_by_wickets

### Step 2 : sns.heatmap(...)
Meaning: Display the correlation matrix in color format.

### Step 3 : annot=True
Meaning:Show the numbers inside the cells as well.


Example Output 😎
index	        |season	| win_by_runs	|win_by_wickets
season	        |1.00	|0.01	        |-0.02
win_by_runs	    |0.01	|1.00	        |-0.45
win_by_wickets	|-0.02	|-0.45	        |1.00

In Heatmap:
🟢 Dark = strong relation
⚪ Light = weak relation
🔴 Negative = opposite relation

Remember this:
df.corr() :👉 Correlation matrix banata hai.
sns.heatmap(df.corr(), annot=True) :👉 Correlation ko visualize karta hai.

## rename(): for coloumns name change
```python
import pandas as pd
match=pd.read_csv('match.csv')
print(match.head())
match.rename(columns={'city': 'place','date': 'dom'}) #coulmn name doesnot change permanantlly
print(match.columns)
```
### Permanent Change 🚀: If you want to rename permanently in the DataFrame use inplace=True

```python
print(match.head())
match.rename(columns={'city': 'place','date': 'dom'},inplace=True)
print(match.head())
print(match.columns)
```
Output 😊

Old:
city      | date
Hyderabad | 2017-04-05

New:
place     | dom
Hyderabad | 2017-04-05

Code     	|Meaning
rename()	|Rename column/index
columns={}	|Column rename
inplace=True|	Permanent change
inplace=False|	New dataframe return (default)


## data.set_index()
```python
data.set_index('id')
```

data.head(2): Show the first 2 rows.
data.set_index('ID'): Set the 'ID' column as the index.
This does not make a permanent change; it only returns a temporary result.


Permanent Change 😎
```python
data.set_index('id',inplace=True)
print(data.index)
```

Example 😎

Before:
Index|id  |Name
0	 |101 |Suraj
1	 |102 |Aman

After:
id	|Name
101	|Suraj
102	|Aman

## data.reset_index()
Convert the index back into a regular column.


Example 🧠
```python
data.set_index('id', inplace=True)
```
To dataframe convert: 
id	|Name
101 |suraj
102 |Aman

here id is index.

Now:
```python
data.reset_index()
```

Output:
index	|id     |Name
0   	| 101	|Suraj
1	    |102	|Aman


It does not make a permanent change so use inplace=True:
```python
data.reset_index()
Permanent Change 😎
data.reset_index(inplace=True)
```

Extra Useful 🔥

If you do not want the old index column:
```python
data.reset_index(drop=True)
```
Example

Before:
id	|Name
101	|Suraj
102	|Aman

```python
data.reset_index(drop=True)
```

After:
Name
Suraj
Aman

And new default index is
0
1



## Notes 📝
Code	        |Meaning
head(2)     	|First 2 rows
set_index('id')	|Column → Index
inplace=True	|Permanent change
reset_index()	|Index → Column
drop=True	    |Do not keep the old index.


Example 
```python
data['winner'].value_counts().reset_index()
```

STEP 1 🚀
data['winner']

Meaning:

Sirf winner column nikalo

Example:

winner
MI
CSK
MI
RCB
STEP 2 😎
.value_counts()

Meaning:

Har winner kitni baar aaya?

Output:

winner
MI     2
CSK    1
RCB    1
Name: count

Ye ab Series hai, DataFrame nahi.

STEP 3 🔥
.reset_index()

Meaning:

Series ko DataFrame mein convert karo
aur normal index banao

Output:

winner	count
MI	2
CSK	1
RCB	1

Before:

type(data['winner'].value_counts())

Output:

pandas.core.series.Series

After:

type(
    data['winner']
    .value_counts()
    .reset_index()
)

Output:

pandas.core.frame.DataFrame


Notes 📝
Function	Meaning
value_counts()	Frequency count
reset_index()	Series → DataFrame
sort_values()	Sort
head()	Top rows


## data.dropna()
Meaning :Remove the rows that contain any missing values ​​(NaN).

```python
data = pd.read_csv('train.csv')
data.head()
data.shape
data.dropna()
data.shape
```

## Example dataset
```python
import pandas as pd
import numpy as np

data = pd.DataFrame({
    'Name': ['Aman', 'Rahul', np.nan, 'Sita'],
    'Age': [21, np.nan, 25, 22],
    'City': ['Delhi', 'Mumbai', 'Pune', np.nan]
})
data.dropna()
print(data)
```
before 
Index    Name   Age    City
0       Aman   21.0    Delhi
1       Rahul   NaN    Mumbai
2       NaN     25.0    Pune
3       Sita    22.0     NaN

After data.dropna()

   Name   Age   City
0  Aman  21.0  Delhi


👉 Explanation:

Row 1 → Age missing ❌ removed
Row 2 → Name missing ❌ removed
Row 3 → City missing ❌ removed

👉 Only row left which does not have any NaN


##  axis parameter (VERY IMPORTANT)
### 🔹 Rows remove (default)
```python
data.dropna(axis=0)
```
👉 same as default: rows delete

### 🔹 Columns remove
```python
data.dropna(axis=1)
```
Result:Empty DataFrame (only columns with NaN values)
👉 Since all columns have NaN values, they can all be removed.

### 🎯 how = 'all'
```python
data.dropna(how='all')
```

👉 means: delete only those row where all values are NaN

#### Example:
```python
df = pd.DataFrame({'A': [np.nan, 1],   'B': [np.nan, 2] })
df.dropna(how='all')
```

Result:
     A    B
1  1.0  2.0
👉 The first row was removed because it was completely empty.



### 🎯  how = 'any' (default behavior)
```python
data.dropna(how='any')
```
👉 Meaning: If even a single NaN is found → delete the row .(This is the default behavior)



Example : 
```python
data.dropna(axis=1, how='all')
```

Meaning 🧠
axis=1 👉 Operate on columns

how='all' 👉 Delete only the column where all values ​​are NaN.

Example 🚀
Data:
Name	Age	Cabin
Suraj	20	NaN
Aman	22	NaN
Riya	25	NaN

Run: data.dropna(axis=1, how='all')

Output:
Name	Age
Suraj	20
Aman	22
Riya	25
The 'Cabin' column was deleted because all its values ​​were NaN.


#### Compare 🏆
1️⃣ data.dropna(axis=1, how='any')
Meaning: Delete the column if even a single NaN exists in it.

2️⃣ data.dropna(axis=1, how='all')
Meaning: Delete the column only if the entire column consists of NaNs.



### 🎯 subset parameter (VERY USEFUL)
```python
data.dropna(subset=['Age'])
```
👉Meaning: Delete the row only if the "Age" column is NaN.

Result:
    Name   Age    City
0   Aman  21.0   Delhi
2    NaN  25.0    Pune
3   Sita  22.0     NaN
👉 Row 1 remove (Age is NaN)



### Difference 🏆
1️⃣ data.dropna()
👉 Deletes the row if there is an NaN in any column

2️⃣ data.dropna(subset=['Cabin'])
👉 Checks only the 'Cabin' column

3️⃣ Multiple columns
data.dropna(subset=['Age', 'Cabin'])
👉 Checks both 'Age' and 'Cabin'



## Example 😎

Before:
Name	Cabin	Embarked
Suraj	|C85	     |S
Aman	|NaN	     |C
Riya	|B20	     |Nan
Tina	|A10	     |Q

Run:
```python
data.dropna(subset=['Cabin', 'Embarked'])
```
Output:
Name	Cabin	Embarked
Suraj	|C85	   |S
Tina	|A10	   |Q

Why? 🤔
Aman ❌Cabin = NaN
Riya ❌Embarked = NaN


### 🧠  Real-world meaning
Think dataset = students record 👇
Name	|Marks	|City
A	    |90 	|Delhi
B	    |NaN	|Mumbai

👉 dropna() = incomplete student records remove ❌

##  Important mistake (common bug)
data.dropna() 👉 this is not change original data 

✔ correct way: data.dropna(inplace=True)
👉 now data is permanently change.

🏁Summary
Function|     Meaning
dropna()|     NaN rows remove
axis=1|       remove columns( work on Columns )
how='all'|    completely empty row only
subset=[]|    specific column check
inplace=True| original data change
axis=0  |     Rows


## data.fillna(0)
meaning is:Wherever there is a NaN (missing value), fill it with 0.

Example 🧠

Before:
Name	Age	Marks
Suraj	20	90
Aman	NaN	85
Riya	22	NaN

Run:
```python
data.fillna(0)
```

Output:
Name	Age	Marks
Suraj	20	90
Aman	0	85
Riya	22	0

Word-by-Word 🚀
fillna()👉 Fill NaN values
0👉 Replace missing values ​​with 0

IMPORTANT 🏆
data.fillna(0) --> This does not make a permanent change.
It only returns a new DataFrame.

Permanent Change 😎
data.fillna(0, inplace=True)

Example: 
```python
data['Age'].fillna( data['Age'].mean(),inplace=True)
```
Meaning:  Replace missing ages with average age

Example :
```python
print(data.columns)
data['Cabin'].fillna("not specified")
```
Meaning 🧠
data['Cabin']
👉 By selecting the Cabin column

.fillna('Not Specified')
👉 Where the vehicle is NaN, enter "Not Specified"

Example 🚀

Before:
Cabin
C85
NaN
B20
NaN

Run : data['Cabin'].fillna('Not Specified')

After:
Cabin
C85
Not Specified
B20
Not Specified

### IMPORTANT 🏆
data['Cabin'].fillna('Not Specified')
👉 it is not change original dataframe.only give result.

Permanent Change 😎
### Method 1:  data['Cabin'] = data['Cabin'].fillna('Not Specified')
### Method 2:   data['Cabin'].fillna('Not Specified',inplace=True)


Example : 
```python
data['Cabin'].fillna("Not Specified", inplace=True)
```
Word-by-Word 🧠
data['Cabin']             |👉 Cabin column select
.fillna("Not Specified")  |👉 Fill "Not Specified" wherever there is NaN.
inplace=True              |👉Make a permanent change to the original data frame.

Example 🚀
Before:
Cabin
C85
NaN
B20
NaN

Run:data['Cabin'].fillna("Not Specified", inplace=True)

After:
Cabin
C85
Not Specified
B20
Not Specified

Verify 😎

Before: print(data['Cabin'].isnull().sum())
Output:687

After:data['Cabin'].fillna("Not Specified", inplace=True)
print(data['Cabin'].isnull().sum())

Output: 0



## Check Missing Values

Before: data['Cabin'].isnull().sum()

Example: 687

After filling: 
data['Cabin'] = data['Cabin'].fillna('Not Specified')
data['Cabin'].isnull().sum()

Output: 0
This means there are no missing values ​​left in the 'Cabin' column.


### 👉 Backward Fill : bfill()
👉 Copy the value below the missing value.

```python
data['Cabin'].fillna(method='bfill')
#or 
data['Cabin'].bfill()
```

Example 🚀

Before:
Cabin
C85
NaN
B20
NaN
D10

Run:data['Cabin'].fillna(method='bfill')

After:
Cabin
C85
B20
B20
D10
D10



### 👉 Forward Fill :ffill()
👉 Copy the value above the missing value.
data['Cabin'].fillna(method='ffill')

Before:
Cabin
C85
NaN
B20

After:
Cabin
C85
C85
B20


## Permanent Change 🔥
```python
data['Cabin'].fillna(method='bfill',inplace=True)
```



## Notes 📝
Code	                  |Meaning
fillna(0)	              |NaN → 0
fillna('Unknown')	      |NaN → Unknown
fillna(mean)	          |NaN → Average
fillna(mode)	          |NaN → Most common value
inplace=True	          |Permanent change
fillna('Not Specified')	  |NaN → Not Specified
isnull().sum()	          |Missing values count
method='ffill'	          |use Previous value 
method='bfill'	          |use Next value 