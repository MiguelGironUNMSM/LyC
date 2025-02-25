from AnalizadorLexico import analizar_lexico
from AnalizadorSintactico import analizar_sintaxis
from clases.Alterar import *

query = """
ALTER TABLE alumnos ADD COLUMN edad INT;
"""

resultado_lexico = analizar_lexico(query)
print("Resultado del analisis lexico:")
for token in resultado_lexico:
    print(token)

# # Base de datos simulada        
# base_datos = BaseDatos().tablas

# resultado_sintactico = analizar_sintaxis(query)
# print("\nResultado del analisis sintactico:")
# print(resultado_sintactico.analizar_semantica(base_datos)) 
