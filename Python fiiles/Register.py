import MySQLdb as db
def registerStud():
    conn=db.connect("localhost","root","root","stp_python")
    c=conn.cursor()
    try:
        print """REGISTER STUDENT HERE: 
ENTER DETAILS:"""
        roll_no=input("ROLL NO: ")
        name=raw_input("NAME: ")
        dept=raw_input("DEPT: ")
        sem=raw_input("SEM: ")
        batch=raw_input("BATCH: ")
        password=raw_input("PASSWORD: ")
        query="insert into stu_detail values({rn},'{n}','{d}','{s}','{b}')"
        c.execute(query.format(rn=roll_no,n=name,d=dept,s=sem,b=batch))
        query="insert into login values({rn},'{p}','{n}','{r}')"
        c.execute(query.format(rn=roll_no,p=password,n=name,r="stu"))
        conn.commit()
        print """****** REGSTRATION SUCCESSFULLY *********
-------------------------------------------------
LOGIN DETAILS FOR PANEL ACCESS"""
        print """YOUR LOGIN ID: %d
YOUR PASSWORD: %s
-------------------------------------------------"""%(roll_no,password)
    except Exception, e:
        print e

    finally:
        c.close()
        conn.close()          

def registerEmp():
    conn=db.connect("localhost","root","root","stp_python")
    c=conn.cursor()
    try:
        print """REGISTER EMPLOYEE HERE: 
ENTER DETAILS"""
        eid=input("EMP ID: ")
        name=raw_input("NAME: ")
        dept=raw_input("DEPT: ")
        doj=raw_input("JOIN DATE: ")
        salary=input("SALARY: ")
        password=raw_input("PASSWORD: ")
        query="insert into emp_detail values({empid},'{n}','{dept}','{doj}',{sal})"
        c.execute(query.format(empid=eid,n=name,dept=dept,doj=doj,sal=salary,))
        query="insert into login values({empid},'{pas}','{name}','emp')"
        c.execute(query.format(empid=eid,pas=password,name=name))
        conn.commit()
        print """****** EMPLOYEE ADDED SUCCESSFULLY *******
---------------------------------------------------
LOGIN DETAILS FOR PANEL ACCESS 
LOGIN ID : %d
PASSWORD : %s 
THANK YOU!!
---------------------------------------------------"""%(eid,password)
    except Exception, e:
        print e
    finally:
        c.close()
        conn.close()

        
