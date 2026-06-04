import pandas as pd

# CSV file read
company = pd.read_csv('Fortune100.csv')

# Grouping by Sector
sector = company.groupby('Sector')

# Type of company
print(type(company))

# Total rows
print(len(company))

# Companies count in each sector
print(sector.size())

# GroupBy object
print(company.groupby('Sector'))

# Sort sector counts descending
print(sector.size().sort_values(ascending=False))

# First company from each sector
print(sector.first())

# Last company from each sector
print(sector.last())


# ==============================
# LOAD IPL DATASET 🏏🔥
# ==============================

delivery = pd.read_csv('deliveries.csv')

print(delivery.head())


# ==============================
# TOTAL RUNS OF EVERY BATSMAN 😎
# ==============================

print(
    delivery.groupby('batsman')[
        'batsman_runs'
    ]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)


# ==============================
# MOST FOURS 🚀
# ==============================

print(
    delivery[
        delivery['batsman_runs'] == 4
    ]
    .groupby('batsman')
    .size()
    .sort_values(ascending=False)
    .head(10)
)


# ==============================
# MOST SIXES 😄🔥
# ==============================

print(
    delivery[
        delivery['batsman_runs'] == 6
    ]
    .groupby('batsman')
    .size()
    .sort_values(ascending=False)
    .head(10)
)


# ==============================
# VIRAT KOHLI TOTAL RUNS 😎
# ==============================

print(
    delivery[
        delivery['batsman'] == 'V Kohli'
    ]['batsman_runs']
    .sum()
)


# ==============================
# MS DHONI TOTAL SIXES 🚀
# ==============================

print(
    delivery[
        (delivery['batsman'] == 'MS Dhoni') &
        (delivery['batsman_runs'] == 6)
    ]
    .shape[0]
)


# ==============================
# CREATE BATSMAN GROUPS 😄🔥
# ==============================

runs = delivery.groupby('batsman')


# ==============================
# GET SPECIFIC GROUP 😎
# ==============================

print(
    runs.get_group('V Kohli')
)


# ==============================
# SHAPE OF GROUP 🚀
# ==============================

print(
    runs.get_group('V Kohli').shape
)


# ==============================
# TOTAL RUNS OF EVERY BATSMAN 😄🔥
# ==============================

print(
    runs['batsman_runs']
    .sum()
)


# ==============================
# TOP 5 RUN SCORERS 😎
# ==============================

print(
    runs['batsman_runs']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)


# ==============================
# FOURS OF EVERY BATSMAN 🚀
# ==============================

new_delivery = delivery[
    delivery['batsman_runs'] == 4
]

print(
    new_delivery.groupby('batsman')[
        'batsman_runs'
    ]
    .count()
    .sort_values(ascending=False)
    .head(10)
)


# ==============================
# VIRAT VS TEAMS 😄🔥
# ==============================

print(
    delivery[
        delivery['batsman'] == 'V Kohli'
    ]
    .groupby('bowling_team')[
        'batsman_runs'
    ]
    .sum()
    .sort_values(ascending=False)
    .head(3)
)


# ==============================
# FUNCTION 🚀
# ==============================

def run_scored(batsman_name):

    vk = delivery[
        delivery['batsman'] == batsman_name
    ]

    return vk.groupby('bowling_team')[
        'batsman_runs'
    ].sum().sort_values(
        ascending=False
    ).index


print(
    run_scored('V Kohli')
)

# ==============================
# isin()
# ==============================


import pandas as pd
df = pd.read_csv('data.csv')
df['City'].isin(['Delhi', 'Pune'])


# == ->only ONE value check 😄
company['Sector'] == 'Technology'

# isin() ->MULTIPLE values check 🚀
company['Sector'].isin(['Technology', 'Retail'])

#Fortune100 Example ->Technology + Retail Companies
print(company[company['Sector'].isin(['Technology', 'Retail'])])

#IPL Example -> Virat + Rohit Rows 😄
print(delivery[delivery['batsman'].isin(['V Kohli', 'RG Sharma'])])


## With groupby 😎🔥Virat + Rohit Total Runs
print(delivery[delivery['batsman'].isin(['V Kohli', 'RG Sharma'])].groupby('batsman')['batsman_runs'].sum())


## NOT isin() 
print(company[~company['Sector'].isin(['Technology', 'Retail'])])

### Question:Find the most destructive death-over batsman in IPL history 
death_over = delivery[delivery['over'] > 15]
runs = death_over.groupby('batsman')['batsman_runs'].sum()
balls = death_over.groupby('batsman')['batsman_runs'].count()
sr = (runs / balls) * 100
mask = balls >= 200
print( sr[mask].sort_values(ascending=False).head(10))

## Example
print(delivery[delivery['batsman'].isin(['V Kohli', 'RG Sharma'])].groupby('batsman')['batsman_runs'].sum())

## merge()
students = pd.DataFrame({'id': [1, 2],'name': ['Suraj', 'Aman']})
marks = pd.DataFrame({'id': [1, 2],'marks': [90, 80]})
print(pd.merge(students, marks, on='id'))


### INNER MERG
pd.merge(students,marks,on='id',how='inner')

### LEFT MERGE 
pd.merge(students,marks,on='id',how='left')

### RIGHT MERGE 
pd.merge(students,marks,on='id',how='right')

### OUTER MERGE 
pd.merge(students,marks,on='id',how='outer')


## Virat Kohli ne kis city me sabse jyada runs banaye 😎🔥
delivery = pd.read_csv('delivery.csv')
matches = pd.read_csv('match.csv')
merge_df = pd.merge(delivery, matches, left_on='match_id', right_on='id')
print(merge_df[ merge_df['batsman'] == 'V Kohli'].groupby('city')['batsman_runs'].sum().sort_values(ascending=False).head())


#Example 2️⃣: Kis player ne Hyderabad me sabse jyada runs banaye 😄🔥
print(merge_df[    merge_df['city'] == 'Hyderabad'].groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10))


#3️⃣ Har season me total matches 😎🚀
print(matches.groupby('season').size())


#4️⃣ Virat Kohli ka har season total runs 🏏🔥
print(merge_df[merge_df['batsman'] == 'V Kohli'].groupby('season')['batsman_runs'].sum().sort_values(ascending=False)).drop_duplicate(subset='season',keep='first')



# Example :
new = delivery.merge(matches,left_on='match_id',right_on='id')
new.groupby(['season', 'batsman'])['batsman_runs'] .sum() .sort_values(ascending=False) .reset_index()


