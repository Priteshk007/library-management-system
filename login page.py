from tkinter import *
from datetime import date
import mysql.connector
from PIL import ImageTk,Image #PIL -> Pillow
from tkinter import messagebox
import smtplib, ssl
import datetime
import wikipedia
import webbrowser
import pyttsx3
import numpy as np
import matplotlib.pyplot as plt
import time
same=True
n=1

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
a = voices[1].name
global query_2
import GUI_P_1






port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "lmscsbs2020@gmail.com"  # Enter your address
  
password = "nxpkkcuduwrfqiyo"
Login=0
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="Library"
)
mycursor = mydb.cursor()
root = Tk()
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("600x500")
same=True
n=0.55

# Adding a background image
background_image =Image.open("Library_image.PNG")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
Canvas1.create_image(300,255,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="red",bd=5)
headingFrame1.place(relx=0.15,rely=0.1,relwidth=0.7,relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to \n CHANDIGARH UNIVERSITY Login Page", bg='black', fg='red', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)




def deleteregister():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="Library"
    )
    mycursor = mydb.cursor()
    delete_number = deleteinfo1.get()
    
    
    x="select count(Book_Number) from issue where Book_Number="+str(delete_number)
    mycursor.execute(x)
    a=mycursor.fetchall()
    y=a[0][0]
    
    x="select count(Book_Number) from books where Book_Number="+str(delete_number)
    mycursor.execute(x)
    a=mycursor.fetchall()
 
    z=a[0][0]
   

   

    if(y==0 and z==1):
        try:
            insertuser = "delete from books where Book_Number="+str(delete_number)
            mycursor.execute(insertuser)
            mydb.commit()
            
            messagebox.showinfo('Success',"deleted successfully")
        except:
            messagebox.showinfo("Error","Can't delete data into Database")
    else:
        messagebox.showinfo("Error","Either book name is invalid or already issued")
    root.destroy()
     
      
    
    
def delete():
    global deleteinfo1 , con, cur, UserTable, root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=700,height=700)
    root.geometry("800x700")


    

    con = mysql.connector.connect( host="localhost",user="root",password="root",database="Library")
    cur = con.cursor()

    # Enter Table Names here
    UserTable = "issue" # Book Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="black")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="red",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="DELETE Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    #book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    deleteinfo1 = Entry(labelFrame)
    deleteinfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=deleteregister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black',command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
    

def deleteregister1():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="Library"
    )
    mycursor = mydb.cursor()
    delete_number = deleteinfo1.get()
    
    
    x="select count(Reader_Number) from issue where Reader_Number="+str(delete_number)
    mycursor.execute(x)
    a=mycursor.fetchall()
    y=a[0][0]
    
    x="select count(Reader_Number) from readers where Reader_Number="+str(delete_number)
    mycursor.execute(x)
    a=mycursor.fetchall()
 
    z=a[0][0]
    
   

   

    if(y==0 and z==1):
        insertuser="Select Reader_mail from Readers where Reader_number="+str(delete_number)
        mycursor.execute(insertuser)
        a=mycursor.fetchall()
        receiver_email =a[0][0]

        mydb.commit()

        Subject="Reader Removed"
        text = " Hi there \n This message is sent from Chandigarh University Library."
        text+="\n"
        text+="This is to inform You that you have been removed from Chandigarh University Library \n We bid you Farewell (<_> )!!!!\n THANK YOU!"

        message = 'Subject: {}\n\n{}'.format(Subject,text)
        try:
            insertuser = "delete from readers where Reader_Number="+str(delete_number)
            mycursor.execute(insertuser)
            mydb.commit()
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
            
            messagebox.showinfo('Success',"deleted successfully")
            
        except:
            messagebox.showinfo("Error","Can't delete data from Database")
    else:
        messagebox.showinfo("Error","Either reader number is invalid or books not returned issued")
    root.destroy()
     
      
    
    
def deleteReader():
    global deleteinfo1 , con, cur, UserTable, root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=700,height=700)
    root.geometry("800x700")


    

    con = mysql.connector.connect( host="localhost",user="root",password="root",database="Library")
    cur = con.cursor()

    # Enter Table Names here
    UserTable = "issue" # Book Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="black")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="red",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="DELETE Reader", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    #book ID
    lb1 = Label(labelFrame,text="Reader ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    deleteinfo1 = Entry(labelFrame)
    deleteinfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=deleteregister1)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black',command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
    


def bookRegister():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="Library"
    )
    mycursor = mydb.cursor()

    Book_number = bookInfo1.get()
    Book_name = bookInfo2.get()
    author = bookInfo3.get()
    status=bookInfo4.get()
    
    
    insertBooks = "insert into books"+" values ("+str(Book_number)+",'"+Book_name+"','"+author+"','"+status+"')"
    try:
        mycursor.execute(insertBooks)
        mydb.commit()
        messagebox.showinfo('Success',"Book added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
   
    
    root.destroy()
def addBook(): 
    
    global bookInfo1 ,bookInfo2, bookInfo3,bookInfo4, Canvas1, con, cur, bookTable, root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=700,height=700)
    root.geometry("900x750")


    mypass = "root"
    mydatabase="db"

    con = mysql.connector.connect( host="localhost",user="root",password="root",database="Library")
    cur = con.cursor()
    mycursor = mydb.cursor()
    mycursor.execute("Select MAX(Book_Number) from books")
    a=mycursor.fetchall()
    mydb.commit()
    if(a[0][0]==None):
        y=100+1
    else:
        y=a[0][0]+1
    
    x="Book number(Set as: "+str(y)+")"
    # Enter Table Names here
    bookTable = "books" # Book Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="black")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="red",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
    
        
    # Book ID
    lb1 = Label(labelFrame,text=x, bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Book_name
    lb2 = Label(labelFrame,text="Title : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    # Book Author
    lb3 = Label(labelFrame,text="Author : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)

    # Book Ststus
    lb4 = Label(labelFrame,text="Status(Default=avail) : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
        
                            
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=bookRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black',       command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
    

def View():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="Library"
    )
    mycursor = mydb.cursor()

    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("700x600")

    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#0FE9BD")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="black",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Books", bg='cyan', fg='black', font = ('Courier',20))

    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg='grey')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25

    Label(labelFrame, text="%-10s%-15s%-15s%-10s"%('ID',' NAME','Author','Status'),
    bg='grey',fg='white',font = ('Courier',10,'bold')).place(relx=0.07,rely=0.1)
    Label(labelFrame, text = "------------------------------------------------------------------------------------------------------",bg='grey',fg='white').place (relx=0.05,rely=0.2)
    getBooks = "select * from books"
    try:
        mycursor.execute(getBooks)
    


        for i in mycursor:
            Label(labelFrame,text="%-10s%-15s%-15s%-10s"%(i[0],i[1],i[2],i[3]) ,bg='grey', fg='white',font = ('Courier',10,'bold')).place(relx=0.07,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
    quitBtn = Button(root,text="Quit",bg='#FF5733', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
    
    
def returnRegister():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="Library"
    )
    mycursor = mydb.cursor()

    returnbook_number = returninfo1.get()
    returnuser_number = returninfo2.get()
    
    
    x="select count(Book_Number) from issue where Book_Number="+str(returnbook_number)+" and Reader_Number="+str(returnuser_number)
    mycursor.execute(x)
    a=mycursor.fetchall()
    y=a[0][0]


    if(y==1 ):
        returnuser = "Update  readers set issued_books=issued_books -1 where reader_number="+str(returnuser_number)
        mycursor.execute(returnuser)
        mydb.commit()
        returnuser = "Update  books set status='avail' where book_number="+str(returnbook_number)
        mycursor.execute(returnuser)
        mydb.commit()
        insertuser="Select Reader_mail from Readers where Reader_number="+str(returnuser_number)
        mycursor.execute(insertuser)
        a=mycursor.fetchall()
        receiver_email =a[0][0]
        
        mydb.commit()

        Subject="BOOK Returned"
        text = " Dear Reader \n This message is sent from Chandigarh University Library."
        text+="\n"
        text+="The issued book has been returned by You\n"+"BOOK Number: "+str(returnbook_number)+"\n \n THANK YOU!"

        message = 'Subject: {}\n\n{}'.format(Subject,text)
        
        
        try:
            returnuser = "Delete from issue where Book_Number=" + str(returnbook_number)
            mycursor.execute(returnuser)
            mydb.commit()

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
            
            messagebox.showinfo('Success',"returned successfully")
        except:
            messagebox.showinfo("Error","Cant return book from Database")
    else:
        messagebox.showinfo("Error","Either book name is invalid or already returned")
    root.destroy()

    
def returnBook(): 
    
    global returninfo1 , returninfo2, Canvas1, con, cur, UserTable, root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=700,height=700)
    root.geometry("900x750")


    

    con = mysql.connector.connect( host="localhost",user="root",password="root",database="Library")
    cur = con.cursor()

    # Enter Table Names here
    UserTable = "issue" # Book Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="black")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="red",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="return Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    #book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    returninfo1 = Entry(labelFrame)
    returninfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # reader_ID
    lb2 = Label(labelFrame,text="Reader ID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    returninfo2 = Entry(labelFrame)
    returninfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)

    

                      
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=returnRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black',command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

def searchregister():
    searchbook_number = returninfo1.get()
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="Library"
    )
    mycursor = mydb.cursor()

    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("900x750")

    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#0FE9BD")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="black",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Searched Books", bg='cyan', fg='black', font = ('Courier',17))

    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg='grey')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25

    Label(labelFrame, text="%-10s%-15s%-15s%-10s"%('ID',' NAME','Author','Status'),
    bg='grey',fg='white',font = ('Courier',10,'bold')).place(relx=0.07,rely=0.1)
    Label(labelFrame, text = "-------------------------------------------------------------------------------------------------------------------------------------",bg='grey',fg='white').place (relx=0.05,rely=0.2)
    getBooks = "select * from books where Book_name like'%"+searchbook_number+"%'" +"or Book_name like'"+searchbook_number+"%'"+"or Book_name like'%"+searchbook_number+"'"
    try:
        mycursor.execute(getBooks)
    


        for i in mycursor:
            Label(labelFrame,text="%-10s%-15s%-15s%-10s"%(i[0],i[1],i[2],i[3]) ,bg='grey', fg='white',font = ('Courier',10,'bold')).place(relx=0.07,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
    quitBtn = Button(root,text="Quit",bg='#FF5733', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
    root.destroy()
    
def search():
    
    global returninfo1 ,  Canvas1, con, cur, UserTable, root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=700,height=700)
    root.geometry("900x750")


    

    con = mysql.connector.connect( host="localhost",user="root",password="root",database="Library")
    cur = con.cursor()

    # Enter Table Names here
    UserTable = "issue" # Book Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="black")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="red",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="search Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    #book ID
    lb1 = Label(labelFrame,text="Book name : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    returninfo1 = Entry(labelFrame)
    returninfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    
                      
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=searchregister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black',command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
    root.destroy()
    
def searchregister1():
    searchreader_number = returninfo1.get()
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="Library"
    )
    mycursor = mydb.cursor()

    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("850x700")

    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#0FE9BD")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="black",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.4,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Searched Reader", bg='cyan', fg='black', font = ('Courier',20))

    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg='grey')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25

    Label(labelFrame, text="%-10s%-15s%-15s"%('ID',' NAME','Book count'),
    bg='grey',fg='white',font = ('Courier',15,'bold')).place(relx=0.07,rely=0.1)
    Label(labelFrame, text = "-----------------------------------------------------------------------------------------------------------------------------------------------------------",bg='grey',fg='white').place (relx=0.05,rely=0.2)
    getBooks = "select * from readers where Reader_number="+str(searchreader_number)
    try:
        mycursor.execute(getBooks)
    


        for i in mycursor:
            Label(labelFrame,text="%-10s%-20s%-20s"%(i[0],i[1],i[3]) ,bg='grey', fg='white',font = ('Courier',15,'bold')).place(relx=0.07,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
    quitBtn = Button(root,text="Quit",bg='#FF5733', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
    root.destroy()
    
def searchReader():
    
    global returninfo1 ,  Canvas1, con, cur, UserTable, root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=600,height=600)
    root.geometry("900x750")


    

    con = mysql.connector.connect( host="localhost",user="root",password="root",database="Library")
    cur = con.cursor()

    # Enter Table Names here
    UserTable = "issue" # Book Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="black")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="red",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="search Reader", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    #book ID
    lb1 = Label(labelFrame,text="Reader Number : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    returninfo1 = Entry(labelFrame)
    returninfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    
                      
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=searchregister1)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black',command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
    root.destroy()




def readerRegister():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="Library"
    )
    mycursor = mydb.cursor()

    user_number = userinfo1.get()
    user_name = userinfo2.get()
    mail = userinfo3.get()
    
    issued = userinfo4.get()
    receiver_email = mail
    Subject="Registration In library mangment system"
    
    Subject="Registration In library mangment system"
    text = " Hi "
    
    text+="there \n This message is sent from Chandigarh University Library."
    text+="\nYou have been succesfully registered in Chandigarh university Library \n\n Your Details are: "
    text+="\n   USER NUMBER: " + str(user_number)+"\n   USER NAME: "+user_name+"\n  MAIL ID: "+mail 
    
    
    message = 'Subject: {}\n\n{}'.format(Subject,text)
    
    insertuser = "insert into readers"+" values ("+str(user_number)+",'"+user_name+"','"+mail+"',"+str(issued)+")"
    try:
        mycursor.execute(insertuser)
        mydb.commit()
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        messagebox.showinfo('Success',"Reader added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    
    
    root.destroy()
def Add_reader(): 
    
    global userinfo1 ,userinfo2, userinfo3,userinfo4, Canvas1, con, cur, UserTable, root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=700,height=700)
    root.geometry("950x750")


    mypass = "root"
    mydatabase="db"

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="Library"
    )
    mycursor = mydb.cursor()
    mycursor.execute("Select MAX(Reader_Number) from readers")
    a=mycursor.fetchall()
    mydb.commit()
    if(a[0][0]==None):
        y=1000+1
    else:
        y=a[0][0]+1
  
    x="Reader number(Set as: "+str(y)+")"
    # Enter Table Names here
    UserTable = "readers" # Book Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="black")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="red",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Reader", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # reader ID
    lb1 = Label(labelFrame,text=x, bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    userinfo1 = Entry(labelFrame)
    userinfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # reader_name
    lb2 = Label(labelFrame,text="Name : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    userinfo2 = Entry(labelFrame)
    userinfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    # user Mail
    lb3 = Label(labelFrame,text="Mail : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    userinfo3 = Entry(labelFrame)
    userinfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)

    # USER Count of books
    lb4 = Label(labelFrame,text="COUNT(Default=0) : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    userinfo4 = Entry(labelFrame)
    userinfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
        
                            
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=readerRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black',       command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

def issueRegister():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="Library"
    )
    mycursor = mydb.cursor()

    issuebook_number = issueinfo1.get()
    issueuser_number = issueinfo2.get()
    date = issueinfo3.get()
    
    x="select count(Book_Number) from books where Book_Number="+str(issuebook_number)+" and status='avail'"
    mycursor.execute(x)
    a=mycursor.fetchall()
    y=a[0][0]

    x="select count(Reader_Number) from readers where Reader_Number="+str(issueuser_number)
    mycursor.execute(x)
    a=mycursor.fetchall()
    z=a[0][0]

    

    

    if(y==1 and z==1):
        insertuser = "Update  readers set issued_books=issued_books +1 where reader_number="+str(issueuser_number)
        mycursor.execute(insertuser)
        mydb.commit()
        insertuser = "Update  books set status='booked' where book_number="+str(issuebook_number)
        mycursor.execute(insertuser)
        mydb.commit()

        insertuser="Select Reader_mail from Readers where Reader_number="+str(issueuser_number)
        mycursor.execute(insertuser)
        a=mycursor.fetchall()
        receiver_email =a[0][0]
        
        mydb.commit()

        Subject="BOOK ISSUED"
        text = " Hi there \n This message is sent from Chandigarh University Library."
        text+="\n"
        text+="A book has been issued on your name\n"+"BOOK Number: "+str(issuebook_number)+"\n Date(YYYYMMDD): "+str(date)+"\n You must submit the book in 15 days\n THANK YOU!"

        message = 'Subject: {}\n\n{}'.format(Subject,text)
            
        try:
            insertuser = "insert into issue"+" values ("+str(issuebook_number)+","+str(issueuser_number)+","+str(date)+")"
            mycursor.execute(insertuser)
            mydb.commit()

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)

            
            messagebox.showinfo('Success',"issue added successfully")
        except:
            messagebox.showinfo("Error","Can't add data into Database")
    else:
        messagebox.showinfo("Error","Either book name is invalid or already issued")
        
    
    
    
    
    
    
    
    
    
    root.destroy()
def issueBook(): 
    
    global issueinfo1 ,issueinfo2, issueinfo3, Canvas1, con, cur, UserTable, root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=700,height=700)
    root.geometry("900x750")


    

    con = mysql.connector.connect( host="localhost",user="root",password="root",database="Library")
    cur = con.cursor()

    # Enter Table Names here
    UserTable = "issue" # Book Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="black")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="red",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    #book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    issueinfo1 = Entry(labelFrame)
    issueinfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # reader_ID
    lb2 = Label(labelFrame,text="Reader ID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    issueinfo2 = Entry(labelFrame)
    issueinfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)

    # Date of issue
    lb3 = Label(labelFrame,text="date(YYYYMMDD) : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.5, relheight=0.08)
        
    issueinfo3 = Entry(labelFrame)
    issueinfo3.place(relx=0.3,rely=0.5, relwidth=0.62, relheight=0.08)

    
        
        
    
    
        
                            
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=issueRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black',command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
    
def help1():
    GUI_P_1.addquery()
    


def loginRegister():
    
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="Library"
    )
    mycursor = mydb.cursor()
    c=0
    User_id = logininfo1.get()
    User_id=User_id.lower()
    user_pwd = logininfo2.get()
    mycursor.execute("Select * from user")
    data=mycursor.fetchall()
    co=mycursor.rowcount
    ID=[]
    paswd=[]
    for row in data:
        ID.append(row[0])
        paswd.append(row[1])
    for i in range (0,len(ID)):
        
        if ((User_id==ID[i].lower()) and (user_pwd==paswd[i])):
            c+=1
    if(c!=0):
        
        
        root = Tk()
        root.title("Library")
        root.minsize(width=700,height=700)
        root.geometry("1750x830")


        

        con = mysql.connector.connect( host="localhost",user="root",password="root",database="Library")
        cur = con.cursor()

        # Enter Table Names here
        UserTable = "issue" # Book Table

        Canvas1 = Canvas(root)
        
        
        Canvas1.config(bg="black")
        Canvas1.pack(expand=True,fill=BOTH)
            
        headingFrame1 = Frame(root,bg="red",bd=5)
        headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

        headingLabel = Label(headingFrame1, text="      WELCOME TO \nCHANDIGARH UNIVERSITY LIBRARY", bg='black', fg='white', font=('Courier',17))
        headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


        labelFrame = Frame(root,bg='black')
        labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    # adding buttons
        btn1 = Button(root,text="Add Book Details",bg='black', fg='white',font=('Courier',20), command=addBook)
        btn1.place(relx=0.01,rely=0.34, relwidth=0.35,relheight=0.1)
            
        btn2 = Button(root,text="Delete Book",bg='black', fg='white',font=('Courier',20), command=delete)
        btn2.place(relx=0.63,rely=0.34, relwidth=0.35,relheight=0.1)
            
        btn3 = Button(root,text="View Book List",bg='black', fg='white',font=('Courier',20), command=View)
        btn3.place(relx=0.01,rely=0.47,relwidth=0.35,relheight=0.1)
            
        btn4 = Button(root,text="Issue Book to Student",bg='black', fg='white',font=('Courier',20), command = issueBook)
        btn4.place(relx=0.63,rely=0.47, relwidth=0.35,relheight=0.1)
            
        btn5 = Button(root,text="Return Book",bg='black', fg='white',font=('Courier',20), command = returnBook)
        btn5.place(relx=0.01,rely=0.59, relwidth=0.35,relheight=0.1)

        btn5 = Button(root,text="Add reader",bg='black', fg='white',font=('Courier',20), command = Add_reader)
        btn5.place(relx=0.63,rely=0.59, relwidth=0.35,relheight=0.1)

        btn6 = Button(root,text="Search book",bg='black', fg='white',font=('Courier',20), command = search)
        btn6.place(relx=0.01,rely=0.71, relwidth=0.35,relheight=0.1)

       
        
        btn8 = Button(root,text="Search Reader",bg='black', fg='white', font=('Courier',20),command = searchReader)
        btn8.place(relx=0.63,rely=0.71, relwidth=0.35,relheight=0.1)
        
        btn9 = Button(root,text="Delete Reader",bg='black', fg='white', font=('Courier',20),command = deleteReader
                      )
        btn9.place(relx=0.01,rely=0.83, relwidth=0.35,relheight=0.1)
        
        btn10 = Button(root,text="QUIT",bg='black', fg='white', font=('Courier',20),command = root.destroy)
        btn10.place(relx=0.63,rely=0.83, relwidth=0.35,relheight=0.1)
        
        btn7 = Button(root,text="Help ? ",bg='black', fg='white',font=('Courier',20), command =help1 )
        btn7.place(relx=0.87,rely=0.13, relwidth=0.11,relheight=0.1)
        
        
    
    

    
            
    else:
        messagebox.showinfo('showinfo',"LOGIN FAILED ")
        root.destroy()

            
    
    
    
    
       
    
    
def login():
    
    global logininfo1 ,logininfo2, Canvas1, con, cur, UserTable, root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=700,height=700)
    root.geometry("900x750")


    

    con = mysql.connector.connect( host="localhost",user="root",password="root",database="Library")
    cur = con.cursor()

    # Enter Table Names here
    UserTable = "issue" # Book Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="black")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="red",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="LOGIN", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    #book ID
    lb1 = Label(labelFrame,text="USER ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    logininfo1 = Entry(labelFrame)
    logininfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    
    lb2 = Label(labelFrame,text="Password : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    logininfo2 = Entry(labelFrame)
    logininfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)

    

    
        
        
    
    
        
                            
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=lambda:[loginRegister(),root.destroy()])
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black',command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
    root.destroy()
   

def UserRegister():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="Library"
    )
    mycursor = mydb.cursor()

    user_id = userinfo1.get()
    pwd = userinfo2.get()
    
        
    try:
        insertuser = "insert into user"+" values ('"+user_id+"','" + pwd+"')"
        mycursor.execute(insertuser)
        mydb.commit()
        
        messagebox.showinfo('Success',"USER details added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
        
        
    
    
    
    
    
    
    
    
    
    root.destroy()
def Create_user(): 
    
    global userinfo1 ,userinfo2, Canvas1, con, cur, UserTable, root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=700,height=700)
    root.geometry("800x700")


    

    con = mysql.connector.connect( host="localhost",user="root",password="root",database="Library")
    cur = con.cursor()

    # Enter Table Names here
    UserTable = "" # Book Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="black")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="red",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="ADD USER", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    #book ID
    lb1 = Label(labelFrame,text="USERID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    userinfo1 = Entry(labelFrame)
    userinfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # reader_ID
    lb2 = Label(labelFrame,text="Password : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    userinfo2 = Entry(labelFrame)
    userinfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
            
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=UserRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black',command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
    
    

    


# adding buttons
btn1 = Button(root,text="LOGIN",bg='black', fg='white', command=login)
btn1.place(relx=0.35,rely=0.49, relwidth=0.35,relheight=0.1)
    

    
btn3 = Button(root,text="Create USER",bg='black', fg='white', command=Create_user)
btn3.place(relx=0.35,rely=0.62,relwidth=0.35,relheight=0.1)
    

btn5 = Button(root,text="QUIT",bg='black', fg='white', command = root.destroy)
btn5.place(relx=0.35,rely=0.74, relwidth=0.35,relheight=0.1)


root.mainloop()
mydb.commit()

