from dataclasses import field
from marshmallow_dataclass import dataclass
import marshmallow.validate


@dataclass
class CpfUser:
    """Class for validate and serialize/deserialize Cpf data
    """
    cpf_re = r"([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}" + \
             r"[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}" + \
             r"[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})"
    cpf: str = field(metadata={"validate":
                     marshmallow.validate.Regexp(cpf_re)})
