def p_crear(t):
    '''crear : CREAR TABLA IDENTIFICADOR PARENTESIS_IZQ columnas PARENTESIS_DER'''
    t[0]=("crear_tabla",t[3],t[5])

def p_lista_columnas_crear(t):
    '''lista_columnas : lista_columnas COMA lista_columna
                      | lista_columna'''
    if len(t)==4:
        t[0]=t[1]+[t[3]]
    else:
        t[0]=[t[1]]

def p_lista_columna_crear(t):
    '''lista_columna : IDENTIFICADOR  tipo_dato restricciones'''
    t[0]=("columna",t[1],t[2],t[3])

def p_tipo_dato(t):
    '''tipo_dato : ENTERO
            | CADENA
            | CARACTER
            | DECIMAL
            | FECHA'''
    
    t[0]=t[1]

def p_restricciones(t):
    '''restricciones : restricciones restriccion
                     | restriccion
                     | empty '''
    
    if len(t)==3:
        t[0]=t[1]+[t[2]]
    elif len(t)==2:
        t[0]=[t[1]]
    else:
        t[0]:[]

def p_restriccion(t):
    '''restriccion : CLAVE_PRIMARIA
                   | CLAVE_FORANEA
                   | AUTOINCREMENTAL
                   | NO_NULO'''
    t[0] = t[1]  

##########################################
def p_crear(t):
    '''crear : CREAR TABLA IDENTIFICADOR PARENTESIS_IZQ lista_columnas PARENTESIS_DER'''
    t[0] = ('crear', t[3], t[5])

def p_lista_columnas_crear(t):
    '''lista_columnas : IDENTIFICADOR tipo_dato
                     | lista_columnas COMA IDENTIFICADOR tipo_dato'''
    if len(t) == 3:
        t[0] = [(t[1], t[2])]
    else:
        t[0] = t[1] + [(t[3], t[4])]

def p_tipo_dato(t):
    '''tipo_dato : ENTERO
                | CADENA
                | CARACTER
                | FECHA
                | BOOLEANO
                | DECIMAL'''
    t[0] = t[1]