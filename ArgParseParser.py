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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\n")
        buf.write("\60\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\5\2\16")
        buf.write("\n\2\3\2\3\2\3\2\3\2\6\2\24\n\2\r\2\16\2\25\3\3\3\3\6")
        buf.write("\3\32\n\3\r\3\16\3\33\3\4\3\4\6\4 \n\4\r\4\16\4!\3\5\3")
        buf.write("\5\6\5&\n\5\r\5\16\5\'\3\6\3\6\6\6,\n\6\r\6\16\6-\3\6")
        buf.write("\2\2\7\2\4\6\b\n\2\2\2\63\2\r\3\2\2\2\4\27\3\2\2\2\6\35")
        buf.write("\3\2\2\2\b#\3\2\2\2\n)\3\2\2\2\f\16\7\7\2\2\r\f\3\2\2")
        buf.write("\2\r\16\3\2\2\2\16\23\3\2\2\2\17\24\5\n\6\2\20\24\5\b")
        buf.write("\5\2\21\24\5\4\3\2\22\24\5\6\4\2\23\17\3\2\2\2\23\20\3")
        buf.write("\2\2\2\23\21\3\2\2\2\23\22\3\2\2\2\24\25\3\2\2\2\25\23")
        buf.write("\3\2\2\2\25\26\3\2\2\2\26\3\3\2\2\2\27\31\7\b\2\2\30\32")
        buf.write("\7\6\2\2\31\30\3\2\2\2\32\33\3\2\2\2\33\31\3\2\2\2\33")
        buf.write("\34\3\2\2\2\34\5\3\2\2\2\35\37\7\n\2\2\36 \7\6\2\2\37")
        buf.write("\36\3\2\2\2 !\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2\"\7\3\2\2")
        buf.write("\2#%\7\3\2\2$&\7\6\2\2%$\3\2\2\2&\'\3\2\2\2\'%\3\2\2\2")
        buf.write("\'(\3\2\2\2(\t\3\2\2\2)+\7\4\2\2*,\7\6\2\2+*\3\2\2\2,")
        buf.write("-\3\2\2\2-+\3\2\2\2-.\3\2\2\2.\13\3\2\2\2\t\r\23\25\33")
        buf.write("!\'-")
        return buf.getvalue()


class ArgParseParser ( Parser ):

    grammarFileName = "ArgParse.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "POSITIONALARGNAME", "ARGSATTR", "WORD", 
                      "LINE", "INITIALDESK", "DOUBLEDASH", "LOWERCASEWORD", 
                      "DASHFLAG" ]

    RULE_program = 0
    RULE_namedattribute = 1
    RULE_flag = 2
    RULE_positionalarg = 3
    RULE_multiargs = 4

    ruleNames =  [ "program", "namedattribute", "flag", "positionalarg", 
                   "multiargs" ]

    EOF = Token.EOF
    POSITIONALARGNAME=1
    ARGSATTR=2
    WORD=3
    LINE=4
    INITIALDESK=5
    DOUBLEDASH=6
    LOWERCASEWORD=7
    DASHFLAG=8

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

        def multiargs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArgParseParser.MultiargsContext)
            else:
                return self.getTypedRuleContext(ArgParseParser.MultiargsContext,i)


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
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ArgParseParser.INITIALDESK:
                self.state = 10
                self.match(ArgParseParser.INITIALDESK)


            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 17
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ArgParseParser.ARGSATTR]:
                    self.state = 13
                    self.multiargs()
                    pass
                elif token in [ArgParseParser.POSITIONALARGNAME]:
                    self.state = 14
                    self.positionalarg()
                    pass
                elif token in [ArgParseParser.DOUBLEDASH]:
                    self.state = 15
                    self.namedattribute()
                    pass
                elif token in [ArgParseParser.DASHFLAG]:
                    self.state = 16
                    self.flag()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ArgParseParser.POSITIONALARGNAME) | (1 << ArgParseParser.ARGSATTR) | (1 << ArgParseParser.DOUBLEDASH) | (1 << ArgParseParser.DASHFLAG))) != 0)):
                    break

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
            self.state = 21
            self.match(ArgParseParser.DOUBLEDASH)
            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.match(ArgParseParser.LINE)
                self.state = 25 
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
            self.state = 27
            self.match(ArgParseParser.DASHFLAG)
            self.state = 29 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 28
                self.match(ArgParseParser.LINE)
                self.state = 31 
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
            self.state = 33
            self.match(ArgParseParser.POSITIONALARGNAME)
            self.state = 35 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 34
                self.match(ArgParseParser.LINE)
                self.state = 37 
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


    class MultiargsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARGSATTR(self):
            return self.getToken(ArgParseParser.ARGSATTR, 0)

        def LINE(self, i:int=None):
            if i is None:
                return self.getTokens(ArgParseParser.LINE)
            else:
                return self.getToken(ArgParseParser.LINE, i)

        def getRuleIndex(self):
            return ArgParseParser.RULE_multiargs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiargs" ):
                listener.enterMultiargs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiargs" ):
                listener.exitMultiargs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiargs" ):
                return visitor.visitMultiargs(self)
            else:
                return visitor.visitChildren(self)




    def multiargs(self):

        localctx = ArgParseParser.MultiargsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_multiargs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(ArgParseParser.ARGSATTR)
            self.state = 41 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 40
                self.match(ArgParseParser.LINE)
                self.state = 43 
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





