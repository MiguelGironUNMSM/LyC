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

# 3. Modificar la definición de una columna:
def p_alteracion_modificar(t):
    """alteracion : MODIFICAR opt_column IDENTIFICADOR lista_columna_crear"""
    # t[3] es el nombre de la columna, t[4] la nueva definición (por ejemplo, nuevo tipo)
    t[0] = ("modify_column", t[3], t[4])

# 4. Renombrar una columna:  
#    ALTER TABLE [table_name] RENAME COLUMN [OldName] TO [NewName];
def p_alteracion_rename(t):
    """alteracion : RENOMBRAR opt_column IDENTIFICADOR A IDENTIFICADOR"""
    t[0] = ("rename_column", t[3], t[5])

# 5. Cambiar una columna:
# ALTER TABLE [table_name] CHANGE [old_column_name] [new_column_name] [column definition]
def p_alteracion_change(t): 
    """alteracion : CAMBIAR opt_column IDENTIFICADOR IDENTIFICADOR lista_columna_crear"""

# 6. Agregar una restricción (constraint):
# Ejemplo: ALTER TABLE nombre_tabla AGREGAR RESTRICCION PK_Person CLAVE_PRIMARIA (ID);
def p_alteracion_add_constraint(t):
    """alteracion : AGREGAR RESTRICCION IDENTIFICADOR constraint_definicion"""
    # t[3] es el nombre de la restricción, t[4] su definición
    t[0] = ("add_constraint", t[3], t[4])

# 7. Eliminar una restricción:
# Ejemplo: ALTER TABLE nombre_tabla SOLTAR RESTRICCION PK_Person;
def p_alteracion_drop_constraint(t):
    """alteracion : SOLTAR RESTRICCION IDENTIFICADOR"""
    # t[3] es el nombre de la restricción a eliminar
    t[0] = ("drop_constraint", t[3])

# Definición de restricciones Basicas

def p_constraint_definicion(t):
    """constraint_definicion : CLAVE_PRIMARIA PARENTESIS_IZQ IDENTIFICADOR PARENTESIS_DER
                             | UNICO PARENTESIS_IZQ IDENTIFICADOR PARENTESIS_DER
    """
    # Manejo de la producción
    if t.slice[1].type == "CLAVE_PRIMARIA":
        # CLAVE_PRIMARIA (columna)
        t[0] = ("primary_key", t[3])
    else:
        # UNICO (columna)
        t[0] = ("unique", t[3])
