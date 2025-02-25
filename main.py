from AnalizadorLexico import analizar_lexico
from AnalizadorSintactico import analizar_sintaxis

query = """
SELECCIONAR nombre , apellido DESDE Usuarios
"""

resultado_lexico = analizar_lexico(query)
print("Resultado del analisis lexico:")
for token in resultado_lexico:
    print(token)

resultado_sintactico = analizar_sintaxis(query)
print("\nResultado del analisis sintactico:")
print(resultado_sintactico)

# Base de datos simulada        
base_de_datos = {
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

