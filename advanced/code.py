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