
class AlterarTabla:
    """
    Representa la instrucción principal:
    ALTERAR TABLA nombreTabla (lista de alteraciones)
    """
    def __init__(self, nombre_tabla, alteraciones):
        """
        :param nombre_tabla: Nombre de la tabla que se va a alterar (str)
        :param alteraciones: Lista de objetos que representan las alteraciones
                             (AgregarColumna, SoltarColumna, ModificarColumna, etc.)
        """
        self.nombre_tabla = nombre_tabla
        self.alteraciones = alteraciones

    def __repr__(self):
        return f"AlterarTabla(tabla='{self.nombre_tabla}', alteraciones={self.alteraciones})"

    def analizar(self, entorno):
        """
        Lógica de validaciones semánticas para ALTERAR TABLA.
        1. Verificar que la tabla 'nombre_tabla' exista en el entorno.
        2. Para cada alteración, llamar su propio método de análisis.
        """
        if not entorno.existe_tabla(self.nombre_tabla):
            raise Exception(f"La tabla '{self.nombre_tabla}' no existe.")

        for alteracion in self.alteraciones:
            alteracion.analizar(entorno, self.nombre_tabla)

        return self  # Puedes retornar self o lo que necesites según tu diseño.


class AgregarColumna:
    """
    Representa la operación:
    ALTERAR TABLA AGREGAR [COLUMNA] lista_columna_crear
    """
    def __init__(self, lista_columnas):
        """
        :param lista_columnas: Estructura que describe las columnas a crear
        """
        self.lista_columnas = lista_columnas

    def __repr__(self):
        return f"AgregarColumna(columnas={self.lista_columnas})"

    def analizar(self, entorno, nombre_tabla):
        """
        Validaciones semánticas para AGREGAR COLUMNA.
        1. Verificar que cada nueva columna no exista ya en la tabla.
        2. Verificar tipos de datos soportados, restricciones, etc.
        """
        for col_def in self.lista_columnas:
            nombre_columna = col_def.nombre
            if entorno.tabla_tiene_columna(nombre_tabla, nombre_columna):
                raise Exception(
                    f"La columna '{nombre_columna}' ya existe en la tabla '{nombre_tabla}'."
                )
        # Aquí puedes añadir más validaciones según tu lógica.


class SoltarColumna:
    """
    Representa la operación:
    ALTERAR TABLA SOLTAR [COLUMNA] nombreColumna
    """
    def __init__(self, nombre_columna):
        """
        :param nombre_columna: Nombre de la columna a soltar (eliminar)
        """
        self.nombre_columna = nombre_columna

    def __repr__(self):
        return f"SoltarColumna(columna='{self.nombre_columna}')"

    def analizar(self, entorno, nombre_tabla):
        """
        Validaciones semánticas para SOLTAR COLUMNA.
        1. Verificar que la columna exista en la tabla.
        2. Verificar si hay restricciones que impidan su eliminación.
        """
        if not entorno.tabla_tiene_columna(nombre_tabla, self.nombre_columna):
            raise Exception(
                f"No existe la columna '{self.nombre_columna}' en la tabla '{nombre_tabla}'."
            )
        # Más validaciones si fuera necesario.


class ModificarColumna:
    """
    Representa la operación:
    ALTERAR TABLA MODIFICAR [COLUMNA] lista_columna_crear
    """
    def __init__(self, lista_columnas):
        """
        :param lista_columnas: Estructura que describe la(s) columna(s) a modificar
                              y su(s) nueva(s) definición(es).
        """
        self.lista_columnas = lista_columnas

    def __repr__(self):
        return f"ModificarColumna(columnas={self.lista_columnas})"

    def analizar(self, entorno, nombre_tabla):
        """
        Validaciones semánticas para MODIFICAR COLUMNA.
        1. Verificar que la columna exista en la tabla.
        2. Validar el nuevo tipo o restricción.
        """
        for col_def in self.lista_columnas:
            nombre_columna = col_def.nombre
            if not entorno.tabla_tiene_columna(nombre_tabla, nombre_columna):
                raise Exception(
                    f"La columna '{nombre_columna}' no existe en la tabla '{nombre_tabla}'."
                )
        # Más validaciones según tu lógica.


class RenombrarColumna:
    """
    Representa la operación:
    ALTERAR TABLA RENOMBRAR [COLUMNA] oldName A newName
    """
    def __init__(self, nombre_viejo, nombre_nuevo):
        """
        :param nombre_viejo: Nombre de la columna actual
        :param nombre_nuevo: Nuevo nombre para la columna
        """
        self.nombre_viejo = nombre_viejo
        self.nombre_nuevo = nombre_nuevo

    def __repr__(self):
        return f"RenombrarColumna(viejo='{self.nombre_viejo}', nuevo='{self.nombre_nuevo}')"

    def analizar(self, entorno, nombre_tabla):
        """
        Validaciones semánticas para RENOMBRAR COLUMNA.
        1. Verificar que la columna 'nombre_viejo' exista.
        2. Verificar que 'nombre_nuevo' no exista ya en la tabla.
        """
        if not entorno.tabla_tiene_columna(nombre_tabla, self.nombre_viejo):
            raise Exception(
                f"La columna '{self.nombre_viejo}' no existe en la tabla '{nombre_tabla}'."
            )
        if entorno.tabla_tiene_columna(nombre_tabla, self.nombre_nuevo):
            raise Exception(
                f"La columna '{self.nombre_nuevo}' ya existe en la tabla '{nombre_tabla}'."
            )


class CambiarColumna:
    """
    Representa la operación:
    ALTERAR TABLA CAMBIAR [COLUMNA] old_column_name nueva_definicion
    """
    def __init__(self, nombre_viejo, nueva_definicion):
        """
        :param nombre_viejo: Nombre de la columna actual
        :param nueva_definicion: Estructura que describe el nuevo nombre, tipo, restricciones, etc.
        """
        self.nombre_viejo = nombre_viejo
        self.nueva_definicion = nueva_definicion

    def __repr__(self):
        return f"CambiarColumna(viejo='{self.nombre_viejo}', nueva_def='{self.nueva_definicion}')"

    def analizar(self, entorno, nombre_tabla):
        """
        Validaciones semánticas para CAMBIAR COLUMNA.
        1. Verificar que la columna 'nombre_viejo' exista.
        2. Extraer de 'nueva_definicion' el nuevo nombre y validar que no exista.
        3. Validar el tipo y restricciones.
        """
        if not entorno.tabla_tiene_columna(nombre_tabla, self.nombre_viejo):
            raise Exception(
                f"La columna '{self.nombre_viejo}' no existe en la tabla '{nombre_tabla}'."
            )
        # Aquí podrías extraer el nuevo nombre (si existe) y hacer más validaciones
        # según tu estructura de 'nueva_definicion'.
