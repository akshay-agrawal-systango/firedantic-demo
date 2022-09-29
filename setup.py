from .app import app
from .apis import UserAPI, BookAPI

from flask import Blueprint

api = Blueprint('api', __name__,url_prefix='/api')

user_api = UserAPI.as_view('users')
book_api = BookAPI.as_view('books')

api.add_url_rule('/users', view_func=user_api, methods=["GET","POST"])
api.add_url_rule('/users/<user_id>/', view_func=user_api, methods=["PUT"])
api.add_url_rule('/books', view_func=book_api, methods=["GET","POST"])
api.add_url_rule('/books/<book_id>/', view_func=user_api, methods=["PUT"])


app.register_blueprint(api)

