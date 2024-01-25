#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str.split(',')[2][1:28] + str[-13:8] + str.split(',')[-1][-12:-8]
print(str)
