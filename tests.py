import unittest
import json
import marshmallow
from email_dto import Email_user
from cpf_dto import CpfUser
from address_dto import Address
from birthday_dto import Birthday_user
from telephone_dto import Telephone_user
from spreadsheet_error_fixer import ErrorFixer


class TestUnit(unittest.TestCase):

    def test_birthday_user(self):
        test1 = Birthday_user.Schema().loads(json.dumps(
                                             {"birthday": "05/05/1995"}))
        self.assertIsInstance(test1, Birthday_user)
        self.assertRaises(marshmallow.exceptions.ValidationError, lambda:
                          Birthday_user.Schema().loads(json.dumps(
                            {"birthday": "05/05/199"})))

    def test_telephone_user(self):
        test1 = Telephone_user.Schema().loads(json.dumps(
                            {"telephone": "(11) 12345-6789"}))
        self.assertIsInstance(test1, Telephone_user)
        self.assertRaises(marshmallow.exceptions.ValidationError, lambda:
                          Telephone_user.Schema().loads(json.dumps(
                                {"telephone": "(111) 12345-6789"})))

    def test_email_user(self):
        test1 = Email_user.Schema().loads(json.dumps(
                        {"email_address": "gutobioit@gmail.com"}))
        self.assertIsInstance(test1, Email_user)
        self.assertRaises(marshmallow.exceptions.ValidationError, lambda:
                          Email_user.Schema().loads(json.dumps(
                            {"email_address": 1})))

    def test_CpfUser(self):
        test1 = CpfUser.Schema().loads(json.dumps({"cpf": '18470526812'}))
        self.assertIsInstance(test1, CpfUser)
        self.assertRaises(marshmallow.exceptions.ValidationError, lambda:
                          CpfUser.Schema().loads(json.dumps(
                              {"cpf": '184705268'})))

    def test_address_user(self):
        test1 = Address.Schema().loads(json.dumps(
                        {"street": "RUA Test Test", "number": "123",
                         "city": "São Paulo", "state": "SP",
                         "zip_code": "12345-678"}))
        self.assertIsInstance(test1, Address)
        self.assertRaises(marshmallow.exceptions.ValidationError, lambda:
                          Address.Schema().loads(json.dumps(
                              {"street": "RUA Test Test 123",
                               "number": "123", "city": "São Paulo",
                               "state": "SP", "zip_code": "12345-678"})))
        test2 = Address.Schema().loads(json.dumps(
                              {"street": "RUA Test Test", "number": "99999",
                               "city": "São Paulo", "state": "SP",
                               "zip_code": "12345-678"}))
        self.assertIsInstance(test2, Address)
        self.assertRaises(marshmallow.exceptions.ValidationError, lambda:
                          Address.Schema().loads(json.dumps(
                              {"street": "RUA Test Test 123",
                               "number": "999999", "city": "São Paulo",
                               "state": "SP", "zip_code": "12345-678"})))
        zip_test = Address.Schema().loads(json.dumps(
                    {"street": "RUA Test Test", "number": "123",
                     "city": "São Paulo", "state": "SP",
                     "zip_code": "12345-678"}))
        self.assertIsInstance(zip_test, Address)
        self.assertRaises(marshmallow.exceptions.ValidationError, lambda:
                          Address.Schema().loads(json.dumps(
                           {"street": "RUA Test Test", "number": "123",
                            "city": "São Paulo", "state": "SP",
                            "zip_code": "1234-678"})))

class TestErrorFixer(unittest.TestCase):
    
        def test_cpf_error_fixer(self):
            test1 = ErrorFixer.cpf_fixer('18470526812')
            self.assertEqual(test1, '184.705.268-12')
            test2 = ErrorFixer.cpf_fixer('184705268')
            self.assertEqual(test2, '000.000.000-00')

        def test_telephone_error_fixer(self):
            test1 = ErrorFixer.telephone_fixer("1112345678")
            self.assertEqual(test1, '(11) 1234-5678')
            test2 = ErrorFixer.telephone_fixer("11123")
            self.assertEqual(test2, '(00) 0000-0000')

        def test_birthday_error_fixer(self):
            test1 = ErrorFixer.birthday_fixer("2003-03-04 23:59:59")
            self.assertEqual(test1, '04/03/2003')
            test2 = ErrorFixer.birthday_fixer("05/05/199")
            self.assertEqual(test2, '00/00/0000')

        def test_numeric_filter(self):
            test1 = ErrorFixer.numeric_filter("1112345678")
            self.assertEqual(test1, '1112345678')
            test2 = ErrorFixer.numeric_filter("11123")
            self.assertEqual(test2, '11123')
            test3 = ErrorFixer.numeric_filter("2003-03-04 23:59:59")
            self.assertEqual(test3, '2003-03-04 23:59:59')
            test4 = ErrorFixer.numeric_filter("05/05/199")
            self.assertEqual(test4, '05/05/199')
            test5 = ErrorFixer.numeric_filter(None)
            self.assertEqual(test5, '00000000000')
            test6 = ErrorFixer(123)
            self.assertEqual(test6.spreadsheet, 123)



if __name__ == '__main__':
    unittest.main()
