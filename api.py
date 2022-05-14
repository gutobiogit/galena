
from flask import Flask, request, jsonify

import data_model


app = Flask(__name__)
#api = restful.Api(app)

def get_data():
    x=data_model.run()
    json_obj=dict()
    outer_dict=dict()
    for index, dados in enumerate(x):
        json_obj['cpf']= dados.cpf
        json_obj['name']= dados.name
        json_obj['address']=dados.address
        json_obj['email']=dados.email
        json_obj['group']=dados.group
        json_obj['group_name']=dados.group_name
        json_obj['telephone']=dados.telephone
        json_obj['birthday']=dados.birthday
        outer_dict[index]=json_obj.copy() 

    return outer_dict

@app.route('/v1/data', methods=['GET'])
def get_all():
    output=get_data()
    return  output

 
if __name__ == '__main__':
    app.run(debug=True)
