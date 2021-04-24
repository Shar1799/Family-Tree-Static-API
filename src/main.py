"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, FamilyStructure # Importa elementos de models
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

#Creación de un objeto family 
calvo_family = FamilyStructure('Calvo')

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():

    members = calvo_family.get_all_members()
    response_body = {
        "family": members
    }

    return jsonify(response_body), 200

#Buscar por id
@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id=None):

    member = calvo_family.get_member(member_id)

    #Condicional si el id existe 
    if member:
        return jsonify(member), 200
    else:
        return jsonify({"Mensaje":"Id no existe"}), 400 #Si no existe


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
