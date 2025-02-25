from clases.Crear import Crear

def p_crear(t):
    """crear : CREAR TABLA IDENTIFICADOR PARENTESIS_IZQ lista_columnas_crear PARENTESIS_DER"""
    # t[1] : CREAR
    # t[2] : TABLA
    # t[3] : IDENTIFICADOR
    # t[4] : PARENTESIS_IZQ
    # t[5] : lista_columnas_crear ("columna", nombreColumna, tipoDato, restricciones)
    # t[6] : PARENTESIS_DER
    
    nombre_tabla = t[3]
    columnas = {}
    llave_primaria = None
    llaves_foraneas = {}
    
    for columna in t[5]:
        nombre_columna = columna[1] # Identificador de la columna
        tipo_dato = columna[2] # Tipo de dato
        restricciones = columna[3] # Lista de restricciones
        
        columnas[nombre_columna] = tipo_dato

        for restriccion in restricciones:
            if restriccion == "CLAVE_PRIMARIA":
                if llave_primaria is not None:
                    raise Exception(f"Error semántico: Más de una clave primaria en la tabla '{nombre_tabla}'")
                llave_primaria = nombre_columna
            elif restriccion.startswith("CLAVE_FORANEA"):
                referencia = restriccion.split(":")[1]  # Extraer la referencia "tabla.columna"
                llaves_foraneas[nombre_columna] = referencia

    
    t[0] = Crear(nombre_tabla, columnas, llave_primaria, llaves_foraneas)

def p_lista_columnas_crear(t):
    """lista_columnas_crear : lista_columnas_crear COMA lista_columna_crear
                      | lista_columna_crear"""
    if len(t) == 4:
        t[0] = t[1] + [t[3]]
    else:
        t[0] = [t[1]]