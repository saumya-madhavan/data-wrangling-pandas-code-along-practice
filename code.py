# --------------
import pandas as pd 
import numpy as np

# Read the data using pandas module.
df=pd.read_csv(path)
## df.shape
##  df.head(3)
# Find the list of unique cities where matches were played
#print("Unique cities = ",np.unique(df['city']))
print("Unique cities = ",df['city'].unique())
# Find the columns which contains null values if any ?
print("Columns with Null values = ",df.columns[df.isna().any()].tolist())
# List down top 5 most played venues
len(np.unique(df['match_code']))
df.dtypes
t1=df[['match_code','venue']].drop_duplicates()
print("1", t1.venue.value_counts(ascending=False).head())
print("2", df.groupby(['venue'])['match_code'].nunique().sort_values(ascending=False).head())
# Make a runs count frequency table
print("Runs - Frequency table",df.runs.value_counts())
# How many seasons were played and in which year they were played 
df['year']=df.date.apply(lambda x:x[:4])
print("No. of Seasons", df.year.unique().shape[0])
print("Year of Seasons", df.year.unique())
df.date=pd.to_datetime(df.date,format='%Y-%m-%d')
df.date.head()
# No. of matches played per season
t2=df[['year','match_code']].drop_duplicates()
print("No. of matches each season", t2.year.value_counts(ascending=False).head())
# Total runs across the seasons
print("Total no. of runs each season", df.groupby(['year'])['total'].sum())
# Teams who have scored more than 200+ runs. Show the top 10 results
t3=df.groupby(['match_code','batting_team'])['total'].sum().reset_index()
t4=t3.sort_values(by='total',ascending=False).reset_index(drop=True)
print("Top 10 teams scored more than 200+ runs", t4.loc[t4.total>200,:].head(10))
# What are the chances of chasing 200+ target
##t5=df.loc[(df.inning==2) & (df.winner==df.batting_team),:].reset_index(drop=True)
##t5.groupby(['match_code','batting_team'])['total'].sum().reset_index()
##print("Chasing 200+ target").sort_values(ascending=False)

g1=df.groupby(['match_code','batting_team','inning'])['total'].sum().reset_index()
g2=g1.loc[((g1.total>200) & (g1.inning==2)),:].reset_index(drop=True)
print("Chasing 200+ target",g2.shape[0])

# Which team has the highest win count in their respective seasons ?
s1=df.groupby(['year','winner'])['match_code'].nunique()
s2=s1.groupby(level=0,group_keys=False)
print("Highest win in each season",s2.apply(lambda x:x.sort_values(ascending=False).head(1)))







