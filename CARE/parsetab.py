
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CREATE DEFINE DIAGNOSE HAS ID LIST LP PERIOD REMOVE RP program : function\n                | create_patient\n                | remove_patient\n                | add_symptoms\n                | list_symptoms\n                | diagnose_patient \n                | specific_diagnose\n                | create_illness\n                | add_conditions\n                \n                \n    function : ID\n     create_patient : ID PERIOD CREATE remove_patient : ID PERIOD REMOVE create_illness : DEFINE PERIOD LP ID RP  add_conditions : ID LP ID RP PERIOD ID LP ID RP  add_symptoms : ID PERIOD HAS LP ID RP  list_symptoms : ID PERIOD LIST  diagnose_patient : ID PERIOD DIAGNOSE  specific_diagnose : ID PERIOD ID LP ID RP PERIOD ID LP RP'
    
_lr_action_items = {'ID':([0,13,14,23,24,25,30,35,36,],[11,16,22,27,28,29,34,37,38,]),'DEFINE':([0,],[12,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,17,18,20,21,31,33,40,41,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-16,-17,-13,-15,-14,-18,]),'PERIOD':([11,12,26,32,],[13,15,30,35,]),'LP':([11,15,16,19,34,37,],[14,23,24,25,36,39,]),'CREATE':([13,],[17,]),'REMOVE':([13,],[18,]),'HAS':([13,],[19,]),'LIST':([13,],[20,]),'DIAGNOSE':([13,],[21,]),'RP':([22,27,28,29,38,39,],[26,31,32,33,40,41,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'function':([0,],[2,]),'create_patient':([0,],[3,]),'remove_patient':([0,],[4,]),'add_symptoms':([0,],[5,]),'list_symptoms':([0,],[6,]),'diagnose_patient':([0,],[7,]),'specific_diagnose':([0,],[8,]),'create_illness':([0,],[9,]),'add_conditions':([0,],[10,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> function','program',1,'p_program','care_parse.py',10),
  ('program -> create_patient','program',1,'p_program','care_parse.py',11),
  ('program -> remove_patient','program',1,'p_program','care_parse.py',12),
  ('program -> add_symptoms','program',1,'p_program','care_parse.py',13),
  ('program -> list_symptoms','program',1,'p_program','care_parse.py',14),
  ('program -> diagnose_patient','program',1,'p_program','care_parse.py',15),
  ('program -> specific_diagnose','program',1,'p_program','care_parse.py',16),
  ('program -> create_illness','program',1,'p_program','care_parse.py',17),
  ('program -> add_conditions','program',1,'p_program','care_parse.py',18),
  ('function -> ID','function',1,'p_function','care_parse.py',24),
  ('create_patient -> ID PERIOD CREATE','create_patient',3,'p_create_patient','care_parse.py',33),
  ('remove_patient -> ID PERIOD REMOVE','remove_patient',3,'p_remove_patient','care_parse.py',39),
  ('create_illness -> DEFINE PERIOD LP ID RP','create_illness',5,'p_create_illness','care_parse.py',45),
  ('add_conditions -> ID LP ID RP PERIOD ID LP ID RP','add_conditions',9,'p_add_conditions','care_parse.py',51),
  ('add_symptoms -> ID PERIOD HAS LP ID RP','add_symptoms',6,'p_add_symptoms','care_parse.py',57),
  ('list_symptoms -> ID PERIOD LIST','list_symptoms',3,'p_list_symptoms','care_parse.py',63),
  ('diagnose_patient -> ID PERIOD DIAGNOSE','diagnose_patient',3,'p_diagnose_patient','care_parse.py',75),
  ('specific_diagnose -> ID PERIOD ID LP ID RP PERIOD ID LP RP','specific_diagnose',10,'p_specific_diagnose','care_parse.py',81),
]
