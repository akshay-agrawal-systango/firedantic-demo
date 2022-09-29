from .app import app
from .apis import UserAPI

from flask import Blueprint

api = Blueprint('api', __name__,url_prefix='/api')

user_api = UserAPI.as_view('users')

api.add_url_rule('/users', view_func=user_api, methods=["GET","POST"])
api.add_url_rule('/users/<user_id>/', view_func=user_api, methods=["PUT"])


app.register_blueprint(api)

