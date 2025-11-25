def positivo(num):
    """Retorna si el número es mayor que cero."""
    return num > 0


def negativo(num):
    """Retorna si el número es menor que cero."""
    return num < 0


def neutro(num):
    """Retorna si el número es igual a cero."""
    return num == 0


def identificarsigno():
    """
    Solicita un número al usua y determina si es positivo,
    negativo o neutro usando las tres funciones.
    """
    try:
       
        entrad = input("ingresa un numero: ")
        num = float(entrad)
        if positivo(num):
            print(f"El número {num} es **positivo** **⬆️**.")
        elif negativo(num):
            print(f"El número {num} es **negativo** **⬇️**.")
        elif neutro(num):
            print(f"El número {num} es **neutro** (Cero) **0️⃣**.")
        
    except ValueError:
        print("Error introduce un número real.")


if __name__ == "__main__":
    identificarsigno()