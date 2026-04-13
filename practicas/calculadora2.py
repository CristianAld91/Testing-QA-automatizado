while True:
    print("bienvenido a la calculadora simple")
    print("Seleccione una operación:")
    print("1. Sumar")
    print("2. Restar")  
    print("3. Multiplicar")
    print("4. Dividir") 
    print("5. Salir")
    
    option = input("Elige una opción: ")        
    
    match option:
        case '1':   
            num1 = int(input("Ingresa un número: "))
            num2 = int(input("Ingresa otro número: "))  
            result = num1 + num2
            print(f"Resultado: {result}")
        case '2':
            num1 = int(input("Ingresa un número: "))    
            num2 = int(input("Ingresa otro número: "))
            result = num1 - num2
            print(f"Resultado: {result}")
        case '3':
            num1 = int(input("Ingresa un número: "))    
            num2 = int(input("Ingresa otro número: "))
            result = num1 * num2    
            print(f"Resultado: {result}")
        case '4':
            num1 = float(input("Ingresa un número: "))    
            num2 = float(input("Ingresa otro número: "))
            if num2 != 0:
                result = num1 / num2
                print(f"Resultado: {result}")
            else:
                print("No se puede dividir por cero.")
        case '5':
            print("Saliendo del programa.") 
            print("Gracias por usar la calculadora simple. ¡Hasta luego!")
            break
    
    