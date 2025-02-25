from AnalizadorLexico import analizar_lexico
from AnalizadorSintactico import analizar_sintaxis

query = """
ELIMINAR PRIMEROS 3 DESDE Ventas DONDE Edad > 30
"""

resultado_lexico = analizar_lexico(query)
print("Resultado del análisis léxico:")
for token in resultado_lexico:
    print(token)

resultado_sintactico = analizar_sintaxis(query)
print("\nResultado del análisis sintáctico:")
print(resultado_sintactico)



