from dataclasses import field
from marshmallow_dataclass import dataclass
import marshmallow.validate


@dataclass
class Telephone_user:
    """Class for keeping track of Address."""
    phone_re= "(^\(\d{2}\) \d{4,6}-\d{4,6}$)"
    telephone: str = field(metadata={"validate": marshmallow.validate.Regexp(phone_re)})
