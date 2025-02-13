import ply.yacc as yacc
from AnalizadorLexico import tokens

# Definir la precedencia de los operadores
precedence = (
    ("left", "Y", "O"),  # Operadores lógicos
    (
        "left",
        "MENOR",
        "MAYOR",
        "MENOR_IGUAL",
        "MAYOR_IGUAL",
        "IGUALDAD",
        "DIFERENTE",
    ),  # Comparadores
    ("left", "MAS", "MENOS"),  # Operadores aritméticos
    ("left", "MULTIPLICACION", "DIVISION", "MODULO"),  # Operadores aritméticos
)

# Definición de la gramática del analizador sintáctico
def p_instruccion(t):
    """instruccion : seleccion
    | insertar
    | alterar
    | actualizar
    | eliminar
    | soltar
    | crear
    | transaccion"""
    t[0] = t[1]

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
        t[0]= []


def p_restriccion(t):
    """restriccion : CLAVE_PRIMARIA
                    | CLAVE_FORANEA
                    | AUTOINCREMENTAL
                    | NO_NULO"""
    t[0] = t[1]


def p_lista_columna_crear(t):
    """lista_columna_crear : IDENTIFICADOR  tipo_dato restricciones"""
    nombreColumna = t[1]
    tipoDato = t[2]
    restricciones = list(t[3])

    t[0] = ("columna", nombreColumna, tipoDato, restricciones)

