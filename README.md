# CARE_PL4

Care is a prototype Health Care protocal language

To Create a patient simply write The Patient's name
followed by .()

ex Angel.()

To add a symptom:
    use the patient's name
    then use .has() with symptom

ex:
Angel.has(fever)

To list a patient's sintom's use list()
    ex:
    Angel.list()

To auto diagnose patient
    Simply write : Patient_Name.diagnose

Ex:
Angel.diagnose

to define your own illnesses
    Simply write : illness(ILLNESS_NAME).add()
    
to add the simptom just write it inside the add

illness(flu).add()
illness(flu0.add(fever)


