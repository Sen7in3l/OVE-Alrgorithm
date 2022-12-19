#!/usr/bin/env python3
import random
import numpy as np
import sys

#Define desubtitution and subtitution functions
def desubstitution(x):
    alphabet = 'abcdefghijklmnopqrstuvwxyz123456789~!@#$%^&*()_+{}:"<>?-=[];,./'
    key = 'g+szp!ywf)vlkq<^8jr$o(,.-1id>#e:{9t6=~[2m}cb34u&7]?_*xa/%n"h@5;'
    result = ""
    for letter in x:
        if letter.lower() in alphabet:
            result += key[alphabet.find(letter.lower())]
        else:
            result += letter
    return result
    
def substitution(x):
    alphabet = 'abcdefghijklmnopqrstuvwxyz123456789~!@#$%^&*()_+{}:"<>?-=[];,./'
    key = 'g+szp!ywf)vlkq<^8jr$o(,.-1id>#e:{9t6=~[2m}cb34u&7]?_*xa/%n"h@5;'
    result = ""
    for letter in x:
        if letter.lower() in key:
            result += alphabet[key.find(letter.lower())]
        else:
            result += letter
    return result

def encrypt():
    enter = sys.argv[2]
    #Subtitute Input
    enterstring = substitution(enter)

    stringarray = list(enterstring)
    ivar = len(stringarray)
    randhash = random.getrandbits(128)
    multinum = random.randint(32,36)

    encrypted_message = ""
    if len(str(randhash)) == 38:
       encrypted_message += "00" + str(randhash)
    else:
       encrypted_message += "0" + str(randhash)
    for i in range(0,ivar):
        encrypted_message += str(ord(stringarray[int(i)]) * (multinum))
        
    #Subtitute Output
    print("Ecnrypted message: " + substitution(encrypted_message))

def decrypt():
    enter = sys.argv[2]

    #Input Desubstitution
    enterstring = desubstitution(enter)

    n = 4
    splitenstring = [enterstring[i:i+n] for i in range(0, len(enterstring), n)]
    del splitenstring[0:10]
    leng = int(len(splitenstring))
    
    def brute():
        output = ""
        multinum = random.randint(32,36)
        for i in range(0,leng):
            echo = (int(splitenstring[i])) / multinum
            output += chr(int(float(echo)))
        #Output Desubstitution
        print(desubstitution(output))

    for i in range(0,12):
        brute()


option = sys.argv[1]

if option == '1':
   encrypt()
elif option == '2':
   decrypt()
else:
   print("Invalid Option")
