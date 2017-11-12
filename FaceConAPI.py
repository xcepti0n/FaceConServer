import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import numpy as np
from flask import Flask,request
from flask_restful import Resource, Api, reqparse
from sklearn.naive_bayes import GaussianNB
import os
import FaceConML
import urlmatch
app = Flask(__name__)
api = Api(app)
FILE_PATH="./min_user_data.csv"
@app.route('/')
class FakeProfile (Resource):
       def post(self):
              tweets = 0
              followers = 0
              following = 0
              likes = 0
              lists = 0
              joined_date = 1390466506
              bio = 0
              location = 0
              has_url = 0
              #default_values=['0','0','0','0','0','1390466506','','0']
              parser = reqparse.RequestParser()
              headers_used = ["tweets","followers","following","likes","lists","joined_date","bio","location"]
              for header in headers_used:
                     print(header)
                     parser.add_argument(header)
              args = parser.parse_args()
              for header in headers_used:
                     print(args[header])
              if(args['tweets']):
                     tweets=args['tweets']
              if(args['followers']):
                     followers=args['followers']
              if(args['following']):
                     following=args['following']
              if(args['likes']):
                     likes = args['likes']
              if(args['joined_date']):
                     joined_date = args['joined_date']
              if(args['lists']):
                     lists = args['lists']
              if(args['bio']):
                     bio = args['bio']
              if(args['location']):
                     location = 1
              has_url = urlmatch.has_url(bio)
              print("tweets: ",tweets,"followers: ",followers,"following: ",following,"likes: ",likes,"joined_date: ",joined_date,"lists: ",lists,"bio: ",bio, "location: ",location,"has_url",has_url)
              #loadcsv file
              #predicted = FaceConML.naive_bayes(int(tweets),int(followers),int(following),int(likes),int(lists),int(joined_date),int(has_url),int(location))
              predicted, predicted_proba= FaceConML.random_forest_classifier(int(tweets),int(followers),int(following),int(likes),int(lists),int(joined_date),int(has_url),int(location))
              print (predicted)
              if(predicted==1):
                     value="fake profile"
              else:
                     value="legitimate profile"
              return { 'title': 'FaceCon','profile_type': value,'Probability':predicted_proba}
api.add_resource(FakeProfile,'/fakeprof')
if __name__ == '__main__':
       port = int(os.environ.get('PORT', 5000))
app.run("0.0.0.0",port=port)
