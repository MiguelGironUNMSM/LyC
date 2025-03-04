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

        tabla = base_datos[self.nombre_tabla]
        clave_primaria = tabla.get("llave_primaria", None)

        for columna in self.columnas:
            if columna not in tabla["columnas"]:
                raise Exception(f"Error semántico: la columna '{columna}' no existe en la tabla '{self.nombre_tabla}'.")

        # **Manejo de múltiples filas**
        if isinstance(self.valores[0], list):  # Si es una lista de listas (varias filas)
            filas = self.valores
        else:
            filas = [self.valores]  # Si es una sola fila, la convertimos en una lista de listas

        for fila in filas:
            # Se verifica que el número de columnas sea igual al número de valores en cada fila
            if len(self.columnas) != len(fila):
                raise Exception(f"Error semántico: el número de columnas y valores no coincide en la tabla '{self.nombre_tabla}'.")

            for valor, col in zip(fila, self.columnas):
                restricciones = tabla["columnas"][col].get("restricciones", [])
                base_datos_tipo = tabla["columnas"][col]["tipo"].upper()

                es_nulo = (isinstance(valor, str) and valor.upper() == "NULO")

                # Validaciones de tipo de datos
                if not es_nulo:
                    if base_datos_tipo == "ENTERO":
                        try:
                            valor_convertido = int(valor)
                        except:
                            raise Exception(f"Error semántico: el valor '{valor}' no es un entero.")
                    elif base_datos_tipo == "FLOTANTE":
                        try:
                            valor_convertido = float(valor)
                        except:
                            raise Exception(f"Error semántico: el valor '{valor}' no es un flotante.")
                    else:
                        valor_convertido = valor  # Para otros tipos, se usa el valor original

                    # Validación de clave primaria (evitar duplicados)
                    if clave_primaria and col == clave_primaria:
                        if valor_convertido in tabla["columnas"][col]["datos"]:
                            raise Exception(f"Error semántico: El valor '{valor}' ya existe como clave primaria en '{col}'.")

                    # Validación de clave primaria: evitar duplicados
                    if clave_primaria and col == clave_primaria:
                        # Se compara el valor convertido (asegúrate que en la base de datos se almacenan del mismo tipo)
                        if valor_convertido in tabla["columnas"][col]["datos"]:
                            raise Exception(f"Error semántico: El valor '{valor}' ya existe como clave primaria en '{col}'.")

                    # Validación de clave foránea:
                    # Se asume que la columna es clave foránea si aparece en el diccionario "llaves_foraneas"
                    if col in tabla.get("llaves_foraneas", {}):
                        # Obtener la referencia: formato "tabla_ref.columna_ref"
                        ref = tabla["llaves_foraneas"][col]
                        tabla_ref, col_ref = ref.split(".")
                        # Verificar que el valor convertido exista en la columna referenciada de la tabla foránea
                        if valor_convertido not in base_datos[tabla_ref]["columnas"][col_ref]["datos"]:
                            raise Exception(
                                f"Error semántico: El valor '{valor_convertido}' en la columna '{col}' "
                                f"no existe en '{tabla_ref}.{col_ref}' (clave foránea)."
                            )
            # Se valida el no nulo en las columnas correspondientes
            # Se valida la no repetición de llaves primarias
            # Se valida la inserción de llaves foráneas
        
    def ejecutar(self, base_datos):
        self.analizar_semantica(base_datos)
        # Verificar si es una lista de listas (varias filas) o una sola fila
        if isinstance(self.valores[0], list):  # Múltiples filas
            filas = self.valores
        else:  # Una sola fila
            filas = [self.valores]  # Convertir en lista de listas

        sql = f"INSERT INTO {self.nombre_tabla} ({', '.join(self.columnas)}) VALUES "

        # Crear una lista de valores formateados para la consulta
        valores_sql = [f"({', '.join(fila)})" for fila in filas]

        # Unir todas las filas con ", " y completar la consulta SQL
        sql += ", ".join(valores_sql)

        return sql