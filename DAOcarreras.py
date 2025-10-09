from carreras import Carreras
from ConnexionDatabase import ConnDatabase

class DAOcarreras:
    def __init__(self,host,user,password,database,nombre="Quimica",):
        self.connexion = ConnDatabase(host,user,password,database)
        self.cursor = self.connexion.mydb.cursor()
        self.nombre = Carreras(nombre)

    def crear_carrera(self,nombre):
        self.nombre.setNombre(nombre)
        self.cursor.execute('INSERT INTO carreras(nombre) VALUES (%s)',(self.nombre.getNombre(),))
        self.connexion.mydb.commit()

    def actualizar_carrera(self,nuevo_nombre,nombre_viejo):
        self.nombre.setNombre(nombre_viejo)
        self.cursor.execute('UPDATE carreras SET nombre= %s WHERE nombre=%s',(nuevo_nombre, self.nombre.getNombre()))
        self.connexion.mydb.commit()

    def eliminar_carrera(self,nombre_eliminar):
        self.nombre.setNombre(nombre_eliminar)
        self.cursor.execute('DELETE FROM carreras WHERE nombre= %s', (self.nombre.getNombre(),))
        self.connexion.mydb.commit()

    def mostrar_carreras(self):
        self.cursor.execute('SELECT nombre FROM carreras')
        resultado = self.cursor.fetchall()
        return resultado
    

    

    

    