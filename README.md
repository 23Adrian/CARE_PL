# CARE_PL4

Care is a prototype Health Care protocol language

To Create a patient simply write the patient's name
followed by .()

Ex: 
Angel.()

To add a symptom use the patient's name
then use .has() with symptom

Ex:
Angel.has(fever)

To list a patient's symptoms use list()

Ex:
Angel.list()

To auto diagnose patient
    Simply write : Patient_Name.diagnose

Ex:
Angel.diagnose

To define your own illnesses
    Simply write : illness(ILLNESS_NAME).add()
    
Ex:
illness(flu).add()

To add the symptom just write it inside the add

Ex:
illness(flu).add(fever)


