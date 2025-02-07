import ply.yacc as yacc
from AnalizadorLexico import tokens  # Importar los tokens de tu analizador léxico

# Definir la precedencia de los operadores
precedence = (
    ('left', 'Y', 'O'),  # Operadores lógicos
    ('left', 'MENOR', 'MAYOR', 'MENOR_IGUAL', 'MAYOR_IGUAL', 'IGUALDAD', 'DIFERENTE'),  # Comparadores
    ('left', 'MAS', 'MENOS'),  # Operadores aritméticos
    ('left', 'MULTIPLICACION', 'DIVISION', 'MODULO'),  # Operadores aritméticos
)

# Definición de la gramática del analizador sintáctico
def p_instruccion(t):
    '''instruccion : seleccion
                   | insertar
                   | actualizar
                   | eliminar
                   | soltar
                   | crear    
                   | transaccion''' 
    t[0] = t[1]

###########################################################################
def p_crear(t):
    '''crear : CREAR TABLA IDENTIFICADOR PARENTESIS_IZQ lista_columnas PARENTESIS_DER'''
    t[0] = ('crear', t[3], t[5])

def p_lista_columnas_crear(t):
    '''lista_columnas : lista_columnas COMA lista_columna
                      | lista_columna'''
    if len(t)==4:
        t[0]=t[1]+[t[3]]
    else:
        t[0]=[t[1]]


def p_tipo_dato(t):
    '''tipo_dato : ENTERO 
                | CADENA 
                | CARACTER
                | FECHA
                | BOOLEANO
                | DECIMAL
                | TEXTO especificacion
                | FLOTANTE'''
    if len(t) == 3:
        t[0]=(t[1],t[2])
    else:
        t[0] = t[1]

def p_especificacion(t):
    '''especificacion : PARENTESIS_IZQ NUMERO PARENTESIS_DER'''
    t[0]=t[2]

def p_restricciones(t):
    '''restricciones : restricciones restriccion
                     | restriccion
                     | empty '''
    
    if len(t)==3:
        t[0]=t[1]+[t[2]]
    elif len(t)==2:
        t[0]=[t[1]]
    else:
        t[0]:[]

def p_restriccion(t):
    '''restriccion : CLAVE_PRIMARIA
                   | CLAVE_FORANEA
                   | AUTOINCREMENTAL
                   | NO_NULO'''
    t[0] = t[1] 

def p_lista_columna_crear(t):
    '''lista_columna : IDENTIFICADOR  tipo_dato restricciones'''
    nombreColumna=t[1]
    tipoDato=t[2]
    restricciones = list(t[3])  
    
    t[0]=("columna",nombreColumna,tipoDato,restricciones)
###########################################################################

###########################################################################
def p_seleccion(t):
    '''seleccion : SELECCIONAR lista_columnas DESDE IDENTIFICADOR condicion_opt'''
    t[0] = ('seleccion', t[2], t[4], t[5])
    if t[5] == None:
        t[0] = ('seleccion', t[2], t[4])

# Agregar la regla para manejar el token 'TODO' (asterisco)
def p_lista_columnas(t):
    '''lista_columnas : IDENTIFICADOR
                      | lista_columnas COMA IDENTIFICADOR
                      | TODO'''  # Agregar aquí la opción para 'TODO' (el asterisco)
    if len(t) == 2:
        t[0] = [t[1]]
    elif len(t) == 4:
        t[0] = t[1] + [t[3]]
    else:
        t[0] = ['*']  # Si es el caso de 'TODO'

def p_condicion_opt(t):
    '''condicion_opt : DONDE condicion
                     | empty'''
    if len(t) == 3:
        t[0] = t[2]
    else:
        t[0] = None

def p_condicion(t):
    '''condicion : IDENTIFICADOR comparador valor
                 | condicion Y condicion
                 | condicion O condicion'''
    if len(t) == 4:
        t[0] = (t[1], t[2], t[3])
    else:
        t[0] = (t[1], t[2], t[3], t[4])

# Regla para el operador de comparación
def p_comparador(t):
    '''comparador : IGUALDAD
                  | MAYOR
                  | MENOR
                  | MAYOR_IGUAL
                  | MENOR_IGUAL
                  | DIFERENTE'''
    t[0] = t[1]

def p_valor(t):
    '''valor : NUMERO
             | CADENA
             | IDENTIFICADOR'''
    t[0] = t[1]


###########################################################################

###########################################################################
def p_insertar(t):
    '''insertar : INSERTAR EN IDENTIFICADOR lista_columnas VALORES PARENTESIS_IZQ lista_valores PARENTESIS_DER'''
    t[0] = ('insertar', t[3], t[6])


def p_lista_valores(t):
    '''lista_valores : valor
                     | lista_valores COMA valor'''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[0] = t[1] + [t[3]]
###########################################################################

###########################################################################
def p_actualizar(t):
    '''actualizar : ACTUALIZAR IDENTIFICADOR COLOCAR lista_asignaciones condicion_opt'''
    t[0] = ('actualizar', t[2], t[4], t[5])

def p_lista_asignaciones(t):
    '''lista_asignaciones : IDENTIFICADOR IGUALDAD valor
                          | lista_asignaciones COMA IDENTIFICADOR IGUALDAD valor'''
    if len(t) == 4:
        t[0] = [(t[1], t[2], t[3])]
    else:
        t[0] = t[1] + [(t[3], t[4], t[5])]
###########################################################################

###########################################################################
def p_eliminar(t):
    '''eliminar : ELIMINAR DESDE IDENTIFICADOR condicion_opt'''
    t[0] = ('eliminar', t[3], t[4])
###########################################################################

###########################################################################
def p_soltar(t):
    '''soltar : SOLTAR TABLA IDENTIFICADOR'''
    t[0]=('soltar',t[3])
###########################################################################

###########################################################################
def p_transaccion(t):
    '''transaccion : INICIAR_TRANSACCION
                   | CONFIRMAR
                   | REVERTIR'''
    t[0] = t[1]
###########################################################################

# Regla de la producción vacía (para manejar la opción 'empty')
def p_empty(t):
    'empty :'
    pass

# Manejo de errores sintácticos
def p_error(t):
    if t:
        print(f"Error de sintaxis en '{t.value}'")
    else:
        print("Error de sintaxis en la entrada")

# Construcción del analizador
parser = yacc.yacc()

# Función para analizar una consulta SQL en español
def analizar_consulta(consulta):
    return parser.parse(consulta)

# Prueba con una consulta SQL en español
consulta_prueba = '''CREAR TABLA wasaa (
                        id ENTERO AUTOINCREMENTAL CLAVE PRIMARIA,
                        nombre "CADENA" NO NULO)'''

resultado = analizar_consulta(consulta_prueba)
print("Resultado de la consulta:")
print(resultado)
