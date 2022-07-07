from main import *


# read
def readAndEncrypt(filename):
    file = open('new.txt', "r") # read from decrypted file
    data = file.read()
    datalist = list(data) # to list
    encrypted_list = list() # desired output
    encrypted_list_str = list()

    for data in datalist:
        current = ord(data)
        current = encryptChar(current)
        encrypted_list.append(current)
    file.close()

    return encrypted_list


# saves encrypted output
def readAndEncryptAndSave(inp_file, out_file):
    enc_list = readAndEncrypt(inp_file)

    file1 = open(out_file, "w")  # Renamed from output to file1

    for enc in enc_list:
        file1.write(str(enc))
    file1.close()


print(readAndEncrypt("encrypted.txt"))
print(readAndEncryptAndSave("encrypted.txt", "saved.txt"))
