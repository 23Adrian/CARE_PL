import sys
import queue

from CARE import care_parse

cold = ["sneezing", "sore_throat", "congestion", "coughing"]
flu = ["fever", "aches", "chills", "fatigue", "coughing", "headache"]
dengue = ["high_fever", "headache", "fatigue", "nausea", "skin_rash", "joint_pain", "vomiting"]
norovirus = ["nausea", "vomiting", "low_fever", "diarrhea", "malaise", "muscle_pain"]
stroke = ["dizziness", "severe_headache", "numb_extremities", "confusion"]
diabetes = ["frequent_urination", "weight_loss", "constant_tiredness", "numb_extremities"]

custom_definitions = []


p = queue.Queue(maxsize=0)


def func_parse(func):
    if func == "HELP":
        display_help()
    elif func == "EXIT":
        exit_program()
    else:
        print("Function is not valid")


def create_patient(name):
    if name.lower() in care_parse.patients:
        print("Patient already exists.")
    else:
        print("Added patient: " + name.capitalize())
        care_parse.patients[name.lower()] = []

def patient_queue(name):
    if not name.lower() in care_parse.patients:
        print("Patient " + name.capitalize() + " does not exist.")
        create_patient(name)
        print("Patient is now in a waiting queue")
        p.put(str(name))
        print("There are " + str(p.qsize() - 1) + " persons before him/her.")
    else:
        print("Patient is now in a waiting queue")
        p.put(str(name))
        print("There are " + str(p.qsize() - 1) + " persons before him/her.")


def patient_dequeue():
    if p.empty():
        print("There are no patients left in queue.")

    else:
        person = p.get()
        print("Patient "+ str(person).capitalize() + " has been attended")


def create_illness(name):
    if name.lower() in care_parse.illness:
        print("Illness is all ready created")
    else:
        print("Added illness: " + name.capitalize())
        care_parse.illness[name.lower()] = []
        custom_definitions.append(name)


def remove_patients(name):
    if name.lower() in care_parse.patients:
        print("Removing patient : " + name.capitalize())
        care_parse.patients.pop(name.lower())
    else:
        print("Patient " + name.capitalize() + " does not exist in system.")


def remove_illness(name):
    if name.lower() in care_parse.illness:
        print("removing illness : " + name.capitalize())
        care_parse.illness.pop(name)


def add_conditions(name, symptom):
    if not name.lower() in care_parse.illness:
        print("Adding illness with symptom")
        create_illness(name)
        care_parse.illness[name.lower()].append(symptom.lower())
        print("Condition " + symptom.lower() + "added to" + name.capitalize())

    else:
        (care_parse.illness[name.lower()]).append(symptom.lower())
        print("Adding symptom -> " + symptom + " to Illness definition " + name.capitalize())

def find_matches(name , illness):
    if not name.lower() in care_parse.patients:
        print("Patient " + name.capitalize() + " does not exist.")
    else:
        match = 0                                               # not optimal method
                                                                # see to find a map funtion for better time

        for p in care_parse.patients[name.lower()]:
            for d in (care_parse.illness[illness.lower()]):
                if (p == d):
                    match = match + 1
        match = (match/len(care_parse.illness[illness.lower()])*100)
        print("Patient has " + str(match) + "% of the symptoms of a " + illness)
        if (match >= 60):
            print("Patient could have a " + illness)
        else:
            print("Current data shows that the patient :")
            print(name.capitalize() + "does not have enough symptoms to diagnose as having " + illness.capitalize())


def add_symptom(name, symptom):
    if not name.lower() in care_parse.patients:
        print("Patient not in register. Creating patient and adding symptom... \n")
        create_patient(name.lower())
        care_parse.patients[name.lower()].append(symptom.lower())
        print("Symptom: " + symptom + " added. \n")
    else:
        print("Adding symptom -> " + symptom + " to patient " + name.capitalize())
        (care_parse.patients[name.lower()]).append(symptom)


def list_symptoms(name):
    if not name.lower() in care_parse.patients:
        print("Patient " + name.capitalize() + "does not exist.")
    else:
        print("Patient " + name.capitalize() + " has: \n")
        for p in care_parse.patients[name.lower()]:
            print(p + "\n")

def list_illness_conditions(name):
    if not name.lower() in care_parse.illness:
        print("Illness " + name.capitalize() + "does not exist.")
    else:
        print("Illness " + name.capitalize() + " has: \n")
        for p in care_parse.patients[name.lower()]:
            print(p + "\n")


def diagnose_patient(name):

    print("\nYou are diagnosing a patient")
    if not name.lower() in care_parse.patients:
        print("Patient " + name.capitalize() + " does not exist.")
    else:
        match_flu = 0
        match_cold = 0
        match_dengue = 0
        match_norovirus = 0
        match_stroke = 0
        match_diabetes = 0

        for p in care_parse.patients[name.lower()]:
            for index in range(len(cold)):
                if p == cold[index]:
                    match_cold = match_cold+1

            for index in range(len(flu)):
                if p == flu[index]:
                    match_flu = match_flu+1

            for index in range(len(dengue)):
                if p == dengue[index]:
                    match_dengue = match_dengue+1

            for index in range(len(norovirus)):
                if p == norovirus[index]:
                    match_norovirus = match_norovirus+1

            for index in range(len(stroke)):
                if p == stroke[index]:
                    match_stroke = match_stroke+1

            for index in range(len(diabetes)):
                if p == diabetes[index]:
                    match_diabetes = match_diabetes+1

        match_flu = (match_flu/len(flu))*100
        match_cold = (match_cold/len(cold))*100
        match_dengue = (match_dengue/len(dengue))*100
        match_norovirus = (match_norovirus/len(norovirus))*100
        match_stroke = (match_stroke/len(stroke))*100
        match_diabetes = (match_diabetes/len(diabetes))*100

        if match_cold >= 60:
            print("Patient has " + str(match_cold) + "% of the symptoms of a cold.")
            print( "Patient could have a cold")

        elif match_flu >= 60:
            print("Patient has " + str(match_flu) + "% of the symptoms of a flu.")
            print("Patient could have the flu")

        elif match_dengue >= 60:
            print("Patient has " + str(match_norovirus) + "% of the symptoms of norovirus.")
            print("Patient could have norovirus")

        elif match_norovirus >= 60:
            print("Patient has " + str(match_norovirus) + "% of the symptoms of norovirus.")
            print("Patient could have norovirus")

        elif match_stroke >= 60:
            print("Patient has " + str(match_stroke) + "% of the symptoms of a stroke.")
            print("Patient could have suffered a stroke")
            print("Urgent intervention needed")

        elif match_diabetes >= 60:
            print("Patient has " + str(match_diabetes) + "% of the symptoms of diabetes.")
            print("Patient could have diabetes")

        else:
            print("Patient " + name.capitalize() + "has" + str(match_flu) + "% of the symptoms of a flu")
            print("and " + str(match_cold) + "% symptoms of a cold")
            print("Could not diagnose patient's condition with current data")

        temp = care_parse.patients[name.lower()]


def display_help():
    print('''Care is a prototype Health Care protocol language

    To create a patient simply write the patient's name followed by .create()
    ex Angel.create()

    To remove a patient simply write the patient's name followed by .remove
    ex Angel.remove()
    
    To add a symptom: use the patient's name then use .has() with symptom
    ex: Angel.has(fever)
    
    To list a patient's symptom's use .list() 
    ex: Angel.list()

    To auto diagnose patient simply write the patient's name followed by .diagnose()
    ex: Angel.diagnose()
    
    To define your own illnesses simply write ailment(ILLNESS).create() 
    ex: ailment(flu).create() 
    
    To add symtpoms to your defined illness write ailment(ILLNESS).add(SYMPTOM) 
    ex: ailment(flu).add(fever) 
    
    To add patient to queue write the keyword QUEUE followed by the patient's name
    ex: queue(Angel)
    
    To review a patient and remove from queue use the attend keyword
    ex: attend()
  
    ''')


def display_symptoms():
    print('''Supported symptoms are the following:
    
    sneezing
    sore_throat
    congestion
    coughing
    low_fever
    fever
    high_fever
    aches
    chills
    fatigue
    coughing
    headache
    severe_headache
    nausea
    skin_rash
    joint_pain
    malaise
    vomiting
    diarrhea
    muscle_pain
    dizziness
    numb_extremities
    confusion
    frequent_urination
    weight_loss
    constant_tiredness

    ''')


def exit_program():
    print("")
    print("Exiting CARE. Thank you.")
    print("")
    sys.exit(0)
