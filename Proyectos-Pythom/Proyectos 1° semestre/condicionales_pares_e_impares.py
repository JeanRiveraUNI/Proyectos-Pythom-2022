num1=int(input("Digite un numero: "))
num2=int(input("Digite otro numero: "))
if num1%2==0 and num2%2==0:
    print("Ambos numeros son pares")
elif num1%2==0 and num2%2!=0:
    print(f"{num1} es par")
elif num1%2!=0 and num2%2==0:
    print(f"{num2} es par")
if num1==0:
    print("El primer numero es neutro")
elif num2==0:
    print("El segundo numero es neutro")
elif num1==0 and num2==0:
    print("Ambos numeros son neutros")
else:
    print("Ambos numeros son impares")