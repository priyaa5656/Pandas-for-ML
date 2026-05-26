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