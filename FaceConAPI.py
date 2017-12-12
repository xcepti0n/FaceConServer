from flask import Flask,request
from flask_restful import Resource, Api, reqparse
import FaceConML
import FaceConFeedback
import urlmatch
import os
app = Flask(__name__)
api = Api(app)
@app.route('/')
class FakeProfile (Resource):
       def post(self):
              tweets = 0
              followers = 0
              following = 0
              likes = 0
              lists = 0
              bio = 0
              location = 0
              has_url = 0
              parser = reqparse.RequestParser()
              headers_used = ["tweets","followers","following","likes","lists","bio","location"]
              
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
              if(args['lists']):
                     lists = args['lists']
              if(args['bio']):
                     bio = args['bio']
              if(args['location']):
                     location = 1

              has_url = urlmatch.has_url(bio)

              predicted, predicted_proba= FaceConML.random_forest_classifier(int(tweets),int(followers),int(following),int(likes),int(lists),int(has_url),int(location))

              if(predicted==1 or predicted_proba < 0.8):
                     value="Fake"
              else:
                     value="Legitimate"

              return { 'title': 'FaceCon','profile_type': value,'probability':predicted_proba}

api.add_resource(FakeProfile,'/fakeprof')

class Feedback (Resource):
       def post(self):
              
              tweets = 0
              followers = 0
              following = 0
              likes = 0
              lists = 0
              bio = 0
              location = 0
              has_url = 0
              profile_type = -1
              parser = reqparse.RequestParser()
              headers_used = ["tweets","followers","following","likes","lists","bio","location","profile_type"]

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
              if(args['lists']):
                     lists = args['lists']
              if(args['bio']):
                     bio = args['bio']
              if(args['location']):
                     location = 1
              if(args['profile_type']):
                     profile_type = args['profile_type']
              has_url = urlmatch.has_url(bio)
              
              if(int(profile_type) == 1 or int(profile_type) == 0):
                     FaceConFeedback.append_data(int(tweets),int(followers),int(following),int(likes),int(lists),int(has_url),int(location),int(profile_type))
                     return {'response':'OK', 'code':200}
              
              return { 'response':'ERROR', 'code':400}
              
api.add_resource(Feedback,'/feedback')

if __name__ == '__main__':
       port = int(os.environ.get('PORT', 5000))
app.run("127.0.0.1",port=port)
