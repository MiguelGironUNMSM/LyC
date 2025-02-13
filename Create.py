import ply.yacc as yacc
from AnalizadorLexico import tokens  # Importar los tokens de tu analizador léxico

def p_crear(t):
    """crear : CREAR TABLA IDENTIFICADOR PARENTESIS_IZQ lista_columnas_crear PARENTESIS_DER"""
    t[0] = ("crear", t[3], t[5])

def p_lista_columnas_crear(t):
    """lista_columnas_crear : lista_columnas_crear COMA lista_columna_crear
                      | lista_columna_crear"""
    if len(t) == 4:
        t[0] = t[1] + [t[3]]
    else:
        t[0] = [t[1]]

