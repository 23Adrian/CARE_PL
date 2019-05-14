import ply.yacc as yacc
from CARE import care_lex, function_runner

tokens = care_lex.tokens
patients = {}
illness = {}


def p_program(t):
    ''' program : function
                | create_patient
                | add_symptoms
                | list_symptoms
                | diagnose_patient 
                | specific_diagnose
                | add_conditions
                | create_illness
                | remove_illness
                | remove_patient
                | queue
                | attend
                
                '''


def p_create_illness(p):
    ''' create_illness : AILMENT LP ID RP PERIOD CREATE LP RP'''
    #ailment(flu).create()                         example of syntax
    if len(p) == 9 and str(p[6]) == "create":
        function_runner.create_illness(str(p[3]))


def p_remove_illness(p):
    ''' remove_illness : AILMENT LP ID RP PERIOD REMOVE LP RP'''
    # ailment(flu).remove()
    if len(p) == 9 and str(p[1]) == "ailment" and str(p[6]) == "remove":
        function_runner.remove_illness(str(p[3]))


def p_function(p):
    '''
    function : ID
    '''
    if str(p[1]) == "HELP" or str(p[1]) == "help" or str(p[1]) == "Help":
        function_runner.display_help()
    elif str(p[1]) == "SYMPTOMS" or str(p[1]) == "Symptoms" or str(p[1]) == "symptoms":
        function_runner.display_symptoms()
    elif str(p[1]) == "EXIT" or str(p[1]) == "exit" or str(p[1]) == "Exit":
        function_runner.exit_program()


def p_create_patient(p):
    '''create_patient : ID PERIOD CREATE LP RP'''
    # Patient_name.create() example of syntax
    if len(p) == 6:
        function_runner.create_patient(str(p[1]))


def p_add_conditions(p):
    '''add_conditions : AILMENT LP ID RP PERIOD ADD LP ID RP'''
    #ailment(flu).add(fever)                    example of syntax
    if len(p) == 10 and str(p[6]) == "add":
        function_runner.add_conditions(str(p[3]), str(p[8]))


def p_add_symptoms(p):
    ''' add_symptoms : ID PERIOD HAS LP ID RP '''
    #angel.has(fever)                           example of syntax
    if len(p) == 7 and str(p[3]) == "has":
        function_runner.add_symptom(str(p[1]), str(p[5]))


def p_list_symptoms(p):
    ''' list_symptoms : ID PERIOD LIST LP RP'''
    #angel.list()                               example of syntax
    if len(p) == 6 and str(p[3]) == "list":
        function_runner.list_symptoms(str(p[1]))


def p_remove_patient(p):
    ''' remove_patient : ID PERIOD REMOVE LP RP'''

    if str(p[3]) == "remove" and len(p) == 6:
        function_runner.remove_patients(str(p[1]))


def p_diagnose_patient(p):
    ''' diagnose_patient : ID PERIOD DIAGNOSE LP RP'''
    # angel.diagnose()                            example of syntax
    if len(p) == 6 and str(p[3]) == "diagnose":
        function_runner.diagnose_patient(str(p[1]))


def p_specific_diagnose(p):
    ''' specific_diagnose : ID PERIOD AILMENT LP ID RP PERIOD DIAGNOSE LP RP'''
    # ANGEL.AILMENT(FLU).diagnose()             example of syntax
    if len(p) == 11:
        function_runner.find_matches(str(p[1]),str(p[5]))


def p_queue(p):
    ''' queue : ID LP ID RP'''
    # queue(angel)
    if len(p) == 5 and str(p[1]) == "queue":
        function_runner.patient_queue(str(p[3]))


def p_attend(p):
    ''' attend : ID LP RP'''
    # attend()
    if len(p) == 4 and str(p[1]) == "attend":
        function_runner.patient_dequeue()


def p_error(t):
    print("Syntax error at '%s'" % t.value)


def do_parse(s):
    parser.parse(s)


parser = yacc.yacc()
