'''
Created on Feb 4, 2016

@author: taifa
'''
def isprime(n):
    if n ==1:
        print("1 is special")
        return False
    for x in range(2, n):
        if n % x == 0:
            print("{} equals {} * {}".format(*n, x, n // x))
            return False
        else:
            print(n, "is a prime")
            return True
for n in range(1, 20):
    isprime(n)