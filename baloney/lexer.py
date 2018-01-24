from ply import *

keywords = (
    'LET', 'READ', 'DATA', 'PRINT', 'GOTO', 'IF', 'THEN', 'FOR', 'NEXT', 'TO', 'STEP',
    'END', 'STOP', 'DEF', 'GOSUB', 'DIM', 'REM', 'RETURN', 'RUN', 'LIST', 'NEW',
)

tokens = keywords + (
    'EQUALS', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'POWER',
    'LPAREN', 'RPAREN', 'LT', 'LE', 'GT', 'GE', 'NE',
    'COMMA', 'SEMI', 'INTEGER', 'FLOAT', 'STRING',
    'ID', 'NEWLINE'
)

t_ignore = ' \t'


def t_REM(t):
    r'REM .*'
    return t


def t_ID(t):
    r'[A-Z][A-Z0-9]*'
    if t.value in keywords:
        t.type = t.value
    return t

t_EQUALS = r'equals'
t_PLUS = r'plus'
t_MINUS = r'minus'
t_TIMES = r'times'
t_POWER = r'to the power of'
t_DIVIDE = r'divide'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LT = r'less than'
t_LE = r'less than-equal'
t_GT = r'greater than'
t_GE = r'greater than-equal'
t_NE = r'not equal'
t_COMMA = r'\,'
t_SEMI = r';'
t_INTEGER = r'\d+'
t_FLOAT = r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
t_STRING = r'\".*?\"'


def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1
    return t


def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()