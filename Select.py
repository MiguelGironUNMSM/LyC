import ply.yacc as yacc
from AnalizadorLexico import tokens  # Importar los tokens de tu analizador léxico

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


def p_condicion_opt(t):
    """condicion_opt : DONDE condicion
                    | empty
                    | ORDENAR_POR condicion_order """
    if len(t) == 3:  # Para "DONDE condicion" y "ORDENAR_POR condicion_order"
        t[0] = [t[1], t[2]]
    else:  # Para "empty"
        t[0] = None


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