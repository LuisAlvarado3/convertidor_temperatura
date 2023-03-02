"""
Proyecto   : Convertidor de unidades de temperatura
Autor      : José Luis Márquez Alvarado
Fecha      : Marzo, 2023 
Descripción: Escribe un programa que en un menú se puedan 
    hacer las siguientes conversiones:
    Kelvin    -> Celsius
    Kelvin    -> Farenheit
    Farenheit -> Celsius
    Farenheit -> Kelvin
    Celsius   -> Kelvin
    Celsius   -> Farenheit
"""

from src.temperatura import Temperatura
from src.io_system import clear_window

def main():
    while True:
        clear_window()
        print("""
        +-----------------------------------+
        | Conversión de unidades            |
        +-----------------------------------+
        |   1) Kelvin    -> Celsius         |
        |   2) Kelvin    -> Farenheit       |
        |   3) Farenheit -> Celsius         |
        |   4) Farenheit -> Kelvin          |
        |   5) Celsius   -> Kelvin          |
        |   6) Celsius   -> Farenheit       |
        |   7) Salir                        |
        +-----------------------------------+
        """)
        opcion = input("Ingrese una opción>> ")
        objTemp = Temperatura()
        
        if   opcion == "1": 
            objTemp.solicitar_valor( "Ingrese su cantidad en Kelvin: " )
            objTemp.kelvin_a_celsius()
        elif opcion == "2": 
            objTemp.solicitar_valor( "Ingrese su cantidad en Kelvin: " )
            objTemp.kelvin_a_farenheit()
        elif opcion == "3": 
            objTemp.solicitar_valor( "Ingrese su cantidad en Farenheit: " )
            objTemp.farenheit_a_celsius()
        elif opcion == "4": 
            objTemp.solicitar_valor( "Ingrese su cantidad en Farenheit: " )
            objTemp.farenheit_a_kelvin()
        elif opcion == "5": 
            objTemp.solicitar_valor( "Ingrese su cantidad en Celsius: " )
            objTemp.celsius_a_kelvin()
        elif opcion == "6": 
            objTemp.solicitar_valor( "Ingrese su cantidad en Celsius: " )
            objTemp.celsius_a_farenheit()
        elif opcion == "7": input("Presione enter para finalizar el programa...")
        else:
            input("Seleccione una opción valida...")
            clear_window()
            continue

        for item in ("1" ,"2" ,"3" ,"4" ,"5" ,"6"):
            if opcion == item:
                objTemp.mostrar_datos()
        
        break

main()

