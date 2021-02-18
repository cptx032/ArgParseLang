from ArgParseVisitor import ArgParseVisitor


class TranspilerVisitor(ArgParseVisitor):
    def __init__(self, *args, **kwargs):
        self.language = kwargs.pop("language")
        super(TranspilerVisitor, self).__init__(*args, **kwargs)

    def visitFlag(self, context):
        flag_name = context.DASHFLAG().getText().replace("FLAG:", "").strip()
        description = "".join([i.getText() for i in context.LINE()]).strip()
        return "parser.add_argument('-{flag_name}', action='store_const', const=1, dest='{flag_name}', help='{description}')".format(flag_name=flag_name, description=description)

    def visitNamedattribute(self, context):
        flag_name = context.DOUBLEDASH().getText().replace("ATTR:", "").strip()
        description = "".join([i.getText() for i in context.LINE()]).strip()
        return "parser.add_argument('--{flag_name}', dest='{flag_name}', help='{description}')".format(flag_name=flag_name, description=description)

    def visitProgram(self, context):
        program_desc = ""
        if context.INITIALDESK():
            program_desc = context.INITIALDESK().getText().strip()
        program = "\n".join([(self.visit(node) or "") for node in context.children])
        return """import argparse
parser = argparse.ArgumentParser(description='{}')
{}

args = parser.parse_args()""".format(
            program_desc, program
        )

    def visitPositionalarg(self, context):
        flag_name = context.POSITIONALARGNAME().getText().replace("POS:", "").strip()
        description = "".join([i.getText() for i in context.LINE()]).strip()
        return "parser.add_argument('{flag_name}', help='{description}')".format(flag_name=flag_name, description=description)

    def visitMultiargs(self, context):
        flag_name = context.ARGSATTR().getText().replace("ARGS:", "").strip()
        description = "".join([i.getText() for i in context.LINE()]).strip()
        return "parser.add_argument('{flag_name}', nargs='+', help='{description}')".format(flag_name=flag_name, description=description)
