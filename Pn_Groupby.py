import pandas as pd
import numpy as np

personeller = [
    {"Çalışan":"Ahmet Yılmaz","Departman":"İnsan Kaynakları","Yaş":30,"Semt":"Kadıköy","Maaş":5000},
    {"Çalışan":"Can Ertürk","Departman":"Bilgi İşlem","Yaş":25,"Semt":"Tuzla","Maaş":3000},
    {"Çalışan":"Hasan Korkmaz","Departman":"Muhasebe","Yaş":45,"Semt":"Maltepe","Maaş":4000},
    {"Çalışan":"Cenk Saymaz","Departman":"İnsan Kaynakları","Yaş":50,"Semt":"Tuzla","Maaş":3500},
    {"Çalışan":"Ali Turan","Departman":"Bilgi İşlem","Yaş":23,"Semt":"Kadıköy","Maaş":2750},
    {"Çalışan":"Rıza Ertürk","Departman":"Muhasebe","Yaş":34,"Semt":"Tuzla","Maaş":6500},
    {"Çalışan":"Mustafa Can","Departman":"İnsan Kaynakları","Yaş":42,"Semt":"Maltepe","Maaş":4500}

            ]
df = pd.DataFrame(personeller)

#result = df["Maaş"].sum()
result = df.groupby("Departman").groups
result = df.groupby(["Departman","Semt"]).groups



#for name, group in df.groupby("Semt"):
#    print(name)
#    print(group)
"""for name, group in df.groupby("Departman"):
    print(name)
    print(group)"""
"""result = df.groupby("Semt").get_group("Kadıköy")
result = df.groupby("Departman").get_group("Muhasebe")
result = df.groupby("Departman").sum()
result = df.groupby("Departman").mean()
result = df.groupby("Departman")["Maaş"].mean()
"""


result = df.groupby("Semt")["Maaş"].mean()
result = df.groupby("Semt")["Çalışan"].count()
result = df.groupby("Departman")["Yaş"].max()
result = df.groupby("Departman")["Maaş"].min()
result = df.groupby("Departman")["Maaş"].max()
result = df.groupby("Departman")["Maaş"].max()["Muhasebe"]
result = df.groupby("Departman").agg(np.mean)
result = df.groupby("Departman")["Maaş"].agg([np.sum,np.mean,np.max,np.min])
result = df.groupby("Departman")["Maaş"].agg([np.sum,np.mean,np.max,np.min]).loc["Muhasebe"]


print(result)




