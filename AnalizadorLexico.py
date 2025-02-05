import ply.lex as lex



tokens = [

# Definición de Datos
'CREAR', # CREATE
'ALTERAR', # ALTER
'SOLTAR', # DROP
'RENOMBRAR', # RENAME

# Manipulación de Datos
'SELECCIONAR', # SELECT
'INSERTAR', # INSERT
'ELIMINAR', # DELETE
'REEMPLAZAR', # REPLACE
'VALORES', # VALUES
'ACTUALIZAR', # UPDATE
'MEZCLAR', # MERGE

# Consulta y Filtrado de Datos
'DESDE', # FROM
'DONDE', # WHERE
'AGRUPAR_POR', # GROUP BY
'ORDENAR_POR', # ORDER BY
'TENIENDO', #HAVING
'TABLA', # TABLE
'LIMITAR', #LIMIT

# Control de Transacciones
'CONFIRMAR', # COMMIT
'REVERTIR', # ROLLBACK
'PUNTO_GUARDADO', # SAVEPOINT
'INICIAR_TRANSACCION', # BEGIN TRANSACTION
'ESTABLECER_TRANSACCION', # SET TRANSACTION

#Operadores Logicos y de Comparación
'Y', # AND
'O', # OR
'NO', # NOT
'MAYOR',#>
'MENOR',#<
'MAYOR_IGUAL',#>=
'MENOR_IGUAL',#<=
'IGUALDAD', # '='
'DIFERENTE', #!=
'ENTRE', #BETWEEN
'SIMILAR_A', #LIKE
'ES_NULO', #IS NULL
'NO_ES_NULO', #IS NOT NULL

# Unión de Tablas
'UNIR', # JOIN
'UNIR_INTERIOR', # INNER JOIN
'UNIR_IZQUIERDA', # LEFT JOIN
'UNIR_DERECHA', # RIGHT JOIN

#Operadores aritmeticos
'MAS', #+
'MENOS', #-
'MULTIPLICACION', #*
'DIVISION', #/
'MODULO', #%

# Palabras clave de subconsulta
'EXISTE', # EXISTS
'TODOS', # ALL
'ALGUNO', # ANY
'ALGUNOS', # SOME
'CUALQUIERA', # ANY
'RANGO', # RANGE

# Palabras clave de funciones de agregación
'CONTAR', # COUNT
'SUMA', # SUM
'PROMEDIO', # AVG
'MAXIMO', # MAX
'MINIMO', # MIN

#Tipos de datos
'FECHA', # DATE
'BOOLEANO', # BOOLEAN
'DECIMAL', # DECIMAL
'NULO', # NULL
'ENTERO', # INTEGER
'TEXTO', # TEXT
'CARACTER', # CHAR
'NO_NULO', #NOT NULL

#Identificadores / Claves
'IDENTIFICADOR', # IDENTIFICADOR
'IDENTIFICADOR_INVALIDO', 
'CADENA', #VARCHAR
'NUMERO', # NÚMERO
'FLOTANTE', #FLOAT
'CLAVE_PRIMARIA', # PRIMARY KEY
'CLAVE_FORANEA', # FOREIGN KEY

# Palabras clave de manejo de procedimientos almacenados
'INICIO', # BEGIN
'FIN', # END
'SI', # IF
'SINO', # ELSE
'CASO', # CASE
'MIENTRAS', # WHILE
'PARA', # FOR
'ENTONCES', # THEN

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

'ASCENDENTE', #ASC
'DESCENDENTE',#DESC
'COMO', # AS
'DISTINTO', # DISTINCT
'OBTENER', #GET
'COLOCAR', #SET 
'AUTOINCREMENTAL', #AUTO_INCREMENT
]

# Definición de Datos
t_CREAR = r'CREAR'
t_ALTERAR = r'ALTERAR'
t_SOLTAR = r'SOLTAR'
t_RENOMBRAR = r'RENOMBRAR'

# Manipulación de Datos
t_SELECCIONAR = r'SELECCIONAR'
t_INSERTAR = r'INSERTAR'
t_ELIMINAR = r'ELIMINAR'
t_REEMPLAZAR = r'REEMPLAZAR'
t_VALORES = r'VALORES'
t_ACTUALIZAR = r'ACTUALIZAR'
t_MEZCLAR = r'MEZCLAR'

# Consulta y Filtrado de Datos
t_DESDE = r'DESDE'
t_DONDE = r'DONDE'
t_AGRUPAR_POR = r'AGRUPAR POR'
t_ORDENAR_POR = r'ORDENAR POR'
t_TENIENDO = r'TENIENDO'
t_TABLA = r'TABLA'
t_LIMITAR = r'LIMITAR'

# Control de Transacciones
t_CONFIRMAR = r'CONFIRMAR'
t_REVERTIR = r'REVERTIR'
t_PUNTO_GUARDADO = r'PUNTO GUARDADO'
t_INICIAR_TRANSACCION = r'INICIAR TRANSACCION'
t_ESTABLECER_TRANSACCION = r'ESTABLECER TRANSACCION'

# Operadores Logicos y de Comparación
t_Y = r'Y'
t_O = r'O'
t_NO = r'NO'
t_MAYOR = r'>'
t_MENOR = r'<'
t_MAYOR_IGUAL = r'>='
t_MENOR_IGUAL = r'<='
t_IGUALDAD = r'='
t_DIFERENTE = r'!='
t_ENTRE = r'ENTRE'
t_SIMILAR_A = r'SIMILAR A'
t_ES_NULO = r'ES NULO'
t_NO_ES_NULO = r'NO ES NULO'

# Unión de Tablas
t_UNIR = r'UNIR'
t_UNIR_INTERIOR = r'UNIR INTERIOR'
t_UNIR_IZQUIERDA = r'UNIR IZQUIERDA'
t_UNIR_DERECHA = r'UNIR DERECHA'

# Operadores aritmeticos 
t_MAS = r'\+'
t_MENOS = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_MODULO=r'%'

# Palabras clave de subconsulta
t_EXISTE = r'EXISTE'
t_TODOS = r'TODOS'
t_ALGUNO = r'ALGUNO'
t_ALGUNOS = r'ALGUNOS'
t_CUALQUIERA = r'CUALQUIERA'
t_RANGO = r'RANGO'

# Palabras clave de funciones de agregación
t_CONTAR = r'CONTAR'
t_SUMA = r'SUMA'
t_PROMEDIO = r'PROMEDIO'
t_MAXIMO = r'MAXIMO'
t_MINIMO = r'MINIMO'

# Tipos de datos
t_FECHA = r'FECHA'
t_BOOLEANO = r'BOOLEANO'
t_DECIMAL = r'DECIMAL'
t_NULO = r'NULO'
t_ENTERO = r'ENTERO'
t_TEXTO = r'TEXTO'
t_CARACTER = r'CARACTER'
t_NO_NULO = r'NO_NULO'

# Identificadores / Claves
t_CLAVE_PRIMARIA = r'CLAVE PRIMARIA'
t_CLAVE_FORANEA = r'CLAVE FORANEA'

# Palabras clave de manejo de procedimientos almacenados
t_INICIO = r'INICIO'
t_FIN = r'FIN'
t_SI = r'SI'
t_SINO = r'SINO'
t_CASO = r'CASO'
t_MIENTRAS = r'MIENTRAS'
t_PARA = r'PARA'
t_ENTONCES = r'ENTONCES'

# Caracteres especiales
t_COMA = r','
t_PUNTO = r'\.'
t_TODO = r"\*" 
t_ignore = ' \t'  # Ignorar espacios y tabs
t_PARENTESIS_DER = r'\)'
t_PARENTESIS_IZQ = r'\('
t_PYC = r'\;'

# Otros
t_CONVERTIR=r'CONVERTIR'
t_EN = r'EN'
t_ES = r'ES'

t_ASCENDENTE = r'ASCENDENTE'
t_DESCENDENTE = r'DESCENDENTE'
t_COMO = r'COMO'
t_DISTINTO = r'DISTINTO'
t_OBTENER = r'OBTENER'
t_COLOCAR = r'COLOCAR'
t_AUTOINCREMENTAL = r'AUTOINCREMENTAL'

def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    keywords = {
    # Definición de Datos
    'CREAR': 'CREAR', 'ALTERAR': 'ALTERAR', 'SOLTAR': 'SOLTAR', 'RENOMBRAR': 'RENOMBRAR',

    # Manipulación de Datos
    'SELECCIONAR': 'SELECCIONAR', 'INSERTAR': 'INSERTAR', 'ELIMINAR': 'ELIMINAR', 
    'REEMPLAZAR': 'REEMPLAZAR', 'VALORES': 'VALORES', 'ACTUALIZAR': 'ACTUALIZAR', 'MEZCLAR': 'MEZCLAR',

    # Consulta y Filtrado de Datos
    'DESDE': 'DESDE', 'DONDE': 'DONDE', 'AGRUPAR': 'AGRUPAR', 'ORDENAR': 'ORDENAR', 'POR': 'POR',
    'TENIENDO': 'TENIENDO', 'TABLA': 'TABLA', 'LIMITAR': 'LIMITAR',

    # Control de Transacciones
    'CONFIRMAR': 'CONFIRMAR', 'REVERTIR': 'REVERTIR', 'PUNTO': 'PUNTO', 'GUARDADO': 'GUARDADO', 
    'INICIAR': 'INICIAR', 'TRANSACCION': 'TRANSACCION', 'ESTABLECER': 'ESTABLECER',

    # Operadores Lógicos y de Comparación
    'Y': 'Y', 'O': 'O', 'NO': 'NO','ENTRE': 'ENTRE', 'SIMILAR_A': 'SIMILAR_A',
    'ES_NULO': 'ES_NULO', 'NO_ES_NULO': 'NO_ES_NULO',

    # Unión de Tablas
    'UNIR': 'UNIR', 'UNIR_INTERIOR': 'UNIR_INTERIOR', 'UNIR_IZQUIERDA': 'UNIR_IZQUIERDA',
    'UNIR_DERECHA': 'UNIR_DERECHA',

    # Palabras clave de Subconsulta
    'EXISTE': 'EXISTE', 'TODOS': 'TODOS', 'ALGUNO': 'ALGUNO', 'ALGUNOS': 'ALGUNOS', 
    'CUALQUIERA': 'CUALQUIERA', 'RANGO': 'RANGO',

    # Palabras clave de Funciones de Agregación
    'CONTAR': 'CONTAR', 'SUMA': 'SUMA', 'PROMEDIO': 'PROMEDIO', 
    'MAXIMO': 'MAXIMO', 'MINIMO': 'MINIMO',

    # Tipos de Datos
    'FECHA': 'FECHA', 'BOOLEANO': 'BOOLEANO', 'DECIMAL': 'DECIMAL', 'NULO': 'NULO',
    'ENTERO': 'ENTERO', 'TEXTO': 'TEXTO', 'CARACTER': 'CARACTER', 'NO_NULO': 'NO_NULO',

    # Identificadores / Claves
    'CLAVE': 'CLAVE', 'PRIMARIA': 'PRIMARIA', 'FORANEA': 'FORANEA',

    # Palabras clave de Manejo de Procedimientos Almacenados
    'INICIO': 'INICIO', 'FIN': 'FIN', 'SI': 'SI', 'SINO': 'SINO', 'CASO': 'CASO',
    'MIENTRAS': 'MIENTRAS', 'PARA': 'PARA', 'ENTONCES': 'ENTONCES',

    # Otros
    'CONVERTIR': 'CONVERTIR', 'EN': 'EN', 'ES': 'ES', 'ASCENDENTE': 'ASCENDENTE', 
    'DESCENDENTE': 'DESCENDENTE', 'COMO': 'COMO', 'DISTINTO': 'DISTINTO',
    'OBTENER': 'OBTENER', 'COLOCAR': 'COLOCAR', 'AUTOINCREMENTAL': 'AUTOINCREMENTAL'
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