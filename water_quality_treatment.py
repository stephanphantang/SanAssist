import pandas as pd
import random as rd
import numpy as np

rd.seed(10)

commune_dep= pd.read_csv("communes-departement-region.csv", sep=",")

commune_departement_name= commune_dep[["nom_commune", "code_departement"]]

com_dep_final=commune_departement_name.drop_duplicates()

nitrates_concentration= []
for i in range(36010):    
    nitrates_concentration.append(rd.normalvariate(18,15))

#nitrates is in mg/L, over 50mg/L danger for health
nitrates_concentration_all_positive= list(np.abs(nitrates_concentration))

nitrites_concentration= []
for j in range(36010):    
    nitrites_concentration.append(rd.normalvariate(1,1))

#nitrites is in mg/L, over 3mg/L danger for health
nitrites_concentration_all_positive= list(np.abs(nitrites_concentration))

dictionnary_water = {"nom_commune":com_dep_final["nom_commune"], "departement": com_dep_final["code_departement"], "nitrite (mg/L)": nitrites_concentration_all_positive, "nitrate (mg/L)": nitrates_concentration_all_positive}

water_df= pd.DataFrame(data = dictionnary_water)

water_df.to_csv("water_quality_df.csv", index=False)




