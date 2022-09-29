from flask_restful import Resource
from flask import request
from .models import User, Book



class UserAPI(Resource):

    def get(self):
        users = User.find()
        return {'users': users}


    def post(self):
        data = request.json

        email = data.get("email").lower()
        
        user = User(email=email)
        user.save()

        return {'user': user}, 200

    def put(self, user_id):
        data = request.json

        book = data.get("book").lower()
        
        user = User.get_by_doc_id(user_id)
        user_books = user.books
        user.books = user_books.append(book)
        user.save()

        return {'user': user}, 200


class BookAPI(Resource):

    def get(self):
        books = Book.find()
        return {'books': books}


    def post(self):
        data = request.json

        name = data.get("name").lower()
        author = data.get("author").lower()
        
        book = Book(name=name, author=author)
        book.save()

        return {'book': book}, 200


