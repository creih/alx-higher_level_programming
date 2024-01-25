#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str.split(',')[2][1:28] + str.split(',')[-1][-23:-17] + str[0:6]
print(str)
