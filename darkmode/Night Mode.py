import tkinter as tk
from tkinter import PhotoImage

# setting root window:
root = tk.Tk()
root.title("Night Mode")
root.config(bg="#CECCBE")
root.geometry("800x400")

# setting switch state:
btnState = False

# setting switch function:
def switch():
    global btnState
    if btnState:
        btn.config(image=offImg, bg="#CECCBE", activebackground="#CECCBE")
        root.config(bg="#CECCBE")
        txt.config(text="Dark Mode: OFF", bg="#CECCBE")
        btnState = False
    else:
        btn.config(image=onImg, bg="#2B2B2B", activebackground="#2B2B2B")
        root.config(bg="#2B2B2B")
        txt.config(text="Dark Mode: ON", bg="#2B2B2B")
        btnState = True

# loading the switch images:
onImg = PhotoImage(file=r"switch-on.png")
offImg = PhotoImage(file=r"switch-off.png")

# Night mode label:
txt = tk.Label(root, text="Dark Mode: OFF", font="FixedSys 17", bg="#CECCBE", fg="green")
txt.place(relx=0.5, rely=0.35, anchor="center")

# switch widget:
btn = tk.Button(root, text="OFF", borderwidth=0, command=switch, bg="#CECCBE", activebackground="#CECCBE")
btn.place(relx=0.5, rely=0.5, anchor="center")
btn.config(image=offImg)

# window in mainloop:
root.mainloop()
