while True:
    print("")
    print("1. 📃 Contador de vocales \n")
    print("2. 📒 Verificar si empieza con a\n")
    print("3. 🔐 Verificar contraseña\n")
    print("4. Salir\n")

    try:
        opcion = int(input("Elegir una opción: "))
        print("")
    except ValueError:
        print("")
        print("Ingresá un número válido.\n")
        continue

    if opcion == 1:
        try:
            palabra1 = input("Ingresar una palabra: ")
            vocal = "aeiouáéíóú"
            contador = 0

            for letra in palabra1.lower(): # Convierte las letras mayusculas en minuscula
                if letra in vocal:
                    contador += 1
            print("")
            print(f"Tiene {contador} vocal(es).\n")
        except ValueError:
            print("")
            print("#Error. Solo se puede operar con palabras")

    elif opcion == 2:
        palabra = input("Ingresar una palabra: ")

        if palabra.startswith("a"): # Consulta si la palabra ingresada empieza con "a"
            print("")
            print("empieza con a\n")
        else:
            print("")
            print("No empieza con a\n")

    elif opcion == 3:
        contraseña_correcta = "python123"

        for intento in range(3):
            contraseña = input("Ingresar contraseña: ")
            if contraseña == "python123":
                print("")
                print("🔓 Acceso concedido\n")
                break
            else:
                print("")
                print("🔒 contraseña incorrecta\n")
        else:
            print("")
            print("Demasiados intentos\n")

    elif opcion == 4:
        print("¡Adios!\n")
        break
    else:
        print("")
        print("Opción no válida. Elegí del 1 al 4.\n")
