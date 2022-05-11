from dataclasses import field
from marshmallow_dataclass import dataclass
import marshmallow.validate


@dataclass
class Cpf_user:
    """Class for keeping track of Address."""
    cpf_re = "([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})"
    cpf: str = field(metadata={"validate": marshmallow.validate.Regexp(cpf_re)})
