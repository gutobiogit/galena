from mailbox import NotEmptyError
from openpyxl import load_workbook
from address_interface import AddressInterface

wb = load_workbook('tabela-de-exemplo.xlsx')

sheet = wb['results-20220124-165033']

e_mail = dict()
nome = dict()
grupo = dict()
nome_grupo = dict()
cpf = dict()
telefone = dict()
data_nascimento = dict()
endereco = adress_interface()
