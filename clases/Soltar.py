from AnalizadorSemantico import Instruccion

class Soltar(Instruccion):
    def __init__(self,tabla,condicional=None):
        self.tabla = tabla
        self.condicional = condicional
    def analizar_semantica(self, base_datos):
        if self.tabla not in base_datos:
            raise Exception(f"Error: La tabla'{self.tabla} no existe")
        
    def ejecutar(self, base_datos):
        self.analizar_semantica(base_datos)

        sql = f"DROP TABLE {self.tabla}"
        if self.condicional:
            sql += f" IF EXIST"
        return sql
        