from LoginScr import *
from Register import registerStud
while True:
    print """--------------------------------- 
WELCOME TO COLLEGE LIBRARY PANEL 
--------------------------------- 
SELECT THE GIVEN OPTIONS: 
1. for Login 
2. for Register New Student 
3. for EXIT 
---------------------------------"""
    ch=input("Enter your choice: ")
    if ch==1:
        login()
    elif ch==2:
        registerStud()
    elif ch==3:
        exit()
    else:
        print "############ INVALID CHOICE! ############"
