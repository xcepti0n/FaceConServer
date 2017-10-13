from flask import Flask,request
from flask_restful import Resource, Api, reqparse
import os
app = Flask(__name__)
api = Api(app)
@app.route('/')
class FakeProfile (Resource):
       def post(self):
              parser = reqparse.RequestParser()
              parser.add_argument('url', type=str, help='url to get price')
              args = parser.parse_args()
              url = args['url']
              #url =request.args.get('url')
              
              return { 'title':title.get_text(),'currency': currency,'type':typetr, 'price' : price}
              #return currency+" "+price
api.add_resource(FakeProfile,'/fakeprof')
if __name__ == '__main__':
       port = int(os.environ.get('PORT', 5000))
app.run("0.0.0.0",port=port)
