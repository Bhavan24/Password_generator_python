from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
import random
import subprocess

def password():
    passlen = int(passwordLentgh.get())
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*?"
    p =  "".join(random.sample(s,passlen))
    passwordFinal.set(p)

def copy():
    p = passwordFinal.get()
    copy2clip(p)

def copy2clip(txt):
    cmd='echo '+ txt.strip() +'|clip'
    return subprocess.check_call(cmd, shell=True)

root = Tk()
root.title("Password Generator")
root.geometry("403x117")
root.resizable(width=False, height=False)

passwordLentgh = tk.StringVar(root)
passwordFinal = tk.StringVar(root)

gPasswordBtn = tk.Button(root)
gPasswordBtn["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
gPasswordBtn["font"] = ft
gPasswordBtn["fg"] = "#000000"
gPasswordBtn["justify"] = "center"
gPasswordBtn["text"] = "Generate password"
gPasswordBtn["relief"] = "groove"
gPasswordBtn.place(x=190,y=10,width=127,height=30)
gPasswordBtn["command"] = password

copyBtn = tk.Button(root)
copyBtn["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
copyBtn["font"] = ft
copyBtn["fg"] = "#000000"
copyBtn["justify"] = "center"
copyBtn["text"] = "copy"
copyBtn["relief"] = "groove"
copyBtn.place(x=320,y=10,width=60,height=30)
copyBtn["command"] = copy

passwordTxt = tk.Entry(root)
passwordTxt["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
passwordTxt["font"] = ft
passwordTxt["fg"] = "#333333"
passwordTxt["justify"] = "center"
passwordTxt["textvariable"] = passwordFinal
passwordTxt.place(x=150,y=60,width=211,height=31)

lbl1 = tk.Label(root)
lbl1["cursor"] = "watch"
ft = tkFont.Font(family='Times',size=10)
lbl1["font"] = ft
lbl1["fg"] = "#333333"
lbl1["justify"] = "center"
lbl1["text"] = "Password length : "
lbl1["relief"] = "flat"
lbl1.place(x=30,y=10,width=110,height=30)

pLengthTxt = tk.Entry(root)
pLengthTxt["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
pLengthTxt["font"] = ft
pLengthTxt["fg"] = "#333333"
pLengthTxt["justify"] = "center"
pLengthTxt["textvariable"] = passwordLentgh
pLengthTxt.place(x=140,y=10,width=30,height=30)

lbl2 = tk.Label(root)
ft = tkFont.Font(family='Times',size=18)
lbl2["font"] = ft
lbl2["fg"] = "#333333"
lbl2["justify"] = "center"
lbl2["text"] = "Password: "
lbl2["relief"] = "flat"
lbl2.place(x=30,y=50,width=122,height=51)

root.mainloop()