from flask_sqlalchemy import SQLAlchemy
from random import randint

db = SQLAlchemy()

#Clase familia
class FamilyStructure(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), unique=True, nullable=False)
    last_name = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    lucky_numbers = db.Column(db.String(120), nullable=False)
    

    def __init__(self, last_name): 
        self.last_name = last_name

        #Ejmplo de lista de miembros
        self._members = [
        {
            "id": self._generateId(),
            "first_name": "Esmeralda",
            "last_name": last_name,
            "age": '41',
            "lucky_numbers": [98, 2, 78]
        },
        {
            "id": self._generateId(),
            "first_name": "Yocksan",
            "last_name": last_name,
            "age": '16',
            "lucky_numbers": [90, 46, 48]
        },
        {
            "id": self._generateId(),
            "first_name": "Elena",
            "last_name": last_name,
            "age": '65',
            "lucky_numbers": [78, 22, 13]
        },
        {
            "id": self._generateId(),
            "first_name": "Gerson",
            "last_name": last_name,
            "age": '25',
            "lucky_numbers": [17, 26, 47]
        },
        {
            "id": self._generateId(),
            "first_name": "Carmen",
            "last_name": last_name,
            "age": '30',
            "lucky_numbers": [78, 43, 11]
        },
        {
            "id": self._generateId(),
            "first_name": "Deikel",
            "last_name": last_name,
            "age": '12',
            "lucky_numbers": [57, 44, 80]
        },
        {
            "id": self._generateId(),
            "first_name": "Yarit",
            "last_name": last_name,
            "age": '30',
            "lucky_numbers": [68, 21, 99]
        }
        ]

    def _generateId(self): 

        return randint(0, 7)

    #Obtener miembro de la familia con id
    def get_member(self,id):

        for member in self._members:

            if member['id'] == int(id):
                return member

        return None

    def get_all_members(self):
        return self._members

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }