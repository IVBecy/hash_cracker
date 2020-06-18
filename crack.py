# Modules
import hashlib
import sys
import time


#####  Getting the length of the file   #######
def file_length(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
                pass
        return i + 1
        
# "WATERMARK"       
banner = """ 

-----------------------------------------------
|---------------------------------------------|
|             PASSWORD CRACKER                |
|---------------------------------------------|
| # Author: IVBecy                            |
|                                             |
| # The ULTIMATE Password cracker             |
|                                             |
|---------------------------------------------|
-----------------------------------------------

"""


# Self advertising ;)
print(banner)
time.sleep(3)

#Taking inputs and assigning them
print("\n")
PASS_LIST = input("Enter the name of the password list:  ")
print("\n")
HASH_LIST = input("Enter the name of the hash file:  ")
print("\n")
HASH_METHOD = input(
    "Enter your hashing algorithm (md5, sha1, sha256, sha512, sha3_256, sha3_512, blake2s, blake2b):  ")
print("\n")
CASE = input("Lower / Upper case hashes [l/u]:")
print("\n")

######## Variables we need #######
PASSWORDS = {}
a = 0
b = 1

#######  Handling the passwords file  #########
# Reading the file, then hash them, to be able to convert later on

###############################  SHA 1  ###################################

if HASH_METHOD == "sha1":
    for get_pass_hash in range(file_length(PASS_LIST)):
        passes = open(str(PASS_LIST), "r")
        pass_list = passes.readlines()[a:b]
        for p in pass_list:
            p = str(p)
            p = p.replace("[", "")
            p = p.replace("]", "")
            p = p.replace("'", "")
            p = p.replace("\n", "")
            p = p.replace(",", "")
            passw = str(p).encode('utf-8')
            hashed_passw = hashlib.sha1(passw).hexdigest()
            if CASE == "l":
                PASSWORDS[hashed_passw] = p
            elif CASE == "u":
                PASSWORDS[hashed_passw.upper()] = p
        a += 1
        b += 1
    passes.close()

###############################  MD5  ###################################
if HASH_METHOD == "md5":
    for get_pass_hash in range(file_length(PASS_LIST)):
        passes = open(str(PASS_LIST), "r")
        pass_list = passes.readlines()[a:b]
        for p in pass_list:
            p = str(p)
            p = p.replace("[", "")
            p = p.replace("]", "")
            p = p.replace("'", "")
            p = p.replace("\n", "")
            p = p.replace(",", "")
            passw = str(p).encode('utf-8')
            hashed_passw = hashlib.md5(passw).hexdigest()
            if CASE == "l":
                PASSWORDS[hashed_passw] = p
            elif CASE == "u":
                PASSWORDS[hashed_passw.upper()] = p
        a += 1
        b += 1
    passes.close()

###############################  SHA 256  ###################################
if HASH_METHOD == "sha256":
    for get_pass_hash in range(file_length(PASS_LIST)):
        passes = open(str(PASS_LIST), "r")
        pass_list = passes.readlines()[a:b]
        for p in pass_list:
            p = str(p)
            p = p.replace("[", "")
            p = p.replace("]", "")
            p = p.replace("'", "")
            p = p.replace("\n", "")
            p = p.replace(",", "")
            passw = str(p).encode('utf-8')
            hashed_passw = hashlib.sha256(passw).hexdigest()
            if CASE == "l":
                PASSWORDS[hashed_passw] = p
            elif CASE == "u":
                PASSWORDS[hashed_passw.upper()] = p
        a += 1
        b += 1
    passes.close()

###############################  SHA 512  ###################################
if HASH_METHOD == "sha512":
    for get_pass_hash in range(file_length(PASS_LIST)):
        passes = open(str(PASS_LIST), "r")
        pass_list = passes.readlines()[a:b]
        for p in pass_list:
            p = str(p)
            p = p.replace("[", "")
            p = p.replace("]", "")
            p = p.replace("'", "")
            p = p.replace("\n", "")
            p = p.replace(",", "")
            passw = str(p).encode('utf-8')
            hashed_passw = hashlib.sha512(passw).hexdigest()
            if CASE == "l":
                PASSWORDS[hashed_passw] = p
            elif CASE == "u":
                PASSWORDS[hashed_passw.upper()] = p
        a += 1
        b += 1
    passes.close()

###############################  SHA3 256  ###################################
if HASH_METHOD == "sha3_256":
    for get_pass_hash in range(file_length(PASS_LIST)):
        passes = open(str(PASS_LIST), "r")
        pass_list = passes.readlines()[a:b]
        for p in pass_list:
            p = str(p)
            p = p.replace("[", "")
            p = p.replace("]", "")
            p = p.replace("'", "")
            p = p.replace("\n", "")
            p = p.replace(",", "")
            passw = str(p).encode('utf-8')
            hashed_passw = hashlib.sha3_256(passw).hexdigest()
            if CASE == "l":
                PASSWORDS[hashed_passw] = p
            elif CASE == "u":
                PASSWORDS[hashed_passw.upper()] = p
        a += 1
        b += 1
    passes.close()

###############################  SHA3 512  ###################################
if HASH_METHOD == "sha3_512":
    for get_pass_hash in range(file_length(PASS_LIST)):
        passes = open(str(PASS_LIST), "r")
        pass_list = passes.readlines()[a:b]
        for p in pass_list:
            p = str(p)
            p = p.replace("[", "")
            p = p.replace("]", "")
            p = p.replace("'", "")
            p = p.replace("\n", "")
            p = p.replace(",", "")
            passw = str(p).encode('utf-8')
            hashed_passw = hashlib.sha3_512(passw).hexdigest()
            if CASE == "l":
                PASSWORDS[hashed_passw] = p
            elif CASE == "u":
                PASSWORDS[hashed_passw.upper()] = p
        a += 1
        b += 1
    passes.close()

###############################  BLAKE2s (256-bit)  ###################################
if HASH_METHOD == "blake2s":
    for get_pass_hash in range(file_length(PASS_LIST)):
        passes = open(str(PASS_LIST), "r")
        pass_list = passes.readlines()[a:b]
        for p in pass_list:
            p = str(p)
            p = p.replace("[", "")
            p = p.replace("]", "")
            p = p.replace("'", "")
            p = p.replace("\n", "")
            p = p.replace(",", "")
            passw = str(p).encode('utf-8')
            hashed_passw = hashlib.blake2s(passw).hexdigest()
            if CASE == "l":
                PASSWORDS[hashed_passw] = p
            elif CASE == "u":
                PASSWORDS[hashed_passw.upper()] = p
        a += 1
        b += 1
    passes.close()

###############################  BLAKE2b (512-bit)  ###################################
if HASH_METHOD == "blake2b":
    for get_pass_hash in range(file_length(PASS_LIST)):
        passes = open(str(PASS_LIST), "r")
        pass_list = passes.readlines()[a:b]
        for p in pass_list:
            p = str(p)
            p = p.replace("[", "")
            p = p.replace("]", "")
            p = p.replace("'", "")
            p = p.replace("\n", "")
            p = p.replace(",", "")
            passw = str(p).encode('utf-8')
            hashed_passw = hashlib.blake2b(passw).hexdigest()
            if CASE == "l":
                PASSWORDS[hashed_passw] = p
            elif CASE == "u":
                PASSWORDS[hashed_passw.upper()] = p
        a += 1
        b += 1
    passes.close()

###########################################################################################

############################  Finding hashes, in the dictionary  ##########################

# Reseting values
a = 0
b = 1

#########  Handling the hashes file  ###########
hashes = open(str(HASH_LIST), "r")
for get_hashes in range(file_length(HASH_LIST)):
    hash_list = hashes.readlines()
    for p in hash_list:
        p = str(p)
        p = p.replace("[", "")
        p = p.replace("]", "")
        p = p.replace("'", "")
        p = p.replace("\n", "")
        p = p.replace(",", "")
        # Try to find the hash in the txt file, and  in the dictionary
        try:
            print("Password", PASSWORDS[p])
            print("Hash for the password:", p)
            print("\n")
        except:
            pass
    a += 1
    b += 1
hashes.close()

