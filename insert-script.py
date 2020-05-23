import mysql.connector
from datetime import date
mydb = mysql.connector.connect(
    host = "172.17.0.2",
    user= "root",
    passwd = "password",
    database = "cicd"
)

mycursor = mydb.cursor();

sql = "INSERT INTO USER_DETAILS (firstname, lastname,email,username,password,lastupdated) VALUES (%s,%s,%s,%s,%s,%s)"
val =[
('firstname1','lastname1','email1','admin1','admin1',date.today()),
('firstname2','lastname2','email2','admin2','admin2',date.today()),
('firstname3','lastname3','email3','admin3','admin3',date.today()),
('firstname4','lastname4','email4','admin4','admin4',date.today()),
('firstname5','lastname5','email5','admin5','admin5',date.today()),
('firstname6','lastname6','email6','admin6','admin6',date.today()),
('firstname7','lastname7','email7','admin7','admin7',date.today()),
('firstname8','lastname8','email8','admin8','admin8',date.today()),
]

mycursor.executemany(sql,val)
mydb.commit();
print (mycursor.rowcount, "record inserted");
