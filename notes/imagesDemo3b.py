# imagesDemo3b.py
# same as imagesDemo1.py but here we read from base64 encoding
# that we created in imagesDemo3a.py

# view in canvas
# read from base64 encoding
# with transparent pixels
# get size, resize (zoom and subsample)

img64 = """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
TcDXQQAAOw=="""

from tkinter import *

####################################
# customize these functions
####################################

def redrawAll(canvas, data):
    # Draw a background rectangle to highlight the transparency
    # of the images
    canvas.create_rectangle(0, 10, data.width, 190, fill="cyan")
    # Draw the demo info
    font = ("Arial", 16, "bold")
    msg = "Image Demo #3 (read from base64)"
    canvas.create_text(data.width/2, 25, text=msg, font=font)
    # Draw the original size image on the left
    imageSize = ( (data.image.width(), data.image.height()) )
    msg = "Full-size " + str(imageSize)
    canvas.create_text(data.width/5, 50, text=msg, font=font)
    canvas.create_image(data.width/5, 100, anchor=N, image=data.image)
    # Draw a half-size image in the middle
    imageSize = ( (data.halfImage.width(), data.halfImage.height()) )
    msg = "Half-size " + str(imageSize)
    canvas.create_text(data.width/2, 50, text=msg, font=font)
    canvas.create_image(data.width/2, 100, anchor=N, image=data.halfImage)
    # Draw a double-size image on the right
    imageSize = ( (data.doubleImage.width(), data.doubleImage.height()) )
    msg = "Double-size " + str(imageSize)
    canvas.create_text(data.width*4/5, 50, text=msg, font=font)
    canvas.create_image(data.width*4/5, 100, anchor=N, image=data.doubleImage)

import urllib.request
import base64

def init(data):
    data.image = PhotoImage(data=img64)
    data.halfImage = data.image.subsample(2,2)
    data.doubleImage = data.image.zoom(2,2)

def mousePressed(event, data): pass
def keyPressed(event, data): pass
def timerFired(data): pass

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds

    # create the root and the canvas (Note Change: do this BEFORE calling init!)
    root = Tk()

    init(data)
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1000, 600)
