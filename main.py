from carreras import Carreras
from DAOcarreras import DAOcarreras

def menu():
    while True:
        print("<-- Menu de Carreras -->")
        print("1.Crear carreras")
        print("2.Mostrar Carreras")
        print("3.Actualizar carreras")
        print("4.Eliminar carreras")
        print("5.Salir")

        opcion = int(input("Que escoges:"))

        if opcion == 1:
            nombre = input("Introduce el nombre de la carrera:")
            carrera = Carreras(nombre)
            nombre_carrera = carrera.getNombre()
            dao = DAOcarreras(nombre_carrera)
            dao.crear_carrera()
        elif opcion == 2: 
            todo = dao.mostrar_carreras()
            for nom in todo:
                print(f"Nombre de la Carrera: {nom}")
        elif opcion == 3: 
            nombre_2 = input("Introduce el nombre del cual quieres cambiar:")
            nombre_3 = input("Introduce el nombre actual:")
            carrera.setNombre(nombre_2)
            dao_2 = DAOcarreras(nombre_carrera)
            dao_2.actualizar_carrera(nombre_3)
        elif opcion == 4:
            nombre_eliminar = input("Que nombre quieres eliminar:")
            dao_2.eliminar_carrera(nombre_eliminar)
        elif opcion == 5: 
            break

menu()