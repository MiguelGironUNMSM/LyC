class BaseDatos:
    def __init__(self):
        # Ejemplo de cómo podrían almacenarse las tablas y las columnas dentro de ellas.
        self.tablas = {
            "clientes": {
                "columnas": {
                    "id_cliente": {"tipo": "entero", "restricciones": ["no_nulo", "clave_primaria"]},
                    "nombre": {"tipo": "texto", "restricciones": ["no_nulo"]},
                    "email": {"tipo": "texto", "restricciones": ["no_nulo", "unico"]}
                }
            },
            "productos": {
                "columnas": {
                    "id_producto": {"tipo": "entero", "restricciones": ["no_nulo", "clave_primaria"]},
                    "descripcion": {"tipo": "texto", "restricciones": ["no_nulo"]}
                }
            }
        }

    def existe_tabla(self, nombre_tabla):
        """
        Verifica si la tabla existe en la base de datos.
        """
        return nombre_tabla in self.tablas

    def tabla_tiene_columna(self, nombre_tabla, nombre_columna):
        """
        Verifica si una tabla tiene una columna específica.
        """
        if not self.existe_tabla(nombre_tabla):
            raise Exception(f"La tabla '{nombre_tabla}' no existe.")
        return nombre_columna in self.tablas[nombre_tabla]["columnas"]

    def tipo_dato_valido(self, tipo_dato):
        """
        Verifica si el tipo de dato es válido.
        """
        tipos_validos = ["entero", "texto", "fecha", "decimal", "booleano"]  # Ejemplo de tipos válidos
        return tipo_dato in tipos_validos

    def restricciones_validas(self, restricciones):
        """
        Verifica si las restricciones de una columna son válidas.
        """
        restricciones_validas = ["no_nulo", "unico", "clave_primaria", "clave_foranea", "predeterminado"]
        # Verifica que todas las restricciones sean válidas
        return all(restriccion in restricciones_validas for restriccion in restricciones)

    def columna_tiene_restricciones(self, nombre_tabla, nombre_columna):
        """
        Verifica si una columna en una tabla tiene restricciones.
        """
        if not self.tabla_tiene_columna(nombre_tabla, nombre_columna):
            raise Exception(f"La columna '{nombre_columna}' no existe en la tabla '{nombre_tabla}'.")
        restricciones = self.tablas[nombre_tabla]["columnas"][nombre_columna]["restricciones"]
        return len(restricciones) > 0

class Instruccion:
    def __init__(self):
        pass

    def analizar_semantica(self, base_datos):
        raise NotImplementedError()

    def ejecutar(self, base_datos):
        raise NotImplementedError()


class AlterarTabla(Instruccion):
    def __init__(self, nombre_tabla, alteraciones):
        self.nombre_tabla = nombre_tabla
        self.alteraciones = alteraciones

    def __repr__(self):
        return f"AlterarTabla(tabla='{self.nombre_tabla}', alteraciones={self.alteraciones})"

    def analizar_semantica(self, base_datos):
        if not base_datos.existe_tabla(self.nombre_tabla):
            raise Exception(f"La tabla '{self.nombre_tabla}' no existe.")
        for alteracion in self.alteraciones:
            alteracion.analizar_semantica(base_datos, self.nombre_tabla)


class AgregarColumna(Instruccion):
    def __init__(self, lista_columnas):
        self.lista_columnas = lista_columnas

    def __repr__(self):
        return f"AgregarColumna(columnas={self.lista_columnas})"

    def analizar_semantica(self, base_datos, nombre_tabla):
        for col_def in self.lista_columnas:
            nombre_columna = col_def.nombre
            if base_datos.tabla_tiene_columna(nombre_tabla, nombre_columna):
                raise Exception(f"La columna '{nombre_columna}' ya existe en la tabla '{nombre_tabla}'.")
            if not base_datos.tipo_dato_valido(col_def.tipo_dato):
                raise Exception(f"El tipo de dato '{col_def.tipo_dato}' no es válido.")
            if not base_datos.restricciones_validas(col_def.restricciones):
                raise Exception(f"Las restricciones para '{nombre_columna}' no son válidas.")


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
