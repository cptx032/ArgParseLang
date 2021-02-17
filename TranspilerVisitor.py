from ArgParseVisitor import ArgParseVisitor


class TranspilerVisitor(ArgParseVisitor):
    def visitFlag(self, context):
        flag_name = context.DASHFLAG()
        # description = " ".join([word.getText() for word in context.WORD()])
        # description = context.LINE().getText().strip()
        description = "".join([i.getText() for i in context.LINE()]).strip()
        print("NEW FLAG:", flag_name, "DESC", description)
        return super(TranspilerVisitor, self).visitFlag(context)

    def visitNamedattribute(self, context):
        flag_name = context.DOUBLEDASH()
        # description = " ".join([word.getText() for word in context.WORD()])
        # description = context.LINE().getText().strip()
        description = "".join([i.getText() for i in context.LINE()]).strip()
        print("NEW NAMED ATTR:", flag_name, "DESC", description)
        return super(TranspilerVisitor, self).visitNamedattribute(context)

    def visitProgram(self, context):
        program_desc = ""
        if context.INITIALDESK():
            program_desc = context.INITIALDESK().getText().strip()
        print("INITIAL DESK", program_desc)
        return super(TranspilerVisitor, self).visitProgram(context)

    def visitPositionalarg(self, context):
        flag_name = context.POSITIONALARGNAME()
        description = "".join([i.getText() for i in context.LINE()])
        print("FLAG POSITIONAL", flag_name, "DESC", description)
        return super(TranspilerVisitor, self).visitPositionalarg(context)
