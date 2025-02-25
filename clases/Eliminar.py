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
    def __init__(self, tabla, clausula= None, limite = None):
        self.tabla = tabla
        self.clausula = clausula
        self.limite = limite
    
    def analizar_semantica(self, base_datos):
        if self.tabla not in base_datos:
            raise Exception(f"Error: La tabla '{self.tabla}' no existe.")

            
    def ejecutar(self, base_datos):
        """Genera la consulta SQL en formato de texto."""
        # Llamamos la validación aquí
        self.analizar_semantica(base_datos) 
         
        sql = f"DELETE FROM {self.tabla}"
        if self.clausula:
            sql += f" WHERE {self.clausula}"
        if self.limite:
            sql += f" LIMIT {self.limite}"
        return sql 