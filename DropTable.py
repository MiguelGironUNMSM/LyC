import ply.yacc as yacc
from AnalizadorLexico import tokens  # Importar los tokens de tu analizador léxico

def p_soltar(t):
    """soltar : SOLTAR TABLA IDENTIFICADOR"""
    t[0] = ("soltar", t[3])
