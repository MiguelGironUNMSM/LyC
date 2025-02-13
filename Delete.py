import ply.yacc as yacc
from AnalizadorLexico import tokens  # Importar los tokens de tu analizador léxico

def p_eliminar(t):
    """eliminar : ELIMINAR DESDE IDENTIFICADOR condicion_opt"""
    t[0] = ("eliminar", t[3], t[4])