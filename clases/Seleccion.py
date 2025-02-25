class Instruccion:
    def analizar_semantica(self, base_datos):
        raise NotImplementedError()
    
    def ejecutar(self, base_datos):
        raise NotImplementedError()

class Seleccion(Instruccion):
    def __init__(self, columnas, tabla, condiciones=None):
        self.columnas = columnas  # Lista de columnas a seleccionar
        self.tabla = tabla  # Nombre de la tabla
        self.condiciones = condiciones  # Condiciones opcionales

    def analizar_semantica(self, base_datos):
        """Verifica que la tabla y las columnas existan en la base de datos."""
        if self.tabla not in base_datos:
            raise Exception(f"Error: La tabla '{self.tabla}' no existe.")
        
        # Accedemos bien a las columnas
        columnas_disponibles = list(base_datos[self.tabla]["columnas"].keys())  
        
        for columna in self.columnas:
            if columna != "*" and columna not in columnas_disponibles:
                raise Exception(f"Error: La columna '{columna}' no existe en '{self.tabla}'.")

    def ejecutar(self):
        """Genera la consulta SQL en formato de texto."""
        sql = f"SELECT {', '.join(self.columnas)} FROM {self.tabla}"
        if self.condiciones:
            sql += f" WHERE {self.condiciones}"
        return sql
    
def analizar(query, base_datos):
    if not isinstance(query, Instruccion):
        raise Exception
    
    try:
        query.analizar_semantica(base_datos)
        sql_generado = query.ejecutar()
        print("SQL Generado:", sql_generado)  # Muestra la consulta generada
        return sql_generado  # Devuelve la consulta
    except Exception as e:
        print("Error:", e)
        return None

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

consulta = Seleccion(["nombre", "edad"], "empleados")
analizar(consulta, base_de_datos)  
