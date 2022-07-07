from __future__ import print_function
import math

#  formula
key = int(math.pi * 1e14)
values = reverse = []


# This function decrypts the characters
def decryptChar(target):
    target = (((target + 449) / key) - 42)
    return target


# this function reads from the source file
def readAndDecrypt(filename):
    file = open(filename, "r+")
    data = file.read()
    print(list(data))
    datalistint = [data]
    actualdata = []
    datalist = data.split()
    # print(datalist)
    # datalist.remove(' ')
    datalistint = [float(data) for data in datalist]

    for data in datalist:
        current1 = int(decryptChar(int(data)))  # turn data to int
        current1 = chr(current1)  # returns string of each character
        actualdata.append(current1)  # Append
        # print(data)
    file.close()

    return actualdata  # returns desired outcome


"""
this function reads data from the encrypted file, decrypts 
it and saves to new.txt
"""


def readAndDecryptAndSave(inp_file, out_file):
    dec_list = readAndDecrypt(inp_file)

    output = open(out_file, "w")

    for dec in dec_list:
        output.write(str(dec))

    output.close()


"""
    My Output isn't giving me the correct values
"""

# read and decrypts
print(readAndDecrypt("encrypted.txt"))
print(readAndDecryptAndSave("encrypted.txt", "new.txt"))
