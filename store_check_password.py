import uuid
import hashlib

# store the password as plain text
def insecure_store_password(input_pw):
    
    # this will overwrite the entire file!!!
    f = open("pwfile.txt", "w")
    f.write(input_pw)

    f.close()

# retrieve the plaintext password
def insecure_check_password(input_pw):
    # this will read the file
    f = open("pwfile.txt", "r")
    stored_pw = f.read()
    
    if (stored_pw == input_pw):
        print ("ACCESS GRANTED!")
    else:
        print ("ACCESS DENIED!")
    
    f.close()

# salt and hash the password before storing it
def secure_store_password(input_pw):
    
    # add a little salt (uuid) and then encrypt the password
    salt = uuid.uuid4().hex
    secure_pw = hashlib.sha256(salt.encode() + input_pw.encode()).hexdigest() + ':' + salt

    # store the encrupted password
    f = open("pwfile.txt", "w")
    f.write(secure_pw)

    f.close()

# salt and hash the input password then check it against what you stored
def secure_check_password(input_pw):

    # read the encrypted password
    f = open("pwfile.txt", "r")
    hashed_password = f.read()
    
    stored_pw, salt = hashed_password.split(':')

    # encrypt the input_pw with the same hash and if it matches, it's the same password!
    if (stored_pw == hashlib.sha256(salt.encode() + input_pw.encode()).hexdigest()):
        print ("ACCESS GRANTED!")
    else:
        print ("ACCESS DENIED!")
    
    f.close()

todo = input("Would you like to store a password, or check your password? ")
if (todo[:1].lower() == 's'): # this just checks to see if the first character of the input is 's' for 'store'
    pw = input("What would you like your password to be? ")
    # insecure_store_password(pw)
    secure_store_password(pw)
    
else:
    pw = input("Please enter your password: ")
    # insecure_check_password(pw)
    secure_check_password(pw)