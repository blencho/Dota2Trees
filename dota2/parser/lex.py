import ply.lex as lex

tokens = tuple(
    'STRING',

    # Delimiters
    'LBRACE', 'RBRACE',
)

# t_HERO_NAME = r'^npc_dota_hero_([A-Za-z0-9]+)'
t_STRING = r'\"(.*)\"'

t_LPAREN = r'\{'
t_RPAREN = r'\}'

t_ignore = r' \t\r'
t_ignore_COMMENT = r'//.*'

lexer = lex.lex()

def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1
    return t

def main(args):
    if len(args) > 1:
        lexer.input(open(args[1]).read())
    else:
        lexer.input(sys.stdin.read())
    for tok in lexer:
        print tok

if __name__ == '__main__':
    main(sys.argv)
