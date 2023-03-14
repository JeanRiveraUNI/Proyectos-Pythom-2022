import math
from statistics import median
vector=[]
print("\t .:Menu:.")
print("1: Ingresar un elemento al vector")
print("2: Calcular la media y el maximo de los vectores")
print("3: Salir")
opcion=int(input("Digite una opcion del Menu: "))
while opcion==1:
    print("Añadir un elemento al vector")
    nvector=int(input())
    for i in range(nvector):
        vector.append(i)
    print(vector)
    opcion=int(input("Digite una opcion del Menu: "))
print("...................................................")
while opcion==2:
    print("Calcular la media y el maximo del vector")
    mediana=median(vector)
    maxima=max(vector)
    print(f"La cantidad media es: {mediana}, El valor maximo es: {maxima}")
    opcion=int(input("Digite una opcion del Menu: "))
while opcion==3:
    print("Adios, vuelva pronto")
    opcion+=4




