def pedir_opcion():
    print("\nCalculadora:")
    print("\nSeleccione la operación que desea realizar:")
    print("suma: ingrese 1")
    print("resta: ingrese 2")
    print("multiplicación: ingrese 3")
    print("división: ingrese 4")

    opcion = input("Ingrese la opción: \n")

    opcion_valida = {
        "1": "suma", 
        "2": "resta", 
        "3": "multiplicación", 
        "4": "división"
    }

    try:
        opcion_valida[opcion]
    except KeyError:
        print("Opción no válida. Por favor, ingrese una opción válida.")
    return opcion


def pedir_numeros(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Entrada no válida. Por favor, ingrese números válidos.")
            