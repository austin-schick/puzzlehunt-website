# keyEventsDemo.py
#
# keyPressed, keyReleased
# with ctrl and shift

from tkinter import *

def setEventInfo(event, data, eventName):
    ctrl  = ((event.state & 0x0004) != 0)
    shift = ((event.state & 0x0001) != 0)
    msg = eventName + ": "
    msg += "(ctrl=" + str(ctrl) + ")"
    msg += "(shift=" + str(shift) + ")"
    msg += "(char=" + event.char + ")"
    msg += "(keysym=" + event.keysym + ")"
    data.info = msg

def ignoreKey(event):
    # Helper function to return the key from the given event
    ignoreSyms = [ "Shift_L", "Shift_R", "Control_L", "Control_R", "Caps_Lock" ]
    return (event.keysym in ignoreSyms)

def keyPressed(event, data):
    if (ignoreKey(event) == False):
        setEventInfo(event, data, "keyPressed")
        if (event.keysym not in data.pressedLetters):
            data.pressedLetters.add(event.keysym)

def keyReleased(event, data):
    if (ignoreKey(event) == False):
        setEventInfo(event, data, "keyReleased")
        if (event.keysym in data.pressedLetters):
            data.pressedLetters.remove(event.keysym)

def redrawAll(canvas, data):
    # Draw the pressedLetters
    font = ("Arial", 16, "bold")
    msg = "Pressed Letters: " + str(sorted(data.pressedLetters))
    canvas.create_text(data.width/2, data.height/3, text=msg, font=font)
    # Draw the event info message
    font = ("Arial", 16, "bold")
    canvas.create_text(data.width/2, data.height*2/3, text=data.info, font=font)

def init(data):
    data.info = "Key Events Demo"
    data.pressedLetters = set()

def timerFired(data): pass
def mousePressed(event, data): pass

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

    # Note changes #1:
    def keyWrapper(keyFn, event, canvas, data):
        keyFn(event, data)
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
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events

    # Note changes #2:
    root.bind("<KeyPress>", lambda event:
                            keyWrapper(keyPressed, event, canvas, data))
    root.bind("<KeyRelease>", lambda event:
                            keyWrapper(keyReleased, event, canvas, data))

    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(600, 300)

