def cantidad_numeros(cantidad):
    numeros = []
    for i in range(cantidad):
        num  = int(input("Ingrese un numero: "))
        numeros.append(num)
    return numeros
def suma_promedio_cantidad_multiplo_3(numeros):
    suma =0
    for i in numeros:
        suma +=i
    promedio = suma/len(numeros)
    positivos=0
    negativos=0
    ceros=0
    multiplos_3=0
    for i in numeros:
        if i < 0:
            negativos +=1
        elif i>0:
            positivos+=1
        else:
            ceros +=1
    for i in numeros:
        if i %3==0:
            multiplos_3+=1
    print(f"La suma de los numeros es {suma}")
    print(f"El promedio de los numeros es {promedio:.2f}")
    print(f"Hay {positivos} positivos, {negativos} negativos y hay {ceros} ceros")
    print(f"{multiplos_3} son multiplos de 3")
while True:
    print("1. Operaciones con n numeros")
    print("2. Area y perimetro de un rectangulo")
    print("3. Verificar si un numero es primo")
    print("4. Calcular promedio de calificaciones")
    print("5. Encontrar mayor, menor y frecuancia de n numeros")
    print("5. Calculadora de operaciones básicas")
    print("6. Salir del programa.")
    opcion=input("Ingrese una de las opciones: ")
    match opcion:
        case "1":
            cantidad= int(input("Ingrese la cantidad de numeros: "))
            numeros= cantidad_numeros(cantidad)
            print(suma_promedio_cantidad_multiplo_3(numeros))
