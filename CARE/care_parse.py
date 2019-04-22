import ply.yacc as yacc
from CARE import care_lex, function_runner


tokens = care_lex.tokens
patients = {}
patient_symptoms = {}

def p_program(t):
    ''' program : function
                | create_patient '''

def p_function(p):
    '''
    function : ID
    '''

    if p[1] == "HELP" or p[1] == "help" or p[1] == "Help":
        function_runner.display_help()
    elif p[1] == "EXIT" or p[1] == "exit" or p[1] == "Exit":
        function_runner.exit_program()

def p_create_patient(p):
    '''create_patient : ID PERIOD LP RP
                      | ID PERIOD ID LP ID RP '''
    if len(p) == 5:
        function_runner.createPatient(str(p[1]))
    if len(p) == 7 and p[3] == "has":
        function_runner.create_patient_with_symptom(str(p[1]), str(p[5]))


def p_error(t):
    print("Syntax error at '%s'" % t.value)


def do_parse(s):
    parser.parse(s)


parser = yacc.yacc()