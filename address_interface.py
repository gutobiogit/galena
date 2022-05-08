from dataclasses import field
from marshmallow_dataclass import dataclass
import marshmallow.validate

address_regex ="(?:RUA|Rua|R.|AVENIDA|Avenida|AV.|TRAVESSA|Travessa|TRAV.|Trav.).*(?<![0-9])$"
state_regex = "(?:AC|AL|AP|AM|BA|CE|DF|GO|ES|MA|MT|MS|MG|PA|PB|PR|PE|PI|RJ|RN|RS|RO|RR|SP|SC|SE|TO)"
zip_regex = "(?:[0-9]{5}-?[0-9]{3})"


@dataclass
class Address:
    """Class for keeping track of Address."""
    street: str = field(metadata={"validate": marshmallow.validate.Regexp(address_regex)})
    number: int = field(metadata={"validate": marshmallow.validate.Range(min=1,max=999999)})
    city: str
    state: str = field(metadata={"validate": marshmallow.validate.Regexp(state_regex)})
    zip: str = field(metadata={"validate": marshmallow.validate.Regexp(zip_regex)})
