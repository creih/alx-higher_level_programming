#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str.split(',')[2][1:27] + str.split(' ')[-4]+ str.split(',')[-1][12:-8]
print(str)
