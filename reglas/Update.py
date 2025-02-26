from clases.Actualizar import *

def p_actualizar(t):
    """actualizar : ACTUALIZAR IDENTIFICADOR COLOCAR lista_asignaciones DONDE opt_condiciones
                  | ACTUALIZAR IDENTIFICADOR COLOCAR lista_asignaciones
    """
    if len(t) > 5:
        t[0] = Actualizar(tabla=t[2], alteraciones=t[4], condiciones=t[6])  
    else:
        t[0] = Actualizar(tabla=t[2], alteraciones=t[4])


def p_alteraciones_update(t):
    """lista_asignaciones : IDENTIFICADOR IGUALDAD valor
                          | lista_asignaciones COMA IDENTIFICADOR IGUALDAD valor"""
    if len(t) == 3:
        t[0] = [(t[1], t[2], t[3])]
    else:
        t[0] = t[1] + [(t[3],t[4] ,t[5])]