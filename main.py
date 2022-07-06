from __future__ import print_function
import math

""" 
 First I remove raw_input because I am writing python 3 code

 *** Renamed input to my_input ***
 """
try:
    #  Input prompt
    my_input = input("Enter text: ")
except NameError:
    pass

#  formula
key = int(math.pi * 1e14)

text = my_input

values = []


# This function encrypts the character
def encryptChar(target):
    # encryption algorithm

    target = (((target + 42) * key) - 449)
    # Some print statements to identify the points of failure
    # TODO: write proper tests
    return target


# This decrpts the characters
def decryptChar(target):
    target = (((target + 449) / key) - 42)
    return target


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


def readAndDecrypt(filename):
    file = open(filename,  "r+")
    data = file.read()
    datalistint = []
    actualdata = []
    datalist = data.split(" ")
    print(datalist)
    datalist.remove('')
    datalistint = [float(data) for data in datalist]

    for data in datalist:
        current1 = int(decryptChar(data))
        current1 = chr(current1)
        actualdata.append(current1)
    file.close()

    return actualdata


def readAndEncrypt(filename):
    file = open(filename, "r")
    data = file.read()
    print(data)
    datalist = list(data)
    encrypted_list = list()
    # encrypted_list_str = list()

    for data in datalist:
        current = ord(data)
        current = encryptChar(current)
        encrypted_list.append(current)
        print(encrypted_list)
    file.close()

    return encrypted_list


def readAndEncryptAndSave(inp_file, out_file):
    enc_list = readAndEncrypt(inp_file)

    output = open("new.txt", "w+")

    for enc in enc_list:
        output.write(str(enc) + " ")
        print(enc)
    output.close()


def readAndDecryptAndSave(inp_file, out_file):
    dec_list = readAndDecrypt(inp_file)

    output = open(out_file, "w")

    for dec in dec_list:
        output.write(str(dec))

    output.close()


# encryption

for t in text:
    current = ord(t)

    current = encryptChar(current)

    values.append(current)

# decryption

for v in values:
    current = int(decryptChar(v))

    current = chr(current)
    # current = int(current)
    reverse = current

    print(reverse)

# saves encrypted in txt file

output = open("encrypted.txt", 'w')

for v in values:
    output.write(str(v) + " ")

# read and decrypts

print(readAndDecrypt("encrypted.txt"))
# print(readAndEncrypt("encrypted.txt"))
# print(readAndEncryptAndSave("encrypted.txt", "new.txt"))
# print(readAndDecryptAndSave("encrypted.txt", 'saved.txt'))



# reading the file
my_file = open("encrypted.txt", "r")
data = my_file.read()

# replacing end of line('/n') with ' ' and
# splitting the text it further when '.' is seen.
data_into_list = data.replace('\n', ' ').split(".")

# printing the data
print(data_into_list)
my_file.close()
