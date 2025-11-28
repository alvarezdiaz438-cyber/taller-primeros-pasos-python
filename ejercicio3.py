# 1. Función para solicitar y retornar el número del usuario
def solicitar_numero():
    """
    Pide al usuario que digite un número y lo retorna como entero.
    Maneja posibles errores de entrada (como ingresar texto).
    """
    while True:
        try:
            # Pide el número al usuario
            numero = int(input("Digite un número (0 para finalizar): "))
            return numero
        except ValueError:
            # Maneja el caso en que el usuario no ingrese un número válido
            print("Entrada no válida. Por favor, ingrese un valor numérico.")

# 2. Función para verificar la paridad del número
def verificar_paridad(num):
    """
    Determina si el número dado es par o impar (asumiendo que num != 0).
    """
    # Si el residuo de la división por 2 es 0, es par.
    if num % 2 == 0:
        print(f"El número {num} es PAR.")
    else:
        print(f"El número {num} es IMPAR.")

# 3. Función principal que contiene el bucle 'while'
def main():
    """
    Función principal que ejecuta el programa.
    Contiene el bucle 'while' que se ejecuta mientras el número sea diferente de cero.
    """
    # Inicializa la variable de control (el valor inicial es irrelevante,
    # siempre que no sea 0 para entrar al bucle)
    num = 1
    
    print("******** CÓDIGO PRINCIPAL DE PYTHON ********")

    # El bucle se ejecuta mientras num sea diferente de 0
    while num != 0:
        # Llama a la primera función para obtener el número
        num = solicitar_numero()
        
        # Si el número ingresado no es 0, verifica su paridad
        if num != 0:
            # Llama a la segunda función para verificar y mostrar la paridad
            verificar_paridad(num)
        
    print("\nFinalizó el programa.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
