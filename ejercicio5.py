# 1. Función para solicitar la cantidad de números a sumar
def solicitar_cantidad():
    """
    Pide al usuario la cantidad total de números que desea sumar y maneja errores.
    Retorna la cantidad como un entero.
    """
    while True:
        try:
            # Pide la cantidad al usuario
            cantidad = int(input("Digite la cantidad de números para sumar: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa. Intente de nuevo.")
                continue
            return cantidad
        except ValueError:
            # Maneja el caso en que el usuario no ingrese un número válido
            print("Entrada no válida. Por favor, ingrese un número entero positivo.")

# 2. Función para calcular la sumatoria
def calcular_sumatoria(cantidad):
    """
    Recibe la cantidad de números, los solicita en un bucle 'for'
    y calcula la sumatoria total.
    Retorna la suma total.
    """
    # Inicializamos el acumulador
    suma = 0
    
    # El bucle 'for' se ejecuta 'cantidad' veces
    for i in range(cantidad):
        while True:
            try:
                # Se pide el número actual (i+1 para mostrar 1, 2, 3...)
                prompt = f"Digite el Número {i+1}: "
                numero = int(input(prompt))
                break  # Sale del bucle interno si la entrada es válida
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")
                
        # Acumula la suma
        suma += numero
        
    return suma

# 3. Función principal que orquesta la ejecución
def main():
    """
    Función principal que ejecuta el programa de cálculo de sumatoria usando 'for'.
    """
    print("******** CÓDIGO PRINCIPAL DE PYTHON ********")
    
    # Llama a la primera función para obtener el límite del bucle
    cantidad_a_sumar = solicitar_cantidad()
    
    # Llama a la segunda función para calcular la sumatoria
    if cantidad_a_sumar > 0:
        sumatoria_total = calcular_sumatoria(cantidad_a_sumar)
        
        # Muestra el resultado final
        print(f"\nLa sumatoria total es: {sumatoria_total}")
    else:
        print("\nNo se ingresaron números para sumar. La sumatoria es 0.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
