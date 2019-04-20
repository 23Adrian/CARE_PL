import ply.yacc as yacc
import CARE.CARE_Lex



tokens = CARE.CARE_Lex.tokens
patients = []

def p_create_patient(p):








def do_parse(s):
    parser.parse(s)

parser = yacc.yacc()