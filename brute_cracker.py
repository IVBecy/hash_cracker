# Modules
import hashlib
import sys
import time
import itertools

# Defining variables
PASSWORDS = {}
charset = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-=+!.,'?/#~£$%^&*|")

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
| # Brute Force Attack                        |
|---------------------------------------------|
-----------------------------------------------

"""

########### Function for looping through the charset ######################
def bruting():
  brute_list = list(itertools.product(charset, repeat=int(REPEAT_COUNT)))
  for chars in brute_list:
    chars = str(chars)
    chars = chars.replace("'","")
    chars = chars.replace(",", "")
    chars = chars.replace("(", "")
    chars = chars.replace(")", "")
    chars = chars.replace(" ", "")
    ## Geting the hashing algorithm, and hashing based on the input
    #################### Sha1
    if HASH_METHOD == "sha1":
      passw = str(chars).encode('utf-8')
      hashed_passw = hashlib.sha1(passw).hexdigest()
      if CASE == "l":
        PASSWORDS[hashed_passw] = chars
      elif CASE == "u":
        PASSWORDS[hashed_passw.upper()] = chars
    #################### Sha256
    if HASH_METHOD == "sha256":
      passw = str(chars).encode('utf-8')
      hashed_passw = hashlib.sha256(passw).hexdigest()
      if CASE == "l":
        PASSWORDS[hashed_passw] = chars
      elif CASE == "u":
        PASSWORDS[hashed_passw.upper()] = chars
    #################### Sha512
    if HASH_METHOD == "sha512":
      passw = str(chars).encode('utf-8')
      hashed_passw = hashlib.sha512(passw).hexdigest()
      if CASE == "l":
        PASSWORDS[hashed_passw] = chars
      elif CASE == "u":
        PASSWORDS[hashed_passw.upper()] = chars
    #################### Sha3 256
    if HASH_METHOD == "sha3_256":
      passw = str(chars).encode('utf-8')
      hashed_passw = hashlib.sha3_256(passw).hexdigest()
      if CASE == "l":
        PASSWORDS[hashed_passw] = chars
      elif CASE == "u":
        PASSWORDS[hashed_passw.upper()] = chars
     #################### Sha3 512
    if HASH_METHOD == "sha3_512":
      passw = str(chars).encode('utf-8')
      hashed_passw = hashlib.sha3_512(passw).hexdigest()
      if CASE == "l":
        PASSWORDS[hashed_passw] = chars
      elif CASE == "u":
        PASSWORDS[hashed_passw.upper()] = chars
     #################### Blake 2S
    if HASH_METHOD == "blake2s":
      passw = str(chars).encode('utf-8')
      hashed_passw = hashlib.blake2s(passw).hexdigest()
      if CASE == "l":
        PASSWORDS[hashed_passw] = chars
      elif CASE == "u":
        PASSWORDS[hashed_passw.upper()] = chars
     #################### Blake 2B
    if HASH_METHOD == "blake2b":
      passw = str(chars).encode('utf-8')
      hashed_passw = hashlib.blake2b(passw).hexdigest()
      if CASE == "l":
        PASSWORDS[hashed_passw] = chars
      elif CASE == "u":
        PASSWORDS[hashed_passw.upper()] = chars
    #################### MD5
    if HASH_METHOD == "md5":
      passw = str(chars).encode('utf-8')
      hashed_passw = hashlib.md5(passw).hexdigest()
      if CASE == "l":
        PASSWORDS[hashed_passw] = chars
      elif CASE == "u":
        PASSWORDS[hashed_passw.upper()] = chars


# Self advertising ;)
print(banner)
time.sleep(3)
#### Taking commands ####
print("\n")
REPEAT_COUNT = input(
    "Enter the number of characters, that you would like to use:   ")
print("\n")
HASH_LIST = input("Enter the name of the hash file:  ")
print("\n")
HASH_METHOD = input(
    "Enter your hashing algorithm (md5, sha1, sha256, sha512, sha3_256, sha3_512, blake2s, blake2b):  ")
print("\n")
CASE = input("Lower / Upper case hashes [l/u]:")
print("\n")
bruting()
#### Handling the hashes file and looking for any match
a = 0
b = 1
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
        print(PASSWORDS[p], ":", p)
      except:
         pass
hashes.close()
