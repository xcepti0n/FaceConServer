import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import numpy as np
from flask import Flask,request
from flask_restful import Resource, Api, reqparse
from sklearn.naive_bayes import GaussianNB
import pandas as pd
import os
import FaceConML
app = Flask(__name__)
api = Api(app)
FILE_PATH="./min_user_data.csv"
@app.route('/')
class FakeProfile (Resource):
       def post(self):
              statuses_count= 45
              followers_count= 23
              friends_count = 34
              favourites_count = 333
              parser = reqparse.RequestParser()
              headers_used = ["statuses_count","followers_count","friends_count","favourites_count"]
              for header in headers_used:
                     parser.add_argument(header)
              args = parser.parse_args()
              if(args['statuses_count']):
                     statuses_count=args['statuses_count']
              if(args['followers_count']):
                     followers_count=args['followers_count']
              if(args['friends_count']):
                     friends_count = args['friends_count']
              if(args['favourites_count']):
                     favourites_count = args['favourites_count']
              # Headers 
              headers = ["id","name","screen_name","statuses_count","followers_count","friends_count","favourites_count","profile_type"]
              #loadcsv file
              predicted = FaceConML.naive_bayes(int(statuses_count),int(followers_count),int(friends_count),int(favourites_count))
              print (predicted)
              if(predicted==1):
                     value="fake profile"
              else:
                     value="legitimate profile"
              return { 'title': 'FaceCon','value': value}
api.add_resource(FakeProfile,'/fakeprof')
if __name__ == '__main__':
       port = int(os.environ.get('PORT', 5000))
app.run("0.0.0.0",port=port)
