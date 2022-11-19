#creates the base database for the world health organization recommandations, avec pour l'instant la databse de l'air
import pandas as pd
name = ["PM10","PM2,5","Ozone","Dioxyde d'Azote","Dioxyde de Soufre","Monoxyde de Carbone"]
print(len(name))
threshold = [15,5,60,10,40,4]
print(len(threshold))
recommandations = ["Peut causer des troubles cardiaques et pulmonaires, des bronchites, de l'asthme et potentiellement mort, porter un masque, évitez les zones à fort trafic routier, aux périodes de pointe et privilégiez les activités modérées.","Peut causer des troubles cardiaques et pulmonaires, des bronchites, de l'asthme et potentiellement mort, porter un masque, évitez les zones à fort trafic routier, aux périodes de pointe et privilégiez les activités modérées.","réduisez, voire reportez, les activités physiques et sportives intenses2 (dont les compétitions)","réduisez, voire reportez, les activités physiques et sportives intenses2 (dont les compétitions).","réduisez, voire reportez, les activités physiques et sportives intenses2 (dont les compétitions).","réduisez, voire reportez, les activités physiques et sportives intenses2 (dont les compétitions)."]
print(len(recommandations))
d = {"name":name, "threshold":threshold, "recommandations":recommandations}
df = pd.DataFrame(data=d)
print(df)
df.to_csv("ThreshDB.csv")