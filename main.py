from AnalizadorSintactico import analizar_consulta

resultado = analizar_consulta("""
SELECCIONAR nombre, edad, salario 
DESDE empleados 
DONDE edad > 25
ORDENAR POR salario DESCENDENTE;

""")


print("Resultado de la consulta:")
print(resultado)

