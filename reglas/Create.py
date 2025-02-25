from clases.Crear import Crear

def p_crear(t):
    """crear : CREAR TABLA IDENTIFICADOR PARENTESIS_IZQ lista_columnas_crear PARENTESIS_DER"""
    # t[1] : CREAR
    # t[2] : TABLA
    # t[3] : IDENTIFICADOR (nombre de la variable)
    # t[4] : PARENTESIS_IZQ
    # t[5] : lista_columnas_crear ("columna", nombreColumna, tipoDato, [(restricciones, (tabla_referencia, columna_referencia))])
    # t[6] : PARENTESIS_DER
    
    nombre_tabla = t[3]
    columnas = {}
    llave_primaria = None
    llaves_foraneas = {}
    
    for columna in t[5]:
        nombre_columna = columna[1]
        tipo_dato = columna[2]
        restricciones = columna[3]
        
        columnas[nombre_columna] = {
            "tipo": tipo_dato,
            "restricciones": restricciones
        }
        
        llave_primaria = nombre_columna if "CLAVE_PRIMARIA" in restricciones else None
        
  
        for restriccion in restricciones:
            if isinstance(restriccion, tuple) and restriccion[0] == "CLAVE FORANEA":
                tabla_ref, columna_ref = restriccion[1]
                llaves_foraneas[nombre_columna] = f"{tabla_ref}.{columna_ref}"
                
        
    t[0] = Crear(nombre_tabla, columnas, llave_primaria, llaves_foraneas)

def p_lista_columnas_crear(t):
    """lista_columnas_crear : lista_columnas_crear COMA lista_columna_crear
                      | lista_columna_crear"""
    if len(t) == 4:
        t[0] = t[1] + [t[3]]
    else:
        t[0] = [t[1]]