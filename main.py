from DAOcarreras import DAOcarreras

def menu():
        print("Creando la conexion de base de datos:")
        host = input("Host:")
        user = input("User:")
        password = input("Password:")
        database = input("Database:")
        dao = DAOcarreras(None,host,user,password,database)
        
        while True:    
            print("\n <-- Menu de Carreras --> \n")
            print("1.Crear la carrera introducida")
            print("2.Mostrar las Carreras")
            print("3.Actualizar una carrera")
            print("4.Eliminar carreras")
            print("5.Mostrar la conexion a la base de datos")
            print("6.Cambiar la conexion de la base de datos")
            print("7.Salir \n")

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
                host_2 = dao.GetHost()
                user_2 = dao.GetUser()
                password_2 = dao.GetPassword()
                database_2 = dao.GetDatabase()
                print(f'''
                      Host: {host_2}
                      User: {user_2}
                      Password: {password_2}
                      Database: {database_2}
                    ''')
            elif opcion == 6:
                print("Introduce los datos para cambiar la base de datos")
                host_3 = input("Host:")
                user_3 = input("User:")
                password_3 = input("Password:")
                database_3= input("Database:")
                dao.setHost(host_3)
                dao.setUser(user_3)
                dao.setPassword(password_3)
                dao.setDatabase(database_3)
            elif opcion == 7:
                print("Saliendo del programa ....")
                break




menu()
