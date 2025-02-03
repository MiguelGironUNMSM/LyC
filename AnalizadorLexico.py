import ply.lex as lex

tokens = ['SELECCIONAR', 'DESDE', 'DONDE', 'IDENTIFIER', 'NUMBER', 'EQUALS']

t_SELECCIONAR = r'SELECCIONAR'
t_DESDE = r'DESDE'
t_DONDE = r'DONDE'
t_EQUALS = r'='
t_ignore = ' \t'  # Ignorar espacios y tabs

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print(f"Carácter inesperado: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

# Prueba con una consulta
lexer.input("SELECCIONAR nombre DESDE usuarios WHERE edad = 25")

for tok in lexer:
    print(tok)