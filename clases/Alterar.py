from AnalizadorSemantico import Instruccion
class AlterarTabla(Instruccion):
    def __init__(self, nombre_tabla, alteraciones):
        self.nombre_tabla = nombre_tabla
        self.alteraciones = alteraciones

    def __repr__(self):
        return f"AlterarTabla(tabla='{self.nombre_tabla}', alteraciones={self.alteraciones})"

    def analizar_semantica(self, base_datos):
        if self.nombre_tabla not in base_datos:
            raise Exception(f"La tabla '{self.nombre_tabla}' no existe.")
        for alteracion in self.alteraciones:
            alteracion.analizar_semantica(base_datos, self.nombre_tabla)


class AgregarColumna(Instruccion):
    def __init__(self, lista_columnas):
        self.lista_columnas = lista_columnas

    def __repr__(self):
        return f"AgregarColumna(columnas={self.lista_columnas})"

    def analizar_semantica(self, base_datos, nombre_tabla):
        TIPOS_VALIDOS = {"entero", "text", "boleano", "cadena", "flotante", "fecha"} 
        RESTRICCIONES_VALIDAS = {"NO NULO", "UNICO", "LLAVE PRIMARIA", "LLAVE FORANEA"} 
        columnas_disponibles = list(base_datos[self.tabla]["columnas"].keys())  
        
        
        for col_def in self.lista_columnas:
            nombre_columna = col_def.nombre
            if col_def in columnas_disponibles:
                raise Exception(f"La columna '{nombre_columna}' ya existe en la tabla '{nombre_tabla}'.")
            # if :
            #     raise Exception(f"El tipo de dato '' no es válido.")
            # if :
            #     raise Exception(f"Las restricciones para '' no son válidas.")
    
    def ejecutar(self, base_datos):
        return super().ejecutar(base_datos)

class SoltarColumna(Instruccion):
    def __init__(self, nombre_columna):
        self.nombre_columna = nombre_columna

    def __repr__(self):
        return f"SoltarColumna(columna='{self.nombre_columna}')"

    def analizar_semantica(self, base_datos, nombre_tabla):
        if not base_datos.tabla_tiene_columna(nombre_tabla, self.nombre_columna):
            raise Exception(f"No existe la columna '{self.nombre_columna}' en la tabla '{nombre_tabla}'.")
        if base_datos.columna_tiene_restricciones(nombre_tabla, self.nombre_columna):
            raise Exception(f"La columna '{self.nombre_columna}' tiene restricciones y no puede ser eliminada.")


class ModificarColumna(Instruccion):
    def __init__(self, lista_columnas):
        self.lista_columnas = lista_columnas

    def __repr__(self):
        return f"ModificarColumna(columnas={self.lista_columnas})"

    def analizar_semantica(self, base_datos, nombre_tabla):
        for col_def in self.lista_columnas:
            nombre_columna = col_def.nombre
            if not base_datos.tabla_tiene_columna(nombre_tabla, nombre_columna):
                raise Exception(f"La columna '{nombre_columna}' no existe en la tabla '{nombre_tabla}'.")
            if not base_datos.tipo_dato_valido(col_def.tipo_dato):
                raise Exception(f"El tipo de dato '{col_def.tipo_dato}' no es válido para la columna '{nombre_columna}'.")
            if not base_datos.restricciones_validas(col_def.restricciones):
                raise Exception(f"Las restricciones para la columna '{nombre_columna}' no son válidas.")


class RenombrarColumna(Instruccion):
    def __init__(self, nombre_viejo, nombre_nuevo):
        self.nombre_viejo = nombre_viejo
        self.nombre_nuevo = nombre_nuevo

    def __repr__(self):
        return f"RenombrarColumna(viejo='{self.nombre_viejo}', nuevo='{self.nombre_nuevo}')"

    def analizar_semantica(self, base_datos, nombre_tabla):
        if not base_datos.tabla_tiene_columna(nombre_tabla, self.nombre_viejo):
            raise Exception(f"La columna '{self.nombre_viejo}' no existe en la tabla '{nombre_tabla}'.")
        if base_datos.tabla_tiene_columna(nombre_tabla, self.nombre_nuevo):
            raise Exception(f"La columna '{self.nombre_nuevo}' ya existe en la tabla '{nombre_tabla}'.")


class CambiarColumna(Instruccion):
    def __init__(self, nombre_viejo, nueva_definicion):
        self.nombre_viejo = nombre_viejo
        self.nueva_definicion = nueva_definicion

    def __repr__(self):
        return f"CambiarColumna(viejo='{self.nombre_viejo}', nueva_def='{self.nueva_definicion}')"

    def analizar_semantica(self, base_datos, nombre_tabla):
        if not base_datos.tabla_tiene_columna(nombre_tabla, self.nombre_viejo):
            raise Exception(f"La columna '{self.nombre_viejo}' no existe en la tabla '{nombre_tabla}'.")
        if base_datos.tabla_tiene_columna(nombre_tabla, self.nueva_definicion['nombre']):
            raise Exception(f"Ya existe una columna con el nombre '{self.nueva_definicion['nombre']}' en la tabla '{nombre_tabla}'.")
        if not base_datos.tipo_dato_valido(self.nueva_definicion['tipo_dato']):
            raise Exception(f"El tipo de dato '{self.nueva_definicion['tipo_dato']}' no es válido.")
        if not base_datos.restricciones_validas(self.nueva_definicion['restricciones']):
            raise Exception(f"Las restricciones para la nueva definición no son válidas.")
