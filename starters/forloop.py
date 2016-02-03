'''
Created on Feb 3, 2016

@author: taifa
'''
#read a line from a text file
#reasons why python is good

now = open("forloop.txt")
for line in now.readlines():
    print(line, end ='')
    