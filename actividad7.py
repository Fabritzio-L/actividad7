def cantidad_numeros(n):
    numeros = []
    for i in range(n):
        num  = int(input("Ingrese un numero: "))
        numeros.append(num)
    return numeros
while True:
    print("1. Operaciones con n numeros")
    print("2. Area y perimetro de un rectangulo")
    print("3. Verificar si un numero es primo")
    print("4. Calcular promedio de calificaciones")
    print("5. Encontrar mayor, menor y frecuancia de n numeros")
    print("5. Calculadora de operaciones básicas")
    print("6. Salir del programa.")