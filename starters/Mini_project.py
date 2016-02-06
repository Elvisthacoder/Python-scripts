'''
Created on Feb 3, 2016

@author: taifa
'''
import enchant 
d = enchant.Dict("en_US")
def valid_user_input(x):
    try:
        return d.check(x)
    except ValueError:
        return d.suggest(x)
sentence_input = input("Enter sentence: ")

while valid_user_input(sentence_input):
    print("You have successfully entered a sentence/word")
    