from tkinter import*
from PIL import Image,ImageTk
import random
import sys

import os
sys.path.insert(1,"C:\\Users\\DELL\\Desktop\\TkProject\\1")
window = Tk()
window.geometry("1000x500")
window.title("Forgot password")
window.resizable(False,False)


#Photo insert
img0= PhotoImage(file="signup.png")
label1=Label(window, image= img0)
label1.pack(fill=X)

frame=Frame(window,width=300,height=300,bg='white')
frame.place(x=140,y=100)

label=Label(frame,text="Reset Password",fg="Red",bg="white",font=('Gabriola','20','bold'))
label.place(x=95,y=0)

#return to loging page
def openlogin():
   window.destroy()
   import login


#functoion for email
def enter(event):
    email.delete(0,'end')
    
def leave(event):
    a=email.get()
    if a=='':
      email.insert(0,'Enter Your Email')
email=Entry(frame,text="Enter Your Email",width=30,border=0,fg='black',bg='white',font=("Comic Sans Ms", 10, "bold"))
email.place(x=90,y=50)

z=Frame(frame,width=220,height=2,bg='black')
z.place(x=60,y=70)  
     
email.insert(1,'Enter Your Email')
email.bind('<FocusIn>',enter)
email.bind('<FocusOut>',leave)

#New Password

def enter(event):
    newpassword.delete(0,'end')
    
def leave(event):
    a=newpassword.get()
    if a=='':
      newpassword.insert(0,'New Password')
newpassword=Entry(frame,text="New Password",width=30,border=0,fg='black',bg='white',font=("Comic Sans Ms", 10, "bold"),show='*')
newpassword.place(x=100,y=105)


y=Frame(frame,width=180,height=2,bg='black')
y.place(x=60,y=130)  
     
newpassword.insert(1,'New Password')
newpassword.bind('<FocusIn>',enter)
newpassword.bind('<FocusOut>',leave)


#Re-password

def enter(event):
    Confirmpassword.delete(0,'end')
    
def leave(event):
    a=Confirmpassword.get()
    if a=='':
        Confirmpassword.insert(0,'New Password')


Confirmpassword=Entry(frame,text="Confirm Password",width=30,border=0,fg='black',bg='white',font=("Comic Sans Ms", 10, "bold"),show="*")
Confirmpassword.place(x=95,y=165)

z=Frame(frame,width=180,height=2,bg='black')
z.place(x=60,y=185)  
   
Confirmpassword.insert(2,"Confirm Password")
Confirmpassword.bind('<FocusIn>',enter) 
Confirmpassword.bind('<FocusOut>',leave)  


#show password functionalities for passwords
def show():
        if showw.get()==1:
            newpassword.config(show="")
        else:
            newpassword.config(show='*')


showw=IntVar()
b1=Checkbutton(frame,text="Show",bg='white',fg='black',border=0,onvalue=1,variable=showw,offvalue=0, command=show)
b1.place(x=240,y=105)

def show2():
        
        if showww.get()==1:
            Confirmpassword.config(show='')
        else:
            Confirmpassword.config(show='*')
            
 
showww=IntVar()
b2=Checkbutton(frame,text="Show",bg='white',fg='black',border=0,onvalue=1,variable=showww,offvalue=0, command=show2)
b2.place(x=240,y=165)
    


#security questions
def enter(event):
    questions.delete(0,'end')
    
def leave(event):
    a=questions.get()
    if a=='':
      questions.insert(0,'What is your favourite food?')
questions=Entry(frame,text="What is your favourite food?",width=30,border=0,fg='black',bg='white',font=("Comic Sans Ms", 10, "bold"))
questions.place(x=65,y=220)

q=Frame(frame,width=210,height=2,bg='black')
q.place(x=60,y=240)  
     
questions.insert(1,'What is your favourite food?')
questions.bind('<FocusIn>',enter)
questions.bind('<FocusOut>',leave)


# def hide():
#     print('Hide')
#     openeye.config(file='eye1.png')
#     confirmpassword.config(show='*')
#     eyebutton.config(command=show)
    
# def show():
#     openeye.config(file='eye.png')
#     Password.config(show='')
#     eyebutton.config(command=hide)

# openeye= PhotoImage(file='eye1.png')
# eyebutton=Button(frame,image=openeye,bg='white',fg='white',border=0,command=show)
# eyebutton.place(x=235,y=122)


sign = Button(frame,text="Confirm",bg='white',fg='green',border=0,command=lambda:openlogin())
sign.place(x=125,y=260)


window.mainloop()