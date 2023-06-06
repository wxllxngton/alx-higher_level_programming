#!/usr/bin/python3
def uppercase(s):
    for c in s:
        if "a" <= c <= "z":
            uppercase_char = chr(ord(c) - 32)
            print(uppercase_char, end="")
        else:
            print(c, end="")
    print()
