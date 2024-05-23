# Problema 1
def divisible_por_7_y_multiplo_de_5():
    numeros = [num for num in range(1500, 2701) if num % 7 == 0 and num % 5 == 0]
    return numeros

# Problema 2
def patron():
    for i in range(1, 6):
        print("*" * i)
    for i in range(4, 0, -1):
        print("*" * i)

# Problema 3
def contar_pares_impares():
    numeros = []
    continuar = True
    while continuar:
        respuesta = input("Desea ingresar un número? (SI/NO): ")
        if respuesta.upper() == "SI":
            num = int(input("Ingrese el número: "))
            numeros.append(num)
        elif respuesta.upper() == "NO":
            continuar = False
        else:
            print("Respuesta no válida. Por favor, responda SI o NO.")
    
    pares = sum(1 for num in numeros if num % 2 == 0)
    impares = len(numeros) - pares
    print("Números ingresados:", numeros)
    print("Cantidad de números pares:", pares)
    print("Cantidad de números impares:", impares)

# Problema 4
def ingresar_calificaciones(n):
    alumnos = []
    for _ in range(n):
        nombre = input("Ingrese el nombre del alumno: ")
        notas = [int(input(f"Ingrese la nota {i+1} del alumno {nombre}: ")) for i in range(3)]
        alumno = {"Alumno": nombre, "Notas": notas}
        alumnos.append(alumno)
    return alumnos

# Problema 5
def contar_digitos(numero, digito):
    return str(numero).count(str(digito))

# Problema 6
def fibonacci():
    a, b = 0, 1
    while a <= 50:
        print(a)
        a, b = b, a + b

# Problema 7
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Problema 8
def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

# Problema 9
def omitir_vocales(cadena):
    vocales = "AEIOUaeiou"
    return ''.join(char for char in cadena if char not in vocales)

# Problema 10
def convertir_fecha(fecha):
    meses = {
        "Enero": "01", "Febrero": "02", "Marzo": "03", "Abril": "04",
        "Mayo": "05", "Junio": "06", "Julio": "07", "Agosto": "08",
        "Septiembre": "09", "Octubre": "10", "Noviembre": "11", "Diciembre": "12"
    }
    partes = fecha.split()
    if len(partes) == 3:  # Formato "mes día, año"
        mes = meses[partes[0]]
        dia = partes[1].rstrip(",")
        anio = partes[2]
    else:  # Formato "mes/día/año"
        mes, dia, anio = fecha.split("/")
    return f"{anio}-{mes}-{dia}"

# Ejemplos de uso

print("Problema 1:")
print(divisible_por_7_y_multiplo_de_5())

print("\nProblema 2:")
patron()

print("\nProblema 3:")
contar_pares_impares()

print("\nProblema 4:")
alumnos = ingresar_calificaciones(3)
print(alumnos)

print("\nProblema 5:")
print(contar_digitos(15789000, 0))

print("\nProblema 6:")
fibonacci()

print("\nProblema 7:")
print(es_primo(17))

print("\nProblema 8:")
print(factorial(5))

print("\nProblema 9:")
print(omitir_vocales("What's your name?"))

print("\nProblema 10:")
print(convertir_fecha("Septiembre 8, 1636"))
print(convertir_fecha("9/8/1636"))

git commit -m "commit"
git push

