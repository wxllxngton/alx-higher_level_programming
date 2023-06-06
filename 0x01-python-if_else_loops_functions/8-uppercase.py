#!/usr/bin/python3
def uppercase(s):
    output = ""
    for c in s:
        if "a" <= c <= "z":
            uppercase_char = chr(ord(c) - 32)
            output += "{:s}".format(uppercase_char)
        else:
            output += "{:s}".format(c)
    output += "\n"
    print(output, end="")
