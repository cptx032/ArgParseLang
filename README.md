# ArgParseLang

Imagine that you are creating a terminal/command line software and you want receive arguments, like: `my_program --name=Angelina --surname=Jolie`. So, you need to create some code to parse these arguments, and you see that to do this in bash is something like:

```bash
NAME=unset
SURNAME=unset
PARSED_ARGUMENTS=$(getopt -a -n $0 -o "h" --long help,,name:,surname: -- "$@")

VALID_ARGUMENTS=$?
if [ "$VALID_ARGUMENTS" != "0" ]; then
    print_usage
fi

eval set -- "$PARSED_ARGUMENTS"
while :
do
    case "$1" in
        --name ) NAME="$2"; shift 2 ;;
        --surname ) SURNAME="$2"; shift 2 ;;
        -h | --help) print_usage ;;
        --) shift; break ;;
    esac
done
```

The same crazyness you will find in programming languages like C/C++, and so one. Python otherwise, have a more clean API, but can be very weird too:

```python
# from Python docs
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))
```

Just looking, you may ask: "Whats action=store_const means? And what is nargs=+?"

The ArgParse Language was created to help you to create this kind of boiler plate code to parse command line arguments.

Today, ArgParse supports two languages:

- Python 2/3
- Bash

With ArgParse you will just to create a file with the content like:

```
My Program

ATTR:  name     First name
ATTR:  surname  The surname
```

And the argparse will create the code in your language to parse these arguments.

## Installing / Dev environment
- `mkvirtualenv ArgParseLang -p python3` to make a isolated python environment
- `pip install -r requirements.txt` to install python dependencies
- `./get_antlr.sh` to download antlr jars
- `source ./antlr_alias.sh` to configure antlr aliases


## Language Specification
ArgParse is very simple, it have basically 4 types of command line arguments:

- Flags
- Named Attributes
- Arguments (not supported for bash yet)
- Positional Arguments

### Flags
Flags are command line arguments that dont need any extra information beyond itself. It is used basically to indicated some boolean variable. You can use flags in command line arguments by using a single dash followed by a name, as: `my_program -h -j`. In this case we have two flags. When we have many flags we can write `my_program -hj` too. Traditionally flags are indicated by one single letter, but you can create long named flags too, in this case you cannot group many flags together using a single dash, you will need to separate each flag, as: `my_program -help -cp` and **not** `my_program -helpcp`.

### Named Attributes
Differently from flags, named attributes need extra information. They are indicated by two dashes followed by a name, as: `my_program --name=John --surname=Travolta`.

### Arguments
Arguments is as we call here the undefined number of unamed arguments received by a command line program. Many programs receive many files to process, for example, so, is very common to see something like: `my_program FILE1 FILE2 FILE3`. The program doesn't know how many files can receive.

### Positional Arguments
Positional Arguments are very likely "Arguments" the difference is that the number of arguments is known, for example a program that receive a source to process and a file path to save the result, as: `my_program INPUT OUTPUT`.

### Syntax
ArgParse syntax is very simple, in the first lines you must describe your program. Include two blank lines. And them you will specify the command line arguments that you want. The general syntax of a argument is:

```
TYPE: ARGUMENTNAME DESCRIPTION
TYPE: ARGUMENTNAME2 DESCRIPTION2
```

Each argument must be separated from each other by one line. The possible types are: `FLAG` for flags, `ATTR` for named arguments, `POS` for positional arguments and `ARGS` for (undefined number of) arguments.


### Complete Example
One complete example is:

```
This program sums two numbers
Made in MIT NASA labs


POS:   A    the first term of sum
POS:   B    the second term of sum
FLAG:  bin  outputs the result in binary
FLAG:  hex  outputs the result in hexadecimal
```

Save this content in a file named `my_arguments.argparse`.
To create the python code to parse these arguments you must do:

```bash
python main.py my_arguments.argparse --lang=python > my_program.py
```

This command will create a file named `my_program.py` in your current folder. If you do:

```bash
python my_program.py --help
```

You will see:

```
usage: my_program.py [-h] [-bin] [-hex] A B

This program sums two numbers Made in MIT NASA labs

positional arguments:
  A           the first term of sum
  B           the second term of sum

optional arguments:
  -h, --help  show this help message and exit
  -bin        outputs the result in binary
  -hex        outputs the result in hexadecimal
```

## Use in production
To use in production is usefull to separate the ArgParse generated code from the code of your application. Below you will find the tips to achieve that in each output language.

### Python
Having a argparse file named `cl_arguments.argparse`, you can generate a separated python file named `cl_arguments.py` with `python main.py cl_arguments.argparse --lang=python > cl_arguments.py`. Do not edit this file, instead, create another file named `main.py` and do:

```python
from cl_arguments import args

if args.my_flag:
	launch_space_ship()

...
```

### Bash
Having a argparse file named `cl_arguments.argparse`, you can generate a separated bash file named `cl_arguments.sh` with `python main.py cl_arguments.argparse --lang=bash > cl_arguments.sh`. Do not edit this file, instead, create another file named `main.sh` and do:

```bash
# the dot here is an alias to "source", its an import
. cl_arguments.sh

# in the outputed bash file, is created a variable to each command line.
# The variables is upper case
echo $MY_FLAG
```

## Testing ArgParse

To run the unit tests just do:
```bash
python tests.py
```


## I want help/undestand this project
### undestanding the structure of this project
This project have basically three important files:

This project is made using [ANTLR4](https://www.antlr.org/), so the grammar file is located in the main folder, called [ArgParse.g4](ArgParse.g4). To the tree processing we use the visitor pattern in the file [TranspilerVisitor.py](TranspilerVisitor.py), also in the main folder. This file imports the file [outputs.py](outputs.py), that contains the output for each language.

### Writing another output languages
To write another language output just create a class in the [outputs.py](outputs.py) file and edit the [main.py](main.py) to load your class, repeating the pattern already implemented.

We need help to:

- create more output languages:
	- ~~Python~~
	- ~~Bash~~
	- C/C++
	- C#
	- Java
	- Lua
	- Ruby
	- Rust
	- Nim
	- Lua
	- Perl
	- JavaScript/NodeJS
	- Javascript variants (Coffescript, dart, typescript...)
	- Crystal
	- V
	- D
	- R
	- Ada
	- Haskell
	- Lisp
	- SmallTalk
	- AngelScript
	- Vala
	- put your language here...