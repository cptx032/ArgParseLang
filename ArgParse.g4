grammar ArgParse;

program            : INITIALDESK? (positionalarg|namedattribute|flag)*;

namedattribute     : DOUBLEDASH LINE+;
flag               : DASHFLAG LINE+;
positionalarg      : POSITIONALARGNAME LINE+;

POSITIONALARGNAME  : 'POS: ' WORD;
WORD               : [A-Za-z0-9.?]+;
LINE               : ([ \r\t]* WORD [ \r\t]*)+ ([\n]|EOF);
INITIALDESK        : LINE+ [\n][\n];
DOUBLEDASH         : 'ATTR: ' [a-z]+;
LOWERCASEWORD      : [a-z]+;
DASHFLAG           : 'FLAG: ' LOWERCASEWORD;