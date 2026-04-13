import sys
import os

# Añadir el directorio padre al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from practicas.modulo.funciones import suma, resta, multiplicar, dividir
from practicas.modulo.utils import pedir_opcion, pedir_numeros


while True:
    
    opcion = pedir_opcion()

    if opcion in ["1", "2", "3", "4", "5"]:
        num1 = pedir_numeros("Ingrese el primer número: ")
        num2 = pedir_numeros("Ingrese el segundo número: ")

        if opcion == "1":
            resultado = suma(num1, num2)
            print(f"El resultado de la suma es: {resultado}")
        elif opcion == "2":
            resultado = resta(num1, num2)
            print(f"El resultado de la resta es: {resultado}")
        elif opcion == "3":
            resultado = multiplicar(num1, num2)
            print(f"El resultado de la multiplicación es: {resultado}")
        elif opcion == "4":
            resultado = dividir(num1, num2)
            print(f"El resultado de la división es: {resultado}")
        elif opcion == "5":
            print("Gracias por usar la calculadora. ¡Hasta luego!")
            break    
    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")
   