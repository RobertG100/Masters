import sys
import win32com.client as win32

# Use win32.com word module 
openedDoc = win32.gencache.EnsureDispatch('Word.Application')

file= sys.argv[1] #file variable to read in word doc
dictionary = open ( 'wordlist.txt', 'r' ) #open our wordlist in read mode

wordlist = dictionary.readlines() #wordlist variable reads wordlist
dictionary.close()
wordlist = [item.rstrip('\n') for item in wordlist] #wordlist used as array to loop through
results = open('Result.txt', 'w') #results variuable to hold results

found = 'false'
for password in wordlist: # loop through each password in array
                if(found == 'false' ):
                        print(password)
                        try:
                        #Arguments passed(file, ConfirmConversions, ReadOnly, AddToRecentFiles, PasswordDocument) 
                                f = openedDoc.Documents.Open(file, False, False, None, password)
			
                                print("Password cracked! It is "+password) #prints password and writes it to result.txt
                                results.write(password)
                                results.close()

                                found = 'true' #changes pass to true if found
                        except:
                                print("Incorrect password") #if not found, prints incorrect password
                                pass
                else:
                        sys.exit(0) #closes program
