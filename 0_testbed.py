from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
canvas = Canvas(root, width=500, height=400)

# myimg = PhotoImage(file='images/pecos_bill.png')
myimg = Image.open('images/pecos_bill.png')
myimg = myimg.resize((500,400))
myimg = ImageTk.PhotoImage(myimg)
canvas.create_image(10, 10, image=myimg, anchor='nw')
canvas.grid()

root.mainloop()