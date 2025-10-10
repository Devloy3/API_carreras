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
            nombre = input("Inserta una carrera:")
            try:
                resp = req.post(f"http://localhost:5000/crear_carrera", data={"nombre":nombre})
                print(f"La carrera {resp["Nombre"]} ha sido creado")
            except:
                print("Ha fallado la conexion a la base de datos")
        elif opcion == 2:
            print("\n Carreras \n")
            resp = req.get("http://localhost:5000/mostrar")
            datos = resp.json()  # ja és llista de diccionaris
            for carrera in datos:
                print(f"ID: {carrera['id']}  |  Nombre: {carrera['nombre']}")
        elif opcion == 3: 
            idcarreras = input("Introduce el ID la carrera que desea cambiar:")
            nombre_3 = input("Introduce el nombre actual:")
            try: 
                respuesta = req.put(f"http://localhost:5000/modificar_carrera/{idcarreras}",data={"nuevo_nombre":nombre_3})
                print(f"Ha sido actualizado por {respuesta["Nombre"]} ")
            except:
                print("Ha habido un fallo en la base de datos")
        elif opcion == 4:
            nombre_eliminar = input("Introduce el ID que quieres eliminar:")
            try:
                respuesta = req.delete(f"http://localhost:5000/eliminar/{nombre_eliminar}")
                print(f"Se ha eliminado correctamente {respuesta["Eliminado"]}")
            except:
                print("Ha habido un fallo en la base de datos")
        elif opcion == 5:
            print("Saliendo del programa ....")
            break




menu()