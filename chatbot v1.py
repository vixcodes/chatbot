#vixcodes
#simple chatbot

#pip install tkinter

from tkinter import *
root = Tk()
root.title("Chatbot")

def send():
    send = "You -> "+e.get()
    txt.insert(END, "\n"+send)
    user = e.get().lower()
    if(user == "hello"):
        txt.insert(END, "\n" + "Bot -> Hi")
    elif(user == "hi" or user == "hii" or user == "hey"):
        txt.insert(END, "\n" + "Bot -> Hello")
    elif(e.get() == "how are you"):
        txt.insert(END, "\n" + "Bot -> Good. And you?")
    elif(user == "good" or user == "ok" or user == "fine"):
        txt.insert(END, "\n" + "Bot -> Great! How can I help you?")
    else:
        txt.insert(END, "\n" + "Bot -> Sorry! I didn't get you")
    e.delete(0, END)

txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)
e = Entry(root, width=100)
e.grid(row=1, column=0)
send = Button(root, text="Send", command=send).grid(row=1, column=1)
root.mainloop()
