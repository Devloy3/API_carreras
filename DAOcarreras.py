import mysql.connector

class DAOcarreras:
    mydb = mysql.connector.connect(
        host= "localhost",
        user= "root",
        paswoord= "123456",
        database= "carreras"
    )

    cursor = mydb.cursor()

    def __init__(self,nombre):
        self.nombre = nombre

    def crear_carrera(self):
        self.__class__.cursor('INSERT INTO carreras(nombre) VALUES (%)', (self.nombre))
        self.__class__.mydb.commit()

    def actualizar_carrera(self,nuevo_nombre):
        self.__class__.cursor('UPDATE carreras SET nombre= %s WHERE nombre=%s',(nuevo_nombre, self.nombre))
        self.__class__.mydb.commit()

    def eliminar_carrera(self,nombre_eliminar):
        self.__class__.cursor('DELETE FROM carreras WHERE nombre=%s', (nombre_eliminar))
        self.__class__.mydb.commit()

    def mostrar_carreras(self):
        self.__class__.cursor('SELECT * FROM carreras')
        resultado = self.__class__.cursor.fetchall()
        return resultado
    
    
    

    