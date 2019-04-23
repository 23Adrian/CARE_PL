import ply.yacc as yacc
from CARE import care_lex, function_runner


tokens = care_lex.tokens
patients = {}
illness = {}

def p_program(t):
    ''' program : function
                | create_patient
                | remove_patient
                | add_symptoms
                | list_symptoms
                | diagnose_patient 
                | specific_diagnose
                | create_illness
                | add_conditions
                
                '''

def p_function(p):
    '''
    function : ID
    '''

    if p[1] == "HELP" or p[1] == "help" or p[1] == "Help":
        function_runner.display_help()
    elif p[1] == "EXIT" or p[1] == "exit" or p[1] == "Exit":
        function_runner.exit_program()

def p_create_patient(p):
    ''' create_patient : ID PERIOD CREATE '''
    # Angel.create                         example of syntax
    if len(p) == 4 and str(p[3]) == "create":
        function_runner.create_patient(str(p[1]))

def p_remove_patient(p):
    '''remove_patient : ID PERIOD REMOVE'''
    # Angel.remove
    if len(p) == 4 and str(p[3]) == "remove":
        function_runner.remove_patient(str(p[1]))

def p_create_illness(p):
    ''' create_illness : DEFINE PERIOD LP ID RP '''
    # define.(norovirus)                        example of syntax
    if len(p) == 6 and str(p[1]) == "define":
        function_runner.create_illness(str(p[4]))

def p_add_conditions(p):
    ''' add_conditions : ID LP ID RP PERIOD ID LP ID RP '''
    #illness(flu).add(fever)                    example of syntax
    if len(p) == 10 and str(p[6]) == "add":
        function_runner.add_conditions(str(p[3]), str(p[8]))

def p_add_symptoms(p):
    ''' add_symptoms : ID PERIOD HAS LP ID RP '''
    #angel.has(fever)                           example of syntax
    if len(p) == 7 and str(p[3]) == "has":
        function_runner.add_symptom(str(p[1]), str(p[5]))

def p_list_symptoms(p):
    ''' list_symptoms : ID PERIOD LIST '''
    #angel.list                               example of syntax
    if len(p) == 4 and str(p[3]) == "list":
        function_runner.list_symptoms(str(p[1]))


#def p_list_illness_conditions(p):
# 3   ''' list_illness_conditions : ID LP ID RP PERIOD ID LP RP'''
# 3  if len(p) == 9 and p[1] == "illness" and p[6] == "list":
#     function_runner.list_illness_conditions(str(p[3]))

def p_diagnose_patient(p):
    ''' diagnose_patient : ID PERIOD DIAGNOSE '''
    # angel.diagnose                            example of syntax
    if len(p) == 4 and str(p[3]) == "diagnose":
        function_runner.diagnose_patient(str(p[1]))

def p_specific_diagnose(p):
    ''' specific_diagnose : ID PERIOD ID LP ID RP PERIOD ID LP RP'''
    # ANGEL.ILLNESS(FLU).diagnose()             example of syntax
    if len(p) == 11:
        function_runner.find_matches(str(p[1]),str(p[5]))


def p_error(t):
    print("Syntax error at '%s'" % t.value)


def do_parse(s):
    parser.parse(s)


parser = yacc.yacc()
