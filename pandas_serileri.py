import sqlite3
import pandas as pd
import numpy as np

#Data
numbers = [20,30,40,50]

letters = ['a','b','c',20]
scalar = 5
dict = {'a':10,'b':20,'c':30,'d':40}
random_numbers = np.random.randint(10,100,6)

#pandas_series = pd.Series()
#pandas_series = pd.Series(numbers)
#pandas_series = pd.Series(letters)
#pandas_series = pd.Series(5,[0,1,2,3])
#pandas_series = pd.Series(numbers,['a','b','c','d'])
#pandas_series = pd.Series(dict)
#pandas_series = pd.Series(random_numbers)

pandas_series = pd.Series([20,30,40,50],['a','b','c','d'])

#result = pandas_series[0]
#result = pandas_series[-1]
#result = pandas_series[:2]
#result = pandas_series['a']
#result = pandas_series[['a','c']]
#result = pandas_series[['a', 'c', 'e']] bende hata verdi

result = pandas_series.ndim
result = pandas_series.dtype
result = pandas_series.shape
result = pandas_series.sum()
result = pandas_series.max()
result = pandas_series.min()
result = pandas_series + pandas_series
result = pandas_series + 50
result = np.sqrt(pandas_series)
result = pandas_series >= 50
result = pandas_series %2 == 0

print(pandas_series[pandas_series %2 == 0])
print(pandas_series)
print(result)
mercedes2022 = pd.Series([20,30,40,10],["EQS","GLC","CLA","AMG"])
mercedes2023 = pd.Series([40,30,20,10],["EQS","GLC","ALC","AMG"])

total = mercedes2022+mercedes2023
print(total["EQS"])