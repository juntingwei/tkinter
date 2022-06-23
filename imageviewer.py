from tkinter import *
from PIL import ImageTk, Image

root = Tk()

orgimagelist = ["arches.jpg", "bridge.jpg", "door.jpg"]
resizedimagelist = []

#resizing all images from list and putting in resized list

for orgimage in orgimagelist:
    imagehandle = Image.open(str(orgimage))
    new_height = 720
    new_width = int(new_height / imagehandle.height * imagehandle.width)
    imagehandleresize = imagehandle.resize((new_width, new_height))
    imageresize = ImageTk.PhotoImage(imagehandleresize)
    resizedimagelist.append(imageresize)

imagenumber = 0
lastimagenumber = len(resizedimagelist) - 1

print(lastimagenumber)

def previousimage():
    global imagenumber
    global imageViewer
    global currentimage
    global previousButton
    global nextButton
    if imagenumber <= 0:
        previousButton = Button(root, text = "<<", command = previousimage, state = DISABLED)
        return
    else:
        imagenumber = int(imagenumber - 1)
        imageViewer.grid_forget()
        currentimage = resizedimagelist[imagenumber]
        imageViewer = Label(root, image=currentimage)
        nextButton = Button(root, text = ">>", command = nextimage, state = NORMAL)

    if imagenumber == 0:
        previousButton = Button(root, text = "<<", command = previousimage, state = DISABLED)
    
    nextButton.grid(row = 1, column = 2)
    previousButton.grid(row = 1, column = 0)
    imageViewer.grid(row = 0, column = 0, columnspan = 3)


def nextimage():
    global imagenumber
    global imageViewer
    global currentimage
    global previousButton
    global nextButton
    if imagenumber >= lastimagenumber:
        nextButton = Button(root, text = ">>", command = nextimage, state = DISABLED)
        return
    else:
        imagenumber = int(imagenumber + 1)
        imageViewer.grid_forget()
        currentimage = resizedimagelist[imagenumber]
        imageViewer = Label(root, image=currentimage)
        previousButton = Button(root, text = "<<", command = previousimage, state = NORMAL)
    
    if imagenumber == int(len(resizedimagelist)-1):
        nextButton = Button(root, text = ">>", command = nextimage, state = DISABLED)

    nextButton.grid(row = 1, column = 2)
    previousButton.grid(row = 1, column = 0)
    imageViewer.grid(row = 0, column = 0, columnspan = 3)
    

currentimage = resizedimagelist[imagenumber]

#creating widgets
imageViewer = Label(root, image=currentimage)
quitButton = Button(root, text = "Exit Program", command = root.quit)
previousButton = Button(root, text = "<<", command = previousimage, state = DISABLED)
nextButton = Button(root, text = ">>", command = nextimage)

#creating widget to hold image
imageViewer.grid(row = 0, column = 0, columnspan = 3)
previousButton.grid(row = 1, column = 0)
quitButton.grid(row = 1, column = 1)
nextButton.grid(row = 1, column = 2)

#displaying widget (containing image)


root.mainloop()