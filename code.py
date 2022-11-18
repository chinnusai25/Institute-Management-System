#!/usr/bin/python
import MySQLdb
import datetime
import random
# Open database connection
user=raw_input("Enter username: ")
password=raw_input("Enter password: ")
db = MySQLdb.connect("localhost",user, password, "IIIT")

# prepare a cursor object using cursor() method
# abstraction meant for data set traversal
cursor = db.cursor()
cursor1 = db.cursor()
cursor2 = db.cursor()
cursor3 = db.cursor()
cursor4 = db.cursor()
cursor5 = db.cursor()
cursor6 = db.cursor()
cursor7 = db.cursor()
cursor8 = db.cursor()
cursor9 = db.cursor()
cursor10 = db.cursor()
cursor11 = db.cursor()
cursor12 = db.cursor()
cursor13 = db.cursor()

def insertstudent():
    try:
        a = raw_input("Enter Student ID: ")
        b = raw_input("Enter S First Name: ")
        c = raw_input("Enter S Middle Name: ")
        d = raw_input("Enter S Last Name: ")
        e = raw_input("Enter Date of Birth: ")
        f=''
        while(f!='M' and f!='F'):
            f = raw_input("Enter Sex M/F: ").upper()
        g = raw_input("Enter Street Address: ")
        cursor12.execute("SELECT Pin_code from Student_1_Pincode;")
        pins=cursor12.fetchall()
        i = raw_input("Enter Pin code: ")
        fl=0
        for it in pins:
            if it[0]==i:
                fl=1
                break

        if fl==0:
            city=raw_input("Enter city: ")
            cursor.execute("INSERT INTO Student_1_Pincode VALUES ('"+i+"','"+str(city)+"');")
        j = raw_input("Enter Blood Group: ")
        k='100'
        while(not (k.isdigit()) or int(k)<0 or int(k)>6):
            k = raw_input("Enter Year Of Study (0-6): ")
        l=''
        while(l!='UG' and l!='PG' and l!='PHD'):
            l = raw_input("Enter Student Type (UG/PG/PHD): ").upper()
        m='NULL'
        n='NULL'
        if(l=='UG' or l=='PG'):      
            m = raw_input("Enter Branch: ")
        else:
            n = raw_input("Enter Field of Study: ")
        o = raw_input("Enter Mobile Number 1: ")
        p = raw_input("Enter Mobile Number 2: ")
        q = raw_input("Enter Email ID 1: ")
        r = raw_input("Enter Email ID 2: ")
        s = raw_input("Enter Entry ID: ")
        cursor1.execute("INSERT INTO Student_1_A VALUES ("+a+",'"+b+"','"+c+"','"+d +
                        "','"+str(e)+"','"+str(f)+"','"+str(g)+"','"+str(i)+"','"+str(j)+"','"+str(k)+"','"+str(l)+"','"+str(m)+"','"+str(n)+"'"+");")
        if(p != ""):
            cursor2.execute(
                "INSERT INTO Student_Phone_Number VALUES ("+a+",'"+o+"'), ("+a+",'"+p+"');")
        else:
            cursor2.execute(
                "INSERT INTO Student_Phone_Number VALUES ("+a+",'"+o+"');")
        if(r != ""):
            cursor3.execute(
                "INSERT INTO Student_Email_ID VALUES ("+a+",'"+q+"'), ("+a+",'"+r+"');")
        else:
            cursor3.execute(
                "INSERT INTO Student_Email_ID VALUES ("+a+",'"+q+"');")
        cursor5.execute("select Tuition_FEE from Mode_of_Entry where Entry_ID='"+s+"';")
        fee=int(cursor5.fetchone()[0])+12000+20000
        # print "Final fee is "+str(fee)
        if(f=='F'):
            cursor6.execute("INSERT INTO Eligibility_for_Hostels Values ("+a+",'H_AI01','No');")
        else:
            cursor6.execute("INSERT INTO Eligibility_for_Hostels Values ("+a+",'H_AI01','Yes');")
        if(l=='PG' or l=='PHD'):
            cursor7.execute("INSERT INTO Eligibility_for_Hostels Values ("+a+",'H_AI02','Yes');")
        else:
            cursor7.execute("INSERT INTO Eligibility_for_Hostels Values ("+a+",'H_AI02','No');")
        if(f=='M'):
            cursor8.execute("INSERT INTO Eligibility_for_Hostels Values ("+a+",'H_AI03','No');")
        else:
            cursor8.execute("INSERT INTO Eligibility_for_Hostels Values ("+a+",'H_AI03','Yes');")
        cursor9.execute("INSERT INTO Eligibility_for_Hostels Values ("+a+",'H_AI04','Yes');")
        cursor4.execute("INSERT INTO Fees VALUES ("+a+",'H_AI04','"+s+"','M_BI01',"+str(fee)+","+str(fee/2)+",'"+str((datetime.date.today() + datetime.timedelta(6*365/12)).isoformat())+"');")
        cursor10.execute("select Student_ID from Teaching_Assistant")
        cursor13.execute("insert into Academic_Report (Student_ID,Attendance) values ("+a+",'75%');")
        tas=cursor10.fetchall()
        taid=tas[random.randint(0,len(tas)-1)][0]
        # print "INSERT INTO Assigned values ("+a+","+str(taid)+");"
        cursor11.execute("INSERT INTO Assigned values ("+a+","+str(taid)+");")

        # Commit your changes in the database
        db.commit()

        print "\nSuccesfully added in the database\n"
    
    except:
        print "\nError occured\n"
        db.rollback()
    
    return

def change_Mess():
    try:
        Id = input("Enter your Student Id: ")
        newm = raw_input("Enter new mess: ")
        cursor.execute(
            "SELECT * from Fees where Student_ID="+str(Id)+";")
        data = cursor.fetchone()
        if len(data) == 0:
            print "Your Student ID is invalid"
        else:
            cursor2.execute(
                "SELECT * from Fees where Student_ID="+str(Id)+";")
            row2 = cursor2.fetchone()
            feeold = row2[4]
            oldmess = row2[3]
            fee=0
            if(oldmess!=None):
                cursor1.execute(
                    "SELECT * from Mess where Mess_ID='"+str(oldmess)+"';")
                row = cursor1.fetchone()
                fee = row[3]
            cursor3.execute(
                "SELECT * from Mess where Mess_ID='"+str(newm)+"';")
            row1 = cursor3.fetchone()
            fee1 = row1[3]
            feeold = feeold-fee+fee1
            # print "UPDATE Fees SET Mess_ID='"+str(newm) +"',Total_Fees="+str(feeold)+" where Student_ID="+str(Id)+";"
            cursor4.execute("UPDATE Fees SET Mess_ID='"+str(newm) +"',Total_Fees="+str(feeold)+" where Student_ID="+str(Id)+";")
            db.commit()
            print "\nSuccesfully added in the database\n"
    
    except:
        print "\nError occured\n"
        db.rollback()
    
    return

def inserting_courses():
    try:
        Id = input("Enter your Student Id: ")
        cursor.execute(
            "SELECT * from Student_1_A where Student_ID="+str(Id)+";")
        data = cursor.fetchone()
        if len(data) == 0:
            print "Your Student ID is invalid"
        else:
            cursor1.execute("SELECT * from Course;")
            row = cursor1.fetchone()
            while row is not None:
                print row
                row = cursor1.fetchone()
            a = input("Enter No.of courses you want to take: ")
            for i in range(a):
                b = raw_input("Courses you want to take:")
                print"INSERT INTO Courses_Taken VALUES ("+str(Id)+",'"+b+"');"
                cursor.execute(
                    "INSERT INTO Courses_Taken VALUES ("+str(Id)+",'"+b+"');")
            db.commit()
            print "\nSuccesfully added in the database\n"
    
    except:
        print "\nError occured\n"
        db.rollback()
    
    return

def deleting_Mess():
    try:
        Id = input("Enter your Student Id to delete mess: ")
        cursor.execute(
            "SELECT * from Fees where Student_ID="+str(Id)+";")
        data = cursor.fetchone()
        if len(data) == 0:
            print "Your Student ID is invalid"
        else:
            cursor2.execute(
                "SELECT * from Fees where Student_ID="+str(Id)+";")
            row2 = cursor2.fetchone()
            feeold = row2[4]
            oldmess = row2[3]
            cursor1.execute(
                "SELECT * from Mess where Mess_ID='"+oldmess+"';")
            row = cursor1.fetchone()
            fee = row[3]
            feeold = feeold-fee
            cursor3.execute(
                "UPDATE Fees SET Mess_ID=NULL,Total_Fees="+str(feeold)+" where Student_ID="+str(Id)+";")
            db.commit()
            print "\nSuccesfully added in the database\n"
    
    except:
        print "\nError occured\n"
        db.rollback()
    
    return    

def change_Hostel():
    try:
        Id = raw_input("Enter your Student Id: ")
        newh = raw_input("Enter new hostel Id: ")
        cursor10.execute("SELECT * from Eligibility_for_Hostels where Student_ID="+str(Id)+" and Hostel_ID='"+str(newh)+"';")
        q=cursor10.fetchone()
        if(q[2]=="Yes"):
            cursor.execute("SELECT * from Fees where Student_ID="+str(Id)+";")
            data = cursor.fetchone()
            if len(data) == 0:
                print "Your Student ID is invalid"
            else:
                cursor2.execute("SELECT * from Fees where Student_ID="+str(Id)+";")
                row2 = cursor2.fetchone()
                feeold = row2[4]
                oldhostel = row2[1]
                cursor1.execute("SELECT * from Hostel where Hostel_ID='"+str(oldhostel)+"';")
                row = cursor1.fetchone()
                fee = row[3]
                cursor3.execute("SELECT * from Hostel where Hostel_ID='"+str(newh)+"';")
                row1 = cursor3.fetchone()
                fee1 = row1[3]
                feeold = feeold-fee+fee1
                cursor3.execute("UPDATE Fees SET Hostel_ID='"+str(newh) +"',Total_Fees="+str(feeold)+" where Student_ID="+str(Id)+";")
                db.commit()
                print "\nSuccesfully added in the database\n"
        else:
            print"Hostel not eligible"
    
    except:
        print "\nError occured\n"
        db.rollback()
    
    return

def change_StudentInfo():
    try:
        Id = input("Enter your Student Id: ")
        cursor.execute("SELECT * from Fees where Student_ID="+str(Id)+";")
        data = cursor.fetchone()
        if len(data) == 0:
            print "Your Student ID is invalid"
        else:
            fn = raw_input("Enter New First Name: ")
            mn = raw_input("Enter New Middle Name: ")
            ln = raw_input("Enter New Last Name: ")
            Dob = raw_input("Enter New Date of Birth: ")
            Sex = raw_input("Enter new Sex: ")
            Sa = raw_input("Enter new Street Address: ")
            Pin = raw_input("Enter new Pincode: ")
            BG = raw_input("Enter new Blood Group: ")
            YoS = raw_input("Enter new Year of Study: ")
            St = raw_input("Enter new Student Type: ")
            Br = raw_input("Enter new Branch: ")
            FoS = raw_input("Enter new Field of Study: ")
            # print "UPDATE Student_1_A SET S_First_Name='"+fn+"',S_Middle_Name='"+mn+"',S_Last_Name='"+ln+"',Date_Of_Birth='"+Dob+"',Sex='"+Sex + "',Street_Address='"+Sa+"', Pin_Code='"+Pin+"',Blood_Group='"+BG+"',Year_of_Study="+YoS+",Student_Type='"+St+"',Branch='"+Br+"',Field_of_Study='"+FoS+"' where Student_ID="+Id+";"
            cursor3.execute("UPDATE Student_1_A SET S_First_Name='"+str(fn)+"',S_Middle_Name='"+str(mn)+"',S_Last_Name='"+str(ln)+"',Date_Of_Birth='"+str(Dob)+"',Sex='"+str(Sex) + "',Street_Address='" +
                            str(Sa)+"', Pin_Code='"+str(Pin)+"',Blood_Group='"+str(BG)+"',Year_of_Study="+str(YoS)+",Student_Type='"+str(St)+"',Branch='"+str(Br)+"',Field_of_Study='"+str(FoS)+"' where Student_ID="+str(Id)+";")
            db.commit()
            print "\nSuccesfully added in the database\n"
    
    except:
        print "\nError occured\n"
        db.rollback()
    
    return

def insertprofessor():
    try:
        a = raw_input("Enter Professor ID: ")
        b = raw_input("Enter P First Name: ")
        c = raw_input("Enter P Middle Name: ")
        d = raw_input("Enter P Last Name: ")
        e = raw_input("Enter Type: ")
        o = raw_input("Enter Mobile Number 1: ")
        p = raw_input("Enter Mobile Number 2: ")
        q = raw_input("Enter Email ID 1: ")
        r = raw_input("Enter Email ID 2: ")

        cursor1.execute("INSERT INTO Professor VALUES (" +
                        a+",'"+b+"','"+c+"','"+d+"','"+e+"');")

        if(p != ""):
            cursor2.execute(
                "INSERT INTO ProfessorPhoneNumber VALUES ("+a+",'"+o+"'), ("+a+",'"+p+"');")
        else:
            cursor2.execute(
                "INSERT INTO ProfessorPhoneNumber VALUES ("+a+",'"+o+"');")
        if(r != ""):
            cursor3.execute(
                "INSERT INTO ProfessorEmailID VALUES ("+a+",'"+q+"'), ("+a+",'"+r+"');")
        else:
            cursor3.execute(
                "INSERT INTO ProfessorEmailID VALUES ("+a+",'"+q+"');")

        s = raw_input("Enter No.of Qualifications: ")
        for i in range(int(s)):
            t = raw_input("Enter your qualification: ")
            cursor4.execute(
                "INSERT INTO ProfessorQualifications VALUES ("+a+",'"+t+"');")

        s = raw_input("Enter No.of Courses taught: ")
        for i in range(int(s)):
            t = raw_input("Enter Course ID: ")
            u = raw_input("Enter the Teaching period: ")
            print "Select Course_Name from Course where Course_ID='"+t+"');"
            cursor8.execute("Select Course_Name from Course where Course_ID='"+t+"';")
            cname=cursor8.fetchone()
            cursor5.execute(
                "INSERT INTO ProfessorCoursesTaught VALUES ('"+a+"','"+str(cname[0])+"');")
            cursor7.execute(
                "INSERT INTO Teaches VALUES ('"+t+"',"+a+",'"+u+"');")

        s = raw_input("Enter No.of Dependants: ")
        for i in range(int(s)):
            t = raw_input("Enter Dependant name: ")
            u = raw_input("Enter the dependant's relation with the professor: ")
            cursor6.execute(
                "INSERT INTO ProfessorDependent VALUES ("+a+",'"+t+"','"+u+"');")

        # Commit your changes in the database
        # print "\nSuccesfully added in the database"
        db.commit()
        print "\nSuccesfully added in the database\n"
    
    except:
        print "\nError occured\n"
        db.rollback()
    
    return

def insertTA():
    try:
        a = raw_input("Enter Student ID: ")
        b = raw_input("Enter Course ID: ")
        c = raw_input("Enter Type: ")

        cursor1.execute(
            "INSERT INTO Teaching_Assistant VALUES ("+a+",'"+b+"','"+c+"');")
        # Commit your changes in the database
        db.commit()
        print "\nSuccesfully added in the database\n"

    except:
        print "\nError occured\n"
        db.rollback()
    
    return

def insertingSGPA():
    try:
        cursor1.execute("""SELECT count(*)
                            FROM information_schema.columns
                            WHERE table_name = 'Academic_Report';""")

        # Commit your changes in the database
        row = cursor1.fetchone()
        # print "ALTER TABLE Academic_Report ADD SGPA"+str(int(row[0])-1)+"INT;"
        cursor2.execute(
            "ALTER TABLE Academic_Report ADD SGPA"+str(int(row[0])-1)+" INT;")
        # print "\nSuccesfully added in the database "
        # db.commit()
        # Commit your changes in the database
        db.commit()

        print "\nSuccesfully added in the database\n"
    
    except:
        print "\nError occured\n"
        db.rollback()
    
    return

def insertCourse():
    try:
        a = raw_input("Enter Course ID: ")
        b = raw_input("Enter Course Name: ")
        c = raw_input("Enter Duration: ")
        d = raw_input("Enter Credits: ")

        cursor1.execute("INSERT INTO Course VALUES ('" +
                        a+"','"+b+"','"+c+"',"+d+");")
        # Commit your changes in the database
        # print "\nSuccesfully added in the database"
        db.commit()
        print "\nSuccesfully added in the database\n"
    
    except:
        print "\nError occured\n"
        db.rollback()
    
    return

def deletestudent():
    try:
        Id = input("Enter Student ID: ")
        cursor1.execute(
            "DELETE FROM Student_1_A where Student_ID="+str(Id)+";")
        # print "\nRow count: "
        db.commit()
        print "\nSuccesfully added in the database\n"
        
    except:
        print "\nError occured\n"
        db.rollback()
    
    return

def deleteProfessor():
    try:
        Id = input("Enter Professor ID: ")
        cursor1.execute(
            "DELETE FROM Professor where Professor_ID="+str(Id)+";")
        # print "\nRow count: "
        db.commit()
        print "\nSuccesfully added in the database\n"
        
    except:
        print "\nError occured\n"
        db.rollback()
    
    return

def deleteTA():
    try:
        Id = input("Enter Student_ID of TA: ")
        cursor1.execute(
            "DELETE FROM Teaching_Assistant where Student_ID="+str(Id)+";")
        # print "\nRow count: "
        db.commit()
        print "\nSuccesfully added in the database\n"
    
    except:
        print "\nError occured\n"
        db.rollback()
    
    return  

def AddingSGPA_of_Student():
    try:
        Id = raw_input("Enter Student ID: ")
        Sgpa = raw_input("Enter SGPA of "+str(Id)+": ")
        cursor1.execute("SELECT * from Academic_Report where Student_ID="+str(Id)+";")
        row = cursor1.fetchone()
        ind=2

        for i in range(2,len(row)):
            if row[i] is None:
                break
            ind+=1
        if(ind!=len(row)):
            # print "ALTER TABLE Academic_Report ADD SGPA"+str(int(row[0])-1)+"INT;"
            print "update Academic_Report set SGPA"+str(int(row[0])-2)+"="+str(Sgpa)+" where Student_ID=" + str(Id)+";"
            cursor2.execute("update Academic_Report set SGPA" +
                            str(int(ind)-1)+"="+str(Sgpa)+" where Student_ID=" + str(Id)+";")
            # print "\nRow count: "
            # db.commit()
            # Commit your changes in the database
            db.commit()
            print "\nSuccesfully added in the database\n"
        else:
            print "All semesters GPA are updated"

    
    except:
        print "\nError occured\n"
        db.rollback()
    
    return

def showdata(chh):
    try:
        if chh==1:
            cursor1.execute("SELECT * from Student_1_A;")
        if chh==2:
            cursor1.execute("SELECT * from Professor;")
        if chh==3:
            cursor1.execute("SELECT * from Mode_of_Entry;")
        if chh==4:
            cursor1.execute("SELECT * from Mess;")
        if chh==5:
            cursor1.execute("SELECT * from Hostel;")
        data=cursor1.fetchone()
        while data is not None:
            print data
            data=cursor1.fetchone()
    except:
        print "\nError occured\n"
        db.rollback()
    return

while True:
    # Execute the SQL command
    print"1: User\n2: Admin\n3: Show data\n4: Quit"
    ch = input("Your choice: ")

    if ch == 1:
        print "1: Register for courses (Insert)\n2: Modify\n3: Cancel Mess (delete)\n"
        ch11 = input("Your choice: ")
        if(ch11 == 1):
            inserting_courses()
        if(ch11 == 3):
            deleting_Mess()
        if(ch11 == 2):
            print"1:Change Mess\n2:Changing Hostel\n3:Changing Student information"
            x = input("Your choice: ")
            if(x == 1):
                change_Mess()
            if(x == 2):
                change_Hostel()
            if(x == 3):
                change_StudentInfo()

    if ch == 2:
        print "1: insert\n2: Delete\n3: Modify"
        ch11 = input("Your choice: ")
        if(ch11 == 1):
            print "1: Student\n2: Professor\n3: Teaching Assistant\n4: A new sgpa column (After end of a semester)\n5: Course"
            ch1 = input("Enter choice: ")
            if(ch1 == 1):
                insertstudent()
            if(ch1 == 2):
                insertprofessor()
            if(ch1 == 3):
                insertTA()
            if(ch1 == 4):
                insertingSGPA()
            if(ch1 == 5):
                insertCourse()

        elif(ch11 == 2):
            print "1: Student\n2: Professor\n3: Teaching Assistant"
            ch2 = input("Enter your choice: ")
            if ch2 == 1:
                deletestudent()
            elif ch2 == 2:
                deleteProfessor()
            elif ch2 == 3:
                deleteTA()

        elif ch11 == 3:
            print("1: SGPA")
            ch3 = input("Enter choice: ")
            if ch3 == 1:
                AddingSGPA_of_Student()
    elif ch==3:
        chh=input("1: Students\n2: Professors\n3: Modes of entry\n4: Messes\n5: Hostels")
        showdata(chh)
    elif ch==4:
        break


# except:
#    	# Rollback in case there is any error
#    	db.rollback()

# close the cursor
cursor.close()
cursor1.close()
cursor2.close()
cursor3.close()
cursor4.close()
cursor5.close()
cursor6.close()
cursor7.close()
cursor8.close()
cursor9.close()
cursor10.close()
cursor11.close()
cursor12.close()
cursor13.close()

# close the connection
db.close()
