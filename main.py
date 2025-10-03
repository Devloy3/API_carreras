from DAOcarreras import DAOcarreras

def menu():
        dao = DAOcarreras(None)

        while True:    
            print("\n <-- Menu de Carreras --> \n")
            print("1.Crear la carrera introducida")
            print("2.Mostrar las Carreras")
            print("3.Actualizar una carrera")
            print("4.Eliminar carreras")
            print("5.Salir \n")

            opcion = int(input("Introduce una opcion:"))
        
            if opcion == 1:
                nombre = input("Insertar la carrera que quieras insertar:")
                dao.crear_carrera(nombre)
            elif opcion == 2:
                carreras = dao.mostrar_carreras()
                print("\n Carreras \n")
                for carrera in carreras:
                    print(f"Carrera:  {carrera[0]}")
            elif opcion == 3: 
                nombre_2 = input("Introduce el nombre del cual quieres cambiar:")
                nombre_3 = input("Introduce el nombre actual:")
                dao.actualizar_carrera(nombre_3,nombre_2)
            elif opcion == 4:
                nombre_eliminar = input("Que nombre quieres eliminar:")
                dao.eliminar_carrera(nombre_eliminar)
            elif opcion == 5: 
                break

menu()
