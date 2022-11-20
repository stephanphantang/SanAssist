import pandas as pd
from LatLonFinder import coorfinder
from DistCalculator import distance
def GetScoreAir(ville):
    df = pd.read_csv("air_quality_df2.csv")
    coorville=coorfinder(ville)
    #création liste contentant en premier la valeur de la propriété(concentration), la distance minimale entre la ville la plus proche déjà parcourue et la ville en input et l'index
    propCO=[0,10000000000,0]
    propNO2=[0,10000000000000,0]
    propPM10=[0,100000000000000000,0]
    propPM25=[0,100000000000000000,0]
    #dans la database quelle est la concentration la plus haute
    maxpropCO=0
    maxpropNO2=0
    maxpropPM10=0
    maxpropPM25=0
    for i in range(len(df["Lat"])):
        temp_coor=[df["Lat"][i],df["Lon"][i]]
        temp_dist = distance(coorville,temp_coor)
        if str(df["Polluant"][i]) == "CO":
            if propCO[1]>=temp_dist:
                propCO[1]=temp_dist
                propCO[0]=df["valeur brute"][i]
                propCO[2]=i
            if df["valeur brute"][i]>maxpropCO:
                maxpropCO=df["valeur brute"][i]

        elif str(df["Polluant"][i]) == "NO2":
            if propNO2[1]>=temp_dist:
                propNO2[1]=temp_dist
                propNO2[0]=df["valeur brute"][i]
                propNO2[2]=i
            if df["valeur brute"][i]>maxpropNO2:
                maxpropNO2=df["valeur brute"][i]
        elif str(df["Polluant"][i]) == "PM10":
            if propPM10[1]>=temp_dist:
                propPM10[1]=temp_dist
                propPM10[0]=df["valeur brute"][i]
                propPM10[2]=i
            if df["valeur brute"][i]>maxpropPM10:
                maxpropPM10=df["valeur brute"][i]
        elif str(df["Polluant"][i]) == "PM2.5":
            if propPM25[1]>=temp_dist:
                propPM25[1]=temp_dist
                propPM25[0]=df["valeur brute"][i]
                propPM25[2]=i
            if df["valeur brute"][i]>maxpropPM25:
                maxpropPM25=df["valeur brute"][i]
    # print(propNO2)
    # print(propCO)
    # print(propPM10)
    # print(propPM25)
    # print(maxpropPM25)
    # print(maxpropCO)
    # print(maxpropPM10)
    # print(maxpropNO2)

    df_threshold = pd.read_csv("ThreshDB.csv")
    if propPM10[0]<= df_threshold["threshold"][2]:
        scorePPM10=100
    else:
        scorePPM10=((maxpropPM10-propPM10[0])/(maxpropPM10))*100

    if propPM25[0]<= df_threshold["threshold"][3]:
        scorePPM25=100
    else:
        scorePPM25=((maxpropPM25-propPM25[0])/(maxpropPM25))*100

    if propNO2[0]<= df_threshold["threshold"][1]:
        scoreNO2=100
    else:
        scoreNO2=((maxpropNO2-propNO2[0])/(maxpropNO2))*100

    if propCO[0]<= df_threshold["threshold"][0]:
        scoreCO=100
    else:
        scoreCO=((maxpropCO-propCO[0])/(maxpropCO))*100


    return [scoreCO,scoreNO2,scorePPM10,scorePPM25]


    #temp_df=df.loc[:, ~df.columns.isin(['Lat', 'Lon'])]



#list_property = temp_df.loc[list_dist.index(min(list_dist)), :].values.tolist()



