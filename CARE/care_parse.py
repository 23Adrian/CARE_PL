import ply.yacc as yacc
from CARE import care_lex, function_runner


tokens = care_lex.tokens
patients = {}

def p_program(t):
    ''' program : function
                | create_patient
                | add_symptoms
                | list_symptoms
                | diagnose_patient '''

def p_function(p):
    '''
    function : ID
    '''

    if p[1] == "HELP" or p[1] == "help" or p[1] == "Help":
        function_runner.display_help()
    elif p[1] == "EXIT" or p[1] == "exit" or p[1] == "Exit":
        function_runner.exit_program()

def p_create_patient(p):
    '''create_patient : ID PERIOD LP RP'''
    if len(p) == 5:
        function_runner.create_patient(str(p[1]))

def p_add_symptoms(p):
    ''' add_symptoms : ID PERIOD ID LP ID RP '''
    if len(p) == 7 and p[3] == "has":
        function_runner.add_symptom(str(p[1]), str(p[5]))

def p_list_symptoms(p):
    ''' list_symptoms : ID PERIOD ID LP RP'''
    if len(p) == 6 and p[3] == "list":
        function_runner.list_symptoms(str(p[1]))

def p_diagnose_patient(p):
    ''' diagnose_patient : ID PERIOD ID LP RP'''
    if len(p) == 6 and p[3] == "diagnose":
        
        function_runner.diagnose_patient(str(p[1]))

def p_error(t):
    print("Syntax error at '%s'" % t.value)


def do_parse(s):
    parser.parse(s)


parser = yacc.yacc()
