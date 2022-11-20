import pandas as pd
from LatLonFinder import coorfinder
from DistCalculator import distance

def GetScoreWater(ville):
    ThresholdNitra = 50
    ThresholdNitri = 50
    df = pd.read_csv("water_quality_df.csv")
    coorville=coorfinder(ville)
    MaxNitra = max(df["nitrate (mg/L)"])
    MaxNitri = max(df["nitrite (mg/L)"])
    list_dist = []
    for i in range(len(df["Lat"])):
        temp_coor=[df["Lat"][i],df["Lon"][i]]
        temp_dist = distance(coorville,temp_coor)
        list_dist.append(temp_dist)
    PropNitri = df["nitrite (mg/L)"][list_dist.index(min(list_dist))]
    PropNitra = df["nitrate (mg/L)"][list_dist.index(min(list_dist))]
    if PropNitra <= ThresholdNitra:
        ScoreNitra = 100
    else:
        ScoreNitra = ((MaxNitra - PropNitra)/MaxNitra)*100
    if PropNitri <= ThresholdNitri:
        ScoreNitri = 100
    else:
        ScoreNitri = ((MaxNitri - PropNitri)/MaxNitri)*100
    
    return [ScoreNitra,ScoreNitri]
