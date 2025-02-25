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
        
        columnas_disponibles = list(base_datos[self.tabla]["columnas"].keys())
        
        if self.columnas == ["TODO"]:
            self.columnas = ["*"]
            
        for columna in self.columnas:
            if self.columnas != ["*"] and columna not in columnas_disponibles:
                raise Exception(f"Error: La columna '{self.columnas}' no existe en '{self.tabla}'.")

    def ejecutar(self, base_datos):
        """Genera la consulta SQL en formato de texto."""
        self.analizar_semantica(base_datos)
        print(self.condiciones)
        if self.columnas == ['*']:
            sql = f"SELECT * FROM {self.tabla}"
            print(self.condiciones)
            if self.condiciones:
                sql += f" WHERE {self.condiciones}"
            return sql
        else:
            sql = f"SELECT {', '.join(self.columnas)} FROM {self.tabla}"
            if self.condiciones:
                sql += f" WHERE {self.condiciones}"
            return sql
        

