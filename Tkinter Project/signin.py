
from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import ImageTk, Image  


f = ('Times', 14,)
s=('Times','10', 'underline')

def nextPage():
    ws.destroy()
    import login2



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
ws.geometry('600x500')
ws.config(bg='#000000')
ws.iconbitmap('images.png')

#Check for Any Information Missing or Wrong
def insert_record():
    check_counter=0
    warn = ""
    if register_name.get() == "":
       warn = "Name can't be empty"
    else:
        check_counter += 1
        
    if register_email.get() == "":
        warn = "Email can't be empty"
    else:
        check_counter += 1

    if register_mobile.get() == "":
       warn = "Contact can't be empty"
    else:
        check_counter += 1
    
    if  var.get() == "":
        warn = "Select Gender"
    else:
        check_counter += 1

    if variable.get() == "":
       warn = "Select Country"
    else:
        check_counter += 1

    if register_pwd.get() == "":
        warn = "Password can't be empty"
    else:
        check_counter += 1

    if pwd_again.get() == "":
        warn = "Re-enter password can't be empty"
    else:
        check_counter += 1

    if register_pwd.get() != pwd_again.get():
        warn = "Passwords didn't match!"
    else:
        check_counter += 1

    if check_counter == 8:        
        try:
            con = sqlite3.connect('userdata.db')
            cur = con.cursor()
            cur.execute("INSERT INTO record VALUES (:name, :email, :contact, :gender, :country, :password)", {
                            'name': register_name.get(),
                            'email': register_email.get(),
                            'contact': register_mobile.get(),
                            'gender': var.get(),
                            'country': variable.get(),
                            'password': register_pwd.get()

            })
            con.commit()
            nextPage()


        except Exception as ep:
            messagebox.showerror('', ep) 
    else:
        messagebox.showerror('Error', warn)

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
    bd=0, 
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
    bg='#000000',
    fg='#b8860b',
    font=f).grid(row=0, column=0, sticky=W, pady=10)

Label(
    left_frame, 
    text="Enter Password", 
    bg='#000000',
    font=f,fg='#b8860b'
    ).grid(row=1, column=0, pady=10)

email_tf = Entry(
    left_frame, 
    font=f,fg='#b8860b'
    )
pwd_tf = Entry(
    left_frame, 
    font=f,fg='#b8860b',
    show='*'
    )
login_btn = Button(
    left_frame, 
    width=15, 
    text='Login', 
    font=f, 
    relief=SOLID,
    cursor='hand2',
    command=login_response,
    fg='#b8860b'
    )

right_frame = Frame(
    ws, 
    bd=0, 
    bg='#000000',
    relief=SOLID, 
    padx=10, 
    pady=10
    )

Label(
    right_frame, 
    text="Enter Name", 
    bg='#000000',
    font=f,fg='#b8860b'
    ).grid(row=0, column=0, sticky=W, pady=10)



Label(
    right_frame, 
    text="Enter Email", 
    bg='#000000',
    font=f,fg='#b8860b'
    ).grid(row=1, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Contact Number", 
    bg='#000000',
    font=f,fg='#b8860b'
    ).grid(row=2, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Select Gender", 
    bg='#000000',
    font=f,fg='#b8860b'
    ).grid(row=3, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Select Country", 
    bg='#000000',
    font=f,fg='#b8860b'
    ).grid(row=4, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Enter Password", 
    bg='#000000',
    font=f,fg='#b8860b'
    ).grid(row=5, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Re-Enter Password", 
    bg='#000000',
    font=f,fg='#b8860b'
    ).grid(row=6, column=0, sticky=W, pady=10)

gender_frame = LabelFrame(
    right_frame,
    bg='#000000',
    padx=10, 
    pady=10,
    bd=1,
    )


register_name = Entry(
    right_frame, 
    font=f,
    bd=1,
    )

register_email = Entry(
    right_frame, 
    font=f,
    bd=1,
    )

register_mobile = Entry(
    right_frame, 
    font=f,
    bd=1,
    )


male_rb = Radiobutton(
    gender_frame, 
    text='Male',
    bg='#000000',
    variable=var,
    value='male',
    font=('Times', 10),
    bd=0,fg='#b8860b'
    
)

female_rb = Radiobutton(
    gender_frame,
    text='Female',
    bg='#000000',
    variable=var,
    value='female',
    font=('Times', 10),
    bd=0,fg='#b8860b'
  
)

others_rb = Radiobutton(
    gender_frame,
    text='Others',
    bg='#000000',
    variable=var,
    value='others',
    font=('Times', 10),
    bd=0,fg='#b8860b'
   
)

register_country = OptionMenu(
    right_frame, 
    variable, 
    *countries)


register_country.config(
    width=15, 
    font=('Times', 12),
    bd=1,
)
register_pwd = Entry(
    right_frame, 
    font=f,
    bd=1,
    show='*',
    bg='#f8f8ff'
)
pwd_again = Entry(
    right_frame, 
    font=f,
    show='*',
    bd=1, 
    bg='#f8f8ff'
)

register_btn = Button(
    right_frame, 
    width=15, 
    text='Register', 
    font=f,fg='#b8860b',
    bd=0, 
    relief=SOLID,
    cursor='hand2',
    bg='#000000',
    command=insert_record
)

signin1 = Button(right_frame,text="Log In",width="30",height="1",fg='#0096FF',font=s,bg='#000000',bd=0,command=nextPage,cursor='hand2')



# widgets placement
exit_button.place(x=0,y=0)
signin1.grid(row=8, column=1, pady=5, padx=10)
register_name.grid(row=0, column=1, pady=10, padx=20)
register_email.grid(row=1, column=1, pady=10, padx=20) 
register_mobile.grid(row=2, column=1, pady=10, padx=20)
register_country.grid(row=4, column=1, pady=10, padx=20)
register_pwd.grid(row=5, column=1, pady=10, padx=20)
pwd_again.grid(row=6, column=1, pady=10, padx=20)
register_btn.grid(row=7, column=1, pady=10, padx=20)
right_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

gender_frame.grid(row=3, column=1, pady=10, padx=20)
male_rb.pack(expand=True, side=LEFT)
female_rb.pack(expand=True, side=LEFT,)
others_rb.pack(expand=True, side=LEFT)

# infinite loop
ws.mainloop()