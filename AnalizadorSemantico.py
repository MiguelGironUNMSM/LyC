class Nodo:
    def analizar_semantica(self, base_datos):
        raise NotImplementedError()
    
    def ejecutar(self):
        raise NotImplementedError()
    
class Crear(Nodo):
    def __init__(self, nombre_tabla, columnas):
        self.nombre_tabla = nombre_tabla
        self.columnas = columnas
        
    def analizar_semantica(self, base_datos):
        
        # Verificar que la tabla no exista
        if self.nombre_tabla in base_datos:
            raise Exception(f"La tabla {self.nombre_tabla} ya existe")
        
        # Verificar que se estén creando columnas en dicha tabla
        if not self.columnas:
            raise Exception(f"La tabla {self.nombre_tabla} debe tener al menos una columna")
        
        # Verificar que las columnas no existan (la tabla sí existe)
        

def analizar(raiz, base_datos):
    if not isinstance(raiz, Nodo):
        raise Exception
    
    try:
        raiz.analizar_semantica(base_datos)
        raiz.ejecutar()
    except Exception as e:
        print("Error:", e)
        
base_de_datos = {
    "Usuarios": {
        "columnas": ["id", "nombre", "edad"]
    }
}


consulta = Insertar("Usuarios", ["apellido", "edad"], [25, "Juan"])
analizar(consulta, base_de_datos)  # Insertando en la tabla Usuarios los valores ['Juan', 25]
