grammar ArgParse;

program            : INITIALDESK? (multiargs|positionalarg|namedattribute|flag)+;

namedattribute     : DOUBLEDASH LINE+;
flag               : DASHFLAG LINE+;
positionalarg      : POSITIONALARGNAME LINE+;
multiargs          : ARGSATTR LINE+;

POSITIONALARGNAME  : 'POS:' [ ]+ WORD;
ARGSATTR           : 'ARGS:' [ ]+ WORD;
WORD               : [A-Za-z0-9.?]+;
LINE               : ([ \r\t]* WORD [ \r\t]*)+ ([\n]|EOF);
INITIALDESK        : LINE+ [\n][\n];
DOUBLEDASH         : 'ATTR:' [ ]+ [a-z]+;
LOWERCASEWORD      : [a-z]+;
DASHFLAG           : 'FLAG:' [ ]+ LOWERCASEWORD;