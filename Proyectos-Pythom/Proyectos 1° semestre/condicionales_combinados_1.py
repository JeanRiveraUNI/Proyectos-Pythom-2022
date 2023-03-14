edad=int(input("digite su edad: "))

if edad>0 and edad<100:#ambas condiciones deben ser verdaderas.
    #tambien se puede usar la exprecion(if 0<edad<100: ),para hacer rangos de numeros.
    print("es menor de edad")
    if edad>=18:
        print("es mayor de edad")
else:
    print("edad incorrecta")
