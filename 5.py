#5.py
def nombre_mes(numero_mes):
    meses = {
        1: "enero",
        2: "febrero",
        3: "marzo",
        4: "abril"
    }
    return meses.get(numero_mes, "mes no valido")
numero = int(input("ingese el numero del mes (1-4): "))
resultado = nombre_mes(numero)
print(F"el nombre del mes es: {resultado}")