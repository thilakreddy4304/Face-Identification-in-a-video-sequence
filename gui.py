from tkinter import *
import os
from PIL import ImageTk,Image
root=Tk()
root.configure(background="white")
def function1():
    os.system(" py dataset.py")
def function2():
    os.system("py trainer.py")
def function3():
    os.system("py detector.py")
def function4():
    root.destroy()    
root.title("MINIPROJECT")
my_img = ImageTk.PhotoImage(Image.open("GRIET.png"))
my_label = Label(image=my_img)
Label(root,text="FACE RECOGNITION SYSTEM",font=("Helvetica",50,"bold"),fg="Thistle4").grid(row=1,sticky=N+E+W+S,padx=15)
Label(root).grid(row=2,padx=15,pady=15)
my_label.grid(row=0,padx=10,pady=10)
a = ImageTk.PhotoImage(Image.open("circle.png"))
Button(root,text=" Create Dataset",image=a,compound = LEFT,font=("times new roman",25),bg="white",fg='black',command=function1).grid(row=3,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Button(root,text=" Train Dataset",image=a,compound = LEFT,font=("times new roman",25),bg="white",fg='black',command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Button(root,text=" Recognize",image=a,compound = LEFT,font=("times new roman",25),bg="white",fg="black",command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Button(root,text="EXIT",font=("times",30,),bg="red",fg="white",command=function4).grid(row=6,sticky=N+E+W+S,padx=5,pady=5)
root.mainloop()