from tkinter import*
root=Tk()
root.title("토찌")
def  mimelamoiji():
    mimelamoiji=Label(root,text="그냥 해 나 잘거야!! 방해하지 마!")
    mimelamoiji.grid(row=25,column=16)
tojji=Button(root, text="RANDOM", padx=40, pady=25, command=mimelamoiji)
tojji.grid(row=0,column=0)
root.mainloop()
