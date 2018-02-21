# imagesDemo4.py

# based on imagesDemo1.py,
# but here we read/write pixels

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
    msg = "Image Demo #4 (read/write pixels)"
    canvas.create_text(data.width/2, 25, text=msg, font=font)
    # Draw the original size image on the left
    imageSize = ( (data.image.width(), data.image.height()) )
    msg = "Full-size in Gray " + str(imageSize)
    canvas.create_text(data.width/5, 50, text=msg, font=font)
    canvas.create_image(data.width/5, 100, anchor=N, image=data.image)
    # Draw a half-size image in the middle
    imageSize = ( (data.halfImage.width(), data.halfImage.height()) )
    msg = "Half-size " + str(imageSize)
    canvas.create_text(data.width/2, 50, text=msg, font=font)
    canvas.create_image(data.width/2, 100, anchor=N, image=data.halfImage)
    # Draw a double-size image on the right
    imageSize = ( (data.doubleImage.width(), data.doubleImage.height()) )
    msg = "Double-size in Red " + str(imageSize)
    canvas.create_text(data.width*4/5, 50, text=msg, font=font)
    canvas.create_image(data.width*4/5, 100, anchor=N, image=data.doubleImage)

def getRGB(image, x, y):
    return tuple(map(int, image.get(x, y).split(" ")))

def setRGB(image, x, y, red, green, blue):
    image.put(hexColor(red, green, blue), to=(x,y))
    
def hexColor(red, green, blue):
    return ("#%02x%02x%02x" % (red, green, blue))

def grayScale(image):
    for x in range(image.width()):
        for y in range(image.height()):
            (red, green, blue) = getRGB(image, x, y)
            gray = (red*30 + green*59 + blue*11)//100
            setRGB(image, x, y, gray, gray, gray)

def redScale(image, onlyHalf=False):
    for x in range(image.width()):
        for y in range(image.height()):
            (red, green, blue) = getRGB(image, x, y)
            setRGB(image, x, y, red, 0, 0)

def init(data):
    data.image = PhotoImage(file="sampleImage1.gif")
    data.halfImage = data.image.subsample(2,2)
    data.doubleImage = data.image.zoom(2,2)
    grayScale(data.image)
    redScale(data.doubleImage)

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

run(1000, 500)
