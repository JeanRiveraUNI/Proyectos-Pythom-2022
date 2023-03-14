print(" Bienvenido ")
num1=int(input("Ingrese el Primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
num3=int(input("Ingrese el Trecer numero: "))
if num1>num2 and num1>num3:
    print(f"El primer numero es mayor")
elif num2>num1 and num2>num3:
    print(f"El segundo numero es mayor")
elif num3>num1 and num3>num2:
    print(f"El tercer numero es mayor ")
else:
    print(f"Todos los numero son neutros")
