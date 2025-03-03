from AnalizadorSemantico import Instruccion

class Eliminar(Instruccion):
    def __init__(self, tabla, clausula= None, limite = None):
        self.tabla = tabla
        self.clausula = clausula
        self.limite = limite

    def __str__(self):
        return f"Eliminar({self.tabla}, {self.clausula}, {self.limite})"
    
    def analizar_semantica(self, base_datos):
        if self.tabla not in base_datos:
            raise Exception(f"Error: La tabla '{self.tabla}' no existe.")
        if self.clausula:
            # Separar la cláusula en campo y valor
            try:
                columna, valor = self.clausula.replace(" ", "").split("=")
            except ValueError:
                raise Exception("Error: La cláusula WHERE debe tener formato 'columna = valor'.")

            # Verificar si la columna existe en la tabla
            if columna not in base_datos[self.tabla]["columnas"]:
                raise Exception(f"Error: La columna '{columna}' no existe en la tabla '{self.tabla}'.")

            # Convertir el valor al tipo adecuado
            tipo_columna = base_datos[self.tabla]["columnas"][columna]["tipo"]
            if tipo_columna == "entero":
                try:
                    valor = int(valor)
                except ValueError:
                    raise Exception(f"Error: El valor '{valor}' no es un número válido para la columna '{columna}'.")

            # Verificar si el valor existe en la columna
            valores_columna = base_datos[self.tabla]["columnas"][columna]["datos"]
            if valor not in valores_columna:
                raise Exception(f"Error: No existe un registro con '{columna} = {valor}' en la tabla '{self.tabla}'.")

            
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