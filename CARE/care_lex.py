import ply.lex as lex

reserved = {

    'Patient':'PATIENT',
    'True': 'TRUE',
    'False': 'FALSE'

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

data = "Armando.()"

lexer.input(data)

while 1:
     tok = lexer.token()
     if not tok: break
     print(tok)




