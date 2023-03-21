import sqlite3
import pandas as pd
import numpy as np

s1 = pd.Series([3,2,0,1])
s2 = pd.Series([0,3,7,2])

data = dict(apples = s1, oranges = s2)

df = pd.DataFrame(data)

print(df)

