from openpyxl import load_workbook
from spreadsheet_entity import Spreadsheet


def split_address(address):
    address_split = address.split(",")
    address_split = [x.strip(' ') for x in address_split]
    state = address_split[-1].split(" ")[0]
    zip_code = address_split[-1].split(" ")[1]
    city = address_split[-2]
    number = address_split[0].split(" ")[-1].strip(" ")
    street = " ".join(address_split[0].split(" ")[0:-1])
    return [street, number, city, state, zip_code]


wb = load_workbook('tabela-de-exemplo.xlsx')
ws = wb['results-20220124-165033']
objects = []
max_columns=ws.max_column+2
emails = ws["A4":f"A{max_columns}"]
names = ws["B4":f"B{max_columns}"]
groups = ws["C4":f"C{max_columns}"]
group_names = ws["D4":f"D{max_columns}"]
cpfs = ws["E4":f"E{max_columns}"]
telephones = ws["F4":f"F{max_columns}"]
birthdays = ws["G4":f"G{max_columns}"]
address = ws["H4":f"H{max_columns}"]

#print(emails[4][0].value)

for count in range(1,max_columns-3):

    obj = Spreadsheet()
    obj.email = emails[count][0].value
    obj.name = names[count][0].value
    obj.group = groups[count][0].value
    obj.group_name = group_names[count][0].value
    obj.cpf = cpfs[count][0].value
    obj.telephone = telephones[count][0].value
    obj.birthday = birthdays[count][0].value
    obj.address = split_address(address[count][0].value)
    objects.append(obj)
    print(obj.email)
    print(obj.name)
    print(obj.group)
    print(obj.group_name)
    print(obj.cpf)
    print(obj.telephone)
    print(obj.birthday)
    print(obj.address)
    print("\n")
    print("\n")

    objects.append(obj)


# for a in objects:
#     print(a.email)
#     print(a.name)
#     print(a.group)
#     print(a.group_name)
#     print(a.cpf)
#     print(a.telephone)
#     print(a.birthday)
#     print("\n")
#     print("\n")
#print(objects)

# for data in x:
#     for cell in data:
#         print(cell.value)

# for col in ws.iter_cols(min_row=1, max_row=8, min_col=1, max_col=ws.max_column):
#     for cell in col:
#         print(cell.value)
#         if cell.value == 'E-mail':
#             email = cell.column
#         if cell.value == 'Nome':
#             name = cell.column
#         if cell.value == 'Grupo':
#             group = cell.column
#         if cell.value == 'Nome do Grupo':
#             group_name = cell.column
#         if cell.value == 'CPF':
#             cpf = cell.column
#         if cell.value == 'Telefone':
#             telephone = cell.column
#         if cell.value == 'Data Nascto':
#             birthday = cell.column
#         print (email, name, group, group_name, cpf, telephone, birthday)
