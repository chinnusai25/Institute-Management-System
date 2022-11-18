DROP DATABASE IF EXISTS IIIT;
CREATE DATABASE IIIT;
USE IIIT;
DROP TABLE IF EXISTS Student_1_A;
DROP TABLE IF EXISTS Student_1_Pincode;
DROP TABLE IF EXISTS Professor;
DROP TABLE IF EXISTS Teaches;
DROP TABLE IF EXISTS ProfessorDependent;
DROP TABLE IF EXISTS ProfessorEmailID;
DROP TABLE IF EXISTS ProfessorPhoneNumber;
DROP TABLE IF EXISTS ProfessorQualifications;
DROP TABLE IF EXISTS ProfessorCoursesTaught;

CREATE TABLE Student_1_Pincode (
  Pin_code VARCHAR(30) NOT NULL,
  City VARCHAR(30) NOT NULL,
  primary key (Pin_code)
);
INSERT INTO Student_1_Pincode VALUES ("281001","Agra");
INSERT INTO Student_1_Pincode VALUES ("799001","Agartala");
INSERT INTO Student_1_Pincode VALUES ("202001","Aligarh");
INSERT INTO Student_1_Pincode VALUES ("500032","Hyderabad");

CREATE TABLE Student_1_A(
  Student_ID INT NOT NULL,
  S_First_Name VARCHAR(30) NOT NULL,
  S_Middle_Name VARCHAR(30) DEFAULT NULL,
  S_Last_Name VARCHAR(30) NOT NULL,
  Date_of_Birth date NOT NULL,
  Sex VARCHAR(30) NOT NULL,
  Street_Address VARCHAR(30) NOT NULL,
  Pin_code VARCHAR(30) NOT NULL,
  Blood_Group VARCHAR(30) NOT NULL,
  Year_of_Study VARCHAR(30) NOT NULL,
  Student_Type VARCHAR(30) NOT NULL,
  Branch VARCHAR(30) DEFAULT NULL,
  Field_of_Study VARCHAR(30) DEFAULT NULL,
  PRIMARY KEY (Student_ID),
  FOREIGN KEY (Pin_code) REFERENCES Student_1_Pincode (Pin_code) ON DELETE CASCADE
);
INSERT INTO Student_1_A VALUES (201901,"Raj","Shankar","Mahadev",'2000-02-02',"M","2-3/5,Kalyan Colony","281001","O+",2,"UG","CSE",NULL);
INSERT INTO Student_1_A VALUES (201902,"Sunitha","Ruth","Prabhu",'1999-02-03',"F","3/2-4,RamBagh","500032","B+",3,"UG","ECE",NULL);
INSERT INTO Student_1_A VALUES (201903,"Mohd","Imran","Qureshi",'1990-07-11',"M","7/21,Bardhi Nagar","799001","A+",1,"PHD",NULL,"VLSI");
INSERT INTO Student_1_A VALUES (201904,"Rithika","Prakash","Sagar",'1999-12-12',"F","8/32-3,Mayan Nagar","202001","AB-",2,"PG","CSE",NULL);
INSERT INTO Student_1_A VALUES (201905,"Shyam","Lalu","Prasad",'2000-02-12',"M","2/12-12,Surya Nagar","500032","AB+",1,"UG","CHD",NULL);

CREATE TABLE Professor(
  Professor_ID   INT NOT NULL,
  P_First_Name VARCHAR(30) NOT NULL,
  P_Middle_Name VARCHAR(30),
  P_Last_Name VARCHAR(30),
  Professor_Type VARCHAR(30),
  primary key (Professor_ID)
);
INSERT INTO Professor VALUES (20101004,"Madhav","P.","Krishna","Associate");
INSERT INTO Professor VALUES (20094020,"Rajashekar","Kamal","Pooram","Assistant");
INSERT INTO Professor VALUES (20060402,"Venkata","R.","Chopella","Associate");

DROP TABLE IF EXISTS Course;
CREATE TABLE Course(
    Course_ID VARCHAR(30),
    Course_Name VARCHAR(30),
    Duration VARCHAR(30),
    Credits INT,
    PRIMARY KEY(Course_ID)
);
INSERT INTO Course VALUES ("ES305","Science-1","Sem",04);
INSERT INTO Course VALUES ("ESP307","ESW","Sem",02);
INSERT INTO Course VALUES ("ESX105","Data&Application","HalfSem",02);

DROP TABLE IF EXISTS Hostel;
CREATE TABLE Hostel(
    Hostel_ID varchar(30),
    Hostel_Name VARCHAR(30),
    Number_of_Rooms INT,
    Hostel_Fee INT,
    PRIMARY KEY(Hostel_ID)
);
INSERT INTO Hostel VALUES ("H_AI01","Young Boys hostel",350,15000);
INSERT INTO Hostel VALUES ("H_AI02","Kinshuk Nivas",150,22000);
INSERT INTO Hostel VALUES ("H_AI03","BlaBla Hostel",600,13000);
INSERT INTO Hostel VALUES ("H_AI04","Bharath Nivas",400,20000);

DROP TABLE IF EXISTS Mess;
CREATE TABLE Mess(
    MESS_ID VARCHAR(30),
    Mess_Name VARCHAR(30),
    Capacity INT,
    Mess_Fee INT,
    PRIMARY KEY(MESS_ID)
);
INSERT INTO Mess VALUES ("M_BI01","North",250,12000);
INSERT INTO Mess VALUES ("M_BI02","South",150,21000);
INSERT INTO Mess VALUES ("M_BI03","Continental",300,8000);
INSERT INTO Mess VALUES ("M_BI04","Vegan",150,10000);

DROP TABLE IF EXISTS Mode_of_Entry;
CREATE TABLE Mode_of_Entry(
    Entry_ID VARCHAR(30),
    Entry_Name VARCHAR(30),
    Seats INT,
    INTerview VARCHAR(30),
    Tuition_FEE INT,
    PRIMARY KEY(Entry_ID)
);
INSERT INTO Mode_of_Entry VALUES ("E_CI01","JEE Main",320,"No",125000);
INSERT INTO Mode_of_Entry VALUES ("E_CI02","UGEE",200,"Yes",100000);
INSERT INTO Mode_of_Entry VALUES ("E_CI03","PGEE",90,"Yes",145000);
INSERT INTO Mode_of_Entry VALUES ("E_CI04","Lateral Entry",40,"Yes",125000);

CREATE TABLE ProfessorDependent(
  Professor_ID INT NOT NULL,
  Dependent_Name VARCHAR(30) NOT NULL,
  Relationship_Type VARCHAR(30) NOT NULL, 
  primary key (Professor_ID,Dependent_Name),
  FOREIGN KEY (Professor_ID) REFERENCES Professor (Professor_ID) ON DELETE CASCADE
);
INSERT INTO ProfessorDependent VALUES (20101004,"Snehal","Daughter");
INSERT INTO ProfessorDependent VALUES (20094020,"Arpita","Wife");
INSERT INTO ProfessorDependent VALUES (20060402,"Priyanka","Wife");

CREATE TABLE Teaches(
  Course_ID  VARCHAR(30) NOT NULL,
  Professor_ID INT NOT NULL,
  Teaching_Period varchar(30) NOT NULL,
  primary key (Professor_ID,Course_ID),
  FOREIGN KEY (Professor_ID) REFERENCES Professor (Professor_ID) ON DELETE CASCADE,
  FOREIGN KEY (Course_ID) REFERENCES Course (Course_ID) ON DELETE CASCADE
);
INSERT INTO Teaches VALUES ("ES305",20101004,"Fall_2019");
INSERT INTO Teaches VALUES ("ESP307",20094020,"Fall_2019");
INSERT INTO Teaches VALUES ("ESX105",20060402,"Fall_2019");

CREATE TABLE ProfessorPhoneNumber (
  Professor_ID INT NOT NULL,
  Phone_Number VARCHAR(30) NOT NULL,
  primary key (Professor_ID,Phone_Number),
  FOREIGN KEY (Professor_ID) REFERENCES Professor (Professor_ID) ON DELETE CASCADE
);
INSERT INTO ProfessorPhoneNumber VALUES (20101004,"9354026186");
INSERT INTO ProfessorPhoneNumber VALUES (20101004,"9377482414");
INSERT INTO ProfessorPhoneNumber VALUES (20094020,"9422374918");
INSERT INTO ProfessorPhoneNumber VALUES (20094020,"9341240942");
INSERT INTO ProfessorPhoneNumber VALUES (20060402,"9492019293");

CREATE TABLE ProfessorEmailID (
  Professor_ID INT NOT NULL,
  Email_ID VARCHAR(30) NOT NULL,
  primary key (Professor_ID,Email_ID),
  FOREIGN KEY (Professor_ID) REFERENCES Professor (Professor_ID) ON DELETE CASCADE
);
INSERT INTO ProfessorEmailID VALUES (20101004,"Snehal@gmail.com");
INSERT INTO ProfessorEmailID VALUES (20101004,"Madhav@gmail.com");
INSERT INTO ProfessorEmailID VALUES (20094020,"Arpita@gmail.com");
INSERT INTO ProfessorEmailID VALUES (20094020,"Rajeshkar@gmail.com");
INSERT INTO ProfessorEmailID VALUES (20060402,"Venkata@gmail.com");

CREATE TABLE ProfessorQualifications (
  Professor_ID INT NOT NULL,
  Qualifications VARCHAR(30) NOT NULL,
  primary key (Professor_ID,Qualifications),
  FOREIGN KEY (Professor_ID) REFERENCES Professor (Professor_ID) ON DELETE CASCADE
);
INSERT INTO ProfessorQualifications VALUES (20101004,"PHD IIT-H CSE");
INSERT INTO ProfessorQualifications VALUES (20101004,"M-tech IITH-ECE");
INSERT INTO ProfessorQualifications VALUES (20094020,"M-tech IITD-ECE");
INSERT INTO ProfessorQualifications VALUES (20094020,"PHD IITD-ECE");
INSERT INTO ProfessorQualifications VALUES (20060402,"PHD UC Berkeley CSE");

CREATE TABLE ProfessorCoursesTaught (
  Professor_ID INT NOT NULL,
  Courses_Taught VARCHAR(30) NOT NULL,
  primary key (Professor_ID,Courses_Taught),
  FOREIGN KEY (Professor_ID) REFERENCES Professor (Professor_ID) ON DELETE CASCADE
);
INSERT INTO ProfessorCoursesTaught VALUES (20101004,"Science-1");
INSERT INTO ProfessorCoursesTaught VALUES (20094020,"ESW");
INSERT INTO ProfessorCoursesTaught VALUES (20060402,"Data&Applications");

DROP TABLE IF EXISTS Academic_Report;
CREATE TABLE Academic_Report(
    Student_ID INT,
    Attendance VARCHAR(30),
    PRIMARY KEY(Student_ID),
    FOREIGN KEY (Student_ID) REFERENCES Student_1_A(Student_ID) ON DELETE CASCADE
);
INSERT INTO Academic_Report VALUES (201901,"87%");
INSERT INTO Academic_Report VALUES (201902,"86%");
INSERT INTO Academic_Report VALUES (201903,"100%");
INSERT INTO Academic_Report VALUES (201904,"95%");
INSERT INTO Academic_Report VALUES (201905,"100%");

DROP TABLE IF EXISTS Teaching_Assistant;
CREATE TABLE Teaching_Assistant(
    Student_ID INT,
    Course_ID VARCHAR(30),
    TA_Type VARCHAR(30),
    FOREIGN KEY (Student_ID) REFERENCES Student_1_A(Student_ID) ON DELETE CASCADE, 
    PRIMARY KEY (Student_ID),
    FOREIGN KEY (Course_ID) REFERENCES Course(Course_ID) ON DELETE CASCADE
);
INSERT INTO Teaching_Assistant VALUES (201902,"ES305","Full");
INSERT INTO Teaching_Assistant VALUES (201903,"ESP307","Quarter");
INSERT INTO Teaching_Assistant VALUES (201904,"ESX105","Half");

DROP TABLE IF EXISTS Assigned;
CREATE TABLE Assigned(
    Student_ID INT,
    TA_Student_ID INT,
    PRIMARY KEY(Student_ID),
    FOREIGN KEY (Student_ID) REFERENCES Student_1_A(Student_ID) ON DELETE CASCADE,
    FOREIGN KEY (TA_Student_ID) REFERENCES Teaching_Assistant(Student_ID) ON DELETE CASCADE
);
INSERT INTO Assigned VALUES (201901,201902);
INSERT INTO Assigned VALUES (201902,201903);
INSERT INTO Assigned VALUES (201903,201904);
INSERT INTO Assigned VALUES (201904,201903);
INSERT INTO Assigned VALUES (201905,201904);

DROP TABLE IF EXISTS Eligibility_for_Hostels;
CREATE TABLE Eligibility_for_Hostels(
    Student_ID INT,
    Hostel_ID varchar(30),
    Eligibility VARCHAR(30),
    PRIMARY KEY(Student_ID,Hostel_ID),
    FOREIGN KEY (Student_ID) REFERENCES Student_1_A(Student_ID) ON DELETE CASCADE,
    FOREIGN KEY (Hostel_ID) REFERENCES Hostel(Hostel_ID) ON DELETE CASCADE
);
INSERT INTO Eligibility_for_Hostels VALUES (201901,"H_AI01","Yes");
INSERT INTO Eligibility_for_Hostels VALUES (201902,"H_AI01","No");
INSERT INTO Eligibility_for_Hostels VALUES (201903,"H_AI01","Yes");
INSERT INTO Eligibility_for_Hostels VALUES (201904,"H_AI01","No");
INSERT INTO Eligibility_for_Hostels VALUES (201905,"H_AI01","Yes");
INSERT INTO Eligibility_for_Hostels VALUES (201901,"H_AI02","Yes");
INSERT INTO Eligibility_for_Hostels VALUES (201902,"H_AI02","No");
INSERT INTO Eligibility_for_Hostels VALUES (201903,"H_AI02","Yes");
INSERT INTO Eligibility_for_Hostels VALUES (201904,"H_AI02","No");
INSERT INTO Eligibility_for_Hostels VALUES (201905,"H_AI02","Yes");
INSERT INTO Eligibility_for_Hostels VALUES (201901,"H_AI03","No");
INSERT INTO Eligibility_for_Hostels VALUES (201902,"H_AI03","Yes");
INSERT INTO Eligibility_for_Hostels VALUES (201903,"H_AI03","No");
INSERT INTO Eligibility_for_Hostels VALUES (201904,"H_AI03","Yes");
INSERT INTO Eligibility_for_Hostels VALUES (201905,"H_AI03","No");
INSERT INTO Eligibility_for_Hostels VALUES (201901,"H_AI04","Yes");
INSERT INTO Eligibility_for_Hostels VALUES (201902,"H_AI04","Yes");
INSERT INTO Eligibility_for_Hostels VALUES (201903,"H_AI04","Yes");
INSERT INTO Eligibility_for_Hostels VALUES (201904,"H_AI04","Yes");
INSERT INTO Eligibility_for_Hostels VALUES (201905,"H_AI04","Yes");

DROP TABLE IF EXISTS Student_Email_ID;
CREATE TABLE Student_Email_ID(
    Student_ID INT,
    S_EMAIL_ID VARCHAR(30),
    FOREIGN KEY (Student_ID) REFERENCES Student_1_A(Student_ID) ON DELETE CASCADE,
    PRIMARY KEY(Student_ID,S_EMAIL_ID)
);
INSERT INTO Student_Email_ID VALUES(201901,"Raj@fmail.com");
INSERT INTO Student_Email_ID VALUES(201902,"Sunita@fmail.com");
INSERT INTO Student_Email_ID VALUES(201903,"Mohammad@fmail.com");
INSERT INTO Student_Email_ID VALUES(201904,"Rithika1@fmail.com");
INSERT INTO Student_Email_ID VALUES(201904,"Rithika2@fmail.com");
INSERT INTO Student_Email_ID VALUES(201905,"Shyam@fmail.com");

DROP TABLE IF EXISTS Student_Phone_Number;
CREATE TABLE Student_Phone_Number(
    Student_ID INT,
    S_Phone_Number varchar(30) ,
    FOREIGN KEY (Student_ID) REFERENCES Student_1_A(Student_ID) ON DELETE CASCADE,
    PRIMARY KEY(Student_ID,S_Phone_Number)
);
INSERT INTO Student_Phone_Number VALUES (201901,"9999999999");
INSERT INTO Student_Phone_Number VALUES (201902,"8888888888");
INSERT INTO Student_Phone_Number VALUES (201903,"7777777777");
INSERT INTO Student_Phone_Number VALUES (201904,"6666666666");
INSERT INTO Student_Phone_Number VALUES (201905,"5555555555");
INSERT INTO Student_Phone_Number VALUES (201905,"4444444444");

DROP TABLE IF EXISTS Fees;
CREATE TABLE Fees(
    Student_ID INT,
    Hostel_ID VARCHAR(30),
    Entry_ID VARCHAR(30),
    Mess_ID VARCHAR(30),
    Total_Fees INT,
    Fee_Paid INT,
    Due_Date DATE,
    FOREIGN KEY (Student_ID) REFERENCES Student_1_A(Student_ID) ON DELETE CASCADE,
    FOREIGN KEY (Hostel_ID) REFERENCES Hostel(Hostel_ID) ON DELETE CASCADE,
    FOREIGN KEY (Entry_ID) REFERENCES Mode_of_Entry(Entry_ID) ON DELETE CASCADE,
    FOREIGN KEY (Mess_ID) REFERENCES Mess(Mess_ID) ON DELETE CASCADE,
    PRIMARY KEY(Student_ID)
);
INSERT INTO Fees VALUES (201901,"H_AI01","E_CI01","M_BI01",152000,152000,'2020-02-01');
INSERT INTO Fees VALUES (201902,"H_AI03","E_CI01","M_BI02",159000,159000,'2020-02-01');
INSERT INTO Fees VALUES (201903,"H_AI01","E_CI03","M_BI03",168000,120000,'2020-05-01');
INSERT INTO Fees VALUES (201904,"H_AI04","E_CI03","M_BI04",175000,175000,'2020-05-01');
INSERT INTO Fees VALUES (201905,"H_AI02","E_CI02","M_BI01",134000,0,'2020-05-01');

DROP TABLE IF EXISTS Courses_Taken;
CREATE TABLE Courses_Taken(
    Student_ID INT,
    Course_ID VARCHAR(30),
    FOREIGN KEY (Student_ID) REFERENCES Student_1_A(Student_ID) ON DELETE CASCADE,
    FOREIGN KEY (Course_ID) REFERENCES Course(Course_ID) ON DELETE CASCADE,
    PRIMARY KEY(Student_ID,Course_ID)
);
INSERT INTO Courses_Taken VALUES (201901,"ES305");
INSERT INTO Courses_Taken VALUES (201902,"ESP307");
INSERT INTO Courses_Taken VALUES (201903,"ES305");
INSERT INTO Courses_Taken VALUES (201904,"ESX105");
INSERT INTO Courses_Taken VALUES (201905,"ESX105");

