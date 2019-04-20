import ply.lex as lex
import sys

reserved = {

    "removePatient": "removePatient",
    "addPatient": "addPatient",
    "HELP": "HELP",
    "EXIT": "EXIT",
    "NAME": "NAME"

}

tokens = list(reserved.values())

t_ignore = r' '

def t_NAME(t):
    r'[a-zA-z][a-zA-Z0-9]*'
    if t.value in reserved:
        t.type - reserved[t.value]
    else:
        t.type = 'NAME'
    return t

def t_error(t):
    print("Error")
    print(t)
    t.lexer.skip(1)


lexer = lex.lex()

