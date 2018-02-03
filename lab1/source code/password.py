#validation cliteria for the passwords
import re# importing the pre-defined regular expressions
p = input("Input your password:  ")
x = True
while x:# loop for checking the various cliteria
    if (len(p)<6 or len(p)>16):#checking for the length
        print('\n length out of range')
        break
    elif not re.search("\d",p):#checking for the numbers
        print('number missing')
        break
    elif not re.search("[$@!*]",p):#checking for the numbers
        print('special character missing')
        break
    elif not re.search("[a-z]",p):#checking for the numbers
        print('lower case missing')
        break
    elif not re.search("[A-Z]",p):#checking for the numbers
        print('upper case missing')
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")
