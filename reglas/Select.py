def p_seleccion(t):
    """seleccion : SELECCIONAR lista_floro lista_columnas DESDE IDENTIFICADOR condicion_opt"""
    t[0] = ("seleccion", t[2], t[3], t[5],t[6])
    if t[6] == None:
        t[0] = ("seleccion", t[2], t[3], t[4], t[5])

def p_lista_floro(t):
    """lista_floro : lista_floro floro
                   | floro
    """
    if len(t)==3:
        t[0]=(t[1],t[2])
    else:
        t[0]=t[1]

def p_floro(t):
    """floro : DISTINTO
             | PRIMEROS VALOR_NUMERO
             | empty
    """
    if 'DISTINTO' in t:  # Si se encontró la palabra DISTINTO
        t[0] = "DISTINTO"
    elif len(t) == 3:  # Si es TOP seguido de un número
        t[0] = ("PRIMEROS", t[2])  # Aquí t[2] es el número
    else:
        t[0] = None  # Cuando floro está vacío (empty)

# Agregar la regla para manejar el token 'TODO' (asterisco)
def p_lista_columnas(t):
    """lista_columnas : IDENTIFICADOR
                    | lista_columnas COMA IDENTIFICADOR
                    | TODO"""  # Agregar aquí la opción para 'TODO' (el asterisco)
    if len(t) == 2:
        t[0] = ('COLUMNAS',[t[1]])
    elif len(t) == 4:
        t[0] = ('COLUMNAS',t[1][1] + [t[3]])
    else:
        t[0] = ["*"]  # Si es el caso de 'TODO'


