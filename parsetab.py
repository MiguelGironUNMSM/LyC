
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'instruccionleftYOleftMENORMAYORMENOR_IGUALMAYOR_IGUALIGUALDADDIFERENTEleftMASMENOSleftMULTIPLICACIONDIVISIONMODULOA ACTUALIZAR AGREGAR AGRUPAR_POR ALGUNO ALGUNOS ALTERAR ASCENDENTE AUTOINCREMENTAL BOOLEANO CADENA CAMBIAR CARACTER CASO CLAVE_FORANEA CLAVE_PRIMARIA COLOCAR COLUMNA COMA COMENTARIO COMILLAS_SIMPLES COMO COMPLETO CON CONFIRMAR CONTAR CONVERTIR CREAR CUALQUIERA DECIMAL DERECHO DESCENDENTE DESDE DIFERENTE DISTINTO DIVISION DONDE ELIMINAR ENTERO ENTONCES ENTRE ES ESTABLECER_TRANSACCION ES_NULO EXISTE FECHA FIN FLOTANTE IDENTIFICADOR IDENTIFICADOR_INVALIDO IGUALDAD INICIAR_TRANSACCION INICIO INSERTAR_EN IZQUIERDO LIMITAR MAS MAXIMO MAYOR MAYOR_IGUAL MENOR MENOR_IGUAL MENOS MEZCLAR MIENTRAS MINIMO MODIFICAR MODULO MULTIPLICACION NO NORMAL NO_ES_NULO NO_NULO NULO O OBTENER ORDENAR_POR PARA PARENTESIS_DER PARENTESIS_IZQ PRIMEROS PROMEDIO PUNTO PUNTO_GUARDADO PYC RANGO REEMPLAZAR RENOMBRAR RESTRICCION REVERTIR SALTO_DE_LINEA SELECCIONAR SI SIMILAR_A SINO SOLTAR SUMA TABLA TENIENDO TEXTO TODO TODOS UNIR VALORES VALOR_BOOLEANO VALOR_CADENA VALOR_FLOTANTE VALOR_NUMERO Ycrear : CREAR TABLA IDENTIFICADOR PARENTESIS_IZQ lista_columnas_crear PARENTESIS_DERsoltar : SOLTAR TABLA IDENTIFICADORlista_columna_crear : IDENTIFICADOR tipo_dato restriccionesseleccion : SELECCIONAR lista_floro lista_columnas DESDE IDENTIFICADOR opt_condicionestransaccion : INICIAR_TRANSACCIONeliminar : eliminar_todo\n| eliminar_donde\n| eliminar_hasta_todo\n| eliminar_hasta_dondeinsertar : INSERTAR_EN IDENTIFICADOR PARENTESIS_IZQ lista_columnas_creadas PARENTESIS_DER VALORES lista_filasactualizar : ACTUALIZAR IDENTIFICADOR COLOCAR lista_asignaciones opt_condicionesalterar : ALTERAR TABLA IDENTIFICADOR alteracionesunir : UNIR tipo_unir IDENTIFICADOR CON condicionlista_columnas_crear : lista_columnas_crear COMA lista_columna_crear\n| lista_columna_creartransaccion : CONFIRMARlista_columnas_creadas : IDENTIFICADOR\n| lista_columnas_creadas COMA IDENTIFICADORlista_asignaciones : IDENTIFICADOR IGUALDAD valor\n| lista_asignaciones COMA IDENTIFICADOR IGUALDAD valortipo_dato : ENTERO especificacion\n| CADENA especificacion\n| CARACTER especificacion\n| FECHA especificacion\n| BOOLEANO especificacion\n| DECIMAL especificacion\n| TEXTO especificacion\n| FLOTANTE especificaciontransaccion : REVERTIReliminar_todo : ELIMINAR DESDE IDENTIFICADORtipo_unir : NORMAL\n| IZQUIERDO\n| DERECHO\n| COMPLETO\n| emptyalteraciones : alteracioneliminar_donde : ELIMINAR DESDE IDENTIFICADOR clausulalista_filas : fila \n| lista_filas COMA filalista_floro : lista_floro floro\n| floroalteraciones : alteracion COMA alteracioneseliminar_hasta_todo : ELIMINAR PRIMEROS VALOR_NUMERO DESDE IDENTIFICADORcondicion : IDENTIFICADOR IGUALDAD IDENTIFICADORalteracion : AGREGAR opt_column lista_columna_crearfila : PARENTESIS_IZQ lista_valores PARENTESIS_DEReliminar_hasta_donde : ELIMINAR PRIMEROS VALOR_NUMERO DESDE IDENTIFICADOR clausulaespecificacion : PARENTESIS_IZQ VALOR_NUMERO PARENTESIS_DER\n| emptyfloro : DISTINTO\n| PRIMEROS VALOR_NUMERO\n| emptyempty :lista_valores : valor\n| lista_valores COMA valorclausula : DONDE IDENTIFICADOR comparador valoropt_column : COLUMNA\n| emptyinstruccion : seleccion\n| insertar\n| alterar\n| actualizar\n| eliminar\n| soltar\n| crear\n| transaccion\n| unir\n| valorcomparador : IGUALDAD\n| MAYOR\n| MENOR\n| MAYOR_IGUAL\n| MENOR_IGUAL\n| DIFERENTErestricciones : restricciones restriccion\n| restriccion\n| emptylista_columnas : IDENTIFICADOR\n| lista_columnas COMA IDENTIFICADOR\n| TODOalteracion : SOLTAR opt_column IDENTIFICADORvalor : VALOR_NUMERO\n| VALOR_CADENA\n| VALOR_BOOLEANO\n| VALOR_FLOTANTEalteracion : MODIFICAR opt_column lista_columna_crearrestriccion : CLAVE_PRIMARIA\n| CLAVE_FORANEA\n| AUTOINCREMENTAL\n| NO_NULOalteracion : RENOMBRAR opt_column IDENTIFICADOR A IDENTIFICADORopt_condiciones : condiciones\n| emptyalteracion : CAMBIAR opt_column IDENTIFICADOR lista_columna_crearcondiciones : condiciones clausula\n| clausulacondicion_order : IDENTIFICADOR ASCENDENTE\n| IDENTIFICADOR DESCENDENTE\n| IDENTIFICADOR'
    
_lr_action_items = {'SELECCIONAR':([0,],[12,]),'INSERTAR_EN':([0,],[13,]),'ALTERAR':([0,],[14,]),'ACTUALIZAR':([0,],[15,]),'SOLTAR':([0,55,84,],[20,69,69,]),'CREAR':([0,],[21,]),'INICIAR_TRANSACCION':([0,],[22,]),'CONFIRMAR':([0,],[23,]),'REVERTIR':([0,],[24,]),'UNIR':([0,],[25,]),'VALOR_NUMERO':([0,34,48,92,129,130,131,132,133,134,135,137,142,151,171,],[26,53,61,26,26,-69,-70,-71,-72,-73,-74,26,26,169,26,]),'VALOR_CADENA':([0,92,129,130,131,132,133,134,135,137,142,171,],[27,27,27,-69,-70,-71,-72,-73,-74,27,27,27,]),'VALOR_BOOLEANO':([0,92,129,130,131,132,133,134,135,137,142,171,],[28,28,28,-69,-70,-71,-72,-73,-74,28,28,28,]),'VALOR_FLOTANTE':([0,92,129,130,131,132,133,134,135,137,142,171,],[29,29,29,-69,-70,-71,-72,-73,-74,29,29,29,]),'ELIMINAR':([0,],[30,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,16,17,18,19,22,23,24,26,27,28,29,57,60,66,67,74,77,80,93,95,96,97,102,104,105,108,109,110,111,114,116,117,118,119,120,121,122,123,124,125,126,136,138,139,141,143,144,145,146,147,148,149,150,152,153,154,155,156,157,158,159,161,162,166,167,168,170,172,173,],[0,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-6,-7,-8,-9,-5,-16,-29,-82,-83,-84,-85,-2,-30,-12,-36,-53,-37,-53,-11,-92,-93,-96,-13,-43,-4,-42,-45,-81,-86,-19,-95,-53,-53,-53,-53,-53,-53,-53,-53,-53,-1,-47,-10,-38,-94,-3,-76,-77,-87,-88,-89,-90,-21,-49,-22,-23,-24,-25,-26,-27,-28,-44,-56,-91,-20,-75,-46,-39,-48,]),'DISTINTO':([12,31,32,33,35,51,53,],[33,33,-41,-50,-52,-40,-51,]),'PRIMEROS':([12,30,31,32,33,35,51,53,],[34,48,34,-41,-50,-52,-40,-51,]),'IDENTIFICADOR':([12,13,15,25,31,32,33,35,37,39,40,41,42,43,44,45,46,47,51,53,54,56,62,63,68,69,70,71,72,75,76,78,79,83,85,86,87,88,89,90,91,94,113,127,128,140,],[-53,36,38,-53,50,-41,-50,-52,55,57,58,59,-31,-32,-33,-34,-35,60,-40,-51,64,73,80,81,-53,-53,-53,-53,-53,98,101,103,104,107,98,-57,-58,110,98,112,113,115,98,98,161,166,]),'TODO':([12,31,32,33,35,51,53,],[-53,52,-41,-50,-52,-40,-51,]),'TABLA':([14,20,21,],[37,39,40,]),'NORMAL':([25,],[42,]),'IZQUIERDO':([25,],[43,]),'DERECHO':([25,],[44,]),'COMPLETO':([25,],[45,]),'COMA':([26,27,28,29,49,50,52,64,65,67,74,81,99,100,107,109,110,111,114,117,118,119,120,121,122,123,124,125,138,139,141,143,144,145,146,147,148,149,150,152,153,154,155,156,157,158,159,160,163,164,166,167,168,170,172,173,174,],[-82,-83,-84,-85,63,-78,-80,-17,83,84,94,-79,127,-15,-18,-45,-81,-86,-19,-53,-53,-53,-53,-53,-53,-53,-53,-53,165,-38,-94,-3,-76,-77,-87,-88,-89,-90,-21,-49,-22,-23,-24,-25,-26,-27,-28,-14,171,-54,-91,-20,-75,-46,-39,-48,-55,]),'DONDE':([26,27,28,29,60,74,80,95,97,104,114,116,162,167,],[-82,-83,-84,-85,78,78,78,78,-96,78,-19,-95,-56,-20,]),'PARENTESIS_DER':([26,27,28,29,64,65,99,100,107,117,118,119,120,121,122,123,124,125,143,144,145,146,147,148,149,150,152,153,154,155,156,157,158,159,160,163,164,168,169,173,174,],[-82,-83,-84,-85,-17,82,126,-15,-18,-53,-53,-53,-53,-53,-53,-53,-53,-53,-3,-76,-77,-87,-88,-89,-90,-21,-49,-22,-23,-24,-25,-26,-27,-28,-14,170,-54,-75,173,-48,-55,]),'DESDE':([30,49,50,52,61,81,],[47,62,-78,-80,79,-79,]),'PARENTESIS_IZQ':([36,58,106,118,119,120,121,122,123,124,125,165,],[54,75,137,151,151,151,151,151,151,151,151,137,]),'COLOCAR':([38,],[56,]),'AGREGAR':([55,84,],[68,68,]),'MODIFICAR':([55,84,],[70,70,]),'RENOMBRAR':([55,84,],[71,71,]),'CAMBIAR':([55,84,],[72,72,]),'CON':([59,],[76,]),'COLUMNA':([68,69,70,71,72,],[86,86,86,86,86,]),'IGUALDAD':([73,101,103,115,],[92,128,130,142,]),'VALORES':([82,],[106,]),'ENTERO':([98,],[118,]),'CADENA':([98,],[119,]),'CARACTER':([98,],[120,]),'FECHA':([98,],[121,]),'BOOLEANO':([98,],[122,]),'DECIMAL':([98,],[123,]),'TEXTO':([98,],[124,]),'FLOTANTE':([98,],[125,]),'MAYOR':([103,],[131,]),'MENOR':([103,],[132,]),'MAYOR_IGUAL':([103,],[133,]),'MENOR_IGUAL':([103,],[134,]),'DIFERENTE':([103,],[135,]),'A':([112,],[140,]),'CLAVE_PRIMARIA':([117,118,119,120,121,122,123,124,125,143,144,145,146,147,148,149,150,152,153,154,155,156,157,158,159,168,173,],[146,-53,-53,-53,-53,-53,-53,-53,-53,146,-76,-77,-87,-88,-89,-90,-21,-49,-22,-23,-24,-25,-26,-27,-28,-75,-48,]),'CLAVE_FORANEA':([117,118,119,120,121,122,123,124,125,143,144,145,146,147,148,149,150,152,153,154,155,156,157,158,159,168,173,],[147,-53,-53,-53,-53,-53,-53,-53,-53,147,-76,-77,-87,-88,-89,-90,-21,-49,-22,-23,-24,-25,-26,-27,-28,-75,-48,]),'AUTOINCREMENTAL':([117,118,119,120,121,122,123,124,125,143,144,145,146,147,148,149,150,152,153,154,155,156,157,158,159,168,173,],[148,-53,-53,-53,-53,-53,-53,-53,-53,148,-76,-77,-87,-88,-89,-90,-21,-49,-22,-23,-24,-25,-26,-27,-28,-75,-48,]),'NO_NULO':([117,118,119,120,121,122,123,124,125,143,144,145,146,147,148,149,150,152,153,154,155,156,157,158,159,168,173,],[149,-53,-53,-53,-53,-53,-53,-53,-53,149,-76,-77,-87,-88,-89,-90,-21,-49,-22,-23,-24,-25,-26,-27,-28,-75,-48,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'instruccion':([0,],[1,]),'seleccion':([0,],[2,]),'insertar':([0,],[3,]),'alterar':([0,],[4,]),'actualizar':([0,],[5,]),'eliminar':([0,],[6,]),'soltar':([0,],[7,]),'crear':([0,],[8,]),'transaccion':([0,],[9,]),'unir':([0,],[10,]),'valor':([0,92,129,137,142,171,],[11,114,162,164,167,174,]),'eliminar_todo':([0,],[16,]),'eliminar_donde':([0,],[17,]),'eliminar_hasta_todo':([0,],[18,]),'eliminar_hasta_donde':([0,],[19,]),'lista_floro':([12,],[31,]),'floro':([12,31,],[32,51,]),'empty':([12,25,31,68,69,70,71,72,74,80,117,118,119,120,121,122,123,124,125,],[35,46,35,87,87,87,87,87,96,96,145,152,152,152,152,152,152,152,152,]),'tipo_unir':([25,],[41,]),'lista_columnas':([31,],[49,]),'lista_columnas_creadas':([54,],[65,]),'alteraciones':([55,84,],[66,108,]),'alteracion':([55,84,],[67,67,]),'lista_asignaciones':([56,],[74,]),'clausula':([60,74,80,95,104,],[77,97,97,116,136,]),'opt_column':([68,69,70,71,72,],[85,88,89,90,91,]),'opt_condiciones':([74,80,],[93,105,]),'condiciones':([74,80,],[95,95,]),'lista_columnas_crear':([75,],[99,]),'lista_columna_crear':([75,85,89,113,127,],[100,109,111,141,160,]),'condicion':([76,],[102,]),'tipo_dato':([98,],[117,]),'comparador':([103,],[129,]),'lista_filas':([106,],[138,]),'fila':([106,165,],[139,172,]),'restricciones':([117,],[143,]),'restriccion':([117,143,],[144,168,]),'especificacion':([118,119,120,121,122,123,124,125,],[150,153,154,155,156,157,158,159,]),'lista_valores':([137,],[163,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> instruccion","S'",1,None,None,None),
  ('crear -> CREAR TABLA IDENTIFICADOR PARENTESIS_IZQ lista_columnas_crear PARENTESIS_DER','crear',6,'p_crear','Create.py',2),
  ('soltar -> SOLTAR TABLA IDENTIFICADOR','soltar',3,'p_soltar','DropTable.py',2),
  ('lista_columna_crear -> IDENTIFICADOR tipo_dato restricciones','lista_columna_crear',3,'p_lista_columna_crear','ReglasComunes.py',2),
  ('seleccion -> SELECCIONAR lista_floro lista_columnas DESDE IDENTIFICADOR opt_condiciones','seleccion',6,'p_seleccion','Select.py',2),
  ('transaccion -> INICIAR_TRANSACCION','transaccion',1,'p_transaccion_iniciar','Transaction.py',2),
  ('eliminar -> eliminar_todo','eliminar',1,'p_eliminar','Delete.py',3),
  ('eliminar -> eliminar_donde','eliminar',1,'p_eliminar','Delete.py',4),
  ('eliminar -> eliminar_hasta_todo','eliminar',1,'p_eliminar','Delete.py',5),
  ('eliminar -> eliminar_hasta_donde','eliminar',1,'p_eliminar','Delete.py',6),
  ('insertar -> INSERTAR_EN IDENTIFICADOR PARENTESIS_IZQ lista_columnas_creadas PARENTESIS_DER VALORES lista_filas','insertar',7,'p_insertar','Insert.py',3),
  ('actualizar -> ACTUALIZAR IDENTIFICADOR COLOCAR lista_asignaciones opt_condiciones','actualizar',5,'p_actualizar','Update.py',3),
  ('alterar -> ALTERAR TABLA IDENTIFICADOR alteraciones','alterar',4,'p_alterar','Alter.py',4),
  ('unir -> UNIR tipo_unir IDENTIFICADOR CON condicion','unir',5,'p_unir','Join.py',4),
  ('lista_columnas_crear -> lista_columnas_crear COMA lista_columna_crear','lista_columnas_crear',3,'p_lista_columnas_crear','Create.py',6),
  ('lista_columnas_crear -> lista_columna_crear','lista_columnas_crear',1,'p_lista_columnas_crear','Create.py',7),
  ('transaccion -> CONFIRMAR','transaccion',1,'p_transaccion_confirmar','Transaction.py',6),
  ('lista_columnas_creadas -> IDENTIFICADOR','lista_columnas_creadas',1,'p_lista_columnas_creadas','Insert.py',8),
  ('lista_columnas_creadas -> lista_columnas_creadas COMA IDENTIFICADOR','lista_columnas_creadas',3,'p_lista_columnas_creadas','Insert.py',9),
  ('lista_asignaciones -> IDENTIFICADOR IGUALDAD valor','lista_asignaciones',3,'p_lista_asignaciones','Update.py',8),
  ('lista_asignaciones -> lista_asignaciones COMA IDENTIFICADOR IGUALDAD valor','lista_asignaciones',5,'p_lista_asignaciones','Update.py',9),
  ('tipo_dato -> ENTERO especificacion','tipo_dato',2,'p_tipo_dato','ReglasComunes.py',10),
  ('tipo_dato -> CADENA especificacion','tipo_dato',2,'p_tipo_dato','ReglasComunes.py',11),
  ('tipo_dato -> CARACTER especificacion','tipo_dato',2,'p_tipo_dato','ReglasComunes.py',12),
  ('tipo_dato -> FECHA especificacion','tipo_dato',2,'p_tipo_dato','ReglasComunes.py',13),
  ('tipo_dato -> BOOLEANO especificacion','tipo_dato',2,'p_tipo_dato','ReglasComunes.py',14),
  ('tipo_dato -> DECIMAL especificacion','tipo_dato',2,'p_tipo_dato','ReglasComunes.py',15),
  ('tipo_dato -> TEXTO especificacion','tipo_dato',2,'p_tipo_dato','ReglasComunes.py',16),
  ('tipo_dato -> FLOTANTE especificacion','tipo_dato',2,'p_tipo_dato','ReglasComunes.py',17),
  ('transaccion -> REVERTIR','transaccion',1,'p_transaccion_revertir','Transaction.py',10),
  ('eliminar_todo -> ELIMINAR DESDE IDENTIFICADOR','eliminar_todo',3,'p_eliminar_todo','Delete.py',11),
  ('tipo_unir -> NORMAL','tipo_unir',1,'p_tipo_unir','Join.py',11),
  ('tipo_unir -> IZQUIERDO','tipo_unir',1,'p_tipo_unir','Join.py',12),
  ('tipo_unir -> DERECHO','tipo_unir',1,'p_tipo_unir','Join.py',13),
  ('tipo_unir -> COMPLETO','tipo_unir',1,'p_tipo_unir','Join.py',14),
  ('tipo_unir -> empty','tipo_unir',1,'p_tipo_unir','Join.py',15),
  ('alteraciones -> alteracion','alteraciones',1,'p_alteraciones_single','Alter.py',12),
  ('eliminar_donde -> ELIMINAR DESDE IDENTIFICADOR clausula','eliminar_donde',4,'p_eliminar_donde','Delete.py',15),
  ('lista_filas -> fila','lista_filas',1,'p_lista_filas','Insert.py',16),
  ('lista_filas -> lista_filas COMA fila','lista_filas',3,'p_lista_filas','Insert.py',17),
  ('lista_floro -> lista_floro floro','lista_floro',2,'p_lista_floro','Select.py',16),
  ('lista_floro -> floro','lista_floro',1,'p_lista_floro','Select.py',17),
  ('alteraciones -> alteracion COMA alteraciones','alteraciones',3,'p_alteraciones_multiple','Alter.py',17),
  ('eliminar_hasta_todo -> ELIMINAR PRIMEROS VALOR_NUMERO DESDE IDENTIFICADOR','eliminar_hasta_todo',5,'p_eliminar_hasta_todo','Delete.py',20),
  ('condicion -> IDENTIFICADOR IGUALDAD IDENTIFICADOR','condicion',3,'p_condicion','Join.py',21),
  ('alteracion -> AGREGAR opt_column lista_columna_crear','alteracion',3,'p_alteracion_add','Alter.py',24),
  ('fila -> PARENTESIS_IZQ lista_valores PARENTESIS_DER','fila',3,'p_fila','Insert.py',24),
  ('eliminar_hasta_donde -> ELIMINAR PRIMEROS VALOR_NUMERO DESDE IDENTIFICADOR clausula','eliminar_hasta_donde',6,'p_eliminar_hasta_donde','Delete.py',25),
  ('especificacion -> PARENTESIS_IZQ VALOR_NUMERO PARENTESIS_DER','especificacion',3,'p_especificacion','ReglasComunes.py',25),
  ('especificacion -> empty','especificacion',1,'p_especificacion','ReglasComunes.py',26),
  ('floro -> DISTINTO','floro',1,'p_floro','Select.py',25),
  ('floro -> PRIMEROS VALOR_NUMERO','floro',2,'p_floro','Select.py',26),
  ('floro -> empty','floro',1,'p_floro','Select.py',27),
  ('empty -> <empty>','empty',0,'p_empty','Join.py',26),
  ('lista_valores -> valor','lista_valores',1,'p_lista_valores','Insert.py',28),
  ('lista_valores -> lista_valores COMA valor','lista_valores',3,'p_lista_valores','Insert.py',29),
  ('clausula -> DONDE IDENTIFICADOR comparador valor','clausula',4,'p_clausula','Delete.py',29),
  ('opt_column -> COLUMNA','opt_column',1,'p_opt_column','Alter.py',30),
  ('opt_column -> empty','opt_column',1,'p_opt_column','Alter.py',31),
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
  ('comparador -> IGUALDAD','comparador',1,'p_comparador','Delete.py',33),
  ('comparador -> MAYOR','comparador',1,'p_comparador','Delete.py',34),
  ('comparador -> MENOR','comparador',1,'p_comparador','Delete.py',35),
  ('comparador -> MAYOR_IGUAL','comparador',1,'p_comparador','Delete.py',36),
  ('comparador -> MENOR_IGUAL','comparador',1,'p_comparador','Delete.py',37),
  ('comparador -> DIFERENTE','comparador',1,'p_comparador','Delete.py',38),
  ('restricciones -> restricciones restriccion','restricciones',2,'p_restricciones','ReglasComunes.py',34),
  ('restricciones -> restriccion','restricciones',1,'p_restricciones','ReglasComunes.py',35),
  ('restricciones -> empty','restricciones',1,'p_restricciones','ReglasComunes.py',36),
  ('lista_columnas -> IDENTIFICADOR','lista_columnas',1,'p_lista_columnas','Select.py',37),
  ('lista_columnas -> lista_columnas COMA IDENTIFICADOR','lista_columnas',3,'p_lista_columnas','Select.py',38),
  ('lista_columnas -> TODO','lista_columnas',1,'p_lista_columnas','Select.py',39),
  ('alteracion -> SOLTAR opt_column IDENTIFICADOR','alteracion',3,'p_alteracion_drop','Alter.py',38),
  ('valor -> VALOR_NUMERO','valor',1,'p_valor','Delete.py',42),
  ('valor -> VALOR_CADENA','valor',1,'p_valor','Delete.py',43),
  ('valor -> VALOR_BOOLEANO','valor',1,'p_valor','Delete.py',44),
  ('valor -> VALOR_FLOTANTE','valor',1,'p_valor','Delete.py',45),
  ('alteracion -> MODIFICAR opt_column lista_columna_crear','alteracion',3,'p_alteracion_modificar','Alter.py',45),
  ('restriccion -> CLAVE_PRIMARIA','restriccion',1,'p_restriccion','ReglasComunes.py',46),
  ('restriccion -> CLAVE_FORANEA','restriccion',1,'p_restriccion','ReglasComunes.py',47),
  ('restriccion -> AUTOINCREMENTAL','restriccion',1,'p_restriccion','ReglasComunes.py',48),
  ('restriccion -> NO_NULO','restriccion',1,'p_restriccion','ReglasComunes.py',49),
  ('alteracion -> RENOMBRAR opt_column IDENTIFICADOR A IDENTIFICADOR','alteracion',5,'p_alteracion_rename','Alter.py',53),
  ('opt_condiciones -> condiciones','opt_condiciones',1,'p_opt_condiciones','ReglasComunes.py',56),
  ('opt_condiciones -> empty','opt_condiciones',1,'p_opt_condiciones','ReglasComunes.py',57),
  ('alteracion -> CAMBIAR opt_column IDENTIFICADOR lista_columna_crear','alteracion',4,'p_alteracion_change','Alter.py',60),
  ('condiciones -> condiciones clausula','condiciones',2,'p_condiciones','ReglasComunes.py',62),
  ('condiciones -> clausula','condiciones',1,'p_condiciones','ReglasComunes.py',63),
  ('condicion_order -> IDENTIFICADOR ASCENDENTE','condicion_order',2,'p_condicion_order','ReglasComunes.py',105),
  ('condicion_order -> IDENTIFICADOR DESCENDENTE','condicion_order',2,'p_condicion_order','ReglasComunes.py',106),
  ('condicion_order -> IDENTIFICADOR','condicion_order',1,'p_condicion_order','ReglasComunes.py',107),
]
