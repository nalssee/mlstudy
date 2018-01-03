#%%
from sqlplus import *
import sqlplus
sqlplus.core.WORKSPACE = 'Titanic'

with dbopen('db') as c:
    c.load("train.csv")
    c.load("test.csv")
#%%

