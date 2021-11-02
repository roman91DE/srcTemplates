"""
construct src files with prefilled boilerplate code
usage: 
> python3.10 ./srcTemplates [type] [name] [destination]

available template types:
    1. python
    2. pythonScript
    3. c
    4. cpp
    5. cppClass

"""

import os
from sys import argv


def makeFile(destination: str, name:str, template:str, extension:str):
    """generates a new file <name.extension> at <destination> from the specified <template>"""
    istream = open(f"templates/{template}", "r")
    ostream = open(f"{destination}/{name}{extension}", "w")

    for line in istream:
        ostream.write(line.replace("NAME", name))

    istream.close()
    ostream.close()


def main():
    
    if len(argv) < 3:
        print(f"Argument Error - Specify at least 2 arguments: type and name")
        return

    valid_types = ["python","pythonScript", "c", "cpp", "cppClass"]
    template_type = argv[1]
    
    if not template_type in valid_types:
        print(f"Argument Error - {template_type} is not a valid template type!")
        return

    name = argv[2]

    if len(argv) > 3:
        destination = argv[3]
    else:
        destination = os.getcwd()
    
    args = []

    match template_type:
        
        case "python":
            args.append(("python_program.txt", ".py"))

        case "pythonScript":
            args.append(("python_script.txt", ".py"))

        case "c":
            args.append(("c_program.txt", ".c"))

        case "cpp":
            args.append(("cpp_program.txt", ".cpp"))

        case "cppClass":
            args.append(("cpp_class_header.txt", ".h"))
            args.append(("cpp_class_implementation.txt", ".cpp"))

        case _:
            print(f"Error - Something went wrong trying to match {template_type} - Aborted operation!")

    for template, extension in args:
        makeFile(destination, name, template, extension)


if __name__ == "__main__":
    main()
