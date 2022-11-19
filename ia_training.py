# dataset work
import pandas as pd

# Machine Learning
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

#Optimisation bayesienne
from skopt import BayesSearchCV

#export the machine learning problem
import pickle

dataset=pd.read_csv('dataset.csv')

#This function is to convert our database into a one hot encoding table
 
def ohe_conversion(disease_db):
    ohe=pd.DataFrame()
    ohe["Disease"]=list(disease_db["Disease"].values)
    for index,disease_db_row in disease_db.iterrows():
        for symptom_number in range(1,18):
            symptom_treat="Symptom_"+str(symptom_number)
            if not pd.isnull(disease_db_row[symptom_treat]):
                ohe.at[index,disease_db_row[symptom_treat]]=int(1)
    return ohe.fillna(int(0))

#ohe is the Machine Learning processable database
ohe=ohe_conversion(dataset)

#we split the table into the table of Disease and the table of symptoms assiociated to these disease
symptom=ohe.drop("Disease", axis=1).values
disease=ohe["Disease"]

#we split the data here between test and train, test size of 33%
symptom_train, symptom_test, disease_train, disease_test = train_test_split( symptom, disease, test_size=0.33, random_state=42)

#we search the best hyperparameters for a random forest algorithm
hyperparametersRF = {'bootstrap': [True, False],
 'max_depth': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, None],
 'max_features': ['auto', 'sqrt'],
 'min_samples_leaf': [1, 2, 4],
 'min_samples_split': [2, 5, 10],
 'n_estimators': [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000]}

#search of the best hyperparameters using a bayesian optimisation
bayesian = BayesSearchCV(
 estimator = RandomForestClassifier(), 
 search_spaces = hyperparametersRF, 
 n_iter = 10, 
 cv = 5, 
 random_state=42, 
 n_jobs = -1)

#train of the bayesian model
bayesian.fit(symptom_train, disease_train)

#obtain the model with the best hyperparameters of our case
best_random_forest= bayesian.best_estimator_

#train the best random forest to obtain a model
best_random_forest.fit(symptom_train, disease_train)

#export the model in a sav file
filename = 'instantdiag_model.sav'
pickle.dump(best_random_forest, open(filename, 'wb'))