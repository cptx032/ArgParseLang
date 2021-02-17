# Generated from ArgParse.g4 by ANTLR 4.9.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t")
        buf.write("(\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\5\2\f\n\2\3\2\3")
        buf.write("\2\3\2\7\2\21\n\2\f\2\16\2\24\13\2\3\3\3\3\6\3\30\n\3")
        buf.write("\r\3\16\3\31\3\4\3\4\6\4\36\n\4\r\4\16\4\37\3\5\3\5\6")
        buf.write("\5$\n\5\r\5\16\5%\3\5\2\2\6\2\4\6\b\2\2\2*\2\13\3\2\2")
        buf.write("\2\4\25\3\2\2\2\6\33\3\2\2\2\b!\3\2\2\2\n\f\7\6\2\2\13")
        buf.write("\n\3\2\2\2\13\f\3\2\2\2\f\22\3\2\2\2\r\21\5\b\5\2\16\21")
        buf.write("\5\4\3\2\17\21\5\6\4\2\20\r\3\2\2\2\20\16\3\2\2\2\20\17")
        buf.write("\3\2\2\2\21\24\3\2\2\2\22\20\3\2\2\2\22\23\3\2\2\2\23")
        buf.write("\3\3\2\2\2\24\22\3\2\2\2\25\27\7\7\2\2\26\30\7\5\2\2\27")
        buf.write("\26\3\2\2\2\30\31\3\2\2\2\31\27\3\2\2\2\31\32\3\2\2\2")
        buf.write("\32\5\3\2\2\2\33\35\7\t\2\2\34\36\7\5\2\2\35\34\3\2\2")
        buf.write("\2\36\37\3\2\2\2\37\35\3\2\2\2\37 \3\2\2\2 \7\3\2\2\2")
        buf.write("!#\7\3\2\2\"$\7\5\2\2#\"\3\2\2\2$%\3\2\2\2%#\3\2\2\2%")
        buf.write("&\3\2\2\2&\t\3\2\2\2\b\13\20\22\31\37%")
        return buf.getvalue()


class ArgParseParser ( Parser ):

    grammarFileName = "ArgParse.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "POSITIONALARGNAME", "WORD", "LINE", 
                      "INITIALDESK", "DOUBLEDASH", "LOWERCASEWORD", "DASHFLAG" ]

    RULE_program = 0
    RULE_namedattribute = 1
    RULE_flag = 2
    RULE_positionalarg = 3

    ruleNames =  [ "program", "namedattribute", "flag", "positionalarg" ]

    EOF = Token.EOF
    POSITIONALARGNAME=1
    WORD=2
    LINE=3
    INITIALDESK=4
    DOUBLEDASH=5
    LOWERCASEWORD=6
    DASHFLAG=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INITIALDESK(self):
            return self.getToken(ArgParseParser.INITIALDESK, 0)

        def positionalarg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArgParseParser.PositionalargContext)
            else:
                return self.getTypedRuleContext(ArgParseParser.PositionalargContext,i)


        def namedattribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArgParseParser.NamedattributeContext)
            else:
                return self.getTypedRuleContext(ArgParseParser.NamedattributeContext,i)


        def flag(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArgParseParser.FlagContext)
            else:
                return self.getTypedRuleContext(ArgParseParser.FlagContext,i)


        def getRuleIndex(self):
            return ArgParseParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ArgParseParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ArgParseParser.INITIALDESK:
                self.state = 8
                self.match(ArgParseParser.INITIALDESK)


            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ArgParseParser.POSITIONALARGNAME) | (1 << ArgParseParser.DOUBLEDASH) | (1 << ArgParseParser.DASHFLAG))) != 0):
                self.state = 14
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ArgParseParser.POSITIONALARGNAME]:
                    self.state = 11
                    self.positionalarg()
                    pass
                elif token in [ArgParseParser.DOUBLEDASH]:
                    self.state = 12
                    self.namedattribute()
                    pass
                elif token in [ArgParseParser.DASHFLAG]:
                    self.state = 13
                    self.flag()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 18
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NamedattributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOUBLEDASH(self):
            return self.getToken(ArgParseParser.DOUBLEDASH, 0)

        def LINE(self, i:int=None):
            if i is None:
                return self.getTokens(ArgParseParser.LINE)
            else:
                return self.getToken(ArgParseParser.LINE, i)

        def getRuleIndex(self):
            return ArgParseParser.RULE_namedattribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamedattribute" ):
                listener.enterNamedattribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamedattribute" ):
                listener.exitNamedattribute(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamedattribute" ):
                return visitor.visitNamedattribute(self)
            else:
                return visitor.visitChildren(self)




    def namedattribute(self):

        localctx = ArgParseParser.NamedattributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_namedattribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(ArgParseParser.DOUBLEDASH)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.match(ArgParseParser.LINE)
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ArgParseParser.LINE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FlagContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DASHFLAG(self):
            return self.getToken(ArgParseParser.DASHFLAG, 0)

        def LINE(self, i:int=None):
            if i is None:
                return self.getTokens(ArgParseParser.LINE)
            else:
                return self.getToken(ArgParseParser.LINE, i)

        def getRuleIndex(self):
            return ArgParseParser.RULE_flag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFlag" ):
                listener.enterFlag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFlag" ):
                listener.exitFlag(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFlag" ):
                return visitor.visitFlag(self)
            else:
                return visitor.visitChildren(self)




    def flag(self):

        localctx = ArgParseParser.FlagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_flag)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(ArgParseParser.DASHFLAG)
            self.state = 27 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                self.match(ArgParseParser.LINE)
                self.state = 29 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ArgParseParser.LINE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PositionalargContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POSITIONALARGNAME(self):
            return self.getToken(ArgParseParser.POSITIONALARGNAME, 0)

        def LINE(self, i:int=None):
            if i is None:
                return self.getTokens(ArgParseParser.LINE)
            else:
                return self.getToken(ArgParseParser.LINE, i)

        def getRuleIndex(self):
            return ArgParseParser.RULE_positionalarg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPositionalarg" ):
                listener.enterPositionalarg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPositionalarg" ):
                listener.exitPositionalarg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPositionalarg" ):
                return visitor.visitPositionalarg(self)
            else:
                return visitor.visitChildren(self)




    def positionalarg(self):

        localctx = ArgParseParser.PositionalargContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_positionalarg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(ArgParseParser.POSITIONALARGNAME)
            self.state = 33 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 32
                self.match(ArgParseParser.LINE)
                self.state = 35 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ArgParseParser.LINE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





