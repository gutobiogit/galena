from dataclasses import field
from marshmallow_dataclass import dataclass
import marshmallow.validate


@dataclass
class Birthday_user:
    """Class for keeping track of Birthday."""
    birthday_re = r"(^\d{2}\/\d{2}\/\d{4}$)"
    birthday: str = field(metadata={"validate":
                                    marshmallow.validate.Regexp(birthday_re)})
