from DAOcarreras import DAOcarreras
from flask import Flask,jsonify, request as req

class Api:
    def __init__(self):
        self.app = Flask(__name__)
        self.dao = DAOcarreras()
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
            def actualizar():
                carrera = req.get_data()
                nuevo_nombre = req.form["nuevo_nombre"]
                self.dao.actualizar_carrera(nuevo_nombre,carrera)

            @self.app.route("/eliminar/<string:nombre>", methods=['DELETE'])
            def eliminar():
                nuevo_nombre = req.get_data()
                self.dao.eliminar_carrera(nuevo_nombre)
                return jsonify({})


            
                 
                 

    
    def encendido(self):
        self.app.run()



api = Api()
api.encendido()
            
                  