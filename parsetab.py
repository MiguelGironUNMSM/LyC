
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftYOleftMENORMAYORMENOR_IGUALMAYOR_IGUALIGUALDADDIFERENTEleftMASMENOSleftMULTIPLICACIONDIVISIONMODULOACTUALIZAR AGRUPAR_POR ALGUNO ALGUNOS ALTERAR ASCENDENTE AUTOINCREMENTAL BOOLEANO CADENA CARACTER CASO CLAVE_FORANEA CLAVE_PRIMARIA COLOCAR COMA COMENTARIO COMO CONFIRMAR CONTAR CONVERTIR CREAR CUALQUIERA DECIMAL DESCENDENTE DESDE DIFERENTE DISTINTO DIVISION DONDE ELIMINAR EN ENTERO ENTONCES ENTRE ES ESTABLECER_TRANSACCION ES_NULO EXISTE FECHA FIN FLOTANTE IDENTIFICADOR IDENTIFICADOR_INVALIDO IGUALDAD INICIAR_TRANSACCION INICIO INSERTAR LIMITAR MAS MAXIMO MAYOR MAYOR_IGUAL MENOR MENOR_IGUAL MENOS MEZCLAR MIENTRAS MINIMO MODULO MULTIPLICACION NO NO_ES_NULO NO_NULO NULO NUMERO O OBTENER ORDENAR_POR PARA PARENTESIS_DER PARENTESIS_IZQ PROMEDIO PUNTO PUNTO_GUARDADO PYC RANGO REEMPLAZAR RENOMBRAR REVERTIR SALTO_DE_LINEA SELECCIONAR SI SIMILAR_A SINO SOLTAR SUMA TABLA TENIENDO TEXTO TODO TODOS UNIR UNIR_DERECHA UNIR_INTERIOR UNIR_IZQUIERDA VALORES Yinstruccion : seleccion\n| insertar\n| actualizar\n| eliminar\n| soltar\n| crear    \n| transaccioncrear : CREAR TABLA IDENTIFICADOR PARENTESIS_IZQ lista_columnas PARENTESIS_DERlista_columnas : lista_columnas COMA lista_columna\n| lista_columnatipo_dato : ENTERO \n| CADENA \n| CARACTER\n| FECHA\n| BOOLEANO\n| DECIMAL\n| TEXTO especificacion\n| FLOTANTEespecificacion : PARENTESIS_IZQ NUMERO PARENTESIS_DERrestricciones : restricciones restriccion\n| restriccion\n| empty restriccion : CLAVE_PRIMARIA\n| CLAVE_FORANEA\n| AUTOINCREMENTAL\n| NO_NULOlista_columna : IDENTIFICADOR  tipo_dato restriccionesseleccion : SELECCIONAR lista_columnas DESDE IDENTIFICADOR condicion_optlista_columnas : IDENTIFICADOR\n| lista_columnas COMA IDENTIFICADOR\n| TODOcondicion_opt : DONDE condicion\n| emptycondicion : IDENTIFICADOR comparador valor\n| condicion Y condicion\n| condicion O condicioncomparador : IGUALDAD\n| MAYOR\n| MENOR\n| MAYOR_IGUAL\n| MENOR_IGUAL\n| DIFERENTEvalor : NUMERO\n| CADENA\n| IDENTIFICADORinsertar : INSERTAR EN IDENTIFICADOR lista_columnas VALORES PARENTESIS_IZQ lista_valores PARENTESIS_DERlista_valores : valor\n| lista_valores COMA valoractualizar : ACTUALIZAR IDENTIFICADOR COLOCAR lista_asignaciones condicion_optlista_asignaciones : IDENTIFICADOR IGUALDAD valor\n| lista_asignaciones COMA IDENTIFICADOR IGUALDAD valoreliminar : ELIMINAR DESDE IDENTIFICADOR condicion_optsoltar : SOLTAR TABLA IDENTIFICADORtransaccion : INICIAR_TRANSACCION\n| CONFIRMAR\n| REVERTIRempty :'
    
_lr_action_items = {'SELECCIONAR':([0,],[9,]),'INSERTAR':([0,],[10,]),'ACTUALIZAR':([0,],[11,]),'ELIMINAR':([0,],[12,]),'SOLTAR':([0,],[13,]),'CREAR':([0,],[14,]),'INICIAR_TRANSACCION':([0,],[15,]),'CONFIRMAR':([0,],[16,]),'REVERTIR':([0,],[17,]),'$end':([1,2,3,4,5,6,7,8,15,16,17,40,41,43,57,58,60,62,67,69,74,75,76,77,88,92,93,94,95,97,],[0,-1,-2,-3,-4,-5,-6,-7,-54,-55,-56,-57,-53,-57,-57,-52,-33,-28,-49,-32,-45,-50,-43,-44,-8,-35,-36,-34,-46,-51,]),'IDENTIFICADOR':([9,11,22,24,25,26,27,28,38,39,59,61,66,68,73,79,80,81,82,83,84,85,86,87,91,96,],[19,23,38,40,41,42,43,45,19,56,70,19,74,78,74,70,70,74,-37,-38,-39,-40,-41,-42,74,74,]),'TODO':([9,38,61,],[21,21,21,]),'EN':([10,],[22,]),'DESDE':([12,18,19,20,21,29,30,31,32,33,34,35,37,44,45,46,47,48,49,50,51,52,53,63,72,],[24,27,-29,-10,-31,-57,-11,-12,-13,-14,-15,-16,-18,-9,-30,-27,-21,-22,-23,-24,-25,-26,-17,-20,-19,]),'TABLA':([13,14,],[25,26,]),'COMA':([18,19,20,21,29,30,31,32,33,34,35,37,44,45,46,47,48,49,50,51,52,53,55,57,63,71,72,74,75,76,77,89,90,97,98,],[28,-29,-10,-31,-57,-11,-12,-13,-14,-15,-16,-18,-9,-30,-27,-21,-22,-23,-24,-25,-26,-17,28,68,-20,28,-19,-45,-50,-43,-44,96,-47,-51,-48,]),'VALORES':([19,20,21,29,30,31,32,33,34,35,37,44,45,46,47,48,49,50,51,52,53,55,63,72,],[-29,-10,-31,-57,-11,-12,-13,-14,-15,-16,-18,-9,-30,-27,-21,-22,-23,-24,-25,-26,-17,65,-20,-19,]),'PARENTESIS_DER':([19,20,21,29,30,31,32,33,34,35,37,44,45,46,47,48,49,50,51,52,53,63,64,71,72,74,76,77,89,90,98,],[-29,-10,-31,-57,-11,-12,-13,-14,-15,-16,-18,-9,-30,-27,-21,-22,-23,-24,-25,-26,-17,-20,72,88,-19,-45,-43,-44,95,-47,-48,]),'ENTERO':([19,45,],[30,30,]),'CADENA':([19,45,66,73,81,82,83,84,85,86,87,91,96,],[31,31,77,77,77,-37,-38,-39,-40,-41,-42,77,77,]),'CARACTER':([19,45,],[32,32,]),'FECHA':([19,45,],[33,33,]),'BOOLEANO':([19,45,],[34,34,]),'DECIMAL':([19,45,],[35,35,]),'TEXTO':([19,45,],[36,36,]),'FLOTANTE':([19,45,],[37,37,]),'COLOCAR':([23,],[39,]),'CLAVE_PRIMARIA':([29,30,31,32,33,34,35,37,46,47,48,49,50,51,52,53,63,72,],[49,-11,-12,-13,-14,-15,-16,-18,49,-21,-22,-23,-24,-25,-26,-17,-20,-19,]),'CLAVE_FORANEA':([29,30,31,32,33,34,35,37,46,47,48,49,50,51,52,53,63,72,],[50,-11,-12,-13,-14,-15,-16,-18,50,-21,-22,-23,-24,-25,-26,-17,-20,-19,]),'AUTOINCREMENTAL':([29,30,31,32,33,34,35,37,46,47,48,49,50,51,52,53,63,72,],[51,-11,-12,-13,-14,-15,-16,-18,51,-21,-22,-23,-24,-25,-26,-17,-20,-19,]),'NO_NULO':([29,30,31,32,33,34,35,37,46,47,48,49,50,51,52,53,63,72,],[52,-11,-12,-13,-14,-15,-16,-18,52,-21,-22,-23,-24,-25,-26,-17,-20,-19,]),'PARENTESIS_IZQ':([36,42,65,],[54,61,73,]),'DONDE':([40,43,57,74,75,76,77,97,],[59,59,59,-45,-50,-43,-44,-51,]),'NUMERO':([54,66,73,81,82,83,84,85,86,87,91,96,],[64,76,76,76,-37,-38,-39,-40,-41,-42,76,76,]),'IGUALDAD':([56,70,78,],[66,82,91,]),'Y':([69,74,76,77,92,93,94,],[79,-45,-43,-44,-35,-36,-34,]),'O':([69,74,76,77,92,93,94,],[80,-45,-43,-44,-35,-36,-34,]),'MAYOR':([70,],[83,]),'MENOR':([70,],[84,]),'MAYOR_IGUAL':([70,],[85,]),'MENOR_IGUAL':([70,],[86,]),'DIFERENTE':([70,],[87,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'instruccion':([0,],[1,]),'seleccion':([0,],[2,]),'insertar':([0,],[3,]),'actualizar':([0,],[4,]),'eliminar':([0,],[5,]),'soltar':([0,],[6,]),'crear':([0,],[7,]),'transaccion':([0,],[8,]),'lista_columnas':([9,38,61,],[18,55,71,]),'lista_columna':([9,28,38,61,],[20,44,20,20,]),'tipo_dato':([19,45,],[29,29,]),'restricciones':([29,],[46,]),'restriccion':([29,46,],[47,63,]),'empty':([29,40,43,57,],[48,60,60,60,]),'especificacion':([36,],[53,]),'lista_asignaciones':([39,],[57,]),'condicion_opt':([40,43,57,],[58,62,67,]),'condicion':([59,79,80,],[69,92,93,]),'valor':([66,73,81,91,96,],[75,90,94,97,98,]),'comparador':([70,],[81,]),'lista_valores':([73,],[89,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> instruccion","S'",1,None,None,None),
  ('instruccion -> seleccion','instruccion',1,'p_instruccion','AnalizadorSintactico.py',14),
  ('instruccion -> insertar','instruccion',1,'p_instruccion','AnalizadorSintactico.py',15),
  ('instruccion -> actualizar','instruccion',1,'p_instruccion','AnalizadorSintactico.py',16),
  ('instruccion -> eliminar','instruccion',1,'p_instruccion','AnalizadorSintactico.py',17),
  ('instruccion -> soltar','instruccion',1,'p_instruccion','AnalizadorSintactico.py',18),
  ('instruccion -> crear','instruccion',1,'p_instruccion','AnalizadorSintactico.py',19),
  ('instruccion -> transaccion','instruccion',1,'p_instruccion','AnalizadorSintactico.py',20),
  ('crear -> CREAR TABLA IDENTIFICADOR PARENTESIS_IZQ lista_columnas PARENTESIS_DER','crear',6,'p_crear','AnalizadorSintactico.py',25),
  ('lista_columnas -> lista_columnas COMA lista_columna','lista_columnas',3,'p_lista_columnas_crear','AnalizadorSintactico.py',29),
  ('lista_columnas -> lista_columna','lista_columnas',1,'p_lista_columnas_crear','AnalizadorSintactico.py',30),
  ('tipo_dato -> ENTERO','tipo_dato',1,'p_tipo_dato','AnalizadorSintactico.py',38),
  ('tipo_dato -> CADENA','tipo_dato',1,'p_tipo_dato','AnalizadorSintactico.py',39),
  ('tipo_dato -> CARACTER','tipo_dato',1,'p_tipo_dato','AnalizadorSintactico.py',40),
  ('tipo_dato -> FECHA','tipo_dato',1,'p_tipo_dato','AnalizadorSintactico.py',41),
  ('tipo_dato -> BOOLEANO','tipo_dato',1,'p_tipo_dato','AnalizadorSintactico.py',42),
  ('tipo_dato -> DECIMAL','tipo_dato',1,'p_tipo_dato','AnalizadorSintactico.py',43),
  ('tipo_dato -> TEXTO especificacion','tipo_dato',2,'p_tipo_dato','AnalizadorSintactico.py',44),
  ('tipo_dato -> FLOTANTE','tipo_dato',1,'p_tipo_dato','AnalizadorSintactico.py',45),
  ('especificacion -> PARENTESIS_IZQ NUMERO PARENTESIS_DER','especificacion',3,'p_especificacion','AnalizadorSintactico.py',52),
  ('restricciones -> restricciones restriccion','restricciones',2,'p_restricciones','AnalizadorSintactico.py',56),
  ('restricciones -> restriccion','restricciones',1,'p_restricciones','AnalizadorSintactico.py',57),
  ('restricciones -> empty','restricciones',1,'p_restricciones','AnalizadorSintactico.py',58),
  ('restriccion -> CLAVE_PRIMARIA','restriccion',1,'p_restriccion','AnalizadorSintactico.py',68),
  ('restriccion -> CLAVE_FORANEA','restriccion',1,'p_restriccion','AnalizadorSintactico.py',69),
  ('restriccion -> AUTOINCREMENTAL','restriccion',1,'p_restriccion','AnalizadorSintactico.py',70),
  ('restriccion -> NO_NULO','restriccion',1,'p_restriccion','AnalizadorSintactico.py',71),
  ('lista_columna -> IDENTIFICADOR tipo_dato restricciones','lista_columna',3,'p_lista_columna_crear','AnalizadorSintactico.py',75),
  ('seleccion -> SELECCIONAR lista_columnas DESDE IDENTIFICADOR condicion_opt','seleccion',5,'p_seleccion','AnalizadorSintactico.py',85),
  ('lista_columnas -> IDENTIFICADOR','lista_columnas',1,'p_lista_columnas','AnalizadorSintactico.py',92),
  ('lista_columnas -> lista_columnas COMA IDENTIFICADOR','lista_columnas',3,'p_lista_columnas','AnalizadorSintactico.py',93),
  ('lista_columnas -> TODO','lista_columnas',1,'p_lista_columnas','AnalizadorSintactico.py',94),
  ('condicion_opt -> DONDE condicion','condicion_opt',2,'p_condicion_opt','AnalizadorSintactico.py',103),
  ('condicion_opt -> empty','condicion_opt',1,'p_condicion_opt','AnalizadorSintactico.py',104),
  ('condicion -> IDENTIFICADOR comparador valor','condicion',3,'p_condicion','AnalizadorSintactico.py',111),
  ('condicion -> condicion Y condicion','condicion',3,'p_condicion','AnalizadorSintactico.py',112),
  ('condicion -> condicion O condicion','condicion',3,'p_condicion','AnalizadorSintactico.py',113),
  ('comparador -> IGUALDAD','comparador',1,'p_comparador','AnalizadorSintactico.py',121),
  ('comparador -> MAYOR','comparador',1,'p_comparador','AnalizadorSintactico.py',122),
  ('comparador -> MENOR','comparador',1,'p_comparador','AnalizadorSintactico.py',123),
  ('comparador -> MAYOR_IGUAL','comparador',1,'p_comparador','AnalizadorSintactico.py',124),
  ('comparador -> MENOR_IGUAL','comparador',1,'p_comparador','AnalizadorSintactico.py',125),
  ('comparador -> DIFERENTE','comparador',1,'p_comparador','AnalizadorSintactico.py',126),
  ('valor -> NUMERO','valor',1,'p_valor','AnalizadorSintactico.py',130),
  ('valor -> CADENA','valor',1,'p_valor','AnalizadorSintactico.py',131),
  ('valor -> IDENTIFICADOR','valor',1,'p_valor','AnalizadorSintactico.py',132),
  ('insertar -> INSERTAR EN IDENTIFICADOR lista_columnas VALORES PARENTESIS_IZQ lista_valores PARENTESIS_DER','insertar',8,'p_insertar','AnalizadorSintactico.py',140),
  ('lista_valores -> valor','lista_valores',1,'p_lista_valores','AnalizadorSintactico.py',145),
  ('lista_valores -> lista_valores COMA valor','lista_valores',3,'p_lista_valores','AnalizadorSintactico.py',146),
  ('actualizar -> ACTUALIZAR IDENTIFICADOR COLOCAR lista_asignaciones condicion_opt','actualizar',5,'p_actualizar','AnalizadorSintactico.py',155),
  ('lista_asignaciones -> IDENTIFICADOR IGUALDAD valor','lista_asignaciones',3,'p_lista_asignaciones','AnalizadorSintactico.py',159),
  ('lista_asignaciones -> lista_asignaciones COMA IDENTIFICADOR IGUALDAD valor','lista_asignaciones',5,'p_lista_asignaciones','AnalizadorSintactico.py',160),
  ('eliminar -> ELIMINAR DESDE IDENTIFICADOR condicion_opt','eliminar',4,'p_eliminar','AnalizadorSintactico.py',169),
  ('soltar -> SOLTAR TABLA IDENTIFICADOR','soltar',3,'p_soltar','AnalizadorSintactico.py',175),
  ('transaccion -> INICIAR_TRANSACCION','transaccion',1,'p_transaccion','AnalizadorSintactico.py',181),
  ('transaccion -> CONFIRMAR','transaccion',1,'p_transaccion','AnalizadorSintactico.py',182),
  ('transaccion -> REVERTIR','transaccion',1,'p_transaccion','AnalizadorSintactico.py',183),
  ('empty -> <empty>','empty',0,'p_empty','AnalizadorSintactico.py',189),
]
