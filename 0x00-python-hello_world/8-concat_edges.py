#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
        language that combines remarkable power with very clear syntax"
word_first_3 = str[39:67]
word_last_2 = str[:6]
middle_word = str[114:119]
print("{:s}{:s}{:s}".format(word_first_3, middle_word, word_last_2))
