# Generated from ArgParse.g4 by ANTLR 4.9.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\t")
        buf.write("T\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\6\3\33\n")
        buf.write("\3\r\3\16\3\34\3\4\7\4 \n\4\f\4\16\4#\13\4\3\4\3\4\7\4")
        buf.write("\'\n\4\f\4\16\4*\13\4\6\4,\n\4\r\4\16\4-\3\4\5\4\61\n")
        buf.write("\4\3\5\6\5\64\n\5\r\5\16\5\65\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\6\6C\n\6\r\6\16\6D\3\7\6\7H\n\7\r")
        buf.write("\7\16\7I\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\2\2\t\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\3\2\7\7\2\60\60\62;AAC\\c|")
        buf.write("\5\2\13\13\17\17\"\"\3\3\f\f\3\2\f\f\3\2c|\2Z\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\3\21\3\2\2\2\5\32\3\2\2\2\7")
        buf.write("+\3\2\2\2\t\63\3\2\2\2\13:\3\2\2\2\rG\3\2\2\2\17K\3\2")
        buf.write("\2\2\21\22\7R\2\2\22\23\7Q\2\2\23\24\7U\2\2\24\25\7<\2")
        buf.write("\2\25\26\7\"\2\2\26\27\3\2\2\2\27\30\5\5\3\2\30\4\3\2")
        buf.write("\2\2\31\33\t\2\2\2\32\31\3\2\2\2\33\34\3\2\2\2\34\32\3")
        buf.write("\2\2\2\34\35\3\2\2\2\35\6\3\2\2\2\36 \t\3\2\2\37\36\3")
        buf.write("\2\2\2 #\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2\"$\3\2\2\2#!\3")
        buf.write("\2\2\2$(\5\5\3\2%\'\t\3\2\2&%\3\2\2\2\'*\3\2\2\2(&\3\2")
        buf.write("\2\2()\3\2\2\2),\3\2\2\2*(\3\2\2\2+!\3\2\2\2,-\3\2\2\2")
        buf.write("-+\3\2\2\2-.\3\2\2\2.\60\3\2\2\2/\61\t\4\2\2\60/\3\2\2")
        buf.write("\2\61\b\3\2\2\2\62\64\5\7\4\2\63\62\3\2\2\2\64\65\3\2")
        buf.write("\2\2\65\63\3\2\2\2\65\66\3\2\2\2\66\67\3\2\2\2\678\t\5")
        buf.write("\2\289\t\5\2\29\n\3\2\2\2:;\7C\2\2;<\7V\2\2<=\7V\2\2=")
        buf.write(">\7T\2\2>?\7<\2\2?@\7\"\2\2@B\3\2\2\2AC\t\6\2\2BA\3\2")
        buf.write("\2\2CD\3\2\2\2DB\3\2\2\2DE\3\2\2\2E\f\3\2\2\2FH\t\6\2")
        buf.write("\2GF\3\2\2\2HI\3\2\2\2IG\3\2\2\2IJ\3\2\2\2J\16\3\2\2\2")
        buf.write("KL\7H\2\2LM\7N\2\2MN\7C\2\2NO\7I\2\2OP\7<\2\2PQ\7\"\2")
        buf.write("\2QR\3\2\2\2RS\5\r\7\2S\20\3\2\2\2\13\2\34!(-\60\65DI")
        buf.write("\2")
        return buf.getvalue()


class ArgParseLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    POSITIONALARGNAME = 1
    WORD = 2
    LINE = 3
    INITIALDESK = 4
    DOUBLEDASH = 5
    LOWERCASEWORD = 6
    DASHFLAG = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "POSITIONALARGNAME", "WORD", "LINE", "INITIALDESK", "DOUBLEDASH", 
            "LOWERCASEWORD", "DASHFLAG" ]

    ruleNames = [ "POSITIONALARGNAME", "WORD", "LINE", "INITIALDESK", "DOUBLEDASH", 
                  "LOWERCASEWORD", "DASHFLAG" ]

    grammarFileName = "ArgParse.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


