'''
Created on Feb 3, 2016

@author: taifa
'''
def valid_user_input(x):
    try:
        return int(x) > 2
    except ValueError:
        return False

maximum_number_input = input("Maximum Number: ")

while valid_user_input(maximum_number_input):
    maximum_number_input = input("Maximum Number: ")
    print("You have successfully entered a valid number")