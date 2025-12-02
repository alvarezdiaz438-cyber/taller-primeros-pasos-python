#desarrolar un programa que permita seleccionar por consola una opcion y se muestre una lista de opciones (menu)
def mostrar_menu():
    print("seleccione una opcion:")
    print("1. opcion 1")
    print("2. opcion 2")
    print("3. opcion 3")
    opcion = input("ingrese el numero de la opcion deseada: ")
    return opcion
opcion_seleccionada = mostrar_menu()
print(f"ha seleccionado la opcion: {opcion_seleccionada}")
    