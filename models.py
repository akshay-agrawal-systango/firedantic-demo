from typing import List, Any
from pydantic import ValidationError, validator

from firedantic import Model, SubModel, SubCollection


class User(Model):
	__collection__ = "users"
	first_name: str = ''
	last_name: str = ''
	email: str


