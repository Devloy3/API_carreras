from DAOcarreras import DAOcarreras
from flask import Flask,jsonify

class Api:
    def __init__(self,nombre):
        self.app = Flask(__name__)
        self.nombre = DAOcarreras(nombre)

    @self.app.route("/mostrar", met)


























        