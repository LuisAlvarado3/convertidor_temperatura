import os

def float_input( comentario = str() ):
    while True:
        valor = input( comentario )
        try:
            return float( valor )
        except:
            clear_window()
            print("Ingrese un valor numérico...")

def clear_window():
    os.system( 'cls' if os.name == 'nt' else 'clear' )