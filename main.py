from AnalizadorLexico import analizar_lexico
from AnalizadorSintactico import analizar_sintaxis
from clases.Eliminar import Eliminar
from clases.Soltar import Soltar
from clases.Crear import Crear
from clases.Seleccion import Seleccion


query = """
SELECCIONAR nombre, id DESDE empleados DONDE id = 5 UNIR departamentos CON empleados(departamento_id) = departamentos(id)
"""
#ALTERAR TABLA empleados AGREGAR casa ENTERO CLAVE PRIMARIA 
resultado_lexico = analizar_lexico(query)
print("Resultado del analisis lexico:")
for token in resultado_lexico:
    print(token)

# Base de datos simulada con restricciones y auto-incremental
base_datos = {
    "empleados": {
        "columnas": {
            "id": {"tipo": "entero", "restricciones": ["CLAVE PRIMARIA", "AUTOINCREMENTAL"]},
            "nombre": {"tipo": "texto", "restricciones": ["NO NULO"]},
            "edad": {"tipo": "entero", "restricciones": ["NO NULO"]},
            "departamento_id": {"tipo": "entero", "restricciones": ["CLAVE FORANEA", "NO NULO"]}
        },
        "llave_primaria": "id",
        "llaves_foraneas": {"departamento_id": "departamentos.id"}
    },
    "departamentos": {
        "columnas": {
            "id": {"tipo": "entero", "restricciones": ["CLAVE PRIMARIA", "AUTOINCREMENTAL"]},
            "nombre": {"tipo": "texto", "restricciones": ["NO NULO"]}
        },
        "llave_primaria": "id"
    }
}

resultado_sintactico = analizar_sintaxis(query)
print("\nResultado del analisis sintáctico:")
print(resultado_sintactico)
print(resultado_sintactico.ejecutar(base_datos))
