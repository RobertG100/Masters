import hashlib #Module to implement different secure hash algorithms
BLOCKSIZE = 65536 #Used to read in the file in 65kb chunks, to stop a big file
#slowing the system down.

#defining the different hash algorithms to use
Sha1 = hashlib.sha1()
Sha256 = hashlib.sha256()
Sha512 = hashlib.sha512()
Sha3 = hashlib.sha384()

file = input("Enter a Filename to Hash:") #The input function to read user input
with open(file, 'rb') as afile: #Opening the file the user enters, stored in file variable. 'rb' refers to read in binary mode
    buf = afile.read(BLOCKSIZE) #reads contents of file into buffer. Not using arguments would read in any file size e.g. 2GB
 
    #Calculates hash and updates buffer for each algorithm
    Sha1.update(buf) 
    Sha256.update(buf) 
    Sha512.update(buf) 
    Sha3.update(buf) 

print("\nHashes of File", file,":")
print("-----------------------")
print("Sha-1:", Sha1.hexdigest())
print("Sha-256:", Sha256.hexdigest())
print("Sha-512:", Sha512.hexdigest())
print("Sha-3:", Sha3.hexdigest())
