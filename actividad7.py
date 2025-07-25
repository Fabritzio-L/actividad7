def cantidad_numeros(cantidad):
    numeros = []
    for i in range(cantidad):
        num  = int(input("Ingrese un numero: "))
        numeros.append(num)
    return numeros
def cantidad_calificaciones(cantidad):
    calificaciones = []
    for i in range(cantidad):
        calificacion  = int(input("Ingrese una calificacion: "))
        calificaciones.append(calificacion)
    return calificaciones
def suma_promedio_cantidad_multiplo_3(numeros):
    suma =0
    positivos = 0
    negativos = 0
    ceros = 0
    multiplos_3 = 0
    for i in numeros:
        suma +=i
        if i % 3 == 0:
            multiplos_3 += 1
        if i < 0:
            negativos +=1
        elif i>0:
            positivos+=1
        else:
            ceros +=1
    promedio = suma/len(numeros)
    print(f"La suma de los numeros es {suma}")
    print(f"El promedio de los numeros es {promedio:.2f}")
    print(f"Hay {positivos} positivos, {negativos} negativos y hay {ceros} ceros")
    print(f"{multiplos_3} son multiplos de 3")
def area_rectangulo(base,altura):
    return base*altura
def perimetro_rectangulo(base,altura):
    return 2 * (base+altura)
def es_primo(n):
    if n <2:
        return False
    divisores=0
    for i in range(1,n+1):
        if n %i==0:
            divisores+=1
    return divisores == 2
def promedio_calificaciones(calificaciones):
    suma =0
    mayores=0
    riesgo=0
    for i in calificaciones:
        suma +=i
        if i >=85:
            mayores+=1
        else:
            riesgo +=1
    promedio = suma/len(calificaciones)
    return f"El promedio de las calificaciones es {promedio:.2f} en donde {mayores} son mayores o iguales a 85 y {riesgo} estan en zona de riesgo"
def mayor_menor_frecuencia(numeros):
    mayor = numeros[0]
    menor = numeros[0]
    for i in numeros:
        if i > mayor:
            mayor =i
        elif i < menor:
            menor = i
    vistos=[]
    repetidos =0
    for i in range(len(numeros)):
        actual = numeros[i]
        if actual not in vistos:
            frecuencia=0
            for j in range(len(numeros)):
                if numeros[j]==actual:
                    frecuencia +=1
            if frecuencia >1:
                repetidos+=1
            vistos.append(actual)
    return f"El mayor es {mayor}, el menor es {menor} y {repetidos} numeros se repiten"
def calculadora():
    while True:
        print("-"*20)
        print("Menu calculadora")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Volver al menu principal")
        print("-" * 20)
        operacion= input("Elija una de las operaciones: ")
        match operacion:
            case "1":
                a = int(input("Ingrese un numero: "))
                b = int(input("Ingrese un numero: "))
                print(a+b)
            case "2":
                a = int(input("Ingrese un numero: "))
                b = int(input("Ingrese un numero: "))
                print(a-b)
            case "3":
                a = int(input("Ingrese un numero: "))
                b = int(input("Ingrese un numero: "))
                print(a*b)
            case "4":
                a = int(input("Ingrese un numero: "))
                b = int(input("Ingrese un numero: "))
                if b==0:
                    print("Error, no se puede dividir entre 0")
                else:
                    print(a/b)
            case "5":
                print("Volviendo al menu principal")
                break
            case _:
                print("opcion invalida")
while True:
    print("-"*20)
    print("1. Operaciones con n numeros")
    print("2. Area y perimetro de un rectangulo")
    print("3. Verificar si un numero es primo")
    print("4. Calcular promedio de calificaciones")
    print("5. Encontrar mayor, menor y frecuancia de n numeros")
    print("6. Calculadora de operaciones básicas")
    print("7. Salir del programa.")
    print("-"*20)
    opcion=input("Ingrese una de las opciones: ")
    match opcion:
        case "1":
            cantidad= int(input("Ingrese la cantidad de numeros: "))
            numeros= cantidad_numeros(cantidad)
            print(suma_promedio_cantidad_multiplo_3(numeros))
        case "2":
            base= int(input("Ingrese la base del rectangulo: "))
            altura=int(input("Ingrese la altura del rectangulo: "))
            print(f"El area del rectangulo es {area_rectangulo(base,altura)}")
            print(f"El perimetro del rectangulo es {perimetro_rectangulo(base,altura)}")
        case "3":
            n=int(input("Ingrese un numero: "))
            if es_primo(n):
                print("El numero es primo")
            else:
                print("El numero no es primo")
        case "4":
            cantidad = int(input("Ingrese la cantidad de calificaciones: "))
            calificaciones =cantidad_calificaciones(cantidad)
            print(promedio_calificaciones(calificaciones))
        case "5":
            cantidad = int(input("Ingrese la cantidad de numeros: "))
            numeros = cantidad_numeros(cantidad)
            print(mayor_menor_frecuencia(numeros))
        case "6":
            calculadora()
        case "7":
            print("Saliendo del programa...")
            break
        case _:
            print("Error, ingrese una opcion valida")