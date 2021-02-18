class BaseOutput:
    def __init__(self, visitor):
        self.visitor = visitor

    def output(self):
        raise NotImplementedError


class PythonOutput(BaseOutput):
    def __init__(self, visitor):
        self.visitor = visitor

    def output(self):
        final_str = "import argparse\n"
        final_str += "\nparser = argparse.ArgumentParser(description='{}')".format(self.visitor.program_desc)

        for flag_name, description in self.visitor.positionals:
            final_str += "\nparser.add_argument('{flag_name}', help='{description}')".format(flag_name=flag_name, description=description)
        for flag_name, description in self.visitor.flags:
            final_str += "\nparser.add_argument('-{flag_name}', action='store_const', const=1, dest='{flag_name}', help='{description}')".format(flag_name=flag_name, description=description)
        for flag_name, description in self.visitor.namedattributes:
            final_str += "\nparser.add_argument('--{flag_name}', dest='{flag_name}', help='{description}')".format(flag_name=flag_name, description=description)
        for flag_name, description in self.visitor.multiargs:
            final_str += "\nparser.add_argument('{flag_name}', nargs='+', help='{description}')".format(flag_name=flag_name, description=description)

        final_str += "\n\nargs = parser.parse_args()"
        return final_str


class BashOutput(BaseOutput):
    def output(self):
        return "wip"