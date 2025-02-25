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
        nombreColumna = columna[1]
        tipoDato = columna[2]
        restricciones = columna[3]
        
        if restricciones[0] != "CLAVE_FORANEA":
            columnas[nombreColumna] = tipoDato

    t[0] = ("crear", t[3], t[5])

def p_lista_columnas_crear(t):
    """lista_columnas_crear : lista_columnas_crear COMA lista_columna_crear
                      | lista_columna_crear"""
    if len(t) == 4:
        t[0] = t[1] + [t[3]]
    else:
        t[0] = [t[1]]