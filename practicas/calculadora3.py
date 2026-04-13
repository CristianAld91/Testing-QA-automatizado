import practicas.modulo.funciones as funciones

def calculadora(a, b):
    print("Calculadora:")
    print("suma: ingrese 1")
    print("resta: ingrese 2")
    print("multiplicación: ingrese 3")
    print("división: ingrese 4")

    opcion = input("Ingrese la opción: ")
    num1 = float(input("Ingrese el primer número: "))
    a = num1
    num2 = float(input("Ingrese el segundo número: "))
    b = num2
    resultado = 0
    try:
        if opcion == "1":
            resultado = funciones.suma(a, b)
        elif opcion == "2":
            resultado = funciones.resta(a, b)
        elif opcion == "3":
            resultado = funciones.multiplicar(a, b)
        elif opcion == "4":
            resultado = funciones.dividir(a, b)
        else:
            print("Opción no válida")
        print("El resultado es: ", resultado)
    except ValueError:
        print("Error: Entrada no válida. Por favor, ingrese números válidos.")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    finally:
        print("Gracias por usar la calculadora.")   
if __name__ == "__main__":
    calculadora(0, 0)
    

    

