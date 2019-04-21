import ply.lex as lex

reserved = {

    "removePatient": "removePatient",
    "addPatient": "addPatient",
    "HELP": "HELP",
    "EXIT": "EXIT",
    "NAME": "NAME",
    "HAS": "HAS",
    "DIAGNOSE": "DIAGNOSE"

}

tokens = [
    'ID',
    'LP',
    'RP',
    'SEMICOLON',
    'PERIOD',
    'COMMA',
    'STRING'
] + list(reserved.values())

t_ignore = r' '

def t_ID(t):
    r'[a-zA-z][a-zA-Z0-9]*'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t


def t_STRING(t):
    r'\"[a-zA-Z0-9_?!@#$%&*-+().~, \t\n]*\"'
    return t

def t_error(t):
    print("Error")
    print(t)
    t.lexer.skip(1)

t_LP = r'\('

t_RP = r'\)'

t_PERIOD = r'\.'

t_SEMICOLON = r';'

t_COMMA = r'\,'

lexer = lex.lex()

