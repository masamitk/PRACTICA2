#PROBLEMA 1
def get_fuel_percentage():
    while True:
        try:
            fraction = input("Ingrese una fracción en el formato X/Y: ")
            x, y = map(int, fraction.split('/'))
            
            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError
            
            percentage = (x / y) * 100
            
            if percentage < 1:
                print("E")
            elif percentage > 99:
                print("F")
            else:
                print(f"{round(percentage)}%")
            break
        except ZeroDivisionError:
            print("Error: El denominador no puede ser 0. Inténtelo de nuevo.")
        except ValueError:
            print("Error: Entrada no válida. Asegúrese de que X e Y sean enteros y que X sea menor o igual a Y. Inténtelo de nuevo.")

get_fuel_percentage()



#PROBLEMA 2
def get_grades():
    grades_str = input("Ingrese las calificaciones separadas por comas: ")
    try:
        grades_list = [int(grade.strip()) for grade in grades_str.split(',')]
        print("Calificaciones:", grades_list)
    except ValueError:
        print("Error: Asegúrese de que todas las calificaciones sean números enteros. Inténtelo de nuevo.")

get_grades()


#PROBLEMA 3
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * self.radio ** 2

# Ejemplo de uso
circulo = Circulo(5)
print("Área del círculo:", circulo.calcular_area())


#PROBLEMA 4
class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def calcular_area(self):
        return self.largo * self.ancho

# Ejemplo de uso
rectangulo = Rectangulo(4, 6)
print("Área del rectángulo:", rectangulo.calcular_area())


#PROBLEMA 5
class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.nota = None
    
    def display(self):
        print(f"Nombre: {self.nombre}, Número de Registro: {self.numero_registro}, Edad: {self.edad}, Nota: {self.nota}")
    
    def set_age(self, edad):
        self.edad = edad
    
    def set_nota(self, nota):
        self.nota = nota

# Ejemplo de uso
alumno = Alumno("Juan", "12345")
alumno.set_age(20)
alumno.set_nota(95)
alumno.display()


#PROBLEMA 6
class Producto:
    def __init__(self, nombre, precio, año):
        self.nombre = nombre
        self.precio = precio
        self.año = año

class Catalogo:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def mostrar_productos(self):
        for producto in self.productos:
            print(f"Nombre: {producto.nombre}, Precio: {producto.precio}, Año: {producto.año}")
    
    def filtrar_por_año(self, año):
        return [producto for producto in self.productos if producto.año == año]
    
    def filtrar_por_precio_maximo(self, precio_max):
        return [producto for producto in self.productos if producto.precio <= precio_max]

# Ejemplo de uso
catalogo = Catalogo()
producto1 = Producto("Producto1", 100, 2020)
producto2 = Producto("Producto2", 150, 2021)
catalogo.agregar_producto(producto1)
catalogo.agregar_producto(producto2)
catalogo.mostrar_productos()

print("Filtrado por año 2021:")
for p in catalogo.filtrar_por_año(2021):
    print(p.nombre)

print("Filtrado por precio máximo 120:")
for p in catalogo.filtrar_por_precio_maximo(120):
    print(p.nombre)



#PROBLEMA 7

# modulo_numeros.py
import random

def generar_numeros():
    return [random.randint(0, 100) for _ in range(20)]

def mostrar_lista(lista):
    print("Lista:", lista)

def ordenar_lista(lista):
    return sorted(lista)

# main.py
import modulo_numeros

numeros = modulo_numeros.generar_numeros()
modulo_numeros.mostrar_lista(numeros)
numeros_ordenados = modulo_numeros.ordenar_lista(numeros)
modulo_numeros.mostrar_lista(numeros_ordenados)


#PROBLEMA 8

# modulo_numeros.py
import random

def generar_numeros():
    return [random.randint(0, 100) for _ in range(20)]

def mostrar_lista(lista):
    print("Lista:", lista)

def ordenar_lista(lista):
    return sorted(lista)

# main.py
import modulo_numeros

numeros = modulo_numeros.generar_numeros()
modulo_numeros.mostrar_lista(numeros)
numeros_ordenados = modulo_numeros.ordenar_lista(numeros)
modulo_numeros.mostrar_lista(numeros_ordenados)


#PROBLEMA 9 
def suma(a, b):
    try:
        return a + b
    except TypeError:
        return "Error: Tipo de dato no válido."

def resta(a, b):
    try:
        return a - b
    except TypeError:
        return "Error: Tipo de dato no válido."

def producto(a, b):
    try:
        return a * b
    except TypeError:
        return "Error: Tipo de dato no válido."

def division(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError
        return a / b
    except TypeError:
        return "Error: Tipo de dato no válido."
    except ZeroDivisionError:
        return "Error: No es posible dividir entre cero."

import operaciones

print(operaciones.suma(5, 3))
print(operaciones.resta(10, 5))
print(operaciones.producto(4, 7))
print(operaciones.division(20, 4))
print(operaciones.division(20, 0))
print(operaciones.suma(5, "a"))


#PROBLEMA 10

# menu.py
from problema3 import Circulo
from problema4 import Rectangulo

def menu():
    while True:
        print("\n1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            radio = float(input("Ingrese el radio del círculo: "))
            circulo = Circulo(radio)
            print("Área del círculo:", circulo.calcular_area())
        elif opcion == "2":
            largo = float(input("Ingrese el largo del rectángulo: "))
            ancho = float(input("Ingrese el ancho del rectángulo: "))
            rectangulo = Rectangulo(largo, ancho)
            print("Área del rectángulo:", rectangulo.calcular_area())
        elif opcion == "3":
            lado = float(input("Ingrese el lado del cuadrado: "))
            cuadrado = Rectangulo(lado, lado)
            print("Área del cuadrado:", cuadrado.calcular_area())
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

menu()
