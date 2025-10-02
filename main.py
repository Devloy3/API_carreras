from DAOcarreras import DAOcarreras

def menu():
        nombre = input("Introduce una carrera:")
        dao = DAOcarreras(nombre)
    
        while True:    
            print("<-- Menu de Carreras -->")
            print("1.Crear la carrera introducida")
            print("2.Mostrar las Carreras")
            print("3.Actualizar una carrera")
            print("4.Eliminar carreras")
            print("5.Salir")


            opcion = int(input("Introduce una opcion:"))
        
            if opcion == 1:
                 dao.crear_carrera()
            elif opcion == 2: 
                todo = dao.mostrar_carreras()
                print(todo)
            elif opcion == 3: 
                nombre_2 = input("Introduce el nombre del cual quieres cambiar:")
                nombre_3 = input("Introduce el nombre actual:")
                dao_2 = DAOcarreras(nombre_2)
                dao_2.actualizar_carrera(nombre_3)
            elif opcion == 4:
                nombre_eliminar = input("Que nombre quieres eliminar:")
                dao_2.eliminar_carrera(nombre_eliminar)
            elif opcion == 5: 
                break

menu()