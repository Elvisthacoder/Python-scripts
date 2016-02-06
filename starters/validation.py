'''
Created on Feb 5, 2016

@author: taifa
'''
endProgram = 0;
while endProgram != 1:

    #Prompt for a new transaction
    userInput = input("Would you like to start a new transaction?: ");
    userInput = userInput.lower();

    #Validate input
    while userInput not in {'yes', 'no'}:
        print ("Invalid input. Please try again.")
        userInput = input("Would you like to start a new transaction?: ")
        userInput = userInput.lower()

    if userInput == 'yes':
        endProgram = 0
    if userInput == 'no':
        endProgram = 1
        