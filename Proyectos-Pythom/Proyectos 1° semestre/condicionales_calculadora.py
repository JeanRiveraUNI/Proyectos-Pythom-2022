from __future__ import division

print(" Bienvendo ")
print(" Calculadora de operaciones basica ")
print(" Suma: S ; Resta: R ; Multiplicacion: M ; Divicion: D ")
num1=float(input("Ingrese el Primer numero: "))
num2=float(input("Ingrese el segundo numero: "))
operacion=input("Digite la operacion a realizar: ").upper()
if operacion=='S':
    suma=num1+num2
    print(f"\nLa suma es: {suma}")
elif operacion=='R':
    resta=num1-num2
    print(f"\nLa resta es: {resta}")
elif operacion=='M':
    multiplicacion=num1+num2
    print(f"\nLa multiplicacion es: {multiplicacion}")
elif operacion=='D':
    division=num1/num2
    print(f"\nLa divicion es: {division:.2f}")
else:
    print("\nOpreracion no valida")
