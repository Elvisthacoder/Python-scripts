'''
Created on Feb 3, 2016

@author: taifa
'''
a, b = 0, 1
if a < b:
    print('a({}) is less than b'.format(a, b))
else:
    print( 'a({}) is not less than b'.format(a, b))
    
print("True" if a < b else "False")    