def mostrarmenu():
    """Imprime las opciones del menú."""
    print("CÓDIGO PRINCIPAL DE PYTHON")
    print("Digite la letra 'A' para Actualizar Sistema")
    print("Digite la letra 'E' para Eliminar Catálogo")
    print("Digite la letra 'C' para Crear Productos")
    print("Digite la letra 'S' para salir del programa")


def procesaropcion(letras):
    """
    Procesa la opción ingresada por el usuario.
    Retorna True si la opción es 'S' o 's' de lo contrario False.
    """
    letras = letras.upper() 

    if letras == 'A':
        print(" Procesando: Actualizar Sistema")
     
    elif letras == 'E':
        print(" Procesando: Eliminar Catálogo")
      
    elif letras == 'C':
        print("Procesando: Crear Productos")
       
    elif letras == 'S':
        print("Finalizó con éxito")
        return True  
    else:
        print("Sigue dentro del proceso del DO WHILE. Opción no válida. Intente de nuevo.")

    return False 
def main():
    """
    Función principal que ejecuta el bucle de menú.
    Equivalente a la estructura Do-While con 'while True'.
    """
    salir = False
    
    while True:
        mostrarmenu()
        
        
        try:
            letras = str(input("Ingrese su opción: "))
        except EOFError:
            
            print("\nError de lectura de entrada. Saliendo...")
            break
        
       
        salir = procesaropcion(letras)
        
        
        if salir:
            break
            
    print("EL DO-WHILE ha finalizado.")


if __name__ == "__main__":
    main()