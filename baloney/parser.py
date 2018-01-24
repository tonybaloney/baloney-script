# ply requires a global import and then def overriding
from ply import *

from baloney.lexer import tokens

# Specify operator precidence
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'POWER'),
    ('right', 'UMINUS')
)

def p_rulename(p):
    ('pass', None)

# baloney_parser = yacc.yacc()

def parse(data, debug=0):
    baloney_parser.error = 0
    program = baloney_parser.parse(data, debug=debug)
    if baloney_parser.error:
        return None
    return program
