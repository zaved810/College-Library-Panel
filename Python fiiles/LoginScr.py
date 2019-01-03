from FunLib import *
from Register import registerEmp
def login():
    c=0
    while True:
        lid=input("Enter Login ID: ")
        password=raw_input("Enter Password: ")
        user_type=verify(lid,password)
        if user_type[0]=="stu":
            c=0
            print """************* WELCOME %s ***************
-------------------------------------------"""%user_type[1]
            while True:
                print """SELECT THE GIVEN OPTIONS: 
1. for View All Books. 
2. for Search Book. 
3. for EXIT 
--------------------------------- """
                ch=input("Enter your choice: ")
                if ch==1:
                    viewAllBooks()
                elif ch==2:
                    searchBook()
                elif ch==3:
                    exit()
                else:
                    print "Invalid Choice!\nPlease enter the correct choice"

        if user_type[0]=="emp":
            c=0
            print """************* WELCOME %s ***************
-------------------------------------------"""%user_type[1]
            while True:
                print """SELECT THE GIVEN OPTIONS: 
1. for Add Book
2. for Delete Book. 
3. for List All Book. 
4. for Search Book. 
5. for Issue Book.
6. for Return Book.
7. for Add New Employee 
8. for EXIT 
--------------------------------- """
                ch=input("Enter your choice: ")
                if ch==1:
                    addBook()
                elif ch==2:
                    deleteBook()
                elif ch==3:
                    viewAllBooks()
                elif ch==4:
                    searchBook()
                elif ch==5:
                    issueBook(lid)
                elif ch==6:
                    returnBook()
                elif ch==7:
                    registerEmp()
                elif ch==8:
                    exit()
                else:
                    print "Invalid Keyword!\nEnter the correct choice"

        if user_type=="Invalid":
            print "INVALID LOGINID/PASSWORD"
            c+=1
            if c==5:
                print """########### TOO MANY ATTEMPTS ############
--------------------------------------"""
                break
