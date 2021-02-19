import unittest
import os


class TestInvalidPrograms(unittest.TestCase):
    def test_incorrect_desc_spacing(self):
        source = """Program
ATTR: test desc"""
        with open("__temp.argparse", "w") as f:
            f.write(source)
        result = os.system("python main.py __temp.argparse --lang=python > /dev/null 2>&1")
        os.remove("__temp.argparse")
        self.assertNotEqual(result, 0)

    def test_transpiler_without_arguments(self):
        result = os.system("python main.py > /dev/null 2>&1")
        self.assertNotEqual(result, 0)

    def test_attrs_without_descriptions(self):
        source = """Program


ATTR: test"""
        with open("__temp.argparse", "w") as f:
            f.write(source)
        result = os.system("python main.py __temp.argparse --lang=python > /dev/null 2>&1")
        os.remove("__temp.argparse")
        self.assertNotEqual(result, 0)

    def test_wrong_type(self):
        source = """Program


JOHN: test description"""
        with open("__temp.argparse", "w") as f:
            f.write(source)
        result = os.system("python main.py __temp.argparse --lang=python > /dev/null 2>&1")
        os.remove("__temp.argparse")
        self.assertNotEqual(result, 0)

    def test_many_args(self):
        # it is not possible to create a program in argparse with many
        # ARGS types (it is possible with many POS)
        source = """Program


ARGS: test description
ARGS: test2 description"""
        with open("__temp.argparse", "w") as f:
            f.write(source)
        result = os.system("python main.py __temp.argparse --lang=python > /dev/null 2>&1")
        os.remove("__temp.argparse")
        self.assertNotEqual(result, 0)

    def test_valid_program(self):
        source = """Program


ARGS: test description"""
        with open("__temp.argparse", "w") as f:
            f.write(source)
        result = os.system("python main.py __temp.argparse --lang=python > /dev/null 2>&1")
        os.remove("__temp.argparse")
        self.assertEqual(result, 0)


class TestPython(unittest.TestCase):
    def test_valid_help_output(self):
        source = """Program


FLAG: binary just a flag"""
        with open("__temp.argparse", "w") as f:
            f.write(source)
        os.system("python main.py __temp.argparse --lang=python > __temp.py")
        os.system("python __temp.py --help > __output.txt")
        with open("__output.txt") as f:
            content = f.read()
            self.assertIn("usage:", content)
            self.assertIn("-binary", content)
            self.assertIn("just a flag", content)
        os.remove("__temp.argparse")
        os.remove("__temp.py")
        os.remove("__output.txt")

    def test_usage(self):
        source = """Program


FLAG: binary just a flag"""
        with open("__temp.argparse", "w") as f:
            f.write(source)
        os.system("python main.py __temp.argparse --lang=python > __temp.py")
        source = """
from __temp import args
if args.binary:
    print("BINARY!")
else:
    print("NOT BINARY!")
"""
        with open("__usage.py", "w") as f:
            f.write(source)
        os.system("python __usage.py > __output.txt")
        with open("__output.txt") as f:
            content = f.read().strip()
            self.assertEqual(content, "NOT BINARY!")
        os.system("python __usage.py -binary > __output.txt")
        with open("__output.txt") as f:
            content = f.read().strip()
            self.assertEqual(content, "BINARY!")
        os.remove("__temp.argparse")
        os.remove("__temp.py")
        os.remove("__output.txt")
        os.remove("__usage.py")


class TestBash(unittest.TestCase):
    def test_valid_help_output(self):
        source = """Program


FLAG: binary just a flag"""
        with open("__temp.argparse", "w") as f:
            f.write(source)
        os.system("python main.py __temp.argparse --lang=bash > __temp.sh")
        os.system("bash __temp.sh --help > __output.txt")
        with open("__output.txt") as f:
            content = f.read()
            self.assertIn("usage:", content)
            self.assertIn("-binary", content)
            self.assertIn("just a flag", content)
        os.remove("__temp.argparse")
        os.remove("__temp.sh")
        os.remove("__output.txt")

    def test_usage(self):
        source = """Program


FLAG: binary just a flag"""
        with open("__temp.argparse", "w") as f:
            f.write(source)
        os.system("python main.py __temp.argparse --lang=bash > __temp.sh")
        source = """
. __temp.sh
if [ $BINARY = 1 ]
then
    echo BINARY!
else
    echo NOT BINARY!
fi
"""
        with open("__usage.sh", "w") as f:
            f.write(source)
        os.system("bash __usage.sh > __output.txt")
        with open("__output.txt") as f:
            content = f.read().strip()
            self.assertEqual(content, "NOT BINARY!")
        os.system("bash __usage.sh -binary > __output.txt")
        with open("__output.txt") as f:
            content = f.read().strip()
            self.assertEqual(content, "BINARY!")
        os.remove("__temp.argparse")
        os.remove("__temp.sh")
        os.remove("__output.txt")
        os.remove("__usage.sh")


if __name__ == "__main__":
    unittest.main()