from src.io_system import float_input, clear_window

class Temperatura:
    def __init__(self) -> None:
        self.valor = float()

        self.cantidad_inicial = {
            "tipo"   : str(),  
            "valor"  : float()
        }
        self.cantidad_final   = {
            "tipo" : str(), 
            "valor": float()
        }

        self.formula = str()


    def solicitar_valor( self, comentario ):
        self.valor = float_input( comentario )
        self.cantidad_inicial["valor"] = self.valor

    def mostrar_datos( self ):
        clear_window()
        print(f"""
        -------------------------------
        Valor Inicial: 
        {self.cantidad_inicial["tipo"]} = {self.cantidad_inicial["valor"]}
        -------------------------------
        Valor Final: 
        {self.cantidad_final["tipo"]} = {self.cantidad_final["valor"]}
        -------------------------------
        Ecuación:
        {self.formula}
        -------------------------------
        """)

    def kelvin_a_celsius( self ):
        self.cantidad_inicial[ "tipo"  ] = "Kelvin"
        celsius = self.valor - 273.15
        self.cantidad_final  [ "tipo"  ] = "Celsius"
        self.cantidad_final  [ "valor" ] = celsius
        self.formula = f"°C = {self.valor} - 273.15"

    def kelvin_a_farenheit( self ):
        self.cantidad_inicial[ "tipo"  ] = "Kelvin"
        farenheit = ( (9*(self.valor-273.15) )/ 5 ) + 32
        self.cantidad_final  [ "tipo"  ] = "Farenheit"
        self.cantidad_final  [ "valor" ] = farenheit
        self.formula = f"°F = ( (9 * ( {self.valor} - 273.15) )/ 5 ) + 32"

    def farenheit_a_celsius( self ):
        self.cantidad_inicial[ "tipo"  ] = "Farenheit"
        celsius = ( 5 * (self.valor - 32) )/9
        self.cantidad_final  [ "tipo"  ] = "Celsius"
        self.cantidad_final  [ "valor" ] = celsius
        self.formula = f" °C = ( 5 * ( {self.valor} - 32) )/9"

    def farenheit_a_kelvin( self ):
        self.cantidad_inicial[ "tipo"  ] = "Farenheit"
        kelvin = ( ( 5*( self.valor-32 ) )/9 )+273.15
        self.cantidad_final  [ "tipo"  ] = "Kelvin"
        self.cantidad_final  [ "valor" ] = kelvin
        self.formula = f" k = ( ( 5*( {self.valor} - 32 ) )/9 ) + 273.15"

    def celsius_a_kelvin( self ):
        self.cantidad_inicial[ "tipo"  ] = "Celsius"
        kelvin = self. valor + 273.15
        self.cantidad_final  [ "tipo"  ] = "Kelvin"
        self.cantidad_final  [ "valor" ] = kelvin
        self.formula = f" k = {self.valor} + 273.15"

    def celsius_a_farenheit( self ):
        self.cantidad_inicial[ "tipo"  ] = "Celsius"
        farenheit = ( ( 9*self.valor )/ 5) +32
        self.cantidad_final  [ "tipo"  ] = "Farenheit"
        self.cantidad_final  [ "valor" ] = farenheit
        self. formula = f"°F = ( ( 9 * {self.valor} )/ 5) +32"
