import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user', sep='|', index_col='user_id')

# Step 4. See the first 25 entries
df.head(25)
 
# Step 5. See the last 10 entries
df.tail(10)
 
# Step 6. What is the number of observations in the dataset?
df.shape[0]

#  Step 7. What is the number of columns in the dataset?
df.shape[1]

# Step 8. Print the name of all the columns.
df.columns

# Step 9. How is the dataset indexed?
df.index
 
# Step 10. What is the data type of each column?
df.dtypes

# Step 11. Print only the occupation column
df.occupation
df['occupation'] 

# Step 12. How many different occupations are in this dataset?
df.occupation.nunique()

# Step 13. What is the most frequent occupation?
df.occupation.value_counts().head(1).index[0]
 
# Step 14. Summarize the DataFrame.
df.describe()
 
# Step 15. Summarize all the columns
df.describe(include="all")
 
# Step 16. Summarize only the occupation column
df.occupation.describe

# Step 17. What is the mean age of users?
df.age.mean()
round(df.age.mean())
 
# Step 18. What is the age with least occurrence?
df.age.value_counts().tail()