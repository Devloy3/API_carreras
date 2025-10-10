from carreras import Carreras

class DAOcarreras:
    def __init__(self, conexion):
        self.conexion = conexion
        self.cursor = conexion.cursor()
        self.carrera = Carreras("")

    def crear_carrera(self,nombre):
        self.carrera.setNombre(nombre)
        self.cursor.execute('INSERT INTO carreras(nombre) VALUES (%s)',(self.carrera.getNombre(),))
        self.conexion.commit()
        return self.carrera

    def actualizar_carrera(self, nuevo_nombre, nombre_viejo):
        self.carrera.setNombre(nombre_viejo)
        self.cursor.execute(
        'UPDATE carreras SET nombre = %s WHERE nombre = %s',
        (nuevo_nombre, self.carrera.getNombre())
        )
        self.conexion.commit()

    def eliminar_carrera(self,nombre_eliminar):
        self.carrera.setNombre(nombre_eliminar)
        self.cursor.execute('DELETE FROM carreras WHERE nombre= %s', (self.carrera.getNombre(),))
        self.conexion.commit()
        if self.cursor.rowcount > 0:
            return True
        else:
            return False

    def mostrar_carreras(self):
        self.cursor.execute('SELECT nombre FROM carreras')
        resultado = self.cursor.fetchall()
        return resultado