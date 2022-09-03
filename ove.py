#!/usr/bin/python3
import random
import numpy as np

def encrypt():
    enterstring = input("Enter message to encrypt: ")

    stringarray = list(enterstring)
    ivar = len(stringarray)
    randhash = random.getrandbits(128)
    multinum = random.randint(32,36)
    print("\n")

    if len(str(randhash)) == 38:
       print("Encrypted message: " + "00" + str(randhash), end='')
    else:
       print("Encrypted message: " + "0" + str(randhash), end='')
    for i in range(0,ivar):

        print(ord(stringarray[int(i)]) * (multinum), end='')

def decrypt():
    enterstring = input("Enter message to decrypt: ")

    n = 4
    splitenstring = [enterstring[i:i+n] for i in range(0, len(enterstring), n)]

    del splitenstring[0:10]
    leng = int(len(splitenstring))

    print("\n")
    print("Decrypted message: ", end='')

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
