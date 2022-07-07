from __future__ import print_function
import math

"""
 *** Renamed input to my_input ***
 
 *** I separated the files to avoid conflicts ***
 
 *** I Broke the DRY Rule a bit (I havent used python in months) ***
 """


#  First I remove raw_input because I am writing python 3 code
try:
    #  Input prompt
    my_input = input("Enter text: ")
except NameError:
    pass

#  formula
key = int(math.pi * 1e14)

text = my_input

values = reverse = []


# This function encrypts the character
def encryptChar(target):
    # encryption algorithm

    target = (((target + 42) * key) - 449)
    # Some print statements to identify the points of failure
    # TODO: write proper tests
    return target


# This function decrypts the characters
def decryptChar(target):
    target = (((target + 449) / key) - 42)
    return target


# this function should be
def encrypt(input_text):
    col_values = []

    for inp in input_text:
        current = ord(inp)  # fixed typo

        current = encryptChar(current)

        col_values.append(current)
    return col_values


def decrypt(enc_text):
    col_values = []

    for enc in enc_text:
        current = int(decryptChar(enc))
        current = chr(current)
        col_values.append(current)
    return col_values




# encryption

for t in text:
    current = ord(t)

    current = encryptChar(current)

    values.append(current)

# decryption

for v in values:
    current = int(decryptChar(v))

    current = chr(current)
    reverse = current

    print(reverse)

# saves encrypted in txt file

output = open("encrypted.txt", 'w')

for v in values:
    output.write(str(v) + " ")

