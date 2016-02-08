'''
Created on Feb 8, 2016

@author: taifa
'''
#!/usr/bin/python3
def spellcheck(sentence):
    words = open("spell.words").readlines()
    words = list(map(lambda x: x.strip(), words))
    res = sentence.split()
    ret = []
    for item in res:
        if(item in words):
            continue
        else:
            ret.append(item)
    return ret
