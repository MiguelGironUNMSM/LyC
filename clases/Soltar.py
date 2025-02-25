from AnalizadorSemantico import Instruccion

class Soltar(Instruccion):
    """
    Esta clase representa la instrucción Soltar, la cual permite eliminar una tabla de la base de datos.

    Args:
        Instruccion: Herencia de la clase Instruccion
    """
    def __init__(self, nombre_tabla, condiciones):
        """
        Inicializador de la clase Soltar.
        Args:
            nombre_tabla (str): Nombre de la tabla a eliminar 
            condiciones (list): Lista de condiciones para eliminar la tabla
        """
        self.nombre_tabla = nombre_tabla 
        self.condiciones = condiciones
    