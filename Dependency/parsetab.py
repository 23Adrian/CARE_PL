
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD AILMENT CREATE DIAGNOSE HAS ID LIST LP NEWLINE PERIOD REMOVE RP program : function\n                | create_patient\n                | add_symptoms\n                | list_symptoms\n                | diagnose_patient \n                | specific_diagnose\n                | add_conditions\n                | create_illness\n                | remove_illness\n                | remove_patient\n                | queue\n                | attend\n                | NEWLINE\n                \n                 create_illness : AILMENT LP ID RP PERIOD CREATE LP RP remove_illness : AILMENT LP ID RP PERIOD REMOVE LP RP\n    function : ID\n\n    create_patient : ID PERIOD CREATE LP RPadd_conditions : AILMENT LP ID RP PERIOD ADD LP ID RP add_symptoms : ID PERIOD HAS LP ID RP  list_symptoms : ID PERIOD LIST LP RP remove_patient : ID PERIOD REMOVE LP RP diagnose_patient : ID PERIOD DIAGNOSE LP RP specific_diagnose : ID PERIOD AILMENT LP ID RP PERIOD DIAGNOSE LP RP queue : ID LP ID RP attend : ID LP RP'
    
_lr_action_items = {'NEWLINE':([0,],[14,]),'ID':([0,18,19,30,33,50,],[15,26,28,38,41,54,]),'AILMENT':([0,17,],[16,24,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,27,35,37,39,40,42,44,55,56,58,59,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-16,-25,-24,-17,-20,-22,-21,-19,-14,-15,-18,-23,]),'PERIOD':([15,36,45,],[17,43,49,]),'LP':([15,16,20,21,22,23,24,25,46,47,48,53,],[18,19,29,30,31,32,33,34,50,51,52,57,]),'CREATE':([17,43,],[20,47,]),'HAS':([17,],[21,]),'LIST':([17,],[22,]),'DIAGNOSE':([17,49,],[23,53,]),'REMOVE':([17,43,],[25,48,]),'RP':([18,26,28,29,31,32,34,38,41,51,52,54,57,],[27,35,36,37,39,40,42,44,45,55,56,58,59,]),'ADD':([43,],[46,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'function':([0,],[2,]),'create_patient':([0,],[3,]),'add_symptoms':([0,],[4,]),'list_symptoms':([0,],[5,]),'diagnose_patient':([0,],[6,]),'specific_diagnose':([0,],[7,]),'add_conditions':([0,],[8,]),'create_illness':([0,],[9,]),'remove_illness':([0,],[10,]),'remove_patient':([0,],[11,]),'queue':([0,],[12,]),'attend':([0,],[13,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> function','program',1,'p_program','care_parse.py',11),
  ('program -> create_patient','program',1,'p_program','care_parse.py',12),
  ('program -> add_symptoms','program',1,'p_program','care_parse.py',13),
  ('program -> list_symptoms','program',1,'p_program','care_parse.py',14),
  ('program -> diagnose_patient','program',1,'p_program','care_parse.py',15),
  ('program -> specific_diagnose','program',1,'p_program','care_parse.py',16),
  ('program -> add_conditions','program',1,'p_program','care_parse.py',17),
  ('program -> create_illness','program',1,'p_program','care_parse.py',18),
  ('program -> remove_illness','program',1,'p_program','care_parse.py',19),
  ('program -> remove_patient','program',1,'p_program','care_parse.py',20),
  ('program -> queue','program',1,'p_program','care_parse.py',21),
  ('program -> attend','program',1,'p_program','care_parse.py',22),
  ('program -> NEWLINE','program',1,'p_program','care_parse.py',23),
  ('create_illness -> AILMENT LP ID RP PERIOD CREATE LP RP','create_illness',8,'p_create_illness','care_parse.py',29),
  ('remove_illness -> AILMENT LP ID RP PERIOD REMOVE LP RP','remove_illness',8,'p_remove_illness','care_parse.py',36),
  ('function -> ID','function',1,'p_function','care_parse.py',44),
  ('create_patient -> ID PERIOD CREATE LP RP','create_patient',5,'p_create_patient','care_parse.py',56),
  ('add_conditions -> AILMENT LP ID RP PERIOD ADD LP ID RP','add_conditions',9,'p_add_conditions','care_parse.py',63),
  ('add_symptoms -> ID PERIOD HAS LP ID RP','add_symptoms',6,'p_add_symptoms','care_parse.py',70),
  ('list_symptoms -> ID PERIOD LIST LP RP','list_symptoms',5,'p_list_symptoms','care_parse.py',77),
  ('remove_patient -> ID PERIOD REMOVE LP RP','remove_patient',5,'p_remove_patient','care_parse.py',84),
  ('diagnose_patient -> ID PERIOD DIAGNOSE LP RP','diagnose_patient',5,'p_diagnose_patient','care_parse.py',91),
  ('specific_diagnose -> ID PERIOD AILMENT LP ID RP PERIOD DIAGNOSE LP RP','specific_diagnose',10,'p_specific_diagnose','care_parse.py',98),
  ('queue -> ID LP ID RP','queue',4,'p_queue','care_parse.py',105),
  ('attend -> ID LP RP','attend',3,'p_attend','care_parse.py',112),
]
