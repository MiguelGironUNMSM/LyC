def p_lista_columna_crear(t):
    """lista_columna_crear : IDENTIFICADOR  tipo_dato restricciones"""
    nombreColumna = t[1]
    tipoDato = t[2]
    restricciones = list(t[3])

    t[0] = ("columna", nombreColumna, tipoDato, restricciones)


def p_tipo_dato(t):
    """tipo_dato : ENTERO especificacion
    | CADENA especificacion
    | CARACTER especificacion
    | FECHA especificacion
    | BOOLEANO especificacion
    | DECIMAL especificacion
    | TEXTO especificacion
    | FLOTANTE especificacion"""
    if len(t) == 3:
        t[0] = (t[1], t[2])
    else:
        t[0] = (t[1], None)


def p_especificacion(t):
    """especificacion : PARENTESIS_IZQ VALOR_NUMERO PARENTESIS_DER
    | empty"""
    if len(t) == 4:
        t[0] = t[2]
    else:
        t[0] = None


def p_restricciones(t):
    """restricciones : restricciones restriccion
    | restriccion
    | empty"""

    if len(t) == 3:
        t[0] = t[1] + [t[2]]
    elif len(t) == 2:
        t[0] = [t[1]]
    else:
        t[0] = []


def p_restriccion(t):
    """restriccion : CLAVE_PRIMARIA
    | CLAVE_FORANEA
    | AUTOINCREMENTAL
    | NO_NULO"""
    t[0] = t[1]

def p_condicion_opt(t):
    """condicion_opt : DONDE condicion
                    | empty
                    | ORDENAR_POR condicion_order """
    if len(t) == 3:  # Para "DONDE condicion" y "ORDENAR_POR condicion_order"
        t[0] = [t[1], t[2]]
    else:  # Para "empty"
        t[0] = [None]


def p_condicion(t):
    """condicion : IDENTIFICADOR comparador valor
                | condicion Y condicion
                | condicion O condicion"""
    if len(t) == 4:
        t[0] = (t[1], t[2], t[3])
    else:
        t[0] = (t[1], t[2], t[3], t[4])


# Regla para el operador de comparación
def p_comparador(t):
    """comparador : IGUALDAD
                    | MAYOR
                    | MENOR
                    | MAYOR_IGUAL
                    | MENOR_IGUAL
                    | DIFERENTE"""
    t[0] = t[1]


def p_valor(t):
    """valor : VALOR_NUMERO
            |  VALOR_CADENA
            |  VALOR_BOOLEANO
            |  VALOR_FLOTANTE"""
    
    t[0] = t[1]

def p_condicion_order(t):
    """condicion_order : IDENTIFICADOR ASCENDENTE
                       | IDENTIFICADOR DESCENDENTE
                       | IDENTIFICADOR"""
    if len(t)==3:
        t[0]=(t[1],t[2])
    else:
        t[0]=(t[1],'ASCENDENTE')

# Regla de la producción vacía (para manejar la opción 'empty')
def p_empty(t):
    "empty :"
    pass


__all__ = ["p_lista_columna_crear", "p_tipo_dato", "p_especificacion", "p_restricciones", "p_restriccion", "p_condicion_opt", "p_condicion", "p_comparador", "p_valor", "p_condicion_order", "p_empty"]