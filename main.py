#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function, unicode_literals

import argparse
import antlr4
import sys

from ArgParseLexer import ArgParseLexer
from ArgParseParser import ArgParseParser
from TranspilerVisitor import TranspilerVisitor, PythonOutput


# copied from the sources of antlr4, because we cant import them
class ErrorListener(object):

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        pass

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass


class ConsoleErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print("Syntax Error in line: {} column: {}".format(line, column))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Transpiler to ArgParse language'
    )
    parser.add_argument('FILE', help='The file you want to proccess')
    parser.add_argument(
        '--lang',
        dest='lang',
        help='output language. options: python,bash',
    )
    args = parser.parse_args()
    if not args.lang:
        print("You must specify the output language")
        sys.exit(1)
    with open(sys.argv[1]) as _f:
        input_stream = antlr4.InputStream(_f.read())
    lexer = ArgParseLexer(input_stream)
    tokens = antlr4.CommonTokenStream(lexer)
    parser = ArgParseParser(tokens)
    parser.addErrorListener(ConsoleErrorListener())
    parser.buildParseTrees = True
    tree = parser.program()
    transpiler = TranspilerVisitor(language=args.lang)
    transpiler.visit(tree)
    print(transpiler.output())
