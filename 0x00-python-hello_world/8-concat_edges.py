#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
print(str[str.find("object"):str.find("language")] + str[str.find("with"):str.find("very")] + str[str.find("Python"):str.find("is")])