
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'FALSE ID LP PATIENT PERIOD RP TRUE program : function\n                | create_patient\n                | add_symptoms\n                | list_symptoms\n                | diagnose_patient \n    function : ID\n    create_patient : ID PERIOD LP RP add_symptoms : ID PERIOD ID LP ID RP  list_symptoms : ID PERIOD ID LP RP diagnose_patient : ID PERIOD ID LP RP'
    
_lr_action_items = {'ID':([0,8,11,],[7,9,13,]),'$end':([1,2,3,4,5,6,7,12,14,15,],[0,-1,-2,-3,-4,-5,-6,-7,-9,-8,]),'PERIOD':([7,],[8,]),'LP':([8,9,],[10,11,]),'RP':([10,11,13,],[12,14,15,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'function':([0,],[2,]),'create_patient':([0,],[3,]),'add_symptoms':([0,],[4,]),'list_symptoms':([0,],[5,]),'diagnose_patient':([0,],[6,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> function','program',1,'p_program','care_parse.py',9),
  ('program -> create_patient','program',1,'p_program','care_parse.py',10),
  ('program -> add_symptoms','program',1,'p_program','care_parse.py',11),
  ('program -> list_symptoms','program',1,'p_program','care_parse.py',12),
  ('program -> diagnose_patient','program',1,'p_program','care_parse.py',13),
  ('function -> ID','function',1,'p_function','care_parse.py',17),
  ('create_patient -> ID PERIOD LP RP','create_patient',4,'p_create_patient','care_parse.py',26),
  ('add_symptoms -> ID PERIOD ID LP ID RP','add_symptoms',6,'p_add_symptoms','care_parse.py',31),
  ('list_symptoms -> ID PERIOD ID LP RP','list_symptoms',5,'p_list_symptoms','care_parse.py',36),
  ('diagnose_patient -> ID PERIOD ID LP RP','diagnose_patient',5,'p_diagnose_patient','care_parse.py',41),
]
