import ply.lex as lex

reserved = {

    'remove': 'REMOVE',
    'has': 'HAS',
    'list': 'LIST',
    'diagnose': 'DIAGNOSE',
    'create': 'CREATE',
    'define': 'DEFINE',

}

tokens = [
    'ID',
    'LP',
    'RP',
    'PERIOD'

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

t_REMOVE = r'remove'

t_DEFINE = r'define'

t_HAS = r'has'

t_LIST = r'list'

t_DIAGNOSE = r'diagnose'

t_CREATE = r'create'

t_LP = r'\('

t_RP = r'\)'

t_PERIOD = r'\.'

lexer = lex.lex()



