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

# Usage
def usage():
    print("""
    
     Usage: py cracker.py [-pl] [-hl]
    
    -pl: The password list
    -hl: The list of hashes

    Example: py cracker.py -pl password.txt -hl hashes.txt
    
    """)
    sys.exit()

# Taking the terminal commands, then assigning them to variables

if sys.argv[1] != "-pl":
    usage()

PASS_LIST = sys.argv[2]

if sys.argv[3] != "-hl":
    usage()

HASH_LIST = sys.argv[4]


######## Variables we need #######
PASSWORDS = {}
a = 0
b = 1

# Self advertising ;)
print(banner)
time.sleep(3)

#######  Handling the passwords file  #########
# And making a dictionary, with the passwords, to their assigned hash
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
        PASSWORDS[hashed_passw] = p
    a += 1
    b += 1
passes.close()

###########################################################################################

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
        # Try to find the hash in the txt file, in the dictionary
        try:
            print("Password found for hash: ", p)
            print("The password is:  ", PASSWORDS[p])
            print("\n")
        except:
            pass
    a += 1
    b += 1
hashes.close()

