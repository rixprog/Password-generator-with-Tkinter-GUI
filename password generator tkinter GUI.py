import secrets #here we are using secrets to generate cryptographically strong passwords
import string
import pyperclip as pc
from tkinter import *

root= Tk()
passwrd = StringVar()
password_length = IntVar()
password_length.set(0)

def generator():
#defining letters,digits and special characters
        letters=string.ascii_letters
        digits=string.digits
        special_characters=string.punctuation

        alphabets=letters+digits+special_characters #combining all values

        pwd=''

        for i in range(password_length.get()):
            pwd+=''+ pwd.join(secrets.choice(alphabets))
        passwrd.set(pwd)

def copyclipboard():#to copy the password to clipboard
        randompass=passwrd.get()
        pc.copy(randompass)


#Tkinter GUI
root.title("Password Generator")
Label(root,text='password generator',font="Courier 30 bold").pack()
Label(root,text='rixprog',font="Courier 30 bold").pack()
Label(root,text='Enter the length of the password',font=15).pack(pady=4)
Entry(root,textvariable=password_length).pack(pady=4)
Button(root,text='Generate',font=20,height=1,command=generator,).pack(pady=4)
Entry(root,textvariable=passwrd,).pack(pady=15)
Button(root,text='Copy to clipboard',font=15,command=copyclipboard).pack(pady=2)
root.mainloop()











