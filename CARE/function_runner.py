import sys


def func_parse(func, expression=None):
    if func == "HELP":
        display_help()
    elif func == "EXIT":
        exit_program()
    else:
        print("Function is not valid")


def display_help():
    print("Hello help")


def exit_program():
    sys.exit(0)
