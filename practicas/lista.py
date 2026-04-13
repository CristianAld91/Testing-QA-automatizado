listaNombres = ["Juan", "María", "Pedro", "Ana", "Luis"]    


def nombrar(nom):
    if nom in listaNombres:
        print(f"{nom} está en la lista.")
    else:
        print(f"{nom} no está en la lista.")

if __name__ == "__main__":
    nombre = input("Ingrese un nombre: ")
    nombrar(nombre)        