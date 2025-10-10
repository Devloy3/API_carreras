from DAOcarreras import DAOcarreras
from connexionDB import ConexionDB
from flask import Flask,jsonify, request as req

host = input("Introduzca el host de la base de datos (localhost por defecto):")
user = input("Introduzca el usuario de la base de datos (root por defecto):")
password = input("Introduzca la contraseña de la base de datos (123456 por defecto):")
database = input("Introduzca el nombre de la base de datos (carreras por defecto):")

if host == "" and user == "" and password == "" and database == "":
     conexion = ConexionDB().conectar()

else:
     conexion = ConexionDB(host,user,password,database).conectar()


class Api:

    def __init__(self, conexion):
        self.app = Flask(__name__)
        self.dao = DAOcarreras(conexion)
        self.rutas()
    
    def rutas(self):
            @self.app.route("/mostrar", methods=['GET'])
            def mostrar():
                datos = self.dao.mostrar_carreras()
                carreras = [nombre[0] for nombre in datos]
                return jsonify(carreras)
            
            @self.app.route("/crear_carrera", methods=['POST'])
            def crear_carrera():
                nombre = req.form["nombre"]
                carrera = self.dao.crear_carrera(nombre)
                return jsonify({"Nombre": carrera.getNombre() + " " + "creado"})

            @self.app.route("/modificar_carrera/<string:nombre>", methods=['PUT'])
            def actualizar(nombre):
                nuevo_nombre = req.form["nuevo_nombre"]
                self.dao.actualizar_carrera(nuevo_nombre,nombre)

            @self.app.route("/eliminar/<nombre_eliminar>", methods=['DELETE'])
            def eliminar(nombre_eliminar):
                self.dao.eliminar_carrera(nombre_eliminar)
                return jsonify({"Nombre": nombre_eliminar + " " + "eliminado"})
    
    def encendido(self):
        self.app.run()
    
api = Api(conexion)
api.encendido()