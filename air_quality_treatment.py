import pandas as pd

air_quality = pd.read_csv("FR_E2_2022-11-19.csv", sep=";")

#we keep only relevant data
air_quality_filtered= air_quality[["nom site", "Polluant", "valeur brute", "unité de mesure" ]]

#filer the nan value
air_quality_filtered_nan = air_quality_filtered.dropna()

#change a column name
air_quality_filtered_rename = air_quality_filtered_nan.rename({'unité de mesure': 'unit'}, axis=1)

#convert all value into µg/m-3
air_quality_filtered_rename.loc[air_quality_filtered_rename.unit=='mg-m3', 'valeur brute'] = air_quality_filtered_rename.loc[air_quality_filtered_rename.unit=='mg-m3', 'valeur brute']*1000

#grouby site and by molecule
air_quality_filtered_grouped= air_quality_filtered_rename.groupby(['nom site','Polluant'], as_index=False)['valeur brute'].mean()

#save it to csv
air_quality_filtered_grouped.to_csv("air_quality_df.csv", index=False)


