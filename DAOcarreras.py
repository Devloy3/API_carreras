from carreras import Carreras

class DAOcarreras:
    def __init__(self, conexion):
        self.conexion = conexion
        self.cursor = conexion.cursor()
        self.carrera = Carreras(None)

    def crear_carrera(self,nombre):
        self.carrera.setNombre(nombre)
        self.cursor.execute('INSERT INTO carreras(nombre) VALUES (%s)',(self.carrera.getNombre(),))
        self.conexion.commit()
        return self.carrera.getNombre()
    
    def actualizar_carrera(self,nuevo_nombre,idcarreras):
        self.cursor.execute('UPDATE carreras SET nombre=%s WHERE idcarreras=%s',(nuevo_nombre, idcarreras))
        self.conexion.commit()
        self.carrera.setNombre(nuevo_nombre)
        return self.carrera.getNombre()

    def eliminar_carrera(self,idcarreras):
        self.cursor.execute('DELETE FROM carreras WHERE idcarreras= %s', (idcarreras,))
        self.conexion.commit()
        if self.cursor.rowcount > 0:
            return True
        else:
            return False

    def mostrar_carreras(self):
        self.cursor.execute('SELECT * FROM carreras')
        resultado = self.cursor.fetchall()
        return resultado