import mysql.connector
from carreras import Carreras

class DAOcarreras:
    def __init__(self,nombre,host,user,password,database):
        self.setUser(user)
        self.setHost(host)
        self.setDatabase(database)
        self.setPassword(password)
        
        self.mydb = mysql.connector.connect(
            host=self.GetHost(),
            user=self.GetUser(),
            password=self.GetPassword(),
            database=self.GetDatabase()
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
    
    def setHost(self,host):
        self.__host = host 

    def setUser(self,user):
        self.__user = user

    def setPassword(self,password):
        self.__Password = password

    def setDatabase(self,database):
        self.__database = database
    
    def GetHost(self):
        return self.__host
    
    def GetUser(self):
        return self.__user
    
    def GetPassword(self):
        return self.__Password
    
    def GetDatabase(self):
        return self.__database
    

    

    