import sqlite3
import pandas as pd
import numpy as np




list = [["Güleycan",50],["Seymus",60],["Yagmmur",70],["Kartal",100]]
dict = {"İsim":["Güleycan","Seymus","Yağmur","Kartal"],"Notu": [50,60,70,100]}
dict_list = [
    {"isim":"Güleycan","Notu":50},
    {"isim":"Seymus","Notu":60},
    {"isim":"Yağmur","Notu":70},
    {"isim":"Kartal","Notu":100}
            ]

#df = pd.DataFrame([1,2,3,4])
#df = pd.DataFrame(list,columns=["İsim","Notu"],index=[1,2,3,4])
#df = pd.DataFrame(list,[1,2,3,4],["İsim","Notu"])
#df = pd.DataFrame(dict,index= ["212","222","257","300"])
df = pd.DataFrame(dict_list,index= ["212","222","257","300"])


print(df)

