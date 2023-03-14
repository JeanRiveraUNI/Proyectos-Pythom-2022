import math

numero=int(input("Digite un numero: "))
while numero<0:
    print("Error -> el numero ingresado debe ser positivo")
    numero=int(input("Digite un numero"))
print(f"\nSu raiz cuadrada es: {(math.sqrt(numero)):.2f}")
