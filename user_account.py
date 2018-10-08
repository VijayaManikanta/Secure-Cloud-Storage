#!/usr/bin/python
import hashlib
from headers import *

def encrypt():
	os.urandom(24)
        '\x17\x96e\x94]\xa0\xb8\x1e\x8b\xee\xdd\xe9\x91^\x9c\xda\x94\t\xe8S\xa1Oe_'
        rankey=os.urandom(24).encode('hex')
        f=open("key","wb")
        f.write(rankey)
        f.close()
        var1=AESCipher(rankey)
        os.chdir("DATA")
        allfiles=os.listdir(".")
        for files in allfiles:
            enc(files,var1)

def decrypt():
	f=open('key',"rb")
	pt=f.read()
	f.close()
	var1=AESCipher(pt)
	os.chdir("/root/Desktop/Accenture/Cloud/DATA")
	allfiles=os.listdir(".")
	for files in allfiles:
    		dec(files,var1)


def hash_cal(x):
	hash_object = hashlib.sha256(x)
	hex_dig = hash_object.hexdigest()
    #	print(hex_dig)
	return hex_dig

print("welcome to cloud secure data storage")
os.chdir("Cloud")
valid=0
status=True
while True:
        auth=True
    	try:		
		
        	fptr = open("Account.txt","r")
        	print "\nenter username"
        	tmpusr=raw_input()
        	print "\nenter password"
        	tmppwd=raw_input()
		tmppwd=hash_cal(tmppwd)
		for line in fptr:
                        if line.rstrip("\n") == tmpusr:
			    valid=valid+1
                            continue
			
                        elif line.rstrip("\n") == tmppwd:
				if (valid==1):
                                	break;
                        else:
                            auth= False
                            print "wrong user name or password"
			    status=False
			    break;
                if status is True: 
			print("login successful")           
			print("enter the pin to decrypt keys")
                	securekey=raw_input()
                	securehash=hash_cal(securekey)
		     	var1=AESCipher(securehash)
        	     	dec("key",var1)
		     	decrypt()
                     	break
                else:
                    continue


        except IOError:
                print "\ncreate a new account in cloud"
                print "\nenter new username"
                username=raw_input()
                print "\nenter password"
                password=raw_input()
                print "\nenter your password again"
                checkpasswd=raw_input()
                if password==checkpasswd:
		    createptr=open("Account.txt","w")
		    password=hash_cal(checkpasswd)
                    createptr.write(username + "\n")
                    createptr.write(password + "\n")
                    print ("\nuser created successfully")
                    print ("enter the pin to secure the keys generated")
                    securekey=raw_input()
                    securehash=hash_cal(securekey)
		    encrypt()
		    os.chdir('..')
		    var1=AESCipher(securehash)
		    enc("key",var1)
		    print "\n login to continue"
		else :
		    print ("passwords does not match")
while True:
	print("enter a command or enter 'quit' to logout from cloud") 
	command=raw_input()
	if (command=="quit"):
 		    print ("enter the pin to secure the keys generated")
                    securekey=raw_input()
                    securehash=hash_cal(securekey)
		    os.chdir('..')
		    encrypt()
		    os.chdir('..')
		    var1=AESCipher(securehash)
		    enc("key",var1)
		    break;
	else:
		os.system(command)




