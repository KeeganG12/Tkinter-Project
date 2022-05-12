from tkinter import *
from tkinter import messagebox
import sqlite3

def nextPage():
    ws.destroy()
    import Email

f = ('Times', 14,)


con = sqlite3.connect('userdata.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS record(
                    name text, 
                    email text, 
                    contact number, 
                    gender text, 
                    country text,
                    password text
                )
            ''')
con.commit()

           

ws = Tk()
ws.title('Login Page')
ws.geometry('400x300')
ws.config(bg='#000000')
ws.iconbitmap('images.png')
    

def login_response():
    try:
        con = sqlite3.connect('userdata.db')
        c = con.cursor()
        for row in c.execute("Select * from record"):
            username = row[1]
            pwd = row[5]
        
    except Exception as ep:
        messagebox.showerror('', ep)

    uname = email_tf.get()
    upwd = pwd_tf.get()
    check_counter=0
    if uname == "":
       warn = "Username can't be empty"
    else:
        check_counter += 1
    if upwd == "":
        warn = "Password can't be empty"
    else:
        check_counter += 1
    if check_counter == 2:
        if (uname == username and upwd == pwd):
            messagebox.showinfo('Login Status', 'Logged in Successfully!')
        
        else:
            messagebox.showerror('Login Status', 'invalid username or password')
    else:
        messagebox.showerror('', warn)

#Variables 
var = StringVar()
var.set('male')

countries = []
variable = StringVar()
world = open('countries.txt', 'r')
for country in world:
    country = country.rstrip('\n')
    countries.append(country)
variable.set(countries[22])

# widgets
exit_button = Button(ws, text="Exit", command=ws.destroy,bg='#FF0000')
exit_button.pack(pady=0,padx=0)

left_frame = Frame(
    ws, 
    bd=2, 
    bg='#000000',   
    relief=SOLID, 
    padx=10, 
    pady=10, 
    borderwidth = 0
    )

Label(
    left_frame, 
    text="Enter Email",
    borderwidth = 0, 
    bg='#000000',fg='#b8860b',
    font=f).grid(row=0, column=0, sticky=W, pady=10)

Label(
    left_frame, 
    text="Enter Password", 
    bg='#000000',
    font=f,fg='#b8860b'
    ).grid(row=1, column=0, pady=10)

email_tf = Entry(
    left_frame, 
    font=f,
    bd=1,bg='#f8f8ff'
    )
pwd_tf = Entry(
    left_frame, 
    font=f,
    show='*',
    bd=1,bg='#f8f8ff'
    )
login_btn = Button(
    left_frame, 
    width=15, 
    text='Login', 
    font=f, 
    relief=SOLID,
    cursor='hand2',
    command=nextPage,
    bd=0,
    bg='#000000',fg='#b8860b'
    )

transporter = Button(
    left_frame,
    width=15, 
    text='Login', 
    font=f, 
    relief=SOLID,
    command=nextPage,
    bd=0,
    bg='#000000',fg='#b8860b'
)




# widgets placement
email_tf.grid(row=0, column=1, pady=10, padx=20)
pwd_tf.grid(row=1, column=1, pady=10, padx=20)
login_btn.grid(row=2, column=1, pady=10, padx=20)
left_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
exit_button.place(x=0,y=0)


# infinite loop
ws.mainloop()