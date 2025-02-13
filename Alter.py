import ply.yacc as yacc
from AnalizadorLexico import tokens  # Importar los tokens de tu analizador léxico

# Precedencia...

# ALTER TABLE
def p_alterar(t):
    """alterar : ALTERAR TABLA IDENTIFICADOR alteraciones"""
    t[0] = ("alter_table", t[3], t[4])

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

def p_opt_column(t):
    """opt_column : COLUMNA
                  | empty"""
    t[0] = t[1] if t[1] is not None else None

# 2. Eliminar una columna
def p_alteracion_drop(t):
    """alteracion : SOLTAR opt_column IDENTIFICADOR"""
    t[0] = ("drop_column", t[3])

# 3. Modificar (en MySQL se usa MODIFY COLUMN)
# NOTA: Agrega el token MODIFICAR a tu analizador léxico.
def p_alteracion_modificar(t):
    """alteracion : MODIFICAR COLUMNA IDENTIFICADOR tipo_dato restricciones"""
    t[0] = ("modify_column", t[3], (t[4], t[5]))

# 4. Renombrar una columna (en MySQL se usa RENAME COLUMN y se requiere COLUMN)
def p_alteracion_rename(t):
    """alteracion : RENOMBRAR COLUMNA IDENTIFICADOR A IDENTIFICADOR"""
    t[0] = ("rename_column", t[3], t[5])
