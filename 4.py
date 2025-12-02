#4.py
def calcular_acumulado(cantidad):
    acumulado = 0
    for i in range(cantidad):
        numero = float(input(f"ingrese el numero {i+1}: "))
        acumulado += numero
        return acumulado
    cantidad = int(input("ingrese la cantidad de numeros que va a digitar: "))
    resultado = calcular_acumulado(cantidad)
    print(f"el acumulado de los numeros ingresados es: {resultado}")