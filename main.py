import requests as req

def menu():
    while True:    
        print("\n <-- Menú de Carreras --> \n")
        print("1.Crear carrera")
        print("2.Mostrar carreras")
        print("3.Actualizar carrera")
        print("4.Eliminar carrera")
        print("5.Salir \n")

        opcion = int(input("Introduzca una opción:"))
        
        if opcion == 1:
            nombre = input("Inserte una carrera:")
            try:
                resp = req.post(f"http://localhost:5000/crear_carrera", data={"nombre":nombre})
                print(resp.text)
            except:
                print("Ha habido un fallo con la base de datos")
        elif opcion == 2:
            print("\n Carreras \n")
            resp = req.get("http://localhost:5000/mostrar")
            datos = resp.json()  
            for carrera in datos:
                print(f"ID: {carrera['id']}  |  Nombre: {carrera['nombre']}")
        elif opcion == 3: 
            idcarreras = input("Introduzca el ID la carrera que desea cambiar:")
            nombre_3 = input("Introduzca el nombre actual:")
            try: 
                req.put(f"http://localhost:5000/modificar_carrera/{idcarreras}",data={"nuevo_nombre":nombre_3})
                print("Carrera actualizada")
            except:
                print("Ha habido un fallo con la base de datos")
        elif opcion == 4:
            nombre_eliminar = input("Introduzca el ID de la carrera que quiera eliminar:")
            try:
                respuesta = req.delete(f"http://localhost:5000/eliminar/{nombre_eliminar}")
                print(respuesta.text)
            except:
                print("Ha habido un fallo con la base de datos")
        elif opcion == 5:
            print("Saliendo del programa ....")
            break




menu()