from AnalizadorLexico import analizar_lexico
from AnalizadorSintactico import analizar_sintaxis
from clases.Actualizar import Actualizar
from clases.Alterar import AlterarTabla
from clases.Crear import Crear
from clases.Eliminar import Eliminar
from clases.Insertar import Insertar
from clases.Soltar import Soltar
from clases.Seleccion import Seleccion




#SELECCIONAR nombre, id DESDE empleados DONDE id = 5 UNIR COMPLETO departamentos CON empleados(departamento_id) = departamentos(id)

query = """
CREAR TABLA mascotas (
    id ENTERO CLAVE PRIMARIA AUTOINCREMENTAL,
    nombre TEXTO NO NULO ,
    dueno_id ENTERO CLAVE FORANEA REFERENCIA empleados(id), 
    departamento_id ENTERO CLAVE FORANEA REFERENCIA departamentos(id)
)"""
#ALTERAR TABLA empleados AGREGAR casa ENTERO CLAVE PRIMARIA 
resultado_lexico = analizar_lexico(query)
print("Resultado del analisis lexico:")
for token in resultado_lexico:
    print(token)

# Base de datos simulada con restricciones y auto-incremental
base_datos = {
    "empleados": {
        "columnas": {
            "id": {"tipo": "entero", "restricciones": ["CLAVE PRIMARIA"], "datos" : [1, 2, 3]},
            "nombre": {"tipo": "texto", "restricciones": ["NO NULO"], "datos" : ["Andre", "Juan", "Pedro"]},
            "edad": {"tipo": "entero", "restricciones": ["NO NULO"], "datos" : [19, 25, 30]},
            "departamento_id": {"tipo": "entero", "restricciones": ["CLAVE FORANEA", "NO NULO"], "datos" : [1, 2, 3]}
        },
        "llave_primaria": "id",
        "llaves_foraneas": {"departamento_id": "departamentos.id"}
    },
    "departamentos": {
        "columnas": {
            "id": {"tipo": "entero", "restricciones": ["CLAVE PRIMARIA", "AUTOINCREMENTAL"], "datos" : [1, 2, 3]},
            "nombre": {"tipo": "texto", "restricciones": ["NO NULO"], "datos" : ["Finanzas", "Ventas", "Recursos Humanos"]}
        },
        "llave_primaria": "id"
    }
}

resultado_sintactico = analizar_sintaxis(query)
print("\nResultado del analisis sintáctico:")
print(resultado_sintactico)

print("\nResultado del análisis semántico:")
print(resultado_sintactico.ejecutar(base_datos))
