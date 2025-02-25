from AnalizadorSemantico import Instruccion

class Actualizar_tabla(Instruccion):
    """
    Esta clase representa la instrucción Actualizar tabla, la cual es una instrucción que permite modificar los datos de una tabla en la base de datos.
    
    Args:
        Instruccion(): Herencia de la clase Instruccion
    """
    
    def __init__(self, nombre_tabla, alteraciones):
        self.nombre_tabla = nombre_tabla # Nombre de la tabla a la que se le modificarán los datos
        self.alteraciones = alteraciones # Condiciones que se deben cumplir para modificar los datos de la tabla
        
    def analizar_semantica(self, base_datos):
        if (self.nombre_tabla not in base_datos):
            raise Exception(f"La tabla '{self.nombre_tabla}' no existe.")
        
        for alteracion in self.alteraciones:
            
        
    def ejecutar():
        pass