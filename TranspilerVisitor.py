from ArgParseVisitor import ArgParseVisitor
from outputs import PythonOutput, BashOutput


class TranspilerVisitor(ArgParseVisitor):
    def __init__(self, *args, **kwargs):
        self.language = kwargs.pop("language")
        self.program_desc = ""
        self.positionals = []
        self.multiargs = []
        self.namedattributes = []
        self.flags = []
        super(TranspilerVisitor, self).__init__(*args, **kwargs)

    def output(self):
        if self.language == "python":
            return PythonOutput(self).output()
        elif self.language == "bash":
            return BashOutput(self).output()
        print("Language '{}' not supported".format(self.language))

    def visitFlag(self, context):
        flag_name = context.DASHFLAG().getText().replace("FLAG:", "").strip()
        description = "".join([i.getText() for i in context.LINE()]).strip()
        self.flags.append([flag_name, description])

    def visitNamedattribute(self, context):
        flag_name = context.DOUBLEDASH().getText().replace("ATTR:", "").strip()
        description = "".join([i.getText() for i in context.LINE()]).strip()
        self.namedattributes.append([flag_name, description])

    def visitProgram(self, context):
        program_desc = ""
        if context.INITIALDESK():
            program_desc = context.INITIALDESK().getText().strip()
            self.program_desc = program_desc
        super(TranspilerVisitor, self).visitProgram(context)

    def visitPositionalarg(self, context):
        flag_name = context.POSITIONALARGNAME().getText().replace("POS:", "").strip()
        description = "".join([i.getText() for i in context.LINE()]).strip()
        self.positionals.append([flag_name, description])

    def visitMultiargs(self, context):
        flag_name = context.ARGSATTR().getText().replace("ARGS:", "").strip()
        description = "".join([i.getText() for i in context.LINE()]).strip()
        self.multiargs.append([flag_name, description])
