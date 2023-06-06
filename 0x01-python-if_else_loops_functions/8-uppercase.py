#!/usr/bin/python3
def uppercase(s):
    for c in s:
        if "a" <= c <= "z":
            uppercase_char = chr(ord(c) - 32)
            print("{:s}".format(uppercase_char), end="")
        else:
            print("{:s}".format(c), end="")
