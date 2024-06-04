#problema 1
import requests

def obtener_precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        precio_usd = data['bpi']['USD']['rate_float']
        return precio_usd
    except requests.RequestException as e:
        print("Error al consultar el precio de Bitcoin:", e)
        return None

def main():
    try:
        n = float(input("Ingrese la cantidad de Bitcoins que posee: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return
    
    precio_usd = obtener_precio_bitcoin()
    if precio_usd is not None:
        costo_total = n * precio_usd
        print(f"El costo actual de {n} Bitcoins en USD es: ${costo_total:,.4f}")

if __name__ == "__main__":
    main()


#problema 2
from pyfiglet import Figlet
import random

def main():
    figlet = Figlet()
    fuentes = figlet.getFonts()

    fuente = input("Ingrese el nombre de una fuente (o presione Enter para una fuente aleatoria): ")
    if not fuente or fuente not in fuentes:
        fuente = random.choice(fuentes)
        print(f"Fuente seleccionada aleatoriamente: {fuente}")
    
    texto = input("Ingrese el texto a mostrar: ")
    figlet.setFont(font=fuente)
    print(figlet.renderText(texto))

if __name__ == "__main__":
    main()


#problema 3

import requests
import zipfile
import os

def descargar_imagen(url, nombre_archivo):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(nombre_archivo, 'wb') as file:
            file.write(response.content)
        print(f"Imagen descargada y guardada como {nombre_archivo}")
    except requests.RequestException as e:
        print("Error al descargar la imagen:", e)

def comprimir_imagen(nombre_archivo, archivo_zip):
    try:
        with zipfile.ZipFile(archivo_zip, 'w') as zipf:
            zipf.write(nombre_archivo, os.path.basename(nombre_archivo))
        print(f"Imagen comprimida en el archivo {archivo_zip}")
    except Exception as e:
        print("Error al comprimir la imagen:", e)

def descomprimir_imagen(archivo_zip):
    try:
        with zipfile.ZipFile(archivo_zip, 'r') as zipf:
            zipf.extractall()
        print(f"Imagen descomprimida del archivo {archivo_zip}")
    except Exception as e:
        print("Error al descomprimir la imagen:", e)

def main():
    url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    nombre_archivo = "imagen.jpg"
    archivo_zip = "imagen.zip"
    
    descargar_imagen(url, nombre_archivo)
    comprimir_imagen(nombre_archivo, archivo_zip)
    descomprimir_imagen(archivo_zip)

if __name__ == "__main__":
    main()



#problema 4

import requests

def obtener_precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        print("Error al consultar el precio de Bitcoin:", e)
        return None

def guardar_precio_bitcoin(data):
    if data:
        with open("precio_bitcoin.txt", "w") as file:
            file.write(f"USD: {data['bpi']['USD']['rate_float']}\n")
            file.write(f"GBP: {data['bpi']['GBP']['rate_float']}\n")
            file.write(f"EUR: {data['bpi']['EUR']['rate_float']}\n")
        print("Datos de precio de Bitcoin guardados en precio_bitcoin.txt")
    else:
        print("No se pudo obtener los datos para guardar.")

def main():
    data = obtener_precio_bitcoin()
    guardar_precio_bitcoin(data)

if __name__ == "__main__":
    main()

#problema 5

import os

def guardar_tabla_multiplicar(n):
    with open(f"tabla-{n}.txt", "w") as file:
        for i in range(1, 11):
            file.write(f"{n} x {i} = {n*i}\n")
    print(f"Tabla de multiplicar del {n} guardada en tabla-{n}.txt")

def leer_tabla_multiplicar(n):
    try:
        with open(f"tabla-{n}.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print(f"El archivo tabla-{n}.txt no existe.")

def leer_linea_tabla_multiplicar(n, m):
    try:
        with open(f"tabla-{n}.txt", "r") as file:
            lineas = file.readlines()
            if 1 <= m <= 10:
                print(lineas[m-1].strip())
            else:
                print("Número de línea fuera de rango (debe ser entre 1 y 10).")
    except FileNotFoundError:
        print(f"El archivo tabla-{n}.txt no existe.")

def main():
    while True:
        print("\nMenú:")
        print("1. Guardar tabla de multiplicar")
        print("2. Leer tabla de multiplicar")
        print("3. Leer línea de la tabla de multiplicar")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                n = int(input("Ingrese un número entero entre 1 y 10: "))
                if 1 <= n <= 10:
                    guardar_tabla_multiplicar(n)
                else:
                    print("El número debe estar entre 1 y 10.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        elif opcion == "2":
            try:
                n = int(input("Ingrese un número entero entre 1 y 10: "))
                if 1 <= n <= 10:
                    leer_tabla_multiplicar(n)
                else:
                    print("El número debe estar entre 1 y 10.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        elif opcion == "3":
            try:
                n = int(input("Ingrese un número entero entre 1 y 10: "))
                m = int(input("Ingrese el número de línea a leer (1-10): "))
                if 1 <= n <= 10:
                    leer_linea_tabla_multiplicar(n, m)
                else:
                    print("El número debe estar entre 1 y 10.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        elif opcion == "4":
            break
        
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()


#problema 6

def contar_lineas_codigo(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as file:
            lineas = file.readlines()
        
        lineas_codigo = [linea for linea in lineas if linea.strip() and not linea.strip().startswith('#')]
        return len(lineas_codigo)
    except FileNotFoundError:
        print("El archivo no existe.")
        return None
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

def main():
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")
    if not ruta_archivo.endswith(".py"):
        print("El archivo debe tener la extensión .py")
        return
    
    num_lineas = contar_lineas_codigo(ruta_archivo)
    if num_lineas is not None:
        print(f"El archivo {ruta_archivo} tiene {num_lineas} líneas de código.")

if __name__ == "__main__":
    main()
    
    
#problema 7
import sqlite3
import requests
from datetime import datetime

def obtener_tipo_cambio():
    try:
        response = requests.get("https://api.apis.net.pe/v1/tipo-cambio-sunat?fecha=2023-12-31")
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        print("Error al consultar el tipo de cambio:", e)
        return None

def almacenar_tipo_cambio(data):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sunat_info (
            fecha TEXT,
            compra REAL,
            venta REAL
        )
    ''')

    fecha = data['fecha']
    compra = data['compra']
    venta = data['venta']

    cursor.execute('''
        INSERT INTO sunat_info (fecha, compra, venta) VALUES (?, ?, ?)
    ''', (fecha, compra, venta))

    conn.commit()
    conn.close()

def mostrar_contenido_tabla():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM sunat_info')
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)

    conn.close()

def main():
    data = obtener_tipo_cambio()
    if data:
        almacenar_tipo_cambio(data)
        mostrar_contenido_tabla()

if __name__ == "__main__":
    main()



#problema 8
import sqlite3
import requests
from datetime import datetime

def obtener_precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        print("Error al consultar el precio de Bitcoin:", e)
        return None

def obtener_tipo_cambio():
    try:
        response = requests.get("https://api.apis.net.pe/v1/tipo-cambio-sunat?fecha=2023-12-31")
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        print("Error al consultar el tipo de cambio:", e)
        return None

def almacenar_precio_bitcoin(data_bitcoin, data_cambio):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bitcoin (
            fecha TEXT,
            usd REAL,
            gbp REAL,
            eur REAL,
            pen REAL
        )
    ''')

    fecha = datetime.now().strftime('%Y-%m-%d')
    precio_usd = data_bitcoin['bpi']['USD']['rate_float']
    precio_gbp = data_bitcoin['bpi']['GBP']['rate_float']
    precio_eur = data_bitcoin['bpi']['EUR']['rate_float']
    precio_pen = precio_usd * data_cambio['venta']

    cursor.execute('''
        INSERT INTO bitcoin (fecha, usd, gbp, eur, pen) VALUES (?, ?, ?, ?, ?)
    ''', (fecha, precio_usd, precio_gbp, precio_eur, precio_pen))

    conn.commit()
    conn.close()

def mostrar_precio_10_bitcoins():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT usd, eur, pen FROM bitcoin ORDER BY fecha DESC LIMIT 1')
    row = cursor.fetchone()
    
    if row:
        usd, eur, pen = row
        print(f"Precio de compra de 10 Bitcoins en EUR: {10 * eur:,.4f}")
        print(f"Precio de compra de 10 Bitcoins en PEN: {10 * pen:,.4f}")

    conn.close()

def main():
    data_bitcoin = obtener_precio_bitcoin()
    data_cambio = obtener_tipo_cambio()
    if data_bitcoin and data_cambio:
        almacenar_precio_bitcoin(data_bitcoin, data_cambio)
        mostrar_precio_10_bitcoins()

if __name__ == "__main__":
    main()
