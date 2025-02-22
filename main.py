from AnalizadorSintactico import analizar_consulta

resultado = analizar_consulta("""
UNIR departamentos CON departamento = id;
""")


print("Resultado de la consulta:")
print(resultado)

