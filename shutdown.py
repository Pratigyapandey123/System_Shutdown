from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")

def restart_time():
    os.system("shutdown /r /t 20")

def logout():
    os.system("shutdown -l")

def shutdown():
    os.system("shutdown /s /t 1")

st = Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.config(bg="Blue")

rButton = Button(st,text="Restart",font=("Time New Roman",20,"bold"),
                 relief=RAISED, cursor="plus",command=restart)
rButton.place(x=150,y=60,height=50,width=200)

rt_Button = Button(st,text="Restart Time",font=("Time New Roman",20,"bold"),
                   relief=RAISED, cursor="plus",command=restart_time)
rt_Button.place(x=150,y=170,height=50,width=200)

l_Button = Button(st,text="Log-Out",font=("Time New Roman",20,"bold"),
                  relief=RAISED, cursor="plus",command=logout)
l_Button.place(x=150,y=270,height=50,width=200)

s_Button = Button(st,text="Shut Down",font=("Time New Roman",20,"bold"),
                  relief=RAISED, cursor="plus",command=shutdown)
s_Button.place(x=150,y=370,height=50,width=200)




st.mainloop()
