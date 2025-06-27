def jagger_calculator():
    print("¡Bienvenido/a a Jagger Calculator!")

    # 1. Solicitar el nombre de la mascota
    nombre_mascota = input("Por favor, introduce el nombre de tu mascota: ")

    # 2. Solicitar el peso de la mascota en kilogramos
    while True:
        try:
            peso_mascota = float(input("Introduce el peso de tu mascota en kilogramos (ej. 5.5): "))
            if peso_mascota <= 0:
                print("El peso debe ser un número positivo. Inténtalo de nuevo.")
            else:
                break
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número para el peso.")

    # 3. Solicitar el tipo de Jagger Snacks
    tipo_snacks = input("Introduce el tipo de Jagger Snacks (ej. premios, galletas, etc.): ")

    # Calcular la cantidad de snacks según el peso
    cantidad_gramos = ""
    if 1 <= peso_mascota <= 5:
        cantidad_gramos = "25-40 GR"
    elif 5 < peso_mascota <= 10:
        cantidad_gramos = "40-55 GR"
    elif 10 < peso_mascota <= 20:
        cantidad_gramos = "55-70 GR"
    elif 20 < peso_mascota <= 40:
        cantidad_gramos = "70-80 GR"
    elif peso_mascota > 40:
        cantidad_gramos = "80-100 GR"
    else:
        cantidad_gramos = "No se pudo determinar la cantidad. El peso ingresado está fuera de los rangos comunes para esta tabla."

    # Expresar el resultado
    print(f"\nSu mascota {nombre_mascota} puede comer {tipo_snacks} en una cantidad de {cantidad_gramos} al día.")

# Ejecutar la calculadora
jagger_calculator()
