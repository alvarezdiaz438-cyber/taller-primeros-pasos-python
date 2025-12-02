#3.py
def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"
    numero = int(input("ingrese un numero: "))
    resultado = es_par_o_imopar(numero)
    print(f"el numero es: {resultado}")
    