# CARE_PL4

Care is a prototype Health Care protocol language

1.To Create a patient simply write the patient's name
followed by .create

Ex: 
Angel.create

2.To remove a patient simply write the patient's name
followed by .remove

Ex:
Angel.remove

3.To add a symptom use the patient's name
then use .has() with symptom

Ex:
Angel.has(fever)

4.To list a patient's symptoms use list

Ex:
Angel.list

5.To auto diagnose patient
    Simply write : Patient_Name.diagnose

Ex:
Angel.diagnose

6.To define your own illnesses
    Simply write : define.(illness)
    
Ex:
define.(flu)

7.To add the symptom just write it inside the add

Ex:
illness(flu).add(fever)


