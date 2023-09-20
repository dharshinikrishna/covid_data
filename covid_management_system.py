#covidtest
import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="covid19_test")
if conn.is_connected():
    print("successsfully connected")

#covid test table
import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="covid19_test",
)
cursor=conn.cursor()
cursor.execute("create table covid_patient_data(state varchar(100),patient_no int,name varchar(100),age int,address varchar(200),mobile_no int,status varchar(100))")
print("successfully table created")

#covid data
import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="covid19_test",
)
cursor=conn.cursor()

#insert data into table
while True:
    state=input("Enter patient state:")
    patient_no=int(input("Enter patient number:"))
    name=input("Enter patient name:")
    age=int(input("Enter patient age:"))
    address=input("Enter patient's address:")
    mobile_no=int(input("Enter mobile number:"))
    status=input("Enter the status of patient:")
    query="insert into covid_patient_data(state,patient_no,name,age,address,mobile_no,status) values ('{}',{},'{}',{},'{}',{},'{}')".format(state,patient_no,name,age,address,mobile_no,status)
    cursor.execute(query)
    conn.commit()
    print("data inserted successfully")
    choice=int(input("1->Enter more records\n2->Exit\nEnter your choice:"))
    if choice==2:
        break
        exit()

#update data
import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="covid19_test",
)
cursor=conn.cursor()

#update data
query="UPDATE covid_patient_data SET status='(+ve)increased' WHERE patient_no=101"
cursor.execute(query)
conn.commit()
print("data updatted successfully")
