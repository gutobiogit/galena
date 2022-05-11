from dataclasses import field
from marshmallow_dataclass import dataclass
import marshmallow.validate


@dataclass
class Email_user():
    """Class for keeping track of Emails."""
    email_address: str = field(metadata={"validate": marshmallow.validate.Email()})
