import ply.lex as lex



tokens = [

# Comandos SQL
'SELECCIONAR', # SELECT
'DESDE', # FROM
'CREAR', # CREATE
'INSERTAR', # INSERT
'ACTUALIZAR', # UPDATE
'ELIMINAR', # DELETE
'ALTERAR', # ALTER
'TABLA', # TABLE

#Clausulas SQL
'DONDE', # WHERE
'ORDENAR_POR', # ORDER BY
'AGRUPAR_POR', # GROUP BY
'TENIENDO', #HAVING

#Claves
'CLAVE_PRIMARIA', # PRIMARY KEY
'CLAVE_FORANEA', # FOREIGN KEY

#Transacciones
'INICIAR_TRANSACCION', # BEGIN TRANSACTION
'CONFIRMAR', # COMMIT
'REVERTIR', # ROLLBACK

#Condicionales
'SI', # IF
'SINO', # ELSE
'CASO', # CASE
'ENTONCES', # THEN

#Operadores Logicos
'Y', # AND
'O', # OR
'NO', # NOT

#Funciones de Agregacion
'CONTAR', # COUNT
'SUMA', # SUM
'PROMEDIO', # AVG
'MAXIMO', # MAX
'MINIMO', # MIN

#Comparadores y operadores
'MAYOR',#>
'MENOR',#<
'MAYOR_IGUAL',#>=
'MENOR_IGUAL',#<=
'IGUALDAD', # '='
'DIFERENTE', #!=

#Operadores aritmeticos
'MAS', #+
'MENOS', #-
'MULTIPLICACION', #*
'DIVISION', #/
'MODULO', #%

#Tipos de datos
'FECHA', # DATE
'BOOLEANO', # BOOLEAN
'DECIMAL', # DECIMAL
'NULO', # NULL
'ENTERO', # INTEGER
'TEXTO', # TEXT
'CARACTER', # CHAR
#Joins
'UNIR', # JOIN
'UNIR_INTERIOR', # INNER JOIN
'UNIR_IZQUIERDA', # LEFT JOIN
'UNIR_DERECHA', # RIGHT JOIN

#Identificadores
'IDENTIFICADOR', # IDENTIFICADOR
'IDENTIFICADOR_INVALIDO', 
'CADENA', #VARCHAR
'NUMERO', # NÚMERO
'FLOTANTE', #FLOAT

#Caracteres especiales
'COMA', # ','
'TODO', # '*'
'PUNTO', #.
'COMENTARIO', #--
'PARENTESIS_DER',#(
'PARENTESIS_IZQ',#)
'SALTO_DE_LINEA', #\n
'PYC', #;

#Otros
'CONVERTIR', #CAST
'EN', #IN
'ES', #IS
'VALORES', #VALUES
'ASCENDENTE', #ASC
'DESCENDENTE',#DESC
'LIMITAR', #LIMIT
'COMO', # AS
'SIMILAR_A', #LIKE
'DISTINTO', # DISTINCT
'ENTRE', #BETWEEN
'OBTENER', #GET
'COLOCAR', #SET 
]

#Comandos SQL
t_SELECCIONAR = r'SELECCIONAR'
t_INSERTAR = r'INSERTAR'
t_ACTUALIZAR = r'ACTUALIZAR'
t_ELIMINAR = r'ELIMINAR'
t_CREAR = r'CREAR'
t_ALTERAR = r'ALTERAR'
t_TABLA = r'TABLA'
t_DESDE = r'DESDE'

#Clausulas SQL
t_DONDE = r'DONDE'
t_ORDENAR_POR = r'ORDENAR POR'
t_AGRUPAR_POR = r'AGRUPAR POR'
t_TENIENDO = r'TENIENDO'

#Claves
t_CLAVE_PRIMARIA = r'CLAVE PRIMARIA'
t_CLAVE_FORANEA = r'CLAVE FORANEA'

#Transacciones
t_INICIAR_TRANSACCION = r'INICIAR TRANSACCION'
t_CONFIRMAR = r'CONFIRMAR'
t_REVERTIR = r'REVERTIR'

#Condicionales
t_SI = r'SI'
t_SINO = r'SINO'
t_CASO = r'CASO'
t_ENTONCES = r'ENTONCES'

#Operadores Logicos
t_Y = r'Y'
t_O = r'O'
t_NO = r'NO'

#Funciones de Agregacion
t_CONTAR = r'CONTAR'
t_SUMA = r'SUMA'
t_PROMEDIO = r'PROMEDIO'
t_MAXIMO = r'MAXIMO'
t_MINIMO = r'MINIMO'

#Comparadores y operadores
t_MAYOR = r'>'
t_MENOR = r'<'
t_MAYOR_IGUAL = r'>='
t_MENOR_IGUAL = r'<='
t_IGUALDAD = r'='
t_DIFERENTE = r'!='

#Operadores aritmeticos
t_MAS = r'\+'
t_MENOS = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_MODULO = r'%'

#Tipos de datos
t_FECHA = r'FECHA'
t_BOOLEANO = r'BOOLEANO'
t_DECIMAL = r'DECIMAL'
t_NULO = r'NULO'
t_ENTERO = r'ENTERO'
t_TEXTO = r'TEXTO'
t_CARACTER = r'CARACTER'

#Joins
t_UNIR = r'UNIR'
t_UNIR_INTERIOR = r'UNIR INTERIOR'
t_UNIR_IZQUIERDA = r'UNIR IZQUIERDA'
t_UNIR_DERECHA = r'UNIR DERECHA'

#Caracteres especiales
t_COMA = r','
t_PUNTO = r'\.'
t_TODO = r"\*" 
t_ignore = ' \t'  # Ignorar espacios y tabs
t_PARENTESIS_DER = r'\)'
t_PARENTESIS_IZQ = r'\('
t_PyC = r'\;'

#Otros
t_CONVERTIR=r'CONVERTIR'
t_EN = r'EN'
t_ES = r'ES'
t_VALORES = r'VALORES'
t_ASCENDENTE = r'ASCENDENTE'
t_DESCENDENTE = r'DESCENDENTE'
t_LIMITAR = r'LIMITAR'
t_COMO = r'COMO'
t_DISTINTO = r'DISTINTO'
t_ENTRE = r'ENTRE'
t_OBTENER = r'OBTENER'
t_COLOCAR = r'COLOCAR'

def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    keywords = {
    'SELECCIONAR': 'SELECCIONAR', 'INSERTAR': 'INSERTAR', 'ACTUALIZAR': 'ACTUALIZAR', 'ELIMINAR': 'ELIMINAR', 'DESDE': 'DESDE','ALTERAR': 'ALTERAR', 'TABLA': 'TABLA', 'CREAR': 'CREAR',
    'DONDE': 'DONDE', 'ORDENAR': 'ORDENAR', 'AGRUPAR': 'AGRUPAR', 'POR': 'POR',
    'CLAVE': 'CLAVE', 'PRIMARIA': 'PRIMARIA', 'SECUNDARIA': 'SECUNDARIA',
    'INICIAR': 'INICIAR','TRANSACCION': 'TRANSACCION','CONFIRMAR': 'CONFIRMAR', 'REVERTIR': 'REVERTIR',
    'SI': 'SI', 'SINO': 'SINO', 'CASO': 'CASO', 'ENTONCES': 'ENTONCES', 
    'Y': 'Y', 'O': 'O', 'NO': 'NO',
    'CONTAR': 'CONTAR', 'SUMA': 'SUMA', 'PROMEDIO': 'PROMEDIO', 'MAXIMO': 'MAXIMO', 'MINIMO': 'MINIMO',
    'ENTERO': 'ENTERO', 'TEXTO': 'TEXTO', 'FECHA': 'FECHA', 'BOOLEANO': 'BOOLEANO', 'DECIMAL': 'DECIMAL', 'NULO': 'NULO', 'UNIR': 'UNIR', 'INTERIOR': 'INTERIOR', 'IZQUIERDA': 'IZQUIERDA', 'DERECHA': 'DERECHA',
    'ES':'ES', 'EN': 'EN', 'VALORES':'VALORES', 'ASCENDENTE':'ASCENDENTE', 'DESCENDENTE':'DESCENDENTE', 'LIMITAR':'LIMITAR', 'DIFERENTE':'DIFERENTE', 'MAYOR':'MAYOR', 'MENOR':'MENOR', 'SIMILAR':'SIMILAR', 'A':'A', 'DISTINTO': 'DISTINTO', 'COMO': 'COMO', 'ENTRE': 'ENTRE', 'OBTENER': 'OBTENER', 'COLOCAR': 'COLOCAR'
    }
    
    
    t.type = keywords.get(t.value.upper(), 'IDENTIFICADOR')
    return t

def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

def t_FLOTANTE(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
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

def t_IDENTIFICADOR_INVALIDO(t):
    r'[^a-zA-Z_\s\(-]+[a-zA-Z0-9_]*[a-zA-Z]+'
    print(f"Identificador inválido: {t.value}")
    t.lexer.skip(1)
    
lexer = lex.lex()

# Prueba con una consulta
test_query = '''SELECCIONAR (Columna1 - Columna2) COMO rata
                DESDE data 12 
                DONDE columna1 = 1.23'''
lexer.input(test_query)

for tok in lexer:
    print(tok)