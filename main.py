from AnalizadorLexico import analizar_lexico
from AnalizadorSintactico import analizar_sintaxis
from clases.Eliminar import Eliminar

query = """
ELIMINAR DESDE empleados 
"""

resultado_lexico = analizar_lexico(query)
print("Resultado del analisis lexico:")
for token in resultado_lexico:
    print(token)

# Base de datos simulada        
base_datos = {
    "empleados": {
        "columnas": {"id": "INT", "nombre": "VARCHAR", "edad": "INT" },
        "llave_primaria": "id",
        "llaves_foraneas": {"departamento_id": "departamentos.id"}
    },
    "departamentos": {
        "columnas": {"id": "INT", "nombre": "VARCHAR"},
        "llave_primaria": "id"
    }
}

resultado_sintactico = analizar_sintaxis(query)
print("\nResultado del analisis sintactico:")
print(resultado_sintactico.ejecutar(base_datos)) 
