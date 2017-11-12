import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB
import numpy as np
FILE_PATH="./user_data_unshuffled.csv"
#loadcsv file
def predict_using_classifier(model,tweets,followers,following,likes,lists,joined_date,has_url,location):
    #loadcsv file
    dataset = pd.read_csv(FILE_PATH)
    # Get basic statistics of the loaded dataset
    #print(dataset.dtypes)
    #print(dataset.dtypes)
    X=dataset.iloc[:,0:8]
    y=dataset.iloc[:,8]
    print(X.shape,y.shape)
    print(X,y)
    model.fit(X, y)
    #model.predict_proba([[tweets,followers,following,likes,lists,joined_date,has_url,location]])
    predicted= model.predict([[tweets,followers,following,likes,lists,joined_date,has_url,location]])
    return predicted
def naive_bayes(tweets,followers,following,likes,lists,joined_date,has_url,location):
    model = GaussianNB()
    return predict_using_classifier(model,tweets,followers,following,likes,lists,joined_date,has_url,location)

def random_forest_classifier(tweets,followers,following,likes,lists,joined_date,has_url,location):
    model = RandomForestClassifier()
    dataset = pd.read_csv(FILE_PATH)
    # Get basic statistics of the loaded dataset
    #print(dataset.dtypes)
    #print(dataset.dtypes)
    X=dataset.iloc[:,0:8]
    y=dataset.iloc[:,8]
    #print(X.shape,y.shape)
    #print(X,y)
    model.fit(X, y)
    predicted_proba = model.predict_proba([[tweets,followers,following,likes,lists,joined_date,has_url,location]])
    predicted= model.predict([[tweets,followers,following,likes,lists,joined_date,has_url,location]])
    print(predicted,predicted_proba[0][0], predicted_proba[0][1])
    if(predicted == 0):
        predicted_proba = predicted_proba[0][0]
    else:
        predicted_proba = predicted_proba[0][1]
    return predicted, predicted_proba
    #return predict_using_classifier(model,tweets,followers,following,likes,lists,joined_date,has_url,location)
