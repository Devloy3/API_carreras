from DAOcarreras import DAOcarreras
from flask import Flask,jsonify, request as req

class Api:
    def __init__(self,host,user,password,database):
        self.app = Flask(__name__)
        self.dao = DAOcarreras(host,user,password,database)
        self.rutas()
    
    def rutas(self):
            @self.app.route("/mostrar", methods=['GET'])
            def mostrar():
                datos = self.dao.mostrar_carreras()
                carreras = [f"Carrera: {nombre[0]}" for nombre in datos]
                return jsonify(carreras)
            
            @self.app.route("/crear_carrera", methods=['POST'])
            def crear_carrera():
                nombre = req.form["nombre"]
                self.dao.crear_carrera(nombre)
                return jsonify({"Nombre": nombre + "creado"})

            @self.app.route("/modificar_carrera/<string:nombre>", methods=['PUT'])
            def actualizar(nombre):
                nuevo_nombre = req.form["nuevo_nombre"]
                self.dao.actualizar_carrera(nuevo_nombre,nombre)

            @self.app.route("/eliminar/<nombre_eliminar>", methods=['DELETE'])
            def eliminar(nombre_eliminar):
                self.dao.eliminar_carrera(nombre_eliminar)
                return jsonify({"Nombre": nombre_eliminar + "" + "eliminado"})
    
    def encendido(self):
        self.app.run()
    

host = input("Host:")
user = input("User:")
password = input("Contrasenya:")
database = input("Database:")

api = Api(host,user,password,database)
api.encendido()