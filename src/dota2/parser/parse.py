import ply.yacc as yacc

import lex

objs = []
cur_obj = {}
last_token = None

def reset_obj():
    global cur_obj, last_token
    cur_obj = {}
    last_token = None

# Parsing Rules

def p_config (p):
    """config :
    """
    p[0] = ast.Module(p[1])
