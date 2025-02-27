
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'instruccionleftYOleftMENORMAYORMENOR_IGUALMAYOR_IGUALIGUALDADDIFERENTEleftMASMENOSleftMULTIPLICACIONDIVISIONMODULOA ACTUALIZAR AGREGAR AGRUPAR_POR ALGUNO ALGUNOS ALTERAR ASCENDENTE AUTOINCREMENTAL BOOLEANO CADENA CAMBIAR CARACTER CASO CLAVE_FORANEA CLAVE_PRIMARIA COLOCAR COLUMNA COMA COMENTARIO COMILLAS_SIMPLES COMO COMPLETO CON CONFIRMAR CONTAR CONVERTIR CREAR CUALQUIERA DECIMAL DERECHO DESCENDENTE DESDE DIFERENTE DISTINTO DIVISION DONDE ELIMINAR ENTERO ENTONCES ENTRE ES ESTABLECER_TRANSACCION ES_NULO EXISTE FECHA FIN FLOTANTE IDENTIFICADOR IDENTIFICADOR_INVALIDO IGUALDAD INICIAR_TRANSACCION INICIO INSERTAR_EN IZQUIERDO LIMITAR MAS MAXIMO MAYOR MAYOR_IGUAL MENOR MENOR_IGUAL MENOS MEZCLAR MIENTRAS MINIMO MODIFICAR MODULO MULTIPLICACION NO NORMAL NO_ES_NULO NO_NULO NULO O OBTENER ORDENAR_POR PARA PARENTESIS_DER PARENTESIS_IZQ PRIMEROS PROMEDIO PUNTO PUNTO_GUARDADO PYC RANGO REEMPLAZAR REFERENCIA RENOMBRAR RESTRICCION REVERTIR SALTO_DE_LINEA SELECCIONAR SI SIMILAR_A SINO SOLTAR SUMA TABLA TENIENDO TEXTO TODO TODOS UNIR VALORES VALOR_BOOLEANO VALOR_CADENA VALOR_FLOTANTE VALOR_NUMERO Ylista_columna_crear : IDENTIFICADOR tipo_dato restriccionestransaccion : INICIAR_TRANSACCIONinsertar : INSERTAR_EN IDENTIFICADOR PARENTESIS_IZQ lista_columnas_creadas PARENTESIS_DER VALORES lista_filascrear : CREAR TABLA IDENTIFICADOR PARENTESIS_IZQ lista_columnas_crear PARENTESIS_DERsoltar : SOLTAR TABLA IDENTIFICADOR\n              | SOLTAR TABLA IDENTIFICADOR condicional unir : UNIR tipo_unir IDENTIFICADOR CON condicionseleccion : SELECCIONAR lista_floro lista_columnas DESDE IDENTIFICADOR opt_condiciones\n                 | SELECCIONAR lista_floro lista_columnas DESDE IDENTIFICADOR opt_condiciones uniractualizar : ACTUALIZAR IDENTIFICADOR COLOCAR lista_asignaciones DONDE opt_condiciones\n                  | ACTUALIZAR IDENTIFICADOR COLOCAR lista_asignaciones\n    eliminar : eliminar_todo\n                | eliminar_donde\n                | eliminar_hasta_todo\n                | eliminar_hasta_dondealterar : ALTERAR TABLA IDENTIFICADOR alteracionestransaccion : CONFIRMARlista_columnas_creadas : IDENTIFICADOR\n                              | lista_columnas_creadas COMA IDENTIFICADORtipo_dato : ENTERO\n                 | CADENA\n                 | CARACTER\n                 | FECHA\n                 | BOOLEANO\n                 | DECIMAL\n                 | TEXTO\n                 | FLOTANTEtransaccion : REVERTIRtipo_unir : NORMAL\n                 | IZQUIERDO\n                 | DERECHO\n                 | COMPLETO\n                 | emptycondicional : SI EXISTE eliminar_todo : ELIMINAR DESDE IDENTIFICADORalteraciones : alteracionlista_asignaciones : asignacion\n                          | lista_asignaciones COMA asignacionlista_filas : fila \n                  | lista_filas COMA filaeliminar_donde : ELIMINAR DESDE IDENTIFICADOR clausulaalteraciones : alteracion COMA alteracioneslista_floro : lista_floro floro\n                   | florocondicion : especificacion IGUALDAD especificacioneliminar_hasta_todo : ELIMINAR PRIMEROS VALOR_NUMERO DESDE IDENTIFICADORasignacion : IDENTIFICADOR IGUALDAD valorfila : PARENTESIS_IZQ lista_valores PARENTESIS_DERalteracion : AGREGAR opt_column lista_columna_crearempty :eliminar_hasta_donde : ELIMINAR PRIMEROS VALOR_NUMERO DESDE IDENTIFICADOR clausulalista_valores : valor\n    | lista_valores COMA valorlista_columnas_crear : lista_columnas_crear COMA lista_columna_crear\n                      | lista_columna_crearfloro : DISTINTO\n             | emptyespecificacion : IDENTIFICADOR PARENTESIS_IZQ IDENTIFICADOR PARENTESIS_DERinstruccion : seleccion\n    | insertar\n    | alterar\n    | actualizar\n    | eliminar\n    | soltar\n    | crear\n    | transaccion\n    | unir\n    | valorclausula : DONDE IDENTIFICADOR comparador valoropt_column : COLUMNA\n                  | emptyrestricciones : restricciones restriccion\n                     | restriccion\n                     | emptycomparador : IGUALDAD\n                  | MAYOR\n                  | MENOR\n                  | MAYOR_IGUAL\n                  | MENOR_IGUAL\n                  | DIFERENTElista_columnas : IDENTIFICADOR\n                      | lista_columnas COMA IDENTIFICADOR\n                      | TODOalteracion : SOLTAR opt_column IDENTIFICADORvalor : VALOR_NUMERO\n             | VALOR_CADENA\n             | VALOR_BOOLEANO\n             | VALOR_FLOTANTErestriccion : CLAVE_PRIMARIA\n                   | CLAVE_FORANEA referencia \n                   | AUTOINCREMENTAL\n                   | NO_NULOalteracion : MODIFICAR opt_column lista_columna_crearreferencia : REFERENCIA IDENTIFICADOR PARENTESIS_IZQ IDENTIFICADOR PARENTESIS_DERalteracion : RENOMBRAR opt_column IDENTIFICADOR A IDENTIFICADORopt_condiciones : condiciones\n                       | emptyalteracion : CAMBIAR opt_column IDENTIFICADOR lista_columna_crearcondiciones : condiciones clausula\n                   | clausulacondicion_order : IDENTIFICADOR ASCENDENTE\n                       | IDENTIFICADOR DESCENDENTE\n                       | IDENTIFICADOR'
    
_lr_action_items = {'SELECCIONAR':([0,],[12,]),'INSERTAR_EN':([0,],[13,]),'ALTERAR':([0,],[14,]),'ACTUALIZAR':([0,],[15,]),'SOLTAR':([0,53,85,],[20,67,67,]),'CREAR':([0,],[21,]),'INICIAR_TRANSACCION':([0,],[22,]),'CONFIRMAR':([0,],[23,]),'REVERTIR':([0,],[24,]),'UNIR':([0,26,27,28,29,81,105,106,107,108,142,158,],[25,-85,-86,-87,-88,-50,25,-96,-97,-100,-99,-69,]),'VALOR_NUMERO':([0,47,93,133,134,135,136,137,138,139,143,168,],[26,59,26,26,-75,-76,-77,-78,-79,-80,26,26,]),'VALOR_CADENA':([0,93,133,134,135,136,137,138,139,143,168,],[27,27,27,-75,-76,-77,-78,-79,-80,27,27,]),'VALOR_BOOLEANO':([0,93,133,134,135,136,137,138,139,143,168,],[28,28,28,-75,-76,-77,-78,-79,-80,28,28,]),'VALOR_FLOTANTE':([0,93,133,134,135,136,137,138,139,143,168,],[29,29,29,-75,-76,-77,-78,-79,-80,29,29,]),'ELIMINAR':([0,],[30,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,16,17,18,19,22,23,24,26,27,28,29,55,58,64,65,72,73,74,78,81,94,96,101,104,105,106,107,108,111,112,113,114,117,118,119,120,121,122,123,124,125,126,127,128,129,140,141,142,144,145,147,148,149,150,151,153,154,157,158,162,163,164,166,167,169,174,],[0,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-12,-13,-14,-15,-2,-17,-28,-85,-86,-87,-88,-5,-35,-16,-36,-11,-37,-6,-41,-50,-50,-34,-7,-46,-8,-96,-97,-100,-42,-49,-84,-93,-47,-10,-38,-50,-20,-21,-22,-23,-24,-25,-26,-27,-4,-51,-9,-99,-3,-39,-98,-1,-73,-74,-89,-91,-92,-45,-69,-95,-72,-90,-58,-48,-40,-94,]),'DISTINTO':([12,31,32,33,34,50,],[33,33,-44,-56,-57,-43,]),'IDENTIFICADOR':([12,13,15,25,31,32,33,34,36,38,39,40,41,42,43,44,45,46,50,52,54,60,61,66,67,68,69,70,76,77,79,80,84,86,87,88,89,90,91,92,95,116,130,131,132,146,165,172,],[-50,35,37,-50,49,-44,-56,-57,53,55,56,57,-29,-30,-31,-32,-33,58,-43,62,71,81,82,-50,-50,-50,-50,-50,97,100,103,104,110,97,-70,-71,113,97,115,116,71,97,97,156,100,162,170,173,]),'TODO':([12,31,32,33,34,50,],[-50,51,-44,-56,-57,-43,]),'TABLA':([14,20,21,],[36,38,39,]),'NORMAL':([25,],[41,]),'IZQUIERDO':([25,],[42,]),'DERECHO':([25,],[43,]),'COMPLETO':([25,],[44,]),'DONDE':([26,27,28,29,58,72,73,81,94,104,106,108,117,119,142,158,],[-85,-86,-87,-88,79,94,-37,79,79,79,79,-100,-47,-38,-99,-69,]),'COMA':([26,27,28,29,48,49,51,62,63,65,72,73,82,98,99,110,112,113,114,117,119,120,121,122,123,124,125,126,127,128,144,145,147,148,149,150,151,153,154,155,159,160,162,163,164,167,169,171,174,],[-85,-86,-87,-88,61,-81,-83,-18,84,85,95,-37,-82,130,-55,-19,-49,-84,-93,-47,-38,-50,-20,-21,-22,-23,-24,-25,-26,-27,161,-39,-98,-1,-73,-74,-89,-91,-92,-54,168,-52,-95,-72,-90,-48,-40,-53,-94,]),'PARENTESIS_DER':([26,27,28,29,62,63,98,99,110,120,121,122,123,124,125,126,127,128,148,149,150,151,153,154,155,156,159,160,163,164,171,173,174,],[-85,-86,-87,-88,-18,83,129,-55,-19,-50,-20,-21,-22,-23,-24,-25,-26,-27,-1,-73,-74,-89,-91,-92,-54,166,167,-52,-72,-90,-53,174,-94,]),'DESDE':([30,48,49,51,59,82,],[46,60,-81,-83,80,-82,]),'PRIMEROS':([30,],[47,]),'PARENTESIS_IZQ':([35,56,100,109,161,170,],[52,76,131,143,143,172,]),'COLOCAR':([37,],[54,]),'AGREGAR':([53,85,],[66,66,]),'MODIFICAR':([53,85,],[68,68,]),'RENOMBRAR':([53,85,],[69,69,]),'CAMBIAR':([53,85,],[70,70,]),'SI':([55,],[75,]),'CON':([57,],[77,]),'COLUMNA':([66,67,68,69,70,],[87,87,87,87,87,]),'IGUALDAD':([71,102,103,166,],[93,132,134,-58,]),'EXISTE':([75,],[96,]),'VALORES':([83,],[109,]),'ENTERO':([97,],[121,]),'CADENA':([97,],[122,]),'CARACTER':([97,],[123,]),'FECHA':([97,],[124,]),'BOOLEANO':([97,],[125,]),'DECIMAL':([97,],[126,]),'TEXTO':([97,],[127,]),'FLOTANTE':([97,],[128,]),'MAYOR':([103,],[135,]),'MENOR':([103,],[136,]),'MAYOR_IGUAL':([103,],[137,]),'MENOR_IGUAL':([103,],[138,]),'DIFERENTE':([103,],[139,]),'A':([115,],[146,]),'CLAVE_PRIMARIA':([120,121,122,123,124,125,126,127,128,148,149,150,151,153,154,163,164,174,],[151,-20,-21,-22,-23,-24,-25,-26,-27,151,-73,-74,-89,-91,-92,-72,-90,-94,]),'CLAVE_FORANEA':([120,121,122,123,124,125,126,127,128,148,149,150,151,153,154,163,164,174,],[152,-20,-21,-22,-23,-24,-25,-26,-27,152,-73,-74,-89,-91,-92,-72,-90,-94,]),'AUTOINCREMENTAL':([120,121,122,123,124,125,126,127,128,148,149,150,151,153,154,163,164,174,],[153,-20,-21,-22,-23,-24,-25,-26,-27,153,-73,-74,-89,-91,-92,-72,-90,-94,]),'NO_NULO':([120,121,122,123,124,125,126,127,128,148,149,150,151,153,154,163,164,174,],[154,-20,-21,-22,-23,-24,-25,-26,-27,154,-73,-74,-89,-91,-92,-72,-90,-94,]),'REFERENCIA':([152,],[165,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'instruccion':([0,],[1,]),'seleccion':([0,],[2,]),'insertar':([0,],[3,]),'alterar':([0,],[4,]),'actualizar':([0,],[5,]),'eliminar':([0,],[6,]),'soltar':([0,],[7,]),'crear':([0,],[8,]),'transaccion':([0,],[9,]),'unir':([0,105,],[10,141,]),'valor':([0,93,133,143,168,],[11,117,158,160,171,]),'eliminar_todo':([0,],[16,]),'eliminar_donde':([0,],[17,]),'eliminar_hasta_todo':([0,],[18,]),'eliminar_hasta_donde':([0,],[19,]),'lista_floro':([12,],[31,]),'floro':([12,31,],[32,50,]),'empty':([12,25,31,66,67,68,69,70,81,94,120,],[34,45,34,88,88,88,88,88,107,107,150,]),'tipo_unir':([25,],[40,]),'lista_columnas':([31,],[48,]),'lista_columnas_creadas':([52,],[63,]),'alteraciones':([53,85,],[64,111,]),'alteracion':([53,85,],[65,65,]),'lista_asignaciones':([54,],[72,]),'asignacion':([54,95,],[73,119,]),'condicional':([55,],[74,]),'clausula':([58,81,94,104,106,],[78,108,108,140,142,]),'opt_column':([66,67,68,69,70,],[86,89,90,91,92,]),'lista_columnas_crear':([76,],[98,]),'lista_columna_crear':([76,86,90,116,130,],[99,112,114,147,155,]),'condicion':([77,],[101,]),'especificacion':([77,132,],[102,157,]),'opt_condiciones':([81,94,],[105,118,]),'condiciones':([81,94,],[106,106,]),'tipo_dato':([97,],[120,]),'comparador':([103,],[133,]),'lista_filas':([109,],[144,]),'fila':([109,161,],[145,169,]),'restricciones':([120,],[148,]),'restriccion':([120,148,],[149,163,]),'lista_valores':([143,],[159,]),'referencia':([152,],[164,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> instruccion","S'",1,None,None,None),
  ('lista_columna_crear -> IDENTIFICADOR tipo_dato restricciones','lista_columna_crear',3,'p_lista_columna_crear','ReglasComunes.py',2),
  ('transaccion -> INICIAR_TRANSACCION','transaccion',1,'p_transaccion_iniciar','Transaction.py',2),
  ('insertar -> INSERTAR_EN IDENTIFICADOR PARENTESIS_IZQ lista_columnas_creadas PARENTESIS_DER VALORES lista_filas','insertar',7,'p_insertar','Insert.py',3),
  ('crear -> CREAR TABLA IDENTIFICADOR PARENTESIS_IZQ lista_columnas_crear PARENTESIS_DER','crear',6,'p_crear','Create.py',4),
  ('soltar -> SOLTAR TABLA IDENTIFICADOR','soltar',3,'p_soltar','DropTable.py',4),
  ('soltar -> SOLTAR TABLA IDENTIFICADOR condicional','soltar',4,'p_soltar','DropTable.py',5),
  ('unir -> UNIR tipo_unir IDENTIFICADOR CON condicion','unir',5,'p_unir','Join.py',4),
  ('seleccion -> SELECCIONAR lista_floro lista_columnas DESDE IDENTIFICADOR opt_condiciones','seleccion',6,'p_seleccion','Select.py',4),
  ('seleccion -> SELECCIONAR lista_floro lista_columnas DESDE IDENTIFICADOR opt_condiciones unir','seleccion',7,'p_seleccion','Select.py',5),
  ('actualizar -> ACTUALIZAR IDENTIFICADOR COLOCAR lista_asignaciones DONDE opt_condiciones','actualizar',6,'p_actualizar','Update.py',4),
  ('actualizar -> ACTUALIZAR IDENTIFICADOR COLOCAR lista_asignaciones','actualizar',4,'p_actualizar','Update.py',5),
  ('eliminar -> eliminar_todo','eliminar',1,'p_eliminar','Delete.py',5),
  ('eliminar -> eliminar_donde','eliminar',1,'p_eliminar','Delete.py',6),
  ('eliminar -> eliminar_hasta_todo','eliminar',1,'p_eliminar','Delete.py',7),
  ('eliminar -> eliminar_hasta_donde','eliminar',1,'p_eliminar','Delete.py',8),
  ('alterar -> ALTERAR TABLA IDENTIFICADOR alteraciones','alterar',4,'p_alterar','Alter.py',6),
  ('transaccion -> CONFIRMAR','transaccion',1,'p_transaccion_confirmar','Transaction.py',6),
  ('lista_columnas_creadas -> IDENTIFICADOR','lista_columnas_creadas',1,'p_lista_columnas_creadas','Insert.py',8),
  ('lista_columnas_creadas -> lista_columnas_creadas COMA IDENTIFICADOR','lista_columnas_creadas',3,'p_lista_columnas_creadas','Insert.py',9),
  ('tipo_dato -> ENTERO','tipo_dato',1,'p_tipo_dato','ReglasComunes.py',10),
  ('tipo_dato -> CADENA','tipo_dato',1,'p_tipo_dato','ReglasComunes.py',11),
  ('tipo_dato -> CARACTER','tipo_dato',1,'p_tipo_dato','ReglasComunes.py',12),
  ('tipo_dato -> FECHA','tipo_dato',1,'p_tipo_dato','ReglasComunes.py',13),
  ('tipo_dato -> BOOLEANO','tipo_dato',1,'p_tipo_dato','ReglasComunes.py',14),
  ('tipo_dato -> DECIMAL','tipo_dato',1,'p_tipo_dato','ReglasComunes.py',15),
  ('tipo_dato -> TEXTO','tipo_dato',1,'p_tipo_dato','ReglasComunes.py',16),
  ('tipo_dato -> FLOTANTE','tipo_dato',1,'p_tipo_dato','ReglasComunes.py',17),
  ('transaccion -> REVERTIR','transaccion',1,'p_transaccion_revertir','Transaction.py',10),
  ('tipo_unir -> NORMAL','tipo_unir',1,'p_tipo_unir','Join.py',11),
  ('tipo_unir -> IZQUIERDO','tipo_unir',1,'p_tipo_unir','Join.py',12),
  ('tipo_unir -> DERECHO','tipo_unir',1,'p_tipo_unir','Join.py',13),
  ('tipo_unir -> COMPLETO','tipo_unir',1,'p_tipo_unir','Join.py',14),
  ('tipo_unir -> empty','tipo_unir',1,'p_tipo_unir','Join.py',15),
  ('condicional -> SI EXISTE','condicional',2,'p_condicional','DropTable.py',12),
  ('eliminar_todo -> ELIMINAR DESDE IDENTIFICADOR','eliminar_todo',3,'p_eliminar_todo','Delete.py',13),
  ('alteraciones -> alteracion','alteraciones',1,'p_alteraciones_single','Alter.py',14),
  ('lista_asignaciones -> asignacion','lista_asignaciones',1,'p_lista_asignaciones','Update.py',15),
  ('lista_asignaciones -> lista_asignaciones COMA asignacion','lista_asignaciones',3,'p_lista_asignaciones','Update.py',16),
  ('lista_filas -> fila','lista_filas',1,'p_lista_filas','Insert.py',16),
  ('lista_filas -> lista_filas COMA fila','lista_filas',3,'p_lista_filas','Insert.py',17),
  ('eliminar_donde -> ELIMINAR DESDE IDENTIFICADOR clausula','eliminar_donde',4,'p_eliminar_donde','Delete.py',17),
  ('alteraciones -> alteracion COMA alteraciones','alteraciones',3,'p_alteraciones_multiple','Alter.py',19),
  ('lista_floro -> lista_floro floro','lista_floro',2,'p_lista_floro','Select.py',20),
  ('lista_floro -> floro','lista_floro',1,'p_lista_floro','Select.py',21),
  ('condicion -> especificacion IGUALDAD especificacion','condicion',3,'p_condicion','Join.py',21),
  ('eliminar_hasta_todo -> ELIMINAR PRIMEROS VALOR_NUMERO DESDE IDENTIFICADOR','eliminar_hasta_todo',5,'p_eliminar_hasta_todo','Delete.py',22),
  ('asignacion -> IDENTIFICADOR IGUALDAD valor','asignacion',3,'p_asignacion','Update.py',23),
  ('fila -> PARENTESIS_IZQ lista_valores PARENTESIS_DER','fila',3,'p_fila','Insert.py',24),
  ('alteracion -> AGREGAR opt_column lista_columna_crear','alteracion',3,'p_alteracion_add','Alter.py',26),
  ('empty -> <empty>','empty',0,'p_empty','Join.py',26),
  ('eliminar_hasta_donde -> ELIMINAR PRIMEROS VALOR_NUMERO DESDE IDENTIFICADOR clausula','eliminar_hasta_donde',6,'p_eliminar_hasta_donde','Delete.py',27),
  ('lista_valores -> valor','lista_valores',1,'p_lista_valores','Insert.py',28),
  ('lista_valores -> lista_valores COMA valor','lista_valores',3,'p_lista_valores','Insert.py',29),
  ('lista_columnas_crear -> lista_columnas_crear COMA lista_columna_crear','lista_columnas_crear',3,'p_lista_columnas_crear','Create.py',29),
  ('lista_columnas_crear -> lista_columna_crear','lista_columnas_crear',1,'p_lista_columnas_crear','Create.py',30),
  ('floro -> DISTINTO','floro',1,'p_floro','Select.py',29),
  ('floro -> empty','floro',1,'p_floro','Select.py',30),
  ('especificacion -> IDENTIFICADOR PARENTESIS_IZQ IDENTIFICADOR PARENTESIS_DER','especificacion',4,'p_especificacion','Join.py',30),
  ('instruccion -> seleccion','instruccion',1,'p_instruccion','AnalizadorSintactico.py',31),
  ('instruccion -> insertar','instruccion',1,'p_instruccion','AnalizadorSintactico.py',32),
  ('instruccion -> alterar','instruccion',1,'p_instruccion','AnalizadorSintactico.py',33),
  ('instruccion -> actualizar','instruccion',1,'p_instruccion','AnalizadorSintactico.py',34),
  ('instruccion -> eliminar','instruccion',1,'p_instruccion','AnalizadorSintactico.py',35),
  ('instruccion -> soltar','instruccion',1,'p_instruccion','AnalizadorSintactico.py',36),
  ('instruccion -> crear','instruccion',1,'p_instruccion','AnalizadorSintactico.py',37),
  ('instruccion -> transaccion','instruccion',1,'p_instruccion','AnalizadorSintactico.py',38),
  ('instruccion -> unir','instruccion',1,'p_instruccion','AnalizadorSintactico.py',39),
  ('instruccion -> valor','instruccion',1,'p_instruccion','AnalizadorSintactico.py',40),
  ('clausula -> DONDE IDENTIFICADOR comparador valor','clausula',4,'p_clausula','Delete.py',32),
  ('opt_column -> COLUMNA','opt_column',1,'p_opt_column','Alter.py',33),
  ('opt_column -> empty','opt_column',1,'p_opt_column','Alter.py',34),
  ('restricciones -> restricciones restriccion','restricciones',2,'p_restricciones','ReglasComunes.py',34),
  ('restricciones -> restriccion','restricciones',1,'p_restricciones','ReglasComunes.py',35),
  ('restricciones -> empty','restricciones',1,'p_restricciones','ReglasComunes.py',36),
  ('comparador -> IGUALDAD','comparador',1,'p_comparador','Delete.py',36),
  ('comparador -> MAYOR','comparador',1,'p_comparador','Delete.py',37),
  ('comparador -> MENOR','comparador',1,'p_comparador','Delete.py',38),
  ('comparador -> MAYOR_IGUAL','comparador',1,'p_comparador','Delete.py',39),
  ('comparador -> MENOR_IGUAL','comparador',1,'p_comparador','Delete.py',40),
  ('comparador -> DIFERENTE','comparador',1,'p_comparador','Delete.py',41),
  ('lista_columnas -> IDENTIFICADOR','lista_columnas',1,'p_lista_columnas','Select.py',38),
  ('lista_columnas -> lista_columnas COMA IDENTIFICADOR','lista_columnas',3,'p_lista_columnas','Select.py',39),
  ('lista_columnas -> TODO','lista_columnas',1,'p_lista_columnas','Select.py',40),
  ('alteracion -> SOLTAR opt_column IDENTIFICADOR','alteracion',3,'p_alteracion_drop','Alter.py',41),
  ('valor -> VALOR_NUMERO','valor',1,'p_valor','Delete.py',45),
  ('valor -> VALOR_CADENA','valor',1,'p_valor','Delete.py',46),
  ('valor -> VALOR_BOOLEANO','valor',1,'p_valor','Delete.py',47),
  ('valor -> VALOR_FLOTANTE','valor',1,'p_valor','Delete.py',48),
  ('restriccion -> CLAVE_PRIMARIA','restriccion',1,'p_restriccion','ReglasComunes.py',46),
  ('restriccion -> CLAVE_FORANEA referencia','restriccion',2,'p_restriccion','ReglasComunes.py',47),
  ('restriccion -> AUTOINCREMENTAL','restriccion',1,'p_restriccion','ReglasComunes.py',48),
  ('restriccion -> NO_NULO','restriccion',1,'p_restriccion','ReglasComunes.py',49),
  ('alteracion -> MODIFICAR opt_column lista_columna_crear','alteracion',3,'p_alteracion_modificar','Alter.py',48),
  ('referencia -> REFERENCIA IDENTIFICADOR PARENTESIS_IZQ IDENTIFICADOR PARENTESIS_DER','referencia',5,'p_referencia','ReglasComunes.py',56),
  ('alteracion -> RENOMBRAR opt_column IDENTIFICADOR A IDENTIFICADOR','alteracion',5,'p_alteracion_rename','Alter.py',57),
  ('opt_condiciones -> condiciones','opt_condiciones',1,'p_opt_condiciones','ReglasComunes.py',63),
  ('opt_condiciones -> empty','opt_condiciones',1,'p_opt_condiciones','ReglasComunes.py',64),
  ('alteracion -> CAMBIAR opt_column IDENTIFICADOR lista_columna_crear','alteracion',4,'p_alteracion_change','Alter.py',64),
  ('condiciones -> condiciones clausula','condiciones',2,'p_condiciones','ReglasComunes.py',72),
  ('condiciones -> clausula','condiciones',1,'p_condiciones','ReglasComunes.py',73),
  ('condicion_order -> IDENTIFICADOR ASCENDENTE','condicion_order',2,'p_condicion_order','ReglasComunes.py',115),
  ('condicion_order -> IDENTIFICADOR DESCENDENTE','condicion_order',2,'p_condicion_order','ReglasComunes.py',116),
  ('condicion_order -> IDENTIFICADOR','condicion_order',1,'p_condicion_order','ReglasComunes.py',117),
]
