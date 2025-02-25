from clases.Eliminar import E

# DELETE FROM 'nombreTabla'
def p_eliminar(t):
    """eliminar : eliminar_todo
                | eliminar_donde
                | eliminar_hasta_todo
                | eliminar_hasta_donde"""
    t[0] = t[1] # t[3] es el nombre de la tabla

# 1️⃣ Eliminar todos los registros de la tabla
def p_eliminar_todo(t):
    """eliminar_todo : ELIMINAR DESDE IDENTIFICADOR"""
    t[0] = ("eliminar todo", t[2], "todo")  # `todo` indica que elimina todo
    
def p_eliminar_donde(t):
    """eliminar_donde : ELIMINAR DESDE IDENTIFICADOR clausula"""
    t[0] = ("eliminar con condicion", t[3], t[4])   # t[4] es la condición

# 3️⃣ Eliminar los primeros `N` registros sin condición
def p_eliminar_hasta_todo(t):
    """eliminar_hasta_todo : ELIMINAR PRIMEROS VALOR_NUMERO DESDE IDENTIFICADOR"""
    t[0] = ("eliminar todo con tope", t[4], t[2], "todo")  # `t[2]` es `N`, `todo` indica que elimina sin filtro

# 4️⃣ Eliminar los primeros `N` registros con una condición
def p_eliminar_hasta_donde(t):
    """eliminar_hasta_donde : ELIMINAR PRIMEROS VALOR_NUMERO DESDE IDENTIFICADOR clausula"""
    t[0] = ("eliminar con condicion con tope", t[4], t[2], t[5], t[6])  # `t[2]` es `N`, `t[5]` es la condición
    
def p_clausula(t):
    """clausula : DONDE IDENTIFICADOR comparador valor"""
    t[0] = (t[3], t[2], t[4])
    
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
             | VALOR_CADENA
             | VALOR_BOOLEANO
             | VALOR_FLOTANTE"""
    t[0] = t[1]