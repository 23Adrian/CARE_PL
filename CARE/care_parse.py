import ply.yacc as yacc
from CARE import care_lex, function_runner


tokens = care_lex.tokens
patients = []


def p_func(p):
    '''
    func : HELP
        | EXIT
    '''

    if str(p[1]) == "HELP" or str(p[1]) == "EXIT":
        function_runner.func_parse(p[1])


def p_error(p):
    print("Syntax error." + str(p))


def do_parse(s):
    parser.parse(s)


parser = yacc.yacc()