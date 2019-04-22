import sys
from CARE import care_parse

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
    if not name.lower() in care_parse.patients:
        print("Patient " + name.capitalize() + "does not exist.")
    else:
        temp = care_parse.patients[name.lower()]
        print("lol")

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
