#1.py
def identificar_numero(numero):
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "neutro"
    numero = float(input("ingrese un numero: "))
    resultado = identificar_numero(numero)
    print(f"el numero es: {resultado}")