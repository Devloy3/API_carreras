import requests as req

def menu():
    while True:    
        print("\n <-- Menu de Carreras --> \n")
        print("1.Crear una carrera")
        print("2.Mostrar las Carreras")
        print("3.Actualizar una carrera")
        print("4.Eliminar carreras")
        print("5.Salir \n")

        opcion = int(input("Introduce una opcion:"))
        
        if opcion == 1:
            nombre = input("Insertar la carrera que quieras insertar:")
            try: 
                req.post("http://localhost:5000/crear_carrera", nombre=nombre)
                print("Los datos se han guardado perfectamente")
            except:
                print("Ha habido un fallo en la conexion con la base de datos")
        elif opcion == 2:
            print("\n Carreras \n")
            resp = req.get("http://localhost:5000/mostrar")
            print(resp.text)
        elif opcion == 3: 
            nombre_2 = input("Introduce el nombre del cual quieres cambiar:")
            nombre_3 = input("Introduce el nombre actual:")
            try: 
                req.put(f"http://localhost:5000/{nombre_2}",nuevo_nombre=nombre_3)
                print("Carrera actualizada")
            except:
                print("Ha habido un fallo en la base de datos")
        elif opcion == 4:
                nombre_eliminar = input("Que nombre quieres eliminar:")
        elif opcion == 5:
            print("Saliendo del programa ....")
            break




menu()
