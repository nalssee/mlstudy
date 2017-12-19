#%%

# Manually downloaded the file 'housing.csv'
from sqlplus import *
import matplotlib.pyplot as plt

#%%


with dbopen('db') as c:
    c.write('housing.csv')

#%%

with dbopen('db') as c:
    housing = c.rows('housing').df()
    housing.hist(bins=50, figsize=(8, 5))
    plt.show()
#%%
