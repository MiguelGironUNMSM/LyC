class Instruccion:
    def __init__(self):
        pass
    def analizar_semantica(self, base_datos):
        raise NotImplementedError()
    
    def ejecutar(self, base_datos):
        raise NotImplementedError()

# Base de datos simulada        
base_de_datos = {
    "empleados": {
        "columnas": {"id": "INT", "nombre": "VARCHAR", "edad": "INT" },
        "llave_primaria": "id",
        "llaves_foraneas": {"departamento_id": "departamentos.id"}
    },
    "departamentos": {
        "columnas": {"id": "INT", "nombre": "VARCHAR"},
        "llave_primaria": "id"
    }
}

class Crear(Instruccion):
    def __init__(self, nombre_tabla, columnas, llave_primaria=None, llaves_foraneas=None):
        self.nombre_tabla = nombre_tabla
        self.columnas = columnas  
        self.llave_primaria = llave_primaria
        self.llaves_foraneas = llaves_foraneas if llaves_foraneas else {}
        
    def analizar_semantica(self, base_datos):
        # Se verifica si la tabla ya existe
        if self.nombre_tabla in base_datos:
            raise Exception(f"Error semántico: la tabla '{self.nombre_tabla}' ya existe.")
        
        # Se verifica que se estén definiendo columnas
        if not self.columnas:
            raise Exception(f"Error semántico: la tabla '{self.nombre_tabla}' debe tener al menos una columna.")
        
        # Se verifica la unicidad de nombres de columnas
        nombres_columnas = set(self.columnas.keys())
        if len(nombres_columnas) != len(self.columnas):
            raise Exception(f"Error semántico: Hay columnas duplicadas en la tabla '{self.nombre_tabla}'")
        
        # Se verifica que la llave primaria (si es que hay), también se encuentre en las columnas
        if self.llave_primaria:
            if self.llave_primaria not in self.columnas:
                raise Exception(f"Error semántico:: la llave primaria '{self.llave_primaria}' no está en las columnas de la tabla '{self.nombre_tabla}.'")
            
        # Se validan las llaves foráneas (si es que existen)
        for col, ref in self.llaves_foraneas.items():
            if col not in self.columnas:
                raise Exception(f"Error semántico: la columna '{col}' definida como llave foránea no existe en la tabla {self.nombre_tabla}")
            
            ref_tabla, ref_columna = ref.split(".")
            
            if ref_tabla not in base_datos:
                raise Exception(f"Error semántico: la tabla referenciada '{ref_tabla}' no existe.")
            
            if ref_columna not in base_datos[ref_tabla]["columnas"]:
                raise Exception(f"Error semántico: la columna referenciada '{ref_columna}' no existe en la tabla '{ref_tabla}'.")

    def ejecutar(self, base_datos):
        # Se ejecuta el análisis semántico
        self.analizar_semantica(base_datos)
        
        # Se construye la consulta SQL en formato de texto
        columnas_sql = [f"{col} {tipo}" for col, tipo in self.columnas.items()]
        
        if self.llave_primaria:
            columnas_sql.append(f"PRIMARY KEY ({self.llave_primaria})")
        
        for col, ref, in self.llaves_foraneas.items():
            ref_tabla, ref_columna = ref.split(".")
            columnas_sql.append(f"FOREIGN KEY ({col}) REFERENCES {ref_tabla}({ref_columna})")
        
        sql = f"CREATE TABLE {self.nombre_tabla} (\n      " + ",\n        ".join(columnas_sql) + "\n);"
        return sql
    
    
nodo_crear = Crear(
    nombre_tabla="empleado",
    columnas={
        "id": "INT",
        "nombre": "VARCHAR",
        "edad": "INT",
        "departamento_id": "INT"
    },
    llave_primaria="id",
    llaves_foraneas={"departamento_id": "departamentos.id"}
)

print(nodo_crear.ejecutar(base_de_datos))
