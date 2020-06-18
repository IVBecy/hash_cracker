# Hash Cracker
**Usage:** 

```py crack.py ```

```Enter the name of the password list: ``` (Type the name of the file that contains your proper passwords), e.g.: passwords.txt

```Enter the name od the hash file: ``` (Type the name of the file that contains your hashed passwords), e.g.: hashes.txt

```Enter your hashing algorithm (md5, sha1, sha256, sha512, sha3_256, sha3_512, blake2s, blake2b): ``` (Here, simply type the algorithm, that you want to use) e.g.: sha256

```Lower / Upper case hashes [l/u]: ``` (If your hashes, have upper case letters, then type "u", if they are lower case, then type "l")

***Hashing algorithms available:*** md5, sha1, sha256, sha512, sha3_256, sha3_512, blake2s, blake2b

Overall, this code will hash all the passwords in your password file, then compare it to the hashes. If there is any match between the two files, it will show it at the end.


