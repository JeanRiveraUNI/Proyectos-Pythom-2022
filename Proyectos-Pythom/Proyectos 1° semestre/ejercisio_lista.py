print("----------MENU----------")
import math
menu=int(input("Seleccione opcion: \n 1- Area de un circulo. \n 2- Area de un triangulo equilatero. \n 3- Numeros Iguales o distintos. \n 4- Costo del producto. \n 0- Salir."))
while menu != 0:
    if menu ==1:
        print("Ingrese radio del circulo: ")
        r=float(input())
        pi=math.pi
        a=math.pi*(r*r)
        print("El area del circulo con radio de ", r , " es: ",round(a, 2))
    elif menu ==2:
        print("Ingrese valor de un lado: ")
        l=float(input())
        area=math.sqrt(3)*l*l/4
        print("El area del triangulo: ", area)
    elif menu==3:
        print("ingrese tres numeros: ")
        a=int(input("Ingrese a: "))
        b=int(input("Ingrese b: "))
        c=int(input("Ingrese c: "))
        if a+b==c:
            print("IGUALES")
        else:
            print("DISTINTOS")
    elif menu==4:
        print("Ingrese costo del producto")
        costo=float(input())
        print("Ingrese la marca del producto: ")
        m=input()
        if costo >= 2000 and m=="NOSY":
            pa=costo*0.90
            pt=pa*0.95
        elif costo >= 200 and m != "NOSY":
            pt= costo*0.90
        elif costo < 2000 and m != "NOSY" :
            pa=costo*0.95
            pt=pa+pa*0.20
        elif costo < 2000 and m != "NOSY":
            pa=costo*1.20
        print("El valor a pagar es de: $",pt,"pesos.")
    else:
        print("Escriba una opcion valida.")
    menu=int(input("Seleccione opcion: \n 1- Area de un circulo. \n 2- Area de un triangulo equilatero. \n 3- Numeros Iguales o distintos. \n 4- Costo del producto. \n 0- Salir."))
    