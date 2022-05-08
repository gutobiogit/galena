from dataclasses import field
from marshmallow_dataclass import dataclass
import marshmallow.validate


@dataclass
class Cpf_user:
    """Class for keeping track of Address."""
    cpf_re= "([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})"
    cpf: str = field(metadata={"validate": marshmallow.validate.Regexp(cpf_re)})

#>>> test1 = Cpf_user.Schema().loads(json.dumps({"cpf": '18470526812'})) # True
#>>> test2 = Cpf_user.Schema().loads(json.dumps({"cpf": '184705268'})) # False
