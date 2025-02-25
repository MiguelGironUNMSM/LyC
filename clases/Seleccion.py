from AnalizadorSemantico import Instruccion

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

    def ejecutar(self, base_datos):
        """Genera la consulta SQL en formato de texto."""
        self.analizar_semantica(base_datos)
        if self.columnas == ["*"]:
            sql = f"SELECT * FROM {self.tabla}"
        else:
            sql = f"SELECT {', '.join(self.columnas)} FROM {self.tabla}"
            if self.condiciones:
                sql += f" WHERE {self.condiciones}"
            return sql
        

