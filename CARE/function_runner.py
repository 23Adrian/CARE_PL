import sys
import queue

from CARE import care_parse

cold = ["sneezing", "sore throat", "congestion", "coughing"]
flu = ["fever", "aches", "chills", "fatigue", "coughing", "headache"]
definitions = []


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

def patient_Queue(name):
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


def patient_Dequeue():
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
        definitions.append(name)


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
        matchF = 0
        matchC = 0

        for p in care_parse.patients[name.lower()]:
            for index in range(len(cold)):
                if (p == cold[index]):
                    matchC = matchC+1

            for index in range(len(flu)):
                if (p == flu[index]):
                    matchF = matchF+1

        matchF = (matchF/len(flu))*100
        matchC = (matchC/len(cold))*100
        if(matchC >= 60):
            print("Patient has " + str(matchC) + "% of the symptoms of a cold.")
            print( "Patient could have a cold")
        elif(matchF >= 60):
            print("Patient has " + str(matchF) + "% of the symptoms of a flu.")
            print("Patient could have the flu")
        else:
            print("Patient " + name.capitalize() + "has" +str(matchF) + "% of the symptoms of a flu")
            print("and " + str(matchC) + "% symptoms of a cold")
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

def exit_program():
    print("")
    print("Exiting CARE. Thank you.")
    print("")
    sys.exit(0)
