import data_model
from spreadsheet_entity import Spreadsheet


def get_one_data(posted_data):
    one_record = data_model.get_one_record(posted_data)
    json_obj = dict()
    json_list = list()
    json_obj['code'] = posted_data
    json_obj['cpf'] = one_record.cpf
    json_obj['name'] = one_record.name
    json_obj['address'] = one_record.address
    json_obj['email'] = one_record.email.email_address
    json_obj['group'] = one_record.group
    json_obj['group_name'] = one_record.group_name
    json_obj['telephone'] = one_record.telephone
    json_obj['birthday'] = one_record.birthday
    json_obj['address'] = one_record.address
    json_list.append({"id": posted_data, "birthday": json_obj['birthday'],
                      "name": json_obj['name'], "group": json_obj['group'],
                      "cpf": json_obj['cpf'], "username": json_obj['email'],
                      "group_name": json_obj['group_name'],
                      "telephone": json_obj['telephone'],
                      "address": json_obj['address']})
    return json_obj


def get_all_data():
    all_records = data_model.get_all_records()
    json_obj = dict()
    json_list = list()
    for index, dados in enumerate(all_records):
        json_obj['code'] = index
        json_obj['cpf'] = dados.cpf
        json_obj['name'] = dados.name
        json_obj['address'] = dados.address
        json_obj['email'] = dados.email.email_address
        json_obj['group'] = dados.group
        json_obj['group_name'] = dados.group_name
        json_obj['telephone'] = dados.telephone
        json_obj['birthday'] = dados.birthday
        json_obj['address'] = dados.address
        json_list.append({"id": index+1,
                          "birthday": json_obj['birthday'],
                          "name": json_obj['name'],
                          "group": json_obj['group'],
                          "cpf": json_obj['cpf'],
                          "username": json_obj['email'],
                          "group_name": json_obj['group_name'],
                          "telephone": json_obj['telephone'],
                          "address": json_obj['address']})
    return json_list


def delete_record(posted_data):
    message = data_model.delete_row(posted_data)
    return message


def create_new_record(posted_data):
    new_spreadsheet = Spreadsheet()
    new_spreadsheet.name = posted_data['name']
    new_spreadsheet.cpf = posted_data['cpf']
    new_spreadsheet.email = posted_data['email']
    new_spreadsheet.group = posted_data['group']
    new_spreadsheet.group_name = posted_data['group_name']
    new_spreadsheet.telephone = posted_data['telephone']
    new_spreadsheet.birthday = posted_data['birthday']
    new_spreadsheet.address = (posted_data['street'],
                               posted_data['number'],
                               posted_data['city'],
                               posted_data['state'],
                               posted_data['zip_code'])
    message = data_model.add_row(new_spreadsheet)
    return message


def change_record(id_number, posted_data):
    new_spreadsheet = Spreadsheet()
    new_spreadsheet.name = posted_data['name']
    new_spreadsheet.cpf = posted_data['cpf']
    new_spreadsheet.email = posted_data['email']
    new_spreadsheet.group = posted_data['group']
    new_spreadsheet.group_name = posted_data['group_name']
    new_spreadsheet.telephone = posted_data['telephone']
    new_spreadsheet.birthday = posted_data['birthday']
    new_spreadsheet.address = (posted_data['street'],
                               posted_data['number'],
                               posted_data['city'],
                               posted_data['state'],
                               posted_data['zip_code'])
    message = data_model.change_row(id_number, new_spreadsheet)
    return message
