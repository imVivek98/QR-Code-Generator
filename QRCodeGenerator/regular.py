from tkinter import *
from PIL import Image,ImageTk
import pyqrcode

root = Tk()

def generate():
    link_name = name_entry.get()
    link = link_entry.get()
    file_name = link_name + '.png'
    url = pyqrcode.create(link)
    url.png(file_name,scale=8)
    image = ImageTk.PhotoImage(Image.open(file_name))
    image_label = Label(image=image)
    image_label.image = image
    canvas.create_window(200,450,window=image_label)



canvas = Canvas(root,width=400,height=800)
canvas.pack()

app_label = Label(root,text='QRCode Generator',fg='Blue',font=('Arial',30))
canvas.create_window(200,50,window=app_label)

name_label = Label(root,text="Link name")
canvas.create_window(200,100,window=name_label)

name_entry = Entry(root)
canvas.create_window(200,130,window=name_entry)

link_entry = Entry(root)
canvas.create_window(200,190,window=link_entry)


link_label = Label(root,text="Link")
canvas.create_window(200,160,window=link_label)

button = Button(root,text='Generate QRCode',command=generate)
canvas.create_window(200,250,window=button)

root.mainloop()