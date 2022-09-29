from flask_restful import Resource
from flask import request
from .models import User



class UserAPI(Resource):

    def get(self):
        users = User.find()
        return {'users': users}


    def post(self):
        data = request.json

        email = data.get("email").lower()
        
        user = User(email=email)
        user.save()

        return {'user_id': user.id}, 200

    def put(self, user_id):
        data = request.json

        email = data.get("email").lower()
        
        user = User.get_by_doc_id(user_id)
        user.email = email
        user.save()

        return {'user': user}, 200



