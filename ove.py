#!/usr/bin/python3
import random
import numpy as np

def encrypt():
    enterstring = input("Enter message to encrypt: ")

    stringarray = list(enterstring)
    ivar = len(stringarray)
    randhash = random.getrandbits(128)

    #takes random number between 32-36 (I chould make bigger range, but brute force whould also be bigger)
    multinum = random.randint(32,36)
    print("\n")

    #random.getrandbits(128) is generating either 38 or 39 digit numbers, so its putting 0 or 00 at the beggining so it can be divided to 4-digit elements in array when decrypting
    if len(str(randhash)) == 38:
       print("Encrypted message: " + "00" + str(randhash), end='')
    else:
       print("Encrypted message: " + "0" + str(randhash), end='')
    for i in range(0,ivar):
        #multiplies every element from array with random number (multinum)
        print(ord(stringarray[int(i)]) * (multinum), end='')

def decrypt():
    enterstring = input("Enter message to decrypt: ")

    #splits the array into 4 digit long elements
    n = 4
    splitenstring = [enterstring[i:i+n] for i in range(0, len(enterstring), n)]

    #delets pointless numbers, they are 40-digit long in total, but array is devided into 4-digit long segments, so its deleting first 10 elements of the array
    del splitenstring[0:10]
    leng = int(len(splitenstring))

    print("\n")
    print("Decrypted message: ", end='')

    #brute force function, its dividing remaining output with random number from 32 to 36, twlelve times (enough tries to print decrypted human-readable message)
    def brute():
        multinum = random.randint(32,36)
        for i in range(0,leng):
            echo = (int(splitenstring[i])) / multinum
            print(chr(int(float(echo))),end='')

    for i in range(0,12):
        print("")
        brute()

print("Encrypt Message: 1")
print("Decrypt Message: 2\n")
option = input("Enter Option:\n")

if option == '1':
   encrypt()
elif option == '2':
   decrypt()
else:
   print("Invalid Option")
