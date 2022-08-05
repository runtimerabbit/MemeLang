import sys
import pathlib


def Interpreter():
    try:
        with open(sys.argv[1]) as f:
            extension = pathlib.Path(sys.argv[1]).suffix
            if extension == '.mlang':
                acumulator = 0
                line_number = 0
                for line in f:
                    line_number += 1
                    line = line.strip()
                    line_list = line.split()
                    if ';' not in line_list[-1]:
                        print("SyntaxError: ';' not found at end of line",
                              line_number)
                        if "what's 9 + 10? 21" in line:
                            pass
                        elif "NO MY ROBUX" in line:
                            pass
                        elif "stay in school, it makes you better at minecraft" in line:
                            pass
                        elif "GIMME THAT" in line:
                            pass
                        else:
                            print("Unrecongnized '" + line + "'", 'at line',
                                  line_number)
                    elif ';' in line_list[-1]:
                        if "what's 9 + 10? 21" in line:
                            acumulator += 1
                        elif "NO MY ROBUX" in line:
                            acumulator -= 1
                        elif "stay in school, it makes you better at minecraft" in line:
                            number_to_divide = line_list[-1]
                            number_to_divide = number_to_divide.replace(
                                ';', '')
                            try:
                                int_number_to_divide = int(number_to_divide)
                            except ValueError:
                                print(
                                    "SyntaxError: No number to divide acumulator by"
                                )
                            acumulator / int_number_to_divide
                        elif "GIMME THAT" in line:
                            print(acumulator)
                        else:
                            print("Unrecongnized '" + line + "'", 'at line',
                                  line_number)
            else:
                print("FileError: unrecongnized file extension:", extension)
    except FileNotFoundError:
        print("FileNotFoundError: no file or directory named:", sys.argv[1])


Interpreter()
