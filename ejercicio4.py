# 1. Función para solicitar la cantidad de números a sumar
def solicitar_cantidad():
    """
    Pide al usuario la cantidad total de números que desea sumar.
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

# 2. Función para solicitar un número individual y actualizar la suma
def solicitar_numero_y_sumar(suma_actual, indice):
    """
    Pide un número al usuario, lo suma a la suma_actual y retorna la nueva suma.
    El 'indice' se usa para el mensaje al usuario (ej: Número 1, Número 2).
    """
    while True:
        try:
            # Pide el número actual
            prompt = f"Digite el Número {indice}: "
            numero = int(input(prompt))
            
            # Retorna la suma actualizada
            return suma_actual + numero
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

# 3. Función principal que orquesta la ejecución
def main():
    """
    Función principal que ejecuta el programa de cálculo de sumatoria usando un bucle 'for'.
    """
    print("******** CÓDIGO PRINCIPAL DE PYTHON ********")
    
    # 1. Llama a la primera función para obtener el límite del bucle 'for'
    cantidad_a_sumar = solicitar_cantidad()
    
    # Inicializa la variable acumuladora
    suma = 0
    
    # 2. Bucle 'for' para iterar el número de veces requerido
    if cantidad_a_sumar > 0:
        for i in range(cantidad_a_sumar):
            # i es el índice de 0 a cantidad-1. i+1 es el número de la iteración (1, 2, 3...)
            # Llama a la segunda función, actualizando 'suma' en cada paso
            suma = solicitar_numero_y_sumar(suma, i + 1)
        
        # 3. Muestra el resultado final
        print(f"\nLa sumatoria total es: {suma}")
    else:
        print("\nNo se ingresaron números para sumar. La sumatoria es 0.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
