from datetime import datetime
from AnalizadorSemantico import Instruccion

class Insertar(Instruccion):
    def __init__(self, nombre_tabla, columnas, valores):
        self.nombre_tabla = nombre_tabla
        self.columnas = columnas
        self.valores = valores
            
    def __str__(self):
        return f"Insertar({self.nombre_tabla}, {self.columnas}, {self.valores})"
    
    def analizar_semantica(self, base_datos):
        # Se verifica si la tabla existe
        if self.nombre_tabla not in base_datos:
            raise Exception(f"Error semántico: la tabla '{self.nombre_tabla}' no existe.")
        # Se verifica que las columnas existan en la tabla
        for columna in self.columnas:
            if columna not in base_datos[self.nombre_tabla]["columnas"]:
                raise Exception(f"Error semántico: la columna '{columna}' no existe en la tabla '{self.nombre_tabla}'.")
        # Se verifica que el número de columnas sea igual al número de valores
        if len(self.columnas) != len(self.valores):
            raise Exception(f"Error semántico: el número de columnas y valores no coincide en la tabla '{self.nombre_tabla}'.")
        # Se verifica que no se inserten valores en columnas autoincrementales
        for col in self.columnas:
            if "AUTOINCREMENTAL" in base_datos[self.nombre_tabla]["columnas"][col]["restricciones"]:
                raise Exception(f"Error semántico: no se pueden insertar valores en columnas autoincrementales.")
        # Se validan los tipos de datos
        for valor, col in zip(self.valores, self.columnas):
            base_datos_tipo = base_datos[self.nombre_tabla]["columnas"][col]["tipo"].upper()
            if base_datos_tipo == "ENTERO":
                try:
                    int(valor)
                except:
                    raise Exception(f"Error semántico: el valor '{valor}' no es un entero.")
            elif base_datos_tipo == "FLOTANTE":
                try:
                    float(valor)
                except:
                    raise Exception(f"Error semántico: el valor '{valor}' no es un flotante.")
            elif base_datos_tipo == "BOOLEANO":
                if valor.upper() not in ["TRUE", "FALSE"]:
                    raise Exception(f"Error semántico: el valor '{valor}' no es un booleano.")
            elif base_datos_tipo == "FECHA":
                if isinstance(valor, str) and valor.startswith('"') and valor.endswith('"'):
                    valor = valor[1:-1]  # Eliminar las comillas externas
                try:
                    datetime.strptime(valor, "%Y-%m-%d")
                except:
                    raise Exception(f"Error semántico: el valor '{valor}' no es una fecha.")
                
        # Se valida el no nulo en las columnas correspondientes
        # Se valida la no repetición de llaves primarias
        # Se valida la inserción de llaves foráneas
        
        
    
    def ejecutar(self, base_datos):
        self.analizar_semantica(base_datos)
        sql = f"INSERT INTO {self.nombre_tabla} ({', '.join(self.columnas)}) VALUES ({', '.join(self.valores)})"
        return sql