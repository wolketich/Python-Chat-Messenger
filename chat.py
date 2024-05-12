import socket
import threading
from tkinter import messagebox
import rsa

import tkinter as tk
from enc import *

main()

def Connection():
    global connect_windo
    connect_windo = tk.Tk()
    connect_windo.geometry('350x250')
    connect_windo.title('Establishing connection..')
    # creating a label for
    # name using widget label
    tk.Label(text='1.Host \n2.Connect').grid(row=0,column=0)
    global choice_label
    global choiceVar
    choiceVar = tk.StringVar()
    global RemotIP
    RemotIP = tk.StringVar()
    remotlabel = tk.Label(connect_windo,text='Enter Remote ip', font=('calibre',10, 'bold'))
    choice_label = tk.Label(connect_windo, text='Choice: ', font=('calibre',10, 'bold'))
    # creating a entry for input
    # name using widget Entry
    global remotentry
    remotentry = tk.Entry(connect_windo,textvariable=RemotIP, font=('calibre', 10, 'normal'))
    remotlabel.grid(row=1, column=0)
    remotentry.grid(row=1, column=1)

    global choice_Entry
    choice_Entry = tk.Entry(connect_windo, textvariable=choiceVar, font=('calibre', 10, 'normal'))
    # startImage = tk.PhotoImage(file='st.png')
    choice_label.grid(row=2, column=0)
    choice_Entry.grid(row=2, column=1)
    #binding enter
    connect_windo.bind('<Return>', lambda event=None: StartSystem())
    sub_btn = tk.Button(connect_windo, text="Submit",command=StartSystem,padx=70)
    sub_btn.grid(row=4, column=1)
    connect_windo.mainloop()

def StartSystem():
    choice=choiceVar.get()
    choiceVar.set("")
    remot = RemotIP.get()
    if choice == "1":
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("192.168.56.1", 9999))
        server.listen()

        client, _ =server.accept()
    elif choice == "2":
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((remot, 9999))
    else:
        exit()

    threading.Thread(target=sending_msg, args=(client,)).start()
    threading.Thread(target=receiving_msg, args=(client,)).start()
    messagebox.showinfo(message="Connection Successfull !!!")
    connect_windo.destroy()

def sending_msg(c):
    global b
    b = c

def receiving_msg(c):
    while True:
        # print("Friend: "+c.recv(1024).decode())
        msg =  c.recv(1024).decode()
        frndmessages.append(msg)
        frndmessages.config(text=msg)

Connection()
root=tk.Tk()

# setting window size
root.geometry("600x400")
root.title('WeChat()-New Window')
# image = tk.PhotoImage(file='logo.png')
# root.iconphoto(False,image)

def send_Msg():
    msg = msgVar.get()
    print("You: "+msg)
    mymsg.append(msg)
    Mymsgdisp.config(text=msg)
    b.send(msg.encode())
    msgVar.set("")

# creating label for password

msglabel = tk.Label(root, text = 'Message: ', font=('calibre',10,'bold'))
msgVar = tk.StringVar()

# entry for password

msgEntry=tk.Entry(root, textvariable=msgVar, font=('calibre',10,'normal'))
Mymsg = tk.Label(root,text='You: ',font='calibre 10 bold')
Mymsgdisp = tk.Label(root,text='',font='calibre 10 bold')

frndmsg = tk.Label(root,text='Friend: ', font='calibre 10 bold')
frndmsgdisp = tk.Label(root,text='', font='calibre 10 bold')

msglabel.grid(row=1,column=0)
msgEntry.grid(row=1,column=1)
Mymsg.grid(row=2,column=0)
Mymsgdisp.grid(row=2,column=1)
frndmsg.grid(row=3,column=0)
frndmsgdisp.grid(row=3,column=1)
root.bind('<Return>', lambda event=None: send_Msg())
# sendImage = tk.PhotoImage(file='sendmsg.png')
Send_Msg=tk.Button(root,text= 'Send', command = send_Msg,padx=70).grid(row=5,column=1)

root.mainloop()
