import argparse
import baloney.parser as baloney_parser
from baloney.interpreter import BaloneyInterpreter

parser = argparse.ArgumentParser()
parser.add_argument('--lex', type=bool)
parser.add_argument("file", type=str,
                    help="Target .bs file")

def run_lexer(source):
    from baloney.lexer import lexer
    lexer.input(source)
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)

def main(args):
    with open(args.file, 'rb') as source:
        source_str = source.read()
    if args.lex:
        run_lexer(source_str)
    else:
        program = baloney_parser.parse(source_str)
        if not program:
            raise SystemExit
        interpreted_program = BaloneyInterpreter(prog)
        try:
            b.run()
            raise SystemExit
        except RuntimeError:
            pass

if __name__ == '__main__':
    args = parser.parse_args()
    main(args)
