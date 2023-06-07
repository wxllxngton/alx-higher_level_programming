#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
        language that combines remarkable power with very clear syntax"
word_first_3 = str.split()[0][:3]
word_last_2 = str.split()[-1][-2:]
middle_word = " ".join(str.split()[1:-1])
print(f"{word_first_3}{middle_word}{word_last_2}")
