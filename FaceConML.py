import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
FILE_PATH="./user_data_unshuffled.csv"

def naive_bayes(tweets,followers,following,likes,lists,has_url,location):
    model = GaussianNB()
    #loadcsv file
    dataset = pd.read_csv(FILE_PATH)
    # Get basic statistics of the loaded dataset
    X=dataset.iloc[:,0:7]
    y=dataset.iloc[:,7]
    model.fit(X, y)
    predicted= model.predict([[tweets,followers,following,likes,lists,has_url,location]])
    return predicted

def random_forest_classifier(tweets,followers,following,likes,lists,has_url,location):
    model = RandomForestClassifier()
    #load csv file
    dataset = pd.read_csv(FILE_PATH)
    # Get basic statistics of the loaded dataset
    X=dataset.iloc[:,0:7]
    y=dataset.iloc[:,7]
    model.fit(X, y)
    predicted_proba = model.predict_proba([[tweets,followers,following,likes,lists,has_url,location]])
    predicted= model.predict([[tweets,followers,following,likes,lists,has_url,location]])
    print(predicted,predicted_proba[0][0], predicted_proba[0][1])
    if(predicted == 0):
        predicted_proba = predicted_proba[0][0]
    else:
        predicted_proba = predicted_proba[0][1]
    return predicted, predicted_proba
    
