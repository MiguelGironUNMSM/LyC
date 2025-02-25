# from AnalizadorSemantico import Instruccion
# class AlterarTabla(Instruccion):
#     def __init__(self, nombre_tabla, alteraciones):
#         self.nombre_tabla = nombre_tabla
#         self.alteraciones = alteraciones

#     def __repr__(self):
#         return f"AlterarTabla(tabla='{self.nombre_tabla}', alteraciones={self.alteraciones})"

#     def analizar_semantica(self, base_datos):
#         if self.nombre_tabla not in base_datos:
#             raise Exception(f"La tabla '{self.nombre_tabla}' no existe.")
#         for alteracion in self.alteraciones:
#             alteracion.analizar_semantica(base_datos, self.nombre_tabla)
#     def ejecutar(self,base_datos):
#         self.analizar_semantica(base_datos)
#         """Genera en SQL equivalente en ingles"""
#         sql_parts = [f"ALTER TABLE {self.nombre_tabla}"]
#         sql_parts += [alteracion.ejecutar() for alteracion in self.alteraciones]
#         return " ".join(sql_parts)

# class AgregarColumna(Instruccion):
#     def __init__(self, lista_columnas,nombreTabla):
#         self.lista_columnas = lista_columnas
#         self.nombreTabla = nombreTabla

#     def __repr__(self):
#         return f"AgregarColumna(columnas={self.lista_columnas})"

#     def analizar_semantica(self, base_datos, nombre_tabla):
#         columnas_disponibles = list(base_datos[self.nombreTabla]["columnas"]) 
#         for col_def in self.lista_columnas:
#             nombre_columna = col_def.nombre
#             if col_def in columnas_disponibles:
#                 raise Exception(f"La columna '{nombre_columna}' ya existe en la tabla '{nombre_tabla}'.")
#             # if :
#             #     raise Exception(f"El tipo de dato '' no es válido.")
#             # if :
#             #     raise Exception(f"Las restricciones para '' no son válidas.")
    
#     def ejecutar(self, base_datos):
#         sql_columns = []
#         for col in self.lista_columnas:
#           nombre = col["nombre"]
#           tipo = col["tipo"]
#           restricciones = " ".join(col.get("restricciones", []))
#           sql_columns.append(f"ADD COLUMN {nombre} {tipo} {restricciones}")
        
#         return ", ".join(sql_columns)
       

# class SoltarColumna(Instruccion):
#     def __init__(self, nombre_columna):
#         self.nombre_columna = nombre_columna

#     def __repr__(self):
#         return f"SoltarColumna(columna='{self.nombre_columna}')"

#     def analizar_semantica(self, base_datos, nombre_tabla):
#         if not base_datos.tabla_tiene_columna(nombre_tabla, self.nombre_columna):
#             raise Exception(f"No existe la columna '{self.nombre_columna}' en la tabla '{nombre_tabla}'.")
#         if base_datos.columna_tiene_restricciones(nombre_tabla, self.nombre_columna):
#             raise Exception(f"La columna '{self.nombre_columna}' tiene restricciones y no puede ser eliminada.")


# class ModificarColumna(Instruccion):
#     def __init__(self, lista_columnas):
#         self.lista_columnas = lista_columnas

#     def __repr__(self):
#         return f"ModificarColumna(columnas={self.lista_columnas})"

#     def analizar_semantica(self, base_datos, nombre_tabla):
#         for col_def in self.lista_columnas:
#             nombre_columna = col_def.nombre
#             if not base_datos.tabla_tiene_columna(nombre_tabla, nombre_columna):
#                 raise Exception(f"La columna '{nombre_columna}' no existe en la tabla '{nombre_tabla}'.")
            

# class RenombrarColumna(Instruccion):
#     def __init__(self, nombre_viejo, nombre_nuevo):
#         self.nombre_viejo = nombre_viejo
#         self.nombre_nuevo = nombre_nuevo

#     def __repr__(self):
#         return f"RenombrarColumna(viejo='{self.nombre_viejo}', nuevo='{self.nombre_nuevo}')"

#     def analizar_semantica(self, base_datos, nombre_tabla):
#         if not base_datos.tabla_tiene_columna(nombre_tabla, self.nombre_viejo):
#             raise Exception(f"La columna '{self.nombre_viejo}' no existe en la tabla '{nombre_tabla}'.")
#         if base_datos.tabla_tiene_columna(nombre_tabla, self.nombre_nuevo):
#             raise Exception(f"La columna '{self.nombre_nuevo}' ya existe en la tabla '{nombre_tabla}'.")


# class CambiarColumna(Instruccion):
#     def __init__(self, nombre_viejo, nueva_definicion):
#         self.nombre_viejo = nombre_viejo
#         self.nueva_definicion = nueva_definicion

#     def __repr__(self):
#         return f"CambiarColumna(viejo='{self.nombre_viejo}', nueva_def='{self.nueva_definicion}')"

#     def analizar_semantica(self, base_datos, nombre_tabla):
#         if not base_datos.tabla_tiene_columna(nombre_tabla, self.nombre_viejo):
#             raise Exception(f"La columna '{self.nombre_viejo}' no existe en la tabla '{nombre_tabla}'.")
#         if base_datos.tabla_tiene_columna(nombre_tabla, self.nueva_definicion['nombre']):
#             raise Exception(f"Ya existe una columna con el nombre '{self.nueva_definicion['nombre']}' en la tabla '{nombre_tabla}'.")


from AnalizadorSemantico import Instruccion

class AlterarTabla(Instruccion):
    def __init__(self, nombre_tabla, alteraciones):
        self.nombre_tabla = nombre_tabla
        self.alteraciones = alteraciones

    def __repr__(self):
        return f"AlterarTabla(tabla='{self.nombre_tabla}', alteraciones={self.alteraciones})"

    def analizar_semantica(self, base_datos):
        # Verificar que la tabla exista en base_datos
        if self.nombre_tabla not in base_datos:
            raise Exception(f"La tabla '{self.nombre_tabla}' no existe.")
        
        # Validar cada alteración
        for alteracion in self.alteraciones:
            alteracion.analizar_semantica(base_datos, self.nombre_tabla)

    def ejecutar(self, base_datos):
        # Traducir a MySQL
        sql_statements = []
        for alteracion in self.alteraciones:
            sql_statements.append(alteracion.ejecutar(base_datos, self.nombre_tabla))
        return sql_statements


class AgregarColumna(Instruccion):
    def __init__(self, lista_columnas):
        self.lista_columnas = lista_columnas

    def __repr__(self):
        return f"AgregarColumna(columnas={self.lista_columnas})"

    def analizar_semantica(self, base_datos, nombre_tabla):
        # Validar si la tabla tiene la columna
        if nombre_tabla not in base_datos:
            raise Exception(f"La tabla '{nombre_tabla}' no existe.")

        for col_def in self.lista_columnas:
            nombre_columna = col_def.nombre
            if nombre_columna in base_datos[nombre_tabla]["columnas"]:
                raise Exception(f"La columna '{nombre_columna}' ya existe en la tabla '{nombre_tabla}'.")
            if col_def.tipo_dato not in ["entero", "texto", "fecha", "decimal", "booleano"]:
                raise Exception(f"El tipo de dato '{col_def.tipo_dato}' no es válido para la columna '{nombre_columna}'.")
            if not all(restriccion in ["NOT NULL", "UNIQUE", "PRIMARY KEY", "FOREIGN KEY"] for restriccion in col_def.restricciones):
                raise Exception(f"Las restricciones para '{nombre_columna}' no son válidas.")
    
    def ejecutar(self, base_datos, nombre_tabla):
        # Generar la sentencia MySQL para agregar columnas
        sql_statements = []
        for col_def in self.lista_columnas:
            sql = f"ALTER TABLE {nombre_tabla} ADD COLUMN {col_def.nombre} {col_def.tipo_dato}"
            if "NOT NULL" in col_def.restricciones:
                sql += " NOT NULL"
            if "UNIQUE" in col_def.restricciones:
                sql += " UNIQUE"
            if "PRIMARY KEY" in col_def.restricciones:
                sql += " PRIMARY KEY"
            if "FOREIGN KEY" in col_def.restricciones:
                # Aquí agregarías la lógica para claves foráneas si es necesario
                pass
            sql_statements.append(sql)
        return sql_statements


class Columna:
    def __init__(self, nombre, tipo_dato, restricciones):
        self.nombre = nombre
        self.tipo_dato = tipo_dato
        self.restricciones = restricciones


class SoltarColumna(Instruccion):
    def __init__(self, nombre_columna):
        self.nombre_columna = nombre_columna

    def __repr__(self):
        return f"SoltarColumna(columna='{self.nombre_columna}')"

    def analizar_semantica(self, base_datos, nombre_tabla):
        if nombre_tabla not in base_datos:
            raise Exception(f"La tabla '{nombre_tabla}' no existe.")
        if self.nombre_columna not in base_datos[nombre_tabla]["columnas"]:
            raise Exception(f"La columna '{self.nombre_columna}' no existe en la tabla '{nombre_tabla}'.")

    def ejecutar(self, base_datos, nombre_tabla):
        # Generar la sentencia MySQL para soltar columna
        return f"ALTER TABLE {nombre_tabla} DROP COLUMN {self.nombre_columna}"


class ModificarColumna(Instruccion):
    def __init__(self, lista_columnas):
        self.lista_columnas = lista_columnas

    def __repr__(self):
        return f"ModificarColumna(columnas={self.lista_columnas})"

    def analizar_semantica(self, base_datos, nombre_tabla):
        if nombre_tabla not in base_datos:
            raise Exception(f"La tabla '{nombre_tabla}' no existe.")
        for col_def in self.lista_columnas:
            if col_def.nombre not in base_datos[nombre_tabla]["columnas"]:
                raise Exception(f"La columna '{col_def.nombre}' no existe en la tabla '{nombre_tabla}'.")
            if col_def.tipo_dato not in ["entero", "texto", "fecha", "decimal", "booleano"]:
                raise Exception(f"El tipo de dato '{col_def.tipo_dato}' no es válido.")
            if not all(restriccion in ["NOT NULL", "UNIQUE", "PRIMARY KEY", "FOREIGN KEY"] for restriccion in col_def.restricciones):
                raise Exception(f"Las restricciones para la columna '{col_def.nombre}' no son válidas.")
    
    def ejecutar(self, base_datos, nombre_tabla):
        sql_statements = []
        for col_def in self.lista_columnas:
            sql = f"ALTER TABLE {nombre_tabla} MODIFY COLUMN {col_def.nombre} {col_def.tipo_dato}"
            if "NOT NULL" in col_def.restricciones:
                sql += " NOT NULL"
            if "UNIQUE" in col_def.restricciones:
                sql += " UNIQUE"
            if "PRIMARY KEY" in col_def.restricciones:
                sql += " PRIMARY KEY"
            if "FOREIGN KEY" in col_def.restricciones:
                # Aquí agregarías la lógica para claves foráneas si es necesario
                pass
            sql_statements.append(sql)
        return sql_statements


class RenombrarColumna(Instruccion):
    def __init__(self, nombre_viejo, nombre_nuevo):
        self.nombre_viejo = nombre_viejo
        self.nombre_nuevo = nombre_nuevo

    def __repr__(self):
        return f"RenombrarColumna(viejo='{self.nombre_viejo}', nuevo='{self.nombre_nuevo}')"

    def analizar_semantica(self, base_datos, nombre_tabla):
        if nombre_tabla not in base_datos:
            raise Exception(f"La tabla '{nombre_tabla}' no existe.")
        if self.nombre_viejo not in base_datos[nombre_tabla]["columnas"]:
            raise Exception(f"La columna '{self.nombre_viejo}' no existe en la tabla '{nombre_tabla}'.")
        if self.nombre_nuevo in base_datos[nombre_tabla]["columnas"]:
            raise Exception(f"La columna '{self.nombre_nuevo}' ya existe en la tabla '{nombre_tabla}'.")

    def ejecutar(self, base_datos, nombre_tabla):
        return f"ALTER TABLE {nombre_tabla} RENAME COLUMN {self.nombre_viejo} TO {self.nombre_nuevo}"


class CambiarColumna(Instruccion):
    def __init__(self, nombre_viejo, nueva_definicion):
        self.nombre_viejo = nombre_viejo
        self.nueva_definicion = nueva_definicion

    def __repr__(self):
        return f"CambiarColumna(viejo='{self.nombre_viejo}', nueva_def='{self.nueva_definicion}')"

    def analizar_semantica(self, base_datos, nombre_tabla):
        if nombre_tabla not in base_datos:
            raise Exception(f"La tabla '{nombre_tabla}' no existe.")
        if self.nombre_viejo not in base_datos[nombre_tabla]["columnas"]:
            raise Exception(f"La columna '{self.nombre_viejo}' no existe en la tabla '{nombre_tabla}'.")
        if self.nueva_definicion["nombre"] in base_datos[nombre_tabla]["columnas"]:
            raise Exception(f"La columna '{self.nueva_definicion['nombre']}' ya existe en la tabla '{nombre_tabla}'.")
        if self.nueva_definicion["tipo_dato"] not in ["entero", "texto", "fecha", "decimal", "booleano"]:
            raise Exception(f"El tipo de dato '{self.nueva_definicion['tipo_dato']}' no es válido.")
        if not all(restriccion in ["NOT NULL", "UNIQUE", "PRIMARY KEY", "FOREIGN KEY"] for restriccion in self.nueva_definicion["restricciones"]):
            raise Exception(f"Las restricciones para la nueva columna no son válidas.")
    
    def ejecutar(self, base_datos, nombre_tabla):
        sql = f"ALTER TABLE {nombre_tabla} CHANGE COLUMN {self.nombre_viejo} {self.nueva_definicion['nombre']} {self.nueva_definicion['tipo_dato']}"
        if "NOT NULL" in self.nueva_definicion["restricciones"]:
            sql += " NOT NULL"
        if "UNIQUE" in self.nueva_definicion["restricciones"]:
            sql += " UNIQUE"
        if "PRIMARY KEY" in self.nueva_definicion["restricciones"]:
            sql += " PRIMARY KEY"
        if "FOREIGN KEY" in self.nueva_definicion["restricciones"]:
            # Aquí agregarías la lógica para claves foráneas si es necesario
            pass
        return sql
