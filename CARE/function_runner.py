import sys
from CARE import care_parse

cold = ["fever", "congestion", "coughing"]
flu = ["fever", "congestion", "coughing", "bodyache"]


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


def create_illness(name):
    if name.lower in care_parse.illness:
        print("Illness is all ready created")
    else:
        print("Added illness: " + name.capitalize())
        care_parse.illness[name.lower()] = []

def add_conditions(name, symptom):
    if not name.lower() in care_parse.illness:
        print("Adding illness with symptom")
        create_illness(name)
        care_parse.illness[name.lower()].append(symptom.lower())
        print("Condition " + symptom.lower() + "added to" + name.capitalize())

    else:
        (care_parse.illness[name.lower()]).append(symptom.lower())
        print("Adding symptom -> " + symptom + " to Illness definition " + name.capitalize())



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


def diagnose_patient(name):

    print("\nYou are diagnosing a patient")
    if not name.lower() in care_parse.patients:
        print("Patient " + name.capitalize() + "does not exist.")
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
            print("Patient has " + matchC + "% of the symptoms of a cold.")
            print( "Patient could have a cold")
        elif(matchF >= 60):
            print("Patient has " + matchF + "% of the symptoms of a cold.")
            print("Patient could have the flu")
        else:
            print("Could not diagnose patient's condition with current data")

        temp = care_parse.patients[name.lower()]


def display_help():
    print("Hello!"
          "\nCARE is an experimental Health Care Protocol Language."
          "\nTo create a patient: PATIENT_NAME.()"
          "\nTo add symptoms to a patient: PATIENT_NAME.has()"
          "\nTo view patient symptoms: PATIENT_NAME.list()"
          "\nImportant: Only enter 1 symptom at a time."
          "\nImportant: Symptoms must always be added in lowercase")


def exit_program():
    print("")
    print("Exiting CARE. Thank you.")
    print("")
    sys.exit(0)
