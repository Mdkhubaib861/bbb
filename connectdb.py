import mysql.connector

conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mmantc"
    )
cursor1=conn.cursor()
# cursor1.execute("CREATE DATABASE mmantc")
#cursor1.execute("SHOW DATABASES")
#for x in cursor1:
#    print(x)

# cursor1.execute("DROP TABLE IF EXISTS student_info")

# q1='''
# CREATE TABLE student_info(sid INT AUTO_INCREMENT PRIMARY KEY,
#                         st_name VARCHAR(100),
#                         dob DATE NOT NULL,
#                         gender VARCHAR(6) NOT NULL,
#                         email VARCHAR(50) NOT NULL,
#                         category VARCHAR(20) NOT NULL,
#                         address VARCHAR(100) NOT NULL,
#                         aadhaar VARCHAR(15) NOT NULL,
#                         prn VARCHAR(20) NOT NULL,
#                         course VARCHAR(30) NOT NULL,
#                         branch VARCHAR(20) NOT NULL,
#                         year CHAR(10) ,
#                         percent FLOAT,
#                         photo VARCHAR(100) NOT NULL)
# '''

# cursor1.execute(q1)
q1='''
INSERT INTO student_info (
        st_name,dob,gender,email,category,address,
        aadhaar,prn,course,branch,year,percent,photo
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
'''

v1 = (
        'Faisal',
        '2006-06-01',
        'Male',
        'shahfaisal@gmail.com',
        'general',
        'Killa Malegaon',
        '234345675678',
        '23453ASC',
        'Bachelors in Engineer',
        'Electronics and Telecommunications',
        'First',
        82.52,
        'Photo_ShahFaisal_20-11-2006.jpg'
    )

# cursor1.execute(q1, v1)
# conn.commit()

cursor1.execute("SELECT * FROM student_info")
for row in cursor1.fetchall():
    print(row)

cursor1.execute("SELECT COUNT(*) FROM student_info")
print(cursor1.fetchone())
