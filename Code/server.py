#!/usr/bin/python3
from flask import Flask, request, jsonify, session
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_restful import reqparse
from errors import errors


db_connect = create_engine('sqlite:///article.db')
app = Flask(__name__) #Create an instance of the class
api = Api(app)


class ArticlePrice(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser() #defining parameters
        self.reqparse.add_argument('article', type = int, default='')
        self.reqparse.add_argument('color', type = int, default='')
        self.reqparse.add_argument('week', type = int, default='')
        super(ArticlePrice, self).__init__()
        
    def get(self):
        args = self.reqparse.parse_args()
        conn = db_connect.connect() # connect to database
        condition = ""
        if(args['color'] != 0):
            condition = "Where p.article_id=? and p.article_color_id=? and p.week=?"
        else:
            condition = "Where p.article_id=? and p.article_color_id!=? and p.week=?"
        query = """
        Select i.article_name,c.article_color_name,p.week,p.article_price 
        From article_price p
        Inner Join article_item i on i.article_id=p.article_id
        Inner Join article_color c on c.article_color_id=p.article_color_id
        """ + condition
        try:
            data = conn.execute(query,(args['article'],args['color'],args['week'])) # This line performs query and returns json result
            result = {'data': [dict(zip(tuple (data.keys()) ,i)) for i in data.cursor]}
            return jsonify(result)
        except DoesNotExist:
            raise DataNotExistsError
        except Exception:
            raise InternalServerError
    
api.add_resource(ArticlePrice, '/price') # Route_1


if __name__ == '__main__':
     app.run() #Run the Flask application (default port)
