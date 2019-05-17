import ply.lex as lex

reserved = {

    'remove': 'REMOVE',
    'has': 'HAS',
    'list': 'LIST',
    'diagnose': 'DIAGNOSE',
    'create': 'CREATE',
    'ailment': 'AILMENT',
    'add': 'ADD',

}

tokens = [
    'ID',
    'LP',
    'RP',
    'PERIOD',
    'NEWLINE'


] + list(reserved.values())

t_ignore = ' \t'


def t_ID(t):
    r'[a-zA-Z$_][a-zA-Z0-9$_]*'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t


def t_error(t):
    print("Error")
    print(t)
    t.lexer.skip(1)

def t_NEWLINE(t):
    r'\n+'
    pass


t_REMOVE = r'remove'

t_ADD = r'add'

t_AILMENT = r'ailment'

t_HAS = r'has'

t_LIST = r'list'

t_DIAGNOSE = r'diagnose'

t_CREATE = r'create'

t_LP = r'\('

t_RP = r'\)'

t_PERIOD = r'\.'


lexer = lex.lex()
