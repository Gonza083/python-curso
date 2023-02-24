agenda = {}

while True:
    print("1. Añadir persona")
    print("2. Buscar teléfono")
    print("3. Salir")
    opcion = input("Selecciona una opción: ")
    
    if opcion == '1':
        nombre = input("Introduce el nombre de la persona: ")
        telefono = input("Introduce el teléfono de la persona: ")
        agenda[nombre] = telefono
        print(f"Se ha añadido a {nombre} con el teléfono {telefono}")
    elif opcion == '2':
        busqueda = input("Introduce el nombre de la persona: ")
        resultados = [nombre for nombre in agenda.keys() if nombre.startswith(busqueda)]
        if resultados:
            print("Resultados:")
            for resultado in resultados:
                print(f"{resultado} {agenda[resultado]}")
        else:
            print("No se han encontrado resultados")
    elif opcion == '3':
        break
    else:
        print("Opción no válida")

print("Fin del programa")
