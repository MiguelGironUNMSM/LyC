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
    | insertar
    | alterar
    | actualizar
    | eliminar
    | soltar
    | crear
    | transaccion"""
    t[0] = t[1]


###########################################################################
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


###########################################################################


###########################################################################
def p_seleccion(t):
    """seleccion : SELECCIONAR lista_floro lista_columnas DESDE IDENTIFICADOR condicion_opt"""
    t[0] = ("seleccion", t[2], t[3], t[5],t[6])
    if t[6] == None:
        t[0] = ("seleccion", t[2], t[3], t[4], t[5])

def p_lista_floro(t):
    """lista_floro : lista_floro floro
                   | floro
    """
    if len(t)==3:
        t[0]=(t[1],t[2])
    else:
        t[0]=t[1]

def p_floro(t):
    """floro : DISTINTO
             | PRIMEROS VALOR_NUMERO
             | empty
    """
    if 'DISTINTO' in t:  # Si se encontró la palabra DISTINTO
        t[0] = "DISTINTO"
    elif len(t) == 3:  # Si es TOP seguido de un número
        t[0] = ("PRIMEROS", t[2])  # Aquí t[2] es el número
    else:
        t[0] = None  # Cuando floro está vacío (empty)

# Agregar la regla para manejar el token 'TODO' (asterisco)
def p_lista_columnas(t):
    """lista_columnas : IDENTIFICADOR
                    | lista_columnas COMA IDENTIFICADOR
                    | TODO"""  # Agregar aquí la opción para 'TODO' (el asterisco)
    if len(t) == 2:
        t[0] = ('COLUMNAS',[t[1]])
    elif len(t) == 4:
        t[0] = ('COLUMNAS',t[1][1] + [t[3]])
    else:
        t[0] = ["*"]  # Si es el caso de 'TODO'


def p_condicion_opt(t):
    """condicion_opt : DONDE condicion
                    | empty
                    | ORDENAR_POR condicion_order """
    if len(t) == 3:  # Para "DONDE condicion" y "ORDENAR_POR condicion_order"
        t[0] = [t[1], t[2]]
    else:  # Para "empty"
        t[0] = None


def p_condicion(t):
    """condicion : IDENTIFICADOR comparador valor
                | condicion Y condicion
                | condicion O condicion"""
    if len(t) == 4:
        t[0] = (t[1], t[2], t[3])
    else:
        t[0] = (t[1], t[2], t[3], t[4])


# Regla para el operador de comparación
def p_comparador(t):
    """comparador : IGUALDAD
                    | MAYOR
                    | MENOR
                    | MAYOR_IGUAL
                    | MENOR_IGUAL
                    | DIFERENTE"""
    t[0] = t[1]


def p_valor(t):
    """valor : VALOR_NUMERO
            |  VALOR_CADENA
            |  VALOR_BOOLEANO
            |  VALOR_FLOTANTE"""
    
    t[0] = t[1]

def p_condicion_order(t):
    """condicion_order : IDENTIFICADOR ASCENDENTE
                       | IDENTIFICADOR DESCENDENTE
                       | IDENTIFICADOR"""
    if len(t)==3:
        t[0]=(t[1],t[2])
    else:
        t[0]=(t[1],'ASCENDENTE')

###########################################################################


###########################################################################
def p_insertar(t):
    """insertar : INSERTAR EN IDENTIFICADOR PARENTESIS_IZQ lista_columnas_creadas PARENTESIS_DER VALORES lista_filas"""
    t[0] = ("insertar", t[3], t[5], t[8])


def p_lista_columnas_creadas(t):
    """lista_columnas_creadas : IDENTIFICADOR
                              | lista_columnas_creadas COMA IDENTIFICADOR"""
    if len(t) == 4:
        t[0] = ('COLUMNAS',t[1][1] + [t[3]])
    else:
        t[0] = ('COLUMNAS',[t[1]])

def p_lista_filas(t):
    """lista_filas : fila 
                  | lista_filas COMA fila"""
    if len(t)==2:
        t[0]=[t[1]]
    else:
        t[0]=t[1]+[t[3]]

def p_fila(t):
    """fila : PARENTESIS_IZQ lista_valores PARENTESIS_DER"""
    t[0]=t[2]

def p_lista_valores(t):
    """lista_valores : valor
    | lista_valores COMA valor"""
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[0] = t[1] + [t[3]]

###########################################################################


# Regla principal para ALTER TABLE
def p_alterar(t):
    """alterar : ALTERAR TABLA IDENTIFICADOR alteraciones"""
    # t[3]: nombre de la tabla
    # t[4]: lista de alteraciones (cada una representa una modificación)
    t[0] = ("alter_table", t[3], t[4])


# Permitir una o más alteraciones separadas por coma
def p_alteraciones_single(t):
    """alteraciones : alteracion"""
    t[0] = [t[1]]


def p_alteraciones_multiple(t):
    """alteraciones : alteracion COMA alteraciones"""
    t[0] = [t[1]] + t[3]


# 1. Agregar una nueva columna (se puede permitir la palabra opcional COLUMN)
def p_alteracion_add(t):
    """alteracion : AGREGAR opt_column lista_columna_crear"""
    t[0] = ("add_column", t[3])

# Regla para la opción COLUMN (puede estar o no)
def p_opt_column(t):
    """opt_column : COLUMNA
                  | empty"""
    t[0] = t[1] if len(t) > 1 else None

# 2. Eliminar una columna (con o sin la palabra COLUMN):
def p_alteracion_drop(t):
    """alteracion : SOLTAR opt_column IDENTIFICADOR"""
    t[0] = ("drop_column", t[3])


# 3. Modificar (alterar) la definición de una columna:
#    Ejemplo: ALTER TABLE [table_name] MODIFY COLUMN [column definition (nombre, tipo de dato, reestriccion)];
def p_alteracion_alter(t):
    """alteracion : MODIFICAR opt_column IDENTIFICADOR lista_columna_crear"""
    # t[3] es el nombre de la columna, t[4] la nueva definición (por ejemplo, nuevo tipo)
    t[0] = ("modify_column", t[3], t[4])


# 4. Renombrar una columna:  
#    Ejemplo: ALTER TABLE [table_name] RENAME COLUMN [OldName] TO [NewName];
def p_alteracion_rename(t):
    """alteracion : RENOMBRAR opt_column IDENTIFICADOR A IDENTIFICADOR"""
    # t[3] es el nombre actual, t[5] es el nuevo nombre
    t[0] = ("rename_column", t[3], t[5])

# 5. Cambiar una columna:
# ALTER TABLE [table_name] CHANGE [old_column_name] [new_column_name] [column definition]
def p_alteracion_change(t): 
    """alteracion : CAMBIAR opt_column IDENTIFICADOR IDENTIFICADOR lista_columna_crear"""

# # 5. Agregar una restricción (constraint):
# #    Ejemplo: ALTER TABLE Persons ADD CONSTRAINT PK_Person PRIMARY KEY (ID);
# def p_alteracion_add_constraint(t):
#     """alteracion : ADD CONSTRAINT IDENTIFICADOR constraint_definicion"""
#     # t[3] es el nombre de la restricción, t[4] su definición
#     t[0] = ("add_constraint", t[3], t[4])


# 6. Eliminar una restricción:
# #    Ejemplo: ALTER TABLE Persons DROP CONSTRAINT PK_Person;
# def p_alteracion_drop_constraint(t):
#     """alteracion : DROP CONSTRAINT IDENTIFICADOR"""
#     # t[3] es el nombre de la restricción a eliminar
#     t[0] = ("drop_constraint", t[3])


# ---------------------------
# Reglas auxiliares
# ---------------------------


# Ejemplo sencillo para la definición de restricción.
# Puedes ampliarlo según las necesidades.
# def p_constraint_definicion(t):
#     """constraint_definicion : PRIMARY KEY PARENTESIS_IZQ IDENTIFICADOR PARENTESIS_DER
#     | FOREIGN KEY PARENTESIS_IZQ IDENTIFICADOR PARENTESIS_DER REFERENCES IDENTIFICADOR PARENTESIS_IZQ IDENTIFICADOR PARENTESIS_DER
#     """
#     # Aquí se procesaría la definición de la restricción.
#     # Se retorna una tupla o estructura que represente la restricción.
#     if t[1].upper() == "PRIMARY":
#         t[0] = ("primary_key", t[4])
#     else:
#         t[0] = ("foreign_key", t[4], t[7], t[10])


###########################################################################
def p_actualizar(t):
    """actualizar : ACTUALIZAR IDENTIFICADOR COLOCAR lista_asignaciones condicion_opt"""
    t[0] = ("actualizar", t[2], t[4], t[5])


def p_lista_asignaciones(t):
    """lista_asignaciones : IDENTIFICADOR IGUALDAD valor
    | lista_asignaciones COMA IDENTIFICADOR IGUALDAD valor"""
    if len(t) == 4:
        t[0] = [(t[1], t[2], t[3])]
    else:
        t[0] = t[1] + [(t[3], t[4], t[5])]


###########################################################################


###########################################################################
def p_eliminar(t):
    """eliminar : ELIMINAR DESDE IDENTIFICADOR condicion_opt"""
    t[0] = ("eliminar", t[3], t[4])


###########################################################################


###########################################################################
def p_soltar(t):
    """soltar : SOLTAR TABLA IDENTIFICADOR"""
    t[0] = ("soltar", t[3])


###########################################################################


###########################################################################
def p_transaccion(t):
    """transaccion : INICIAR_TRANSACCION
    | CONFIRMAR
    | REVERTIR"""
    t[0] = t[1]


###########################################################################


# Regla de la producción vacía (para manejar la opción 'empty')
def p_empty(t):
    "empty :"
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
consulta_prueba = """                           
                    ALTERAR TABLA kuka AGREGAR mamacita cadena(8), AGREGAR papacito entero
"""
                                                
resultado = analizar_consulta(consulta_prueba)
print("Resultado de la consulta:")
print(resultado)
