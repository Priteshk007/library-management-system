import mysql.connector

x=input("Enter Your Uername: ")
y=input("Enter Your Password: ")
mydb = mysql.connector.connect(
  host="localhost",
  user=x,
  password=y,
  database="Library"
)

mycursor = mydb.cursor()

# create tABLE
mycursor.execute("CREATE TABLE Books (Book_Number int NOT NULL AUTO_INCREMENT, Book_Name VARCHAR(255),Author VARCHAR(255),Status char(20),PRIMARY KEY (Book_Number))")
mycursor.execute("CREATE TABLE Readers (Reader_Number int NOT NULL AUTO_INCREMENT, Reader_Name VARCHAR(255),Reader_mail VARCHAR(255),issued_books int,PRIMARY KEY (Reader_Number))")
mycursor.execute("CREATE TABLE Issue (Book_Number int NOT NULL, Reader_Number int NOT NULL,Issue_Date DATE NOT NULL,PRIMARY KEY (Book_Number))")
mycursor.execute("CREATE TABLE User (User_id varchar(20)NOT NULL, Password varchar(20),PRIMARY KEY(User_id))")
s="INSERT INTO user (User_id,Password) VALUES ('" +"root" + "','" +"root"+"'"+ ")"
mycursor.execute(s)


mycursor.execute("SHOW TABLES")

m=mycursor.fetchall()
print("\n \t \t Congratulations !!!!!!!!!!!!!!!!!!!!!!")
print("\t \t All required tables are Created for You")
print("\n Name of Created tables are")
for i in range(len(m)):
    print(m[i][0])
mydb.commit()



# insert into table
"""for i in range(0,len(x)):
    s="INSERT INTO data (Region,Rep,item,unit) VALUES ('" +x[i] + "'," +"'"+y[i] + "'," +"'"+z[i]  +"',"+ str(k[i]) + ")"
    mycursor.execute(s)"""
    

