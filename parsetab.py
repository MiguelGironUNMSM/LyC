
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'instruccionleftYOleftMENORMAYORMENOR_IGUALMAYOR_IGUALIGUALDADDIFERENTEleftMASMENOSleftMULTIPLICACIONDIVISIONMODULOA ACTUALIZAR AGREGAR AGRUPAR_POR ALGUNO ALGUNOS ALTERAR ASCENDENTE AUTOINCREMENTAL BOOLEANO CADENA CAMBIAR CARACTER CASO CLAVE_FORANEA CLAVE_PRIMARIA COLOCAR COLUMNA COMA COMENTARIO COMILLAS_SIMPLES COMO COMPLETO CON CONFIRMAR CONTAR CONVERTIR CREAR CUALQUIERA DECIMAL DERECHO DESCENDENTE DESDE DIFERENTE DISTINTO DIVISION DONDE ELIMINAR ENTERO ENTONCES ENTRE ES ESTABLECER_TRANSACCION ES_NULO EXISTE FECHA FIN FLOTANTE IDENTIFICADOR IDENTIFICADOR_INVALIDO IGUALDAD INICIAR_TRANSACCION INICIO INSERTAR_EN IZQUIERDO LIMITAR MAS MAXIMO MAYOR MAYOR_IGUAL MENOR MENOR_IGUAL MENOS MEZCLAR MIENTRAS MINIMO MODIFICAR MODULO MULTIPLICACION NO NORMAL NO_ES_NULO NO_NULO NULO O OBTENER ORDENAR_POR PARA PARENTESIS_DER PARENTESIS_IZQ PRIMEROS PROMEDIO PUNTO PUNTO_GUARDADO PYC RANGO REEMPLAZAR REFERENCIA RENOMBRAR RESTRICCION REVERTIR SALTO_DE_LINEA SELECCIONAR SI SIMILAR_A SINO SOLTAR SUMA TABLA TENIENDO TEXTO TODO TODOS UNIR VALORES VALOR_BOOLEANO VALOR_CADENA VALOR_FLOTANTE VALOR_NUMERO Ylista_columna_crear : IDENTIFICADOR tipo_dato restriccionestransaccion : INICIAR_TRANSACCIONinsertar : INSERTAR_EN IDENTIFICADOR PARENTESIS_IZQ lista_columnas_creadas PARENTESIS_DER VALORES lista_filascrear : CREAR TABLA IDENTIFICADOR PARENTESIS_IZQ lista_columnas_crear PARENTESIS_DERsoltar : SOLTAR TABLA IDENTIFICADOR\n              | SOLTAR TABLA IDENTIFICADOR condicional unir : UNIR tipo_unir IDENTIFICADOR CON condicionseleccion : SELECCIONAR lista_floro lista_columnas DESDE IDENTIFICADOR opt_condiciones\n                 | SELECCIONAR lista_floro lista_columnas DESDE IDENTIFICADOR opt_condiciones uniractualizar : ACTUALIZAR IDENTIFICADOR COLOCAR lista_asignaciones DONDE opt_condiciones\n                  | ACTUALIZAR IDENTIFICADOR COLOCAR lista_asignaciones\n    eliminar : eliminar_todo\n                | eliminar_donde\n                | eliminar_hasta_todo\n                | eliminar_hasta_dondealterar : ALTERAR TABLA IDENTIFICADOR alteracionestransaccion : CONFIRMARlista_columnas_creadas : IDENTIFICADOR\n                              | lista_columnas_creadas COMA IDENTIFICADORtipo_dato : ENTERO\n                 | CADENA\n                 | CARACTER\n                 | FECHA\n                 | BOOLEANO\n                 | DECIMAL\n                 | TEXTO\n                 | FLOTANTEtransaccion : REVERTIRtipo_unir : NORMAL\n                 | IZQUIERDO\n                 | DERECHO\n                 | COMPLETO\n                 | emptycondicional : SI EXISTE eliminar_todo : ELIMINAR DESDE IDENTIFICADORalteraciones : alteracionlista_asignaciones : IDENTIFICADOR IGUALDAD valor\n                          | lista_asignaciones COMA IDENTIFICADOR IGUALDAD valorlista_filas : fila \n                  | lista_filas COMA filaeliminar_donde : ELIMINAR DESDE IDENTIFICADOR clausulaalteraciones : alteracion COMA alteracioneslista_floro : lista_floro floro\n                   | florocondicion : especificacion IGUALDAD especificacioneliminar_hasta_todo : ELIMINAR PRIMEROS VALOR_NUMERO DESDE IDENTIFICADORfila : PARENTESIS_IZQ lista_valores PARENTESIS_DERalteracion : AGREGAR opt_column lista_columna_crearempty :eliminar_hasta_donde : ELIMINAR PRIMEROS VALOR_NUMERO DESDE IDENTIFICADOR clausulalista_valores : valor\n    | lista_valores COMA valorlista_columnas_crear : lista_columnas_crear COMA lista_columna_crear\n                      | lista_columna_crearfloro : DISTINTO\n             | emptyespecificacion : IDENTIFICADOR PARENTESIS_IZQ IDENTIFICADOR PARENTESIS_DERinstruccion : seleccion\n    | insertar\n    | alterar\n    | actualizar\n    | eliminar\n    | soltar\n    | crear\n    | transaccion\n    | unir\n    | valorclausula : DONDE IDENTIFICADOR comparador valoropt_column : COLUMNA\n                  | emptyrestricciones : restricciones restriccion\n                     | restriccion\n                     | emptycomparador : IGUALDAD\n                  | MAYOR\n                  | MENOR\n                  | MAYOR_IGUAL\n                  | MENOR_IGUAL\n                  | DIFERENTElista_columnas : IDENTIFICADOR\n                      | lista_columnas COMA IDENTIFICADOR\n                      | TODOalteracion : SOLTAR opt_column IDENTIFICADORvalor : VALOR_NUMERO\n             | VALOR_CADENA\n             | VALOR_BOOLEANO\n             | VALOR_FLOTANTErestriccion : CLAVE_PRIMARIA\n                   | CLAVE_FORANEA referencia \n                   | AUTOINCREMENTAL\n                   | NO_NULOalteracion : MODIFICAR opt_column lista_columna_crearreferencia : REFERENCIA IDENTIFICADOR PARENTESIS_IZQ IDENTIFICADOR PARENTESIS_DERalteracion : RENOMBRAR opt_column IDENTIFICADOR A IDENTIFICADORopt_condiciones : condiciones\n                       | emptyalteracion : CAMBIAR opt_column IDENTIFICADOR lista_columna_crearcondiciones : condiciones clausula\n                   | clausulacondicion_order : IDENTIFICADOR ASCENDENTE\n                       | IDENTIFICADOR DESCENDENTE\n                       | IDENTIFICADOR'
    
_lr_action_items = {'SELECCIONAR':([0,],[12,]),'INSERTAR_EN':([0,],[13,]),'ALTERAR':([0,],[14,]),'ACTUALIZAR':([0,],[15,]),'SOLTAR':([0,53,84,],[20,67,67,]),'CREAR':([0,],[21,]),'INICIAR_TRANSACCION':([0,],[22,]),'CONFIRMAR':([0,],[23,]),'REVERTIR':([0,],[24,]),'UNIR':([0,26,27,28,29,80,104,105,106,107,141,158,],[25,-84,-85,-86,-87,-49,25,-95,-96,-99,-98,-68,]),'VALOR_NUMERO':([0,47,92,132,133,134,135,136,137,138,142,147,169,],[26,59,26,26,-74,-75,-76,-77,-78,-79,26,26,26,]),'VALOR_CADENA':([0,92,132,133,134,135,136,137,138,142,147,169,],[27,27,27,-74,-75,-76,-77,-78,-79,27,27,27,]),'VALOR_BOOLEANO':([0,92,132,133,134,135,136,137,138,142,147,169,],[28,28,28,-74,-75,-76,-77,-78,-79,28,28,28,]),'VALOR_FLOTANTE':([0,92,132,133,134,135,136,137,138,142,147,169,],[29,29,29,-74,-75,-76,-77,-78,-79,29,29,29,]),'ELIMINAR':([0,],[30,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,16,17,18,19,22,23,24,26,27,28,29,55,58,64,65,72,73,77,80,93,95,100,103,104,105,106,107,110,111,112,113,116,117,119,120,121,122,123,124,125,126,127,128,139,140,141,143,144,146,148,149,150,151,153,154,157,158,162,163,164,165,167,168,170,175,],[0,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-12,-13,-14,-15,-2,-17,-28,-84,-85,-86,-87,-5,-35,-16,-36,-11,-6,-41,-49,-49,-34,-7,-46,-8,-95,-96,-99,-42,-48,-83,-92,-37,-10,-49,-20,-21,-22,-23,-24,-25,-26,-27,-4,-50,-9,-98,-3,-39,-97,-1,-72,-73,-88,-90,-91,-45,-68,-94,-38,-71,-89,-57,-47,-40,-93,]),'DISTINTO':([12,31,32,33,34,50,],[33,33,-44,-55,-56,-43,]),'IDENTIFICADOR':([12,13,15,25,31,32,33,34,36,38,39,40,41,42,43,44,45,46,50,52,54,60,61,66,67,68,69,70,75,76,78,79,83,85,86,87,88,89,90,91,94,115,129,130,131,145,166,173,],[-49,35,37,-49,49,-44,-55,-56,53,55,56,57,-29,-30,-31,-32,-33,58,-43,62,71,80,81,-49,-49,-49,-49,-49,96,99,102,103,109,96,-69,-70,112,96,114,115,118,96,96,156,99,162,171,174,]),'TODO':([12,31,32,33,34,50,],[-49,51,-44,-55,-56,-43,]),'TABLA':([14,20,21,],[36,38,39,]),'NORMAL':([25,],[41,]),'IZQUIERDO':([25,],[42,]),'DERECHO':([25,],[43,]),'COMPLETO':([25,],[44,]),'DONDE':([26,27,28,29,58,72,80,93,103,105,107,116,141,158,163,],[-84,-85,-86,-87,78,93,78,78,78,78,-99,-37,-98,-68,-38,]),'COMA':([26,27,28,29,48,49,51,62,63,65,72,81,97,98,109,111,112,113,116,119,120,121,122,123,124,125,126,127,143,144,146,148,149,150,151,153,154,155,159,160,162,163,164,165,168,170,172,175,],[-84,-85,-86,-87,61,-80,-82,-18,83,84,94,-81,129,-54,-19,-48,-83,-92,-37,-49,-20,-21,-22,-23,-24,-25,-26,-27,161,-39,-97,-1,-72,-73,-88,-90,-91,-53,169,-51,-94,-38,-71,-89,-47,-40,-52,-93,]),'PARENTESIS_DER':([26,27,28,29,62,63,97,98,109,119,120,121,122,123,124,125,126,127,148,149,150,151,153,154,155,156,159,160,164,165,172,174,175,],[-84,-85,-86,-87,-18,82,128,-54,-19,-49,-20,-21,-22,-23,-24,-25,-26,-27,-1,-72,-73,-88,-90,-91,-53,167,168,-51,-71,-89,-52,175,-93,]),'DESDE':([30,48,49,51,59,81,],[46,60,-80,-82,79,-81,]),'PRIMEROS':([30,],[47,]),'PARENTESIS_IZQ':([35,56,99,108,161,171,],[52,75,130,142,142,173,]),'COLOCAR':([37,],[54,]),'AGREGAR':([53,84,],[66,66,]),'MODIFICAR':([53,84,],[68,68,]),'RENOMBRAR':([53,84,],[69,69,]),'CAMBIAR':([53,84,],[70,70,]),'SI':([55,],[74,]),'CON':([57,],[76,]),'COLUMNA':([66,67,68,69,70,],[86,86,86,86,86,]),'IGUALDAD':([71,101,102,118,167,],[92,131,133,147,-57,]),'EXISTE':([74,],[95,]),'VALORES':([82,],[108,]),'ENTERO':([96,],[120,]),'CADENA':([96,],[121,]),'CARACTER':([96,],[122,]),'FECHA':([96,],[123,]),'BOOLEANO':([96,],[124,]),'DECIMAL':([96,],[125,]),'TEXTO':([96,],[126,]),'FLOTANTE':([96,],[127,]),'MAYOR':([102,],[134,]),'MENOR':([102,],[135,]),'MAYOR_IGUAL':([102,],[136,]),'MENOR_IGUAL':([102,],[137,]),'DIFERENTE':([102,],[138,]),'A':([114,],[145,]),'CLAVE_PRIMARIA':([119,120,121,122,123,124,125,126,127,148,149,150,151,153,154,164,165,175,],[151,-20,-21,-22,-23,-24,-25,-26,-27,151,-72,-73,-88,-90,-91,-71,-89,-93,]),'CLAVE_FORANEA':([119,120,121,122,123,124,125,126,127,148,149,150,151,153,154,164,165,175,],[152,-20,-21,-22,-23,-24,-25,-26,-27,152,-72,-73,-88,-90,-91,-71,-89,-93,]),'AUTOINCREMENTAL':([119,120,121,122,123,124,125,126,127,148,149,150,151,153,154,164,165,175,],[153,-20,-21,-22,-23,-24,-25,-26,-27,153,-72,-73,-88,-90,-91,-71,-89,-93,]),'NO_NULO':([119,120,121,122,123,124,125,126,127,148,149,150,151,153,154,164,165,175,],[154,-20,-21,-22,-23,-24,-25,-26,-27,154,-72,-73,-88,-90,-91,-71,-89,-93,]),'REFERENCIA':([152,],[166,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'instruccion':([0,],[1,]),'seleccion':([0,],[2,]),'insertar':([0,],[3,]),'alterar':([0,],[4,]),'actualizar':([0,],[5,]),'eliminar':([0,],[6,]),'soltar':([0,],[7,]),'crear':([0,],[8,]),'transaccion':([0,],[9,]),'unir':([0,104,],[10,140,]),'valor':([0,92,132,142,147,169,],[11,116,158,160,163,172,]),'eliminar_todo':([0,],[16,]),'eliminar_donde':([0,],[17,]),'eliminar_hasta_todo':([0,],[18,]),'eliminar_hasta_donde':([0,],[19,]),'lista_floro':([12,],[31,]),'floro':([12,31,],[32,50,]),'empty':([12,25,31,66,67,68,69,70,80,93,119,],[34,45,34,87,87,87,87,87,106,106,150,]),'tipo_unir':([25,],[40,]),'lista_columnas':([31,],[48,]),'lista_columnas_creadas':([52,],[63,]),'alteraciones':([53,84,],[64,110,]),'alteracion':([53,84,],[65,65,]),'lista_asignaciones':([54,],[72,]),'condicional':([55,],[73,]),'clausula':([58,80,93,103,105,],[77,107,107,139,141,]),'opt_column':([66,67,68,69,70,],[85,88,89,90,91,]),'lista_columnas_crear':([75,],[97,]),'lista_columna_crear':([75,85,89,115,129,],[98,111,113,146,155,]),'condicion':([76,],[100,]),'especificacion':([76,131,],[101,157,]),'opt_condiciones':([80,93,],[104,117,]),'condiciones':([80,93,],[105,105,]),'tipo_dato':([96,],[119,]),'comparador':([102,],[132,]),'lista_filas':([108,],[143,]),'fila':([108,161,],[144,170,]),'restricciones':([119,],[148,]),'restriccion':([119,148,],[149,164,]),'lista_valores':([142,],[159,]),'referencia':([152,],[165,]),}

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
  ('lista_asignaciones -> IDENTIFICADOR IGUALDAD valor','lista_asignaciones',3,'p_alteraciones_update','Update.py',14),
  ('lista_asignaciones -> lista_asignaciones COMA IDENTIFICADOR IGUALDAD valor','lista_asignaciones',5,'p_alteraciones_update','Update.py',15),
  ('lista_filas -> fila','lista_filas',1,'p_lista_filas','Insert.py',16),
  ('lista_filas -> lista_filas COMA fila','lista_filas',3,'p_lista_filas','Insert.py',17),
  ('eliminar_donde -> ELIMINAR DESDE IDENTIFICADOR clausula','eliminar_donde',4,'p_eliminar_donde','Delete.py',17),
  ('alteraciones -> alteracion COMA alteraciones','alteraciones',3,'p_alteraciones_multiple','Alter.py',19),
  ('lista_floro -> lista_floro floro','lista_floro',2,'p_lista_floro','Select.py',20),
  ('lista_floro -> floro','lista_floro',1,'p_lista_floro','Select.py',21),
  ('condicion -> especificacion IGUALDAD especificacion','condicion',3,'p_condicion','Join.py',21),
  ('eliminar_hasta_todo -> ELIMINAR PRIMEROS VALOR_NUMERO DESDE IDENTIFICADOR','eliminar_hasta_todo',5,'p_eliminar_hasta_todo','Delete.py',22),
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
