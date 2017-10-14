import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB
import numpy as np
FILE_PATH="./min_user_data.csv"
# Headers 
headers = ["id","name","screen_name","statuses_count","followers_count","friends_count","favourites_count","profile_type"]
#loadcsv file
def naive_bayes(statuses_count,followers_count,friends_count,favourites_count):
    model = GaussianNB()
    dataset = pd.read_csv(FILE_PATH)
    # Get basic statistics of the loaded dataset
    #print(dataset.dtypes)
    #print(dataset.dtypes)
    X=dataset.iloc[:,3:7]
    y=dataset.iloc[:,7]
    print(X.shape,y.shape)
    model.fit(X, y)
    predicted= model.predict([[statuses_count,followers_count,friends_count,favourites_count]])
    return predicted

