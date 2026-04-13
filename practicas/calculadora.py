while True:
    print("\nMenu:")
    print("*************Bienvenido a la calculadora simple**************")
    print("Seleccione una operación:")
    print("1. Sumar:")
    print("2. Restar:")
    print("3. Multiplicar:")
    print("4. Dividir:")
    print("5. Exit")
    
    option = input("Elege una opción: ")
    
    if option == '1':
        num1 = int(input("Ingresa un número: "))
        num2 = int(input("Ingresa otro número: "))  
        result = num1 + num2
        print(f"Resultado: {result}")
        
    elif option == '2':
        num1 = int(input("Ingresa un número: "))
        num2 = int(input("Ingresa otro número: "))
        result = num1 - num2
        print(f"Resultado: {result}")       
    elif option == '3':
        num1 = int(input("Ingresa un número: "))
        num2 = int(input("Ingresa otro número: "))
        result = num1 * num2
        print(f"Resultado: {result}")       
        
    elif option == '4':
        num1 = float(input("Ingresa un número: "))
        num2 = float(input("Ingresa otro número: "))
        if num2 != 0:
            result = num1 / num2
            print(f"Resultado: {result}")
        else:
            print("No se puede dividir por cero.")  
    elif option == '5':
        print("Saliendo del programa.")
        print("Gracias por usar la calculadora simple. ¡Hasta luego!")
        break