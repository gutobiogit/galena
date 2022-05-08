from dataclasses import field
from marshmallow import Schema
from marshmallow_dataclass import dataclass
import marshmallow.validate


@dataclass
class Email_user():
    """Class for keeping track of Address."""
    email_address: str = field(metadata={"validate": marshmallow.validate.Email()})

# test1 = Email_user.Schema().loads(json.dumps({"email_address": 1})) # False
# test1 = Email_user.Schema().loads(json.dumps({"email_address":"gutobioit@gmail.com"})) # True
