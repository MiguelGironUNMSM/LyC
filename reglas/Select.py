from clases.Seleccion import Seleccion

def p_seleccion(t):
    """seleccion : SELECCIONAR lista_floro lista_columnas DESDE IDENTIFICADOR opt_condiciones"""
    # t[1] : SELECCIONAR
    # t[2] : lista_floro
    # t[3] : lista_columnas
    # t[4] : DESDE
    # t[5] : IDENTIFICADOR (nombre de la tabla)
    # t[6] : opt_condiciones (lista de cláusulas, o [] si no hay)
    if t[6]:
        t[0] = Seleccion(columnas=t[3], tabla = t[5])
    else:
        t[0] = Seleccion(columnas=t[3], tabla = t[5],condiciones = t[6])


def p_lista_floro(t):
    """lista_floro : lista_floro floro
                   | floro"""
    if len(t) == 3:
        t[0] = (t[1], t[2])
    else:
        t[0] = t[1]


def p_floro(t):
    """floro : DISTINTO
             | empty"""
    if t[1] == "DISTINTO":  # Se encontró la palabra DISTINCT
        t[0] = "DISTINTO"
    else:
        t[0] = None


def p_lista_columnas(t):
    """lista_columnas : IDENTIFICADOR
                      | lista_columnas COMA IDENTIFICADOR
                      | TODO"""
    if len(t) == 2:
        t[0] = [t[1]]
    elif len(t) == 4:
        # Se asume que t[1] ya es una tupla ('COLUMNAS', lista) para ir acumulando
        t[0] = t[1] + [t[3]]
    else:
        t[0] = ["*"]
