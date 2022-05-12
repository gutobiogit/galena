import json
from marshmallow import ValidationError
from telephone_dto import Telephone_user
from email_dto import Email_user
from cpf_dto import Cpf_user
from address_dto import Address
from birthday_dto import Birthday_user
from spreadsheet_error_fixer import ErrorFixer


class Spreadsheet:

    def __init__(self, sheet=None):
        pass

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        try:
            self._email = Email_user.Schema().loads(json.dumps(
                                {"email_address": value}))
        except ValidationError:
            raise ValueError("Invalid email address")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, value):
        self._group = value

    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, value):
        self._group_name = value

    @property
    def cpf(self):
        return Cpf_user.Schema().dumps(self._cpf)

    @cpf.setter
    def cpf(self, value):
        try:
            self._cpf = Cpf_user.Schema().loads(json.dumps({"cpf": value}))
        except ValidationError:
            value_retried = ErrorFixer.cpf_fixer(value)
            self._cpf = Cpf_user.Schema().loads(
                        json.dumps({"cpf": value_retried}))

    @property
    def telephone(self):
        return Telephone_user.Schema().dumps(self._telephone)

    @telephone.setter
    def telephone(self, value):
        try:
            self._telephone = Telephone_user.Schema().loads(
                        json.dumps({"telephone": value}))
        except ValidationError:
            value_retried = ErrorFixer.telephone_fixer(value)
            self._telephone = Telephone_user.Schema().loads(
                        json.dumps({"telephone": value_retried}))

    @property
    def birthday(self):
        return Birthday_user.Schema().dumps(self._birthday)

    @birthday.setter
    def birthday(self, value):
        try:
            self._birthday = Birthday_user.Schema().loads(
                        json.dumps({"birthday": str(value)}))
        except ValidationError:
            value_retried = ErrorFixer.birthday_fixer(value)
            self._birthday = Birthday_user.Schema().loads(
                        json.dumps({"birthday": str(value_retried)}))

    @property
    def address(self):
        return Address.Schema().dumps(self._address)

    @address.setter
    def address(self, vals):
        street, number, city, state, zip_code = vals
        self._address = Address.Schema().loads(
                        json.dumps({"street": street, "number": number,
                                    "city": city, "state": state,
                                    "zip_code": zip_code}))
