import tkinter
root = tkinter.Tk()
root.geometry("300x200")
root.title("Test window")
label = tkinter.Label(root,text="Enter your name")
label.pack()
name = tkinter.Entry(root)
name.pack()
root.mainloop()