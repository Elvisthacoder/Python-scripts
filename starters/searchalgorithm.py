'''
Created on Feb 7, 2016

@author: taifa
'''
import HTML
now = open("algorithms.txt")
for line in now.readlines():
    print(line, end ='')
    for line in file:
    words = ["number",
             "function"]
    for line_num,line in enumerate(file):
        if any([word in line for word in words]):
        print line_num, line
    table_data = [
        ['number','function'],
        ['paragraph','open'],
    ]
htmlcode = HTML.table(table_data)
print htmlcode