from AnalizadorSemantico import Instruccion

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

class Eliminar(Instruccion):
    def __init__(self,columna, tabla, clausula= None):
    def analizar_semantica(self, base_datos):
        return super().analizar_semantica(base_datos)    