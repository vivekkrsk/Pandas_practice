import pandas as pd
import numpy as np

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
df = pd.read_csv(url, sep='\t')

df.head()

df.head(20)

df.shape[0]
df.info()

df.shape[1]
df.columns

df.index

c=df.groupby('item_name')
c=c.sum()
c=c.sort_values(['quantity'], ascending=False)
c.head(1)
c.head()

c=df.groupby('choice_description').sum()
c=c.sort_values(['quantity'], ascending=False)
c.head(1)
c.head()

df.item_price.dtype
# change item price type

dollarizer=lambda x:float(x[1:-1])
df.item_price=df.item_price.apply(dollarizer)

df.item_price.dtype

# Revenue

revenue=(df['quantity']*df['item_price']).sum()
print(f'Revenue was: ${str(np.round(revenue,2))}')

orders=df.order_id.value_counts().count()
orders

# average revenue per order
df['revenue']=df['quantity']*df['item_price']
order_grouped=df.groupby(by=['order_id']).sum()
order_grouped.mean()['revenue']

# OR

df.groupby(by=['order_id']).sum().mean()['revenue']

# Number of different item sold
df.item_name.value_counts().count()