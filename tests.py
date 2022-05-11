import unittest
import json
import marshmallow
from email_dto import Email_user
from cpf_dto import Cpf_user
from address_dto import Address
from birthday_dto import Birthday_user
from telephone_dto import Telephone_user


class TestUnit(unittest.TestCase):

    def test_birthday_user(self):
        test1 = Birthday_user.Schema().loads(json.dumps({"birthday": "05/05/1995"}))
        self.assertIsInstance(test1, Birthday_user)
        self.assertRaises(marshmallow.exceptions.ValidationError, lambda: Birthday_user.Schema().loads(json.dumps({"birthday": "05/05/199"})))

    def test_telephone_user(self):
        test1 = Telephone_user.Schema().loads(json.dumps({"telephone": "(11) 12345-6789"}))
        self.assertIsInstance(test1, Telephone_user)
        self.assertRaises(marshmallow.exceptions.ValidationError, lambda: Telephone_user.Schema().loads(json.dumps({"telephone": "(111) 12345-6789"})))

    def test_email_user(self):
        test1 = Email_user.Schema().loads(json.dumps({"email_address": "gutobioit@gmail.com"}))
        self.assertIsInstance(test1, Email_user)
        self.assertRaises(marshmallow.exceptions.ValidationError, lambda: Email_user.Schema().loads(json.dumps({"email_address": 1})))

    def test_cpf_user(self):
        test1 = Cpf_user.Schema().loads(json.dumps({"cpf": '18470526812'}))
        self.assertIsInstance(test1, Cpf_user)
        self.assertRaises(marshmallow.exceptions.ValidationError, lambda: Cpf_user.Schema().loads(json.dumps({"cpf": '184705268'})))

    def test_address_user(self):
        test1 = Address.Schema().loads(json.dumps({"street": "RUA Test Test", "number": 123, "city": "São Paulo", "state": "SP", "zip_code": "12345-678"}))
        self.assertIsInstance(test1, Address)
        self.assertRaises(marshmallow.exceptions.ValidationError, lambda: Address.Schema().loads(json.dumps({"street": "RUA Test Test 123", "number": 123, "city": "São Paulo", "state": "SP", "zip_code": "12345-678"})))
        test2 = Address.Schema().loads(json.dumps({"street": "RUA Test Test", "number": 99999, "city": "São Paulo", "state": "SP", "zip_code": "12345-678"}))
        self.assertIsInstance(test2, Address)
        self.assertRaises(marshmallow.exceptions.ValidationError, lambda: Address.Schema().loads(json.dumps({"street": "RUA Test Test 123", "number": 999999, "city": "São Paulo", "state": "SP", "zip_code": "12345-678"})))
        zip_test = Address.Schema().loads(json.dumps({"street": "RUA Test Test", "number": 123, "city": "São Paulo", "state": "SP", "zip_code": "12345-678"}))
        self.assertIsInstance(zip_test, Address)
        self.assertRaises(marshmallow.exceptions.ValidationError, lambda: Address.Schema().loads(json.dumps({"street": "RUA Test Test", "number": 123, "city": "São Paulo", "state": "SP", "zip_code": "1234-678"})))


if __name__ == '__main__':
    unittest.main()
