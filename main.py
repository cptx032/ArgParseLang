#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function, unicode_literals

import antlr4
import sys

from ArgParseLexer import ArgParseLexer
from ArgParseParser import ArgParseParser
from TranspilerVisitor import TranspilerVisitor


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
    with open(sys.argv[1]) as _f:
        input_stream = antlr4.InputStream(_f.read())
    lexer = ArgParseLexer(input_stream)
    tokens = antlr4.CommonTokenStream(lexer)
    parser = ArgParseParser(tokens)
    parser.addErrorListener(ConsoleErrorListener())
    parser.buildParseTrees = True
    tree = parser.program()
    transpiler = TranspilerVisitor()
    transpiler.visit(tree)
    print(tree.toStringTree())
    # import ipdb; ipdb.set_trace(context=10)