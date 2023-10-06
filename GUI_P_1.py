import pyttsx3
from tkinter import *
import tkinter as tk
import webbrowser
from PIL import ImageTk,Image #PIL -> Pillow
from tkinter import messagebox
same=True
n=0.55
import datetime
import wikipedia
import webbrowser

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





def Show_Image(path):
    plt.rcParams["figure.figsize"] = [10, 10]
    plt.rcParams["figure.autolayout"] = True


    im = plt.imread(path)


    fig, ax = plt.subplots()
    ax.set_facecolor("black")
    im = ax.imshow(im, extent=[-35, 70, 8, 60])


    x = np.array(range(58))
    #manager = plt.get_current_fig_manager()
    #manager.full_screen_toggle()
    plt.axis("off")
    plt.show(block=False)
    plt.pause(3) # 3 seconds, I use 1 usually


    plt.close()




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def queryRegister():

    query = queryInfo1.get()
    if 'wikipedia' in query:
        speak('Searching in Wikipedia..')
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences = 2)
        speak("acoording to wikipedia")
        print(results)
        speak(results)




    elif ("CLMS" or "interface" or "clms") in query:
        speak("this is of Chandigarh Library management system or CLMS")
        Show_Image("4.jpeg")
        root.geometry("1200x1200")


    elif 'add book' in query:
        speak("Firstly you have to click on add book option")
        speak("Then fill the details in these box and press okay button")
        speak("Here are some image for help.")
        Show_Image("4.jpeg")
        time.sleep(1)
        Show_Image("proj3.JPG")
        speak("After adding details we get this dialogue box to be appear for confirmation")
        Show_Image("proj4.JPG")
        root.geometry("1200x1200")



    elif 'view book list' in query:
        speak("just click on this option to see the book list")
        Show_Image("proj1_2.JPG")
        time.sleep(1)
        Show_Image("proj3.JPG")
        time.sleep(1)
        Show_Image("proj5.JPG")
        root.geometry("1200x1200")

    elif 'add user' in query:
        speak("Click add user in the library management system to add user then press submit button.")
        Show_Image("4.jpeg")
        time.sleep(1)
        Show_Image("proj5.JPG")
        root.geometry("1200x1200")


    elif 'Login' in query:
        speak("You have to either give the username and password or create a new user in that")
        Show_Image("proj1.JPG")
        time.sleep(1)
        Show_Image("proj2.JPG")

    elif "issue book" in query:
        speak("You have to fill the details in this box")
        Show_Image("PROJ6.JPG")
        time.sleep(1)
        speak("then after filling this a dialogue box appears fro confirmation")
        Show_Image("PROJ7.JPG")
        root.geometry("1200x1200")


    elif "return book" in query:
        speak("You have to fill the details for returning the book")
        Show_Image("PROJ8.JPG")
        time.sleep(1)
        speak("then after filling this a dialogue box appears fro confirmation")
        Show_Image("PROJ9.JPG")
        root.geometry("1200x1200")

    elif "add reader" in query:
        speak("here you have to fill the details for adding a reader")
        Show_Image("PROJ10.JPG")
        time.sleep(1)
        speak("then a dialogue box is appear for confirmation")
        Show_Image("PROJ11.JPG")

    elif "delete book" in query:
        speak("here you have to fill the details for deleting a book")
        Show_Image("PROJ10.JPG")
        time.sleep(1)
        speak("then a dialogue box is appear for confirmation")
        Show_Image("PROJ13.JPG")
        root.geometry("1200x1200")

    elif "search book" in query:
        speak("here you have to give the details for searching a book")
        Show_Image("PROJ14.JPG")
        time.sleep(1)
        speak("then it shows the searched book like this ")
        Show_Image("PROJ15.JPG")
        root.geometry("1200x1200")

    elif "search reader" in query:
        speak("you have to click on search reader option and fill the details")
        Show_Image("4.jpeg")
        time.sleep(1)
        Show_Image("3.jpeg")
        speak("After filling details it shows in searched reader list")
        Show_Image("2.jpeg")
        root.geometry("1200x1200")

    elif "delete reader" in query:
        speak("First select the delete reader option in  Chandigarh Library management system")
        Show_Image("4.jpeg")
        time.sleep(1)
        speak("Enter the Reader ID for deleting the reader")
        Show_Image("1.jpeg")
        root.geometry("1200x1200")



    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
        root.geometry("1200x1200")

    elif 'open facebook' in query:
        webbrowser.open("facebook.com")
        root.geometry("1200x1200")

    elif 'open gmail' in query:
        webbrowser.open("gmail.com")
        root.geometry("1200x1200")

    elif 'open google' in query:
        webbrowser.open("google.com")
        root.geometry("1200x1200")

    elif 'open online compiler' in query:
        webbrowser.open("onlinegd1b.com")
        root.geometry("1200x1200")




    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir! the time is  {strTime}")

        root.geometry("1200x1200")



def addquery():

    global queryInfo1 , Canvas1, con, cur, bookTable, root

    root = tk.Tk()
    root.geometry("1200x1200")
    root.configure(bg='black')





    labelFrame = Frame(root,bg="black")
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    chat = Label(root,text="CHATBOT FOR HELP!",bg="black",fg="red")
    chat.config(font = ("Courier",28))

    Suggestion = Text(root,height=10,width = 15)

    list = Label(root,text="FEW QUERIES FOR FRESIES")
    list.config(font = ("Courier",12))

    Question = """
    Try "CLMS" for view the CHANDIGARH LIBRARY MANAGEMENT SYSTEM
    Try "Login" for view the LOGIN-PAGE
    Try "add book" for viewing the process of adding the book
    """
    list.pack()
    list.place(relx=0.72,rely=0.45, relwidth=0.25, relheight=0.07)
    chat.pack()
    chat.place(relx=0.28,rely=0.029, relwidth=0.45, relheight=0.25)
    Suggestion.pack()
    Suggestion.place(relx=0.72,rely=0.5, relwidth=0.25, relheight=0.15)
    Suggestion.insert(tk.END,Question)


    lb1 = Label(labelFrame,text="ENTER YOUR QUERY : ", fg='black')
    lb1.place(relx=0.019,rely=0.3, relheight=0.08)

    queryInfo1 = Entry(labelFrame,bg='white')
    queryInfo1.place(relx=0.19,rely=0.3, relwidth=0.58, relheight=0.07)

    SubmitBtn = Button(root,text="SUBMIT",bg='black', fg='red',command=queryRegister)
    SubmitBtn.place(relx=0.25,rely=0.7, relwidth=0.12,relheight=0.08)



    quitBtn = Button(root,text="Quit",bg='black', fg='red',command=root.destroy)
    quitBtn.place(relx=0.59,rely=0.7, relwidth=0.12,relheight=0.08)
    root.mainloop()
    root.destroy()

