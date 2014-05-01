# -*- coding: cp1252 -*-
"""
Reverse a String - Enter a string and the program
will reverse it and print it out.
"""

string = raw_input("Whatchu wanna say to me? ")

# print input
print(string)

# reverse string
# [begin:end:step] => leaving begin and end blank and -1 step reverses string
print(string[::-1])
