class BaseOutput:
    def __init__(self, visitor):
        self.visitor = visitor

    def output(self):
        raise NotImplementedError


class PythonOutput(BaseOutput):
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
    # fixme > gerar um warning indicando que nao suporta positional
    def get_usage(self):
        final_str = "\nprint_usage()\n"
        final_str += "{\n"
        final_str += "    echo usage: $0 [-h]"
        for flag_name, description in self.visitor.flags:
            final_str += " [-{}]".format(flag_name)
        for flag_name, description in self.visitor.namedattributes:
            final_str += " [--{} {}]".format(flag_name, flag_name.upper())
        final_str += "\necho"
        final_str += "\necho {}".format(self.visitor.program_desc)
        final_str += "\necho"
        final_str += "\n\n    exit 2\n"
        final_str += "}\n"
        return final_str

    def output(self):
        final_str = ""
        long_options = ""
        short_options = ""
        for flag_name, description in self.visitor.namedattributes:
            final_str += "{}=unset\n".format(flag_name.upper())
            if len(flag_name) == 1:
                short_options += "{}:".format(flag_name)
            else:
                long_options += ",{}:".format(flag_name)

        for flag_name, description in self.visitor.flags:
            final_str += "{}=unset\n".format(flag_name.upper())
            if len(flag_name) == 1:
                short_options += "{}".format(flag_name)
            else:
                long_options += ",{}".format(flag_name)

        for flag_name, description in self.visitor.multiargs:
            final_str += "{}=unset\n".format(flag_name.upper())

        final_str += "PARSED_ARGUMENTS=$(getopt -a -n $0 -o \"h{}\" --long help,{} -- \"$@\")".format(short_options, long_options)
        final_str += "\n" + self.get_usage()

        final_str += "\nVALID_ARGUMENTS=$?"
        final_str += "\nif [ \"$VALID_ARGUMENTS\" != \"0\" ]; then"
        final_str += "\n    print_usage"
        final_str += "\nfi"

        final_str += "\n\neval set -- \"$PARSED_ARGUMENTS\""
        final_str += "\nwhile :\ndo"
        final_str += "\n    case \"$1\" in"
        for flag_name, description in self.visitor.namedattributes:
            final_str += "\n        --{} ) {}=\"$2\"; shift 2 ;;".format(
                flag_name, flag_name.upper()
            )
        for flag_name, description in self.visitor.flags:
            prefix = "-"
            if len(flag_name) > 1:
                prefix = "--"
            final_str += "\n        {}{} ) {}=1; shift ;;".format(
                prefix, flag_name, flag_name.upper()
            )
        final_str += "\n        -h | --help) print_usage ;;"
        final_str += "\n        --) shift; break ;;"
        final_str += "\n        *) print_usage ;;"
        final_str += "\n    esac"
        final_str += "\ndone"

        for flag_name, description in self.visitor.multiargs:
            final_str += '\n{}=$@'.format(flag_name.upper())
        return final_str
