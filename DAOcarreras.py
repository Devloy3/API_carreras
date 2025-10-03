import mysql.connector
from carreras import Carreras

class DAOcarreras:
    
    def __init__(self,nombre):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="carreras"
        )

        self.cursor = self.mydb.cursor()
        self.nombre = Carreras(nombre)

    def crear_carrera(self,nombre):
        self.nombre.setNombre(nombre)
        self.cursor.execute('INSERT INTO carreras(nombre) VALUES (%s)', (self.nombre.getNombre(),))
        self.mydb.commit()

    def actualizar_carrera(self,nuevo_nombre,nombre_viejo):
        self.nombre.setNombre(nombre_viejo)
        self.cursor.execute('UPDATE carreras SET nombre= %s WHERE nombre=%s',(nuevo_nombre, self.nombre.getNombre()))
        self.mydb.commit()

    def eliminar_carrera(self,nombre_eliminar):
        self.nombre.setNombre(nombre_eliminar)
        self.cursor.execute('DELETE FROM carreras WHERE nombre= %s', (self.nombre.getNombre(),))
        self.mydb.commit()

    def mostrar_carreras(self):
        self.cursor.execute('SELECT nombre FROM carreras')
        resultado = self.cursor.fetchall()
        return resultado
    

    

    