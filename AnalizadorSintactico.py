import ply.yacc as yacc
from AnalizadorLexico import tokens  # Importar los tokens de tu analizador léxico

# Precedencia
# Instruccion
# Crear
# Select
# Alter
# Update

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
                    ALTERAR TABLA usuarios
AGREGAR edad ENTERO(3) NO_NULO,
AGREGAR RESTRICCION pk_usuarios CLAVE_PRIMARIA (id_usuario),
AGREGAR RESTRICCION unq_correo UNICO (correo);

"""
                                                
resultado = analizar_consulta(consulta_prueba)
print("Resultado de la consulta:")
print(resultado)
