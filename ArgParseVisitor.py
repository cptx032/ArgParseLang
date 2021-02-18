# Generated from ArgParse.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ArgParseParser import ArgParseParser
else:
    from ArgParseParser import ArgParseParser

# This class defines a complete generic visitor for a parse tree produced by ArgParseParser.

class ArgParseVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ArgParseParser#program.
    def visitProgram(self, ctx:ArgParseParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArgParseParser#namedattribute.
    def visitNamedattribute(self, ctx:ArgParseParser.NamedattributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArgParseParser#flag.
    def visitFlag(self, ctx:ArgParseParser.FlagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArgParseParser#positionalarg.
    def visitPositionalarg(self, ctx:ArgParseParser.PositionalargContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArgParseParser#multiargs.
    def visitMultiargs(self, ctx:ArgParseParser.MultiargsContext):
        return self.visitChildren(ctx)



del ArgParseParser