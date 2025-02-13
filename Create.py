import ply.yacc as yacc
from AnalizadorLexico import tokens  # Importar los tokens de tu analizador léxico

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
    | crear"""
    t[0] = t[1]

