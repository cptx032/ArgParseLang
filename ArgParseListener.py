# Generated from ArgParse.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ArgParseParser import ArgParseParser
else:
    from ArgParseParser import ArgParseParser

# This class defines a complete listener for a parse tree produced by ArgParseParser.
class ArgParseListener(ParseTreeListener):

    # Enter a parse tree produced by ArgParseParser#program.
    def enterProgram(self, ctx:ArgParseParser.ProgramContext):
        pass

    # Exit a parse tree produced by ArgParseParser#program.
    def exitProgram(self, ctx:ArgParseParser.ProgramContext):
        pass


    # Enter a parse tree produced by ArgParseParser#namedattribute.
    def enterNamedattribute(self, ctx:ArgParseParser.NamedattributeContext):
        pass

    # Exit a parse tree produced by ArgParseParser#namedattribute.
    def exitNamedattribute(self, ctx:ArgParseParser.NamedattributeContext):
        pass


    # Enter a parse tree produced by ArgParseParser#flag.
    def enterFlag(self, ctx:ArgParseParser.FlagContext):
        pass

    # Exit a parse tree produced by ArgParseParser#flag.
    def exitFlag(self, ctx:ArgParseParser.FlagContext):
        pass


    # Enter a parse tree produced by ArgParseParser#positionalarg.
    def enterPositionalarg(self, ctx:ArgParseParser.PositionalargContext):
        pass

    # Exit a parse tree produced by ArgParseParser#positionalarg.
    def exitPositionalarg(self, ctx:ArgParseParser.PositionalargContext):
        pass



del ArgParseParser