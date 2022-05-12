import smtplib
from tkinter import *
 
f=('Times','14')

def send_message():
    
    address_info = address.get()
    
    email_body_info = email_body.get()
    
    print(address_info,email_body_info)
    
    sender_email = "tkinteremail@gmail.com"
    
    sender_password = "w9D5rynb"
    
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
 
button = Button(app,text="Send Message",command=send_message,width="30",height="2",bg="#000000",fg='#b8860b',bd=0)
 
button.place(x=15,y=220)
 
 
mainloop()