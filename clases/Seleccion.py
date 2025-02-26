from AnalizadorSemantico import Instruccion

class Seleccion(Instruccion):
    def __init__(self, columnas, tabla, condiciones=None, unir=None):
        self.columnas = columnas  # Lista de columnas a seleccionar
        self.tabla = tabla  # Nombre de la tabla
        self.condiciones = condiciones  # Condiciones opcionales
        self.unir = unir #datos del join

    def analizar_semantica(self, base_datos):
        """Verifica que la tabla y las columnas existan en la base de datos."""
        # Verificar la existencia de la tabla principal
        if self.tabla not in base_datos:
            raise Exception(f"Error: La tabla '{self.tabla}' no existe.")
        
        # Verificar las columnas en la tabla principal
        columnas_disponibles = list(base_datos[self.tabla]["columnas"].keys())
        
        if self.columnas == ["TODO"]:
            self.columnas = ["*"]
            
        for columna in self.columnas:
            if self.columnas != ["*"] and columna not in columnas_disponibles:
                raise Exception(f"Error: La columna '{self.columnas}' no existe en '{self.tabla}'.")
            
        
        # Si hay JOIN, verificamos la tabla unida y su condición
        if self.unir:
            _, tipo, tabla_unida, condicion = self.unir

            if tabla_unida not in base_datos:
                raise Exception(f"Error: La tabla '{tabla_unida}' no existe para el JOIN.")

            # Aquí podrías analizar las condiciones del JOIN también
        

    def ejecutar(self, base_datos):
        """Genera la consulta SQL en formato de texto."""
        self.analizar_semantica(base_datos)

        print(self.condiciones)
        print("Join recibido en ejecutar:", self.unir)


        # Construcción de la parte inicial del SELECT
        if self.columnas == ['*']:
            sql = f"SELECT * FROM {self.tabla}"
        else:
            sql = f"SELECT {', '.join(self.columnas)} FROM {self.tabla}"

        # Procesar JOIN si existe
        if self.unir:
            print("Debug JOIN:", self.unir)  # Verificar la estructura real de self.unir

            # Desempaquetar la estructura de self.unir directamente
            _, tipo_join, tabla_join, condicion_join = self.unir
            (col1, _, tabla1), operador, (col2, _, tabla2) = condicion_join

            # Construcción de la condición del JOIN
            condicion_sql = f"{tabla1}.{col1} {operador} {tabla2}.{col2}"
            sql = f"{tipo_join} JOIN {tabla_join} ON {condicion_sql}"

        # Agregar WHERE si hay condiciones
        if self.condiciones:
            sql = f"{sql} WHERE {self.condiciones}"

        return sql
            

