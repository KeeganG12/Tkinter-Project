
import smtplib
from tkinter import *
from tkinter import messagebox
def nextPage():
    app.destroy()
    import signin


f=('Times','14')
s=('Times','10', 'underline')


def warn1():
    messagebox.showerror('Error', 'Sign in First')

def send_message():
    
    address_info = address.get()
    
    email_body_info = email_body.get()
    
    print(address_info,email_body_info)
    
    sender_email = "***********"
    
    sender_password = "*********"
    
    server = smtplib.SMTP('smtp.gmail.com',587)
    
    server.starttls()
    
    server.login(sender_email,sender_password)
    
    print("Login successful")
    
    server.sendmail(sender_email,address_info,email_body_info)
    
    print("Message sent")
    
    address_entry.delete(0,END)
    email_body_entry.delete(0,END)
    
    
    
 
app = Tk()
 
app.geometry("300x300")

app.config(bg="#000000")
app.wm_attributes('-transparentcolor','#81f542')
app.title("Python Mail Send App")
 

 
address_field = Label(text="Recipient Address :",bg="#000000",fg='#b8860b')
email_body_field = Label(text="Message :",bg="#000000",fg='#b8860b')
 
address_field.place(x=15,y=70)
email_body_field.place(x=15,y=140)
 
address = StringVar()
email_body = StringVar()
 
 
address_entry = Entry(textvariable=address,width="30",bg="#f8f8ff",font=f,fg='#b8860b')
email_body_entry = Entry(textvariable=email_body,width="30",bg="#f8f8ff",font=f,fg='#b8860b')
 
address_entry.place(x=15,y=100)
email_body_entry.place(x=15,y=180)
 
button = Button(app,text="Send Message",command=warn1,width="30",height="2",bg="#f8f8ff",fg='#b8860b')
 
button.place(x=15,y=220)
 
signin1 = Button(app,text="Sign In",width="30",height="1",fg='#0096FF',font=s,bg='#000000',bd=0,command=nextPage)
signin1.place(x=15,y=270)
mainloop()