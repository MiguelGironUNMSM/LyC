from AnalizadorLexico import analizar_lexico
from AnalizadorSintactico import analizar_sintaxis
from clases.Eliminar import Eliminar
from clases.Soltar import Soltar
from clases.Seleccion import Seleccion

query = """
CREAR TABLA mascotas (
    id ENTERO CLAVE_PRIMARIA ,
    nombre TEXTO,
    dueno_id ENTERO CLAVE_FORANEA REFERENCIA duenos(id) 
)
"""

resultado_lexico = analizar_lexico(query)
print("Resultado del analisis lexico:")
for token in resultado_lexico:
    print(token)

# Base de datos simulada        
base_datos = {
    "empleados": {
        "columnas": {"id": "entero", "nombre": "texto", "edad": "INT" },
        "llave_primaria": "id",
        "llaves_foraneas": {"departamento_id": "departamentos.id"}
    },
    "departamentos": {
        "columnas": {"id": "entero", "nombre": "texto"},
        "llave_primaria": "id"
    }
}

resultado_sintactico = analizar_sintaxis(query)
print("\nResultado del analisis sintáctico:")
print(resultado_sintactico)
