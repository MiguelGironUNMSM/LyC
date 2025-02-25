class Instruccion:
    def analizar_semantica(self, base_datos):
        raise NotImplementedError()
    
    def ejecutar(self, base_datos):
        raise NotImplementedError()

class Crear(Instruccion):
    def __init__(self, nombre_tabla, columnas, llave_primaria=None, llaves_foraneas=None):
        self.nombre_tabla = nombre_tabla
        self.columnas = columnas  
        self.llave_primaria = llave_primaria
        self.llaves_foraneas = llaves_foraneas if llaves_foraneas else {}
        
    def analizar_semantica(self, base_datos):
        # Código de analizar
        return True
    
    def ejecutar(self, base_datos):
        # "Genera" la consulta SQL en formato de texto
        return True
    
