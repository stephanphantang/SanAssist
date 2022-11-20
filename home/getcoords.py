import pandas as pd 
from .LatLonFinder import coorfinder



df = pd.read_csv("/Users/alchambron/Documents/Coding_Project/hackatton/sanassist/sanassist/home/air_quality_df.csv")

df = df.replace("ABYMES RN1","ABYMES")
df = df.replace("A7 Salaise Ouest","Salaise Sur Sanne")
df = df.replace("AIX CENTRE ECOLE ART","AIX CENTRE")
df = df.replace("AJACCIO CANETTO","Ajaccio")
df = df.replace("AJACCIO PIATANICCIA","Effrico")
df = df.replace("Alençon Météo-France","Alençon")
df = df.replace("BESSIERES ECONOTRE","BESSIERES")
df = df.replace("Agathois-piscénois","Pezenas")
df = df.replace("Biterrois-Narbonnais","Narbonne")
df = df.replace("Bld peripherique Est","Boulogne-Bilancourt")
df = df.replace("C.C.3 Frontières","Bouzonville")
df = df.replace("CHAPITRE SETMI","Toulouse")
df = df.replace("CIM BOUTEILLERIE","Nantes")
import numpy as np
df1, df2, df3 = np.array_split(df, 3)



LatCity=[]
LonCity = []
for i in df1["nom site"]:
    a = 0
    try:
        coor = coorfinder(str(i))

    except IndexError or ConnectionError:
        df1.drop(df1[df1['nom site'] == i].index, inplace = True)
        a = 1
    if a == 0:
        LatCity.append(coor[0])
        LonCity.append(coor[1])
df1["Lat"]=LatCity
df1["Lon"]=LonCity




LatCity=[]
LonCity = []
for i in df2["nom site"]:
    a=0
    try:
        coor = coorfinder(str(i))

    except IndexError or ConnectionError:
        df2.drop(df2[df2['nom site'] == i].index, inplace = True)
        a=1
    if a == 0:
        LatCity.append(coor[0])
        LonCity.append(coor[1])
df2["Lat"]=LatCity
df2["Lon"]=LonCity



LatCity=[]
LonCity = []
for i in df3["nom site"]:
    a=0
    try:
        coor = coorfinder(str(i))

    except IndexError or ConnectionError:
        df3.drop(df3[df3['nom site'] == i].index, inplace = True)
        a=1
    if a == 0:
        LatCity.append(coor[0])
        LonCity.append(coor[1])
df3["Lat"]=LatCity
df3["Lon"]=LonCity



frames = [df1, df2, df3]

result = pd.concat(frames)
result.to_csv("/Users/alchambron/Documents/Coding_Project/hackatton/testdjango/testdjango/home/air_quality_df2.csv")



