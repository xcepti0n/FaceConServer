import pandas as pd
import os
FILE_NAME = "./feedbackDataset.csv"

def append_data(tweets,followers,following,likes,lists,has_url,location,profile_type):
    feature_values = [[tweets,followers,following,likes,lists,has_url,location,profile_type]]
    feature_names = ['tweets','followers','following','likes','lists','has_url','location','profile_type']
    df = pd.DataFrame(feature_values, columns = feature_names)
    df.to_csv(FILE_NAME, mode = 'a', header = False, index = False)
