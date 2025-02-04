import ply.lex as lex

tokens = [
'SELECCIONAR', # SELECT
'DESDE', # FROM
'CREAR', # CREATE
'INSERTAR', # INSERT
'ACTUALIZAR', # UPDATE
'ELIMINAR', # DELETE
'ALTERAR', # ALTER
'TABLA', # TABLE
'DONDE', # WHERE
'ORDENAR_POR', # ORDER BY
'AGRUPAR_POR', # GROUP BY
'CLAVE_PRIMARIA', # PRIMARY KEY
'CLAVE_FORANEA', # FOREIGN KEY
'INICIAR_TRANSACCION', # BEGIN TRANSACTION
'CONFIRMAR', # COMMIT
'REVERTIR', # ROLLBACK
'SI', # IF
'SINO', # ELSE
'CASO', # CASE
'ENTONCES', # THEN
'Y', # AND
'O', # OR
'NO', # NOT
'CONTAR', # COUNT
'SUMA', # SUM
'PROMEDIO', # AVG
'MAXIMO', # MAX
'MINIMO', # MIN
'DISTINTO', # DISTINCT
'COMO', # AS
'ENTERO', # INTEGER
'TEXTO', # TEXT
'FECHA', # DATE
'BOOLEANO', # BOOLEAN
'DECIMAL', # DECIMAL
'NULO', # NULL
'UNIR', # JOIN
'UNIR_INTERIOR', # INNER JOIN
'UNIR_IZQUIERDA', # LEFT JOIN
'UNIR_DERECHA', # RIGHT JOIN
'IDENTIFICADOR', # IDENTIFICADOR
'IDENTIFICADOR_INVALIDO', 
'CADENA', #VARCHAR
'NUMERO', # NÚMERO
'FLOTANTE', #FLOAT
'COMPARACION', # '='
'COMA', # ','
'TODO', # '*'
'CONVERTIR', #CAST
'PUNTO', #.
'COMENTARIO' #--
'SALTO_DE_LINEA' #\n
'EN', #IN
'VALORES', #VALUES
'ASCENDENTE', #ASC
'DESCENDENTE',#DESC
'LIMITAR', #LIMIT
'DIFERENTE', #!=
'EN', #IN
'MAYOR',#>
'MENOR',#<
'MAYOR_IGUAL',#>=
'MENOR_IGUAL',#<=
'PARENTESIS_DER',#(
'PARENTESIS_IZQ',#)
]

t_SELECCIONAR = r'SELECCIONAR'
t_INSERTAR = r'INSERTAR'
t_ACTUALIZAR = r'ACTUALIZAR'
t_ELIMINAR = r'ELIMINAR'
t_DESDE = r'DESDE'
t_DONDE = r'DONDE'
t_ORDENAR_POR = r'ORDENAR POR'
t_AGRUPAR_POR = r'AGRUPAR POR'
t_CREAR = r'CREAR'
t_ALTERAR = r'ALTERAR'
t_TABLA = r'TABLA'
t_CLAVE_PRIMARIA = r'CLAVE PRIMARIA'
t_CLAVE_FORANEA = r'CLAVE FORANEA'
t_INICIAR_TRANSACCION = r'INICIAR TRANSACCION'
t_CONFIRMAR = r'CONFIRMAR'
t_REVERTIR = r'REVERTIR'
t_SI = r'SI'
t_SINO = r'SINO'
t_CASO = r'CASO'
t_ENTONCES = r'ENTONCES'
t_Y = r'Y'
t_O = r'O'
t_NO = r'NO'
t_CONTAR = r'CONTAR'
t_SUMA = r'SUMA'
t_PROMEDIO = r'PROMEDIO'
t_MAXIMO = r'MAXIMO'
t_MINIMO = r'MINIMO'
t_DISTINTO = r'DISTINTO'
t_COMO = r'COMO'
t_ENTERO = r'ENTERO'
t_TEXTO = r'TEXTO'
t_FECHA = r'FECHA'
t_BOOLEANO = r'BOOLEANO'
t_DECIMAL = r'DECIMAL'
t_NULO = r'NULO'
t_UNIR = r'UNIR'
t_UNIR_INTERIOR = r'UNIR INTERIOR'
t_UNIR_IZQUIERDA = r'UNIR IZQUIERDA'
t_UNIR_DERECHA = r'UNIR DERECHA'
t_CONVERTIR=r'CONVERTIR'
t_COMPARACION = r'='
t_COMA = r','
t_PUNTO = r'\.'
t_TODO = r"\*" 
t_ignore = ' \t'  # Ignorar espacios y tabs
t_EN = r'EN'
t_VALORES = r'VALORES'
t_ASCENDENTE = r'ASCENDENTE'
t_DESCENDENTE = r'DESCENDENTE'
t_LIMITAR = r'LIMITAR'
t_DIFERENTE = r'DIFERENTE'
t_MAYOR = r'MAYOR'
t_MENOR = r'MENOR'
t_MAYOR_IGUAL = r'MAYOR IGUAL'
t_MENOR_IGUAL = r'MENOR IGUAL'
t_PARENTESIS_DER = r'PARENTESIS DER'
t_PARENTESIS_IZQ = r'PARENTESIS IZQ'

def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    keywords = {
    'SELECCIONAR': 'SELECCIONAR', 'INSERTAR': 'INSERTAR', 'ACTUALIZAR': 'ACTUALIZAR', 'ELIMINAR': 'ELIMINAR',
    'DESDE': 'DESDE', 'DONDE': 'DONDE', 'ORDENAR': 'ORDENAR_POR', 'AGRUPAR': 'AGRUPAR_POR', 'CREAR': 'CREAR',
    'ALTERAR': 'ALTERAR', 'TABLA': 'TABLA', 'CLAVE': 'CLAVE_PRIMARIA', 'INICIAR': 'INICIAR_TRANSACCION',
    'CONFIRMAR': 'CONFIRMAR', 'REVERTIR': 'REVERTIR', 'SI': 'SI', 'SINO': 'SINO', 'CASO': 'CASO',
    'ENTONCES': 'ENTONCES', 'Y': 'Y', 'O': 'O', 'NO': 'NO', 'CONTAR': 'CONTAR', 'SUMA': 'SUMA', 'PROMEDIO': 'PROMEDIO',
    'MAXIMO': 'MAXIMO', 'MINIMO': 'MINIMO', 'DISTINTO': 'DISTINTO', 'COMO': 'COMO', 'ENTERO': 'ENTERO', 'TEXTO': 'TEXTO',
    'FECHA': 'FECHA', 'BOOLEANO': 'BOOLEANO', 'DECIMAL': 'DECIMAL', 'NULO': 'NULO', 'UNIR': 'UNIR',
    'INTERIOR': 'UNIR_INTERIOR', 'IZQUIERDA': 'UNIR_IZQUIERDA', 'DERECHA': 'UNIR_DERECHA', 
    }
    t.type = keywords.get(t.value.upper(), 'IDENTIFICADOR')
    return t

def t_IDENTIFICADOR_INVALIDO(t):
    r'[^a-zA-Z_\s-]+[a-zA-Z0-9_]*[a-zA-Z]+'
    print(f"Identificador inválido: {t.value}")
    t.lexer.skip(1)

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FLOTANTE(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

def t_COMENTARIO(t):
    r'--.*'
    pass

def t_error(t):
    print(f"Carácter inesperado: {t.value[0]}")
    t.lexer.skip(1)

def t_SALTO_DE_LINEA(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

lexer = lex.lex()

# Prueba con una consulta
test_query = '''SELECCIONAR *
DESDE tabla1
-- asdajdjsajdasjfasfjasjdfjasdakdj sada sda 
DONDE columna1 = 10 23Ss ddS12 =2w3Sfsa _das21 #dsa IZQUIERDO'''
lexer.input(test_query)

for tok in lexer:
    print(tok)