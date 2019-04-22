import sys
from CARE import care_parse

def func_parse(func, expression=None):
    if func == "HELP":
        display_help()
    elif func == "EXIT":
        exit_program()
    else:
        print("Function is not valid")

def createPatient(name):
       if name in care_parse.patients:
            print("Patient already exists.")
       else:
            print("Added patient: " + name)
            care_parse.patients[name] = []

def create_patient_with_symptom(name, symptom):
      if name in care_parse.patients:
          print("Patient already exists. Adding symptom...")
          print("")
          care_parse.patients[name].append(symptom)
          print("Symptom: " + symptom + " added.")
          print("")
          print("Patient has: ")
          for p in (care_parse.patients[name]):
              print(p + "\n")
#def add_symptom(symptom):


def display_help():
    print("Hello help")


def exit_program():
    print("")
    print("Exiting CARE. Thank you.")
    print("")
    sys.exit(0)
