from email import message
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import data_model
from spreadsheet_entity import Spreadsheet


app = Flask(__name__)
CORS(app, support_credentials=True)

def get_all_data():
   all_records = data_model.run()
   json_obj = dict()
   json_list = list()
   for index, dados in enumerate(all_records):
      json_obj['code']= index
      json_obj['cpf']= dados.cpf
      json_obj['name']= dados.name
      json_obj['address']=dados.address
      json_obj['email']=dados.email.email_address
      json_obj['group']=dados.group
      json_obj['group_name']=dados.group_name
      json_obj['telephone']=dados.telephone
      json_obj['birthday']=dados.birthday
      json_obj['address']=dados.address
      json_list.append({"id":index+1,"birthday":json_obj['birthday'],"fname":json_obj['name'],
                     "group":json_obj['group'],"lname":json_obj['cpf'],"username":json_obj['email'],
                     "group_name":json_obj['group_name'],"telephone":json_obj['telephone'],
                     "address":json_obj['address']})    
   return jsonify(json_list)

def delete_record(posted_data):
    message = data_model.delete_row(posted_data)
    return message
 
def create_new_record(posted_data):
    new_spreadsheet=Spreadsheet()
    new_spreadsheet.name = posted_data['fname']
    new_spreadsheet.cpf = posted_data['lname']
    new_spreadsheet.email = posted_data['email']
    new_spreadsheet.group = posted_data['group']
    new_spreadsheet.group_name = posted_data['group_name']
    new_spreadsheet.telephone = posted_data['telephone']
    new_spreadsheet.birthday = posted_data['birthday']
    new_spreadsheet.address = (posted_data['street'], posted_data['number'],  posted_data['city'],
                              posted_data['state'], posted_data['zip_code'])
    message = data_model.add_row(new_spreadsheet)
    return message


@app.route('/v1/data', methods=['GET'])
def get_all():
    output=get_all_data()
    return  output

@app.route('/v1/data', methods=['POST'])
def add_data():
    message = create_new_record(request.json)
    return jsonify({'message': message})

@app.route('/v1/data/<int:id>', methods=['DELETE'])
def delete_data(id):
    message = delete_record(id)
    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(debug=True)
