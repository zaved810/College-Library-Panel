import MySQLdb as db
def verify(lid,password):
    conn=db.connect("localhost","root","root","stp_python")
    c=conn.cursor()
    try:
        query="select role, name from login where lid=%d and pass='%s'"%(lid,password)
        c.execute(query)
        x=c.fetchall()
        if len(x)==0:
            return "Invalid"
        else:
            return x[0]
    except Exception, e:
        print e
    finally:
        c.close()
        conn.close()
        
def viewAllBooks():
    conn=db.connect("localhost","root","root","stp_python")
    c=conn.cursor()
    try:
        query="select * from books"
        c.execute(query)
        x=c.fetchall()
        if len(x)==0:
            print """################ SORRY, NO BOOK IS AVAILABLE #####################
-----------------------------------------------------------------------------"""
        else:
            for row in x:
                print row
            print "---------------------------------------------------------------------"
    except Exception, e:
        print e
    finally:
        c.close()
        conn.close()

def searchBook():
    conn=db.connect("localhost","root","root","stp_python")
    c=conn.cursor()
    try:
        bid=input("Enter the Book ID: ")
        query="select * from books where bid=%d"%bid
        c.execute(query)
        x=c.fetchall()
        if len(x)==0:
            print "############ NO SUCH BOOK AVAILABLE #############"
            print "-------------------------------------------------"
        else:
            print x[0]
            print "------------------------------------------------------------------------------------"
    except Exception, e:
        print e
    finally:
        c.close()
        conn.close()

def addBook():
    conn=db.connect("localhost","root","root","stp_python")
    c=conn.cursor()
    try:
        print "Enter Details: "
        while True:
            bid=input("BOOK ID: ")
            query="select * from books where bid=%d"%bid
            c.execute(query)
            x=c.fetchall()
            if len(x)!=0:
                print """The Book ID is already in use
PLEASE ENTER A DIFFERENT ONE"""
            else:
                break
        title=raw_input("TITLE: ")
        subject=raw_input("SUBJECT: ")
        author=raw_input("AUTHOR: ")
        quant=input("QUANTITY: ")
        query="insert into books values(%d,'%s','%s','%s',%d)"%(bid,title,subject,author,quant)
        c.execute(query)
        conn.commit()
        print "*************** BOOK IS SUCCESSFULLY ADDED ******************"
        print "--------------------------------------------------------------"
    except Exception, e:
        print e
    finally:
        c.close()
        conn.close()

def deleteBook():
    conn=db.connect("localhost","root","root","stp_python")
    c=conn.cursor()
    try:
        bid=input("Enter the Book ID: ")
        query="select bid from issue_detail where bid=%d"%bid
        c.execute(query)
        x=c.fetchall()
        if len(x)==0:
            query="delete from books where bid=%d"%bid
            c.execute(query)
            conn.commit()
            print """*************** BOOK DELETED SUCCESSFULLY ****************
---------------------------------------------------"""
        else:
            print """####### BOOK CANNOT BE DELETED AS IT IS ALREADY ISSUED #######
----------------------------------------------------------"""
    except Exception, e:
        print e
    finally:
        c.close()
        conn.close()

def issueBook(issueby):
    conn=db.connect("localhost","root","root","stp_python")
    c=conn.cursor()
    try:
        bid=input("Enter the Book ID: ")
        issueto=input("Enter the roll no. of student: ")
        query="select bid from books where bid={id}"
        c.execute(query.format(id=bid))
        x1=c.fetchall()
        query="select name from stu_detail where rollno={it}"
        c.execute(query.format(it=issueto))
        x2=c.fetchall()
        if len(x1)==0 or len(x2)==0:
            print """######### BOOK ISSUE ERROR ##########
-----------------------------------------------"""
        else:
            query_avail="select quant_avail from books where bid={bid}"
            c.execute(query_avail.format(bid=bid))
            x=c.fetchall()
            if x==0:
                print """############# BOOK ISSUE ERROR : BOOK IS NOT AVAILABLE ##############
------------------------------------------------------------------------------"""
            else:
                query="update books set quant_avail=quant_avail-1 where bid={id}"
                c.execute(query.format(id=bid))
                query="insert into issue_detail values({id},{it},{ib})"
                c.execute(query.format(id=bid,it=issueto,ib=issueby))
                conn.commit()
                print """************** BOOK ISSUED TO %s, ID-%d **************
                THANK YOU!!!
                ----------------------------------------------------------------"""%(x2,issueto)

    except Exception, e:
        print e
    finally:
        c.close()
        conn.close()

def returnBook():
    conn=db.connect("localhost","root","root","stp_python")
    c=conn.cursor()
    try:
        bid=input("Enter the Book ID: ")
        roll=input("Enter the roll no. of student: ")
        query="select bid from books where bid=%d"%bid
        c.execute(query)
        x1=c.fetchall()
        query="select rollno from stu_detail where rollno=%d"%roll
        c.execute(query)
        x2=c.fetchall()
        if len(x1)==0 or len(x2)==0:
            print """################## BOOK RETURN ERROR #################
---------------------------------------------------------"""
        else:
            query="select issueto from issue_detail where issueto=%d and bid=%d"%(roll,bid)
            c.execute(query)
            x=c.fetchall()
            if len(x)==0:
                print """############## NO SUCH BOOK ISSUED ###############
--------------------------------------"""
            else:
                query="delete from issue_detail where issueto=%d and bid=%d"%(roll,bid)
                c.execute(query)
                query="update books set quant_avail=quant_avail+1 where bid=%d"%bid
                c.execute(query)
                conn.commit()
                print """************* BOOK SUCCESSFULLY RETURNED *************
----------------------------------------------------------------"""
    except Exception, e:
        print e
    finally:
        c.close()
        conn.close()





