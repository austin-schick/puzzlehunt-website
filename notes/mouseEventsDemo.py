# mouseEventsDemo.py
#
# mousePressed, mouseMoved, mouseReleased
# with left or right button
# and with ctrl and shift
# and mouseMotion (when no button is pressed)

from tkinter import *

def setEventInfo(event, data, eventName):
    ctrl  = ((event.state & 0x0004) != 0)
    shift = ((event.state & 0x0001) != 0)    
    msg = ""
    if ctrl:  msg += "ctrl-"
    if shift: msg += "shift-"
    msg += eventName
    msg += " at " + str((event.x, event.y))
    data.info = msg

def mouseMotion(event, data):
    setEventInfo(event, data, "mouseMotion")
    data.motionPosn = (event.x, event.y)

def leftPressed(event, data):
    setEventInfo(event, data, "leftPressed")
    data.leftPosn = (event.x, event.y)

def leftMoved(event, data):
    setEventInfo(event, data, "leftMoved")
    data.leftPosn = (event.x, event.y)

def leftReleased(event, data):
    setEventInfo(event, data, "leftReleased")
    data.leftPosn = (event.x, event.y)

def rightPressed(event, data):
    setEventInfo(event, data, "rightPressed")
    data.rightPosn = (event.x, event.y)

def rightMoved(event, data):
    setEventInfo(event, data, "rightMoved")
    data.rightPosn = (event.x, event.y)

def rightReleased(event, data):
    setEventInfo(event, data, "rightReleased")
    data.rightPosn = (event.x, event.y)

def redrawAll(canvas, data):
    # Draw the "L"
    font = ("Arial", 24, "bold")
    (cx, cy) = data.leftPosn
    canvas.create_text(cx, cy, text="L", font=font)
    # Draw the "R"
    (cx, cy) = data.rightPosn
    canvas.create_text(cx, cy, text="R", font=font)
    # Draw the "M"
    (cx, cy) = data.motionPosn
    canvas.create_text(cx, cy, text="M", font=font)
    # Draw the event info message
    font = ("Arial", 16, "bold")
    canvas.create_text(300, 25, text=data.info, font=font)

def init(data):
    data.leftPosn = (data.width//4, data.height//2)
    data.rightPosn = (data.width*3//4, data.height//2)
    data.motionPosn = (data.width//2, data.height//2)
    data.info = "Mouse Events Demo"

def timerFired(data): pass
def keyPressed(event, data): pass

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

    # Note changes #1:
    def mouseWrapper(mouseFn, event, canvas, data):
        mouseFn(event, data)
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
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events

    # Note changes #2:
    root.bind("<Button-1>", lambda event:
                            mouseWrapper(leftPressed, event, canvas, data))
    root.bind("<Button-3>", lambda event:
                            mouseWrapper(rightPressed, event, canvas, data))
    canvas.bind("<Motion>", lambda event:
                            mouseWrapper(mouseMotion, event, canvas, data))
    canvas.bind("<B1-Motion>", lambda event:
                            mouseWrapper(leftMoved, event, canvas, data))
    canvas.bind("<B3-Motion>", lambda event:
                            mouseWrapper(rightMoved, event, canvas, data))
    root.bind("<B1-ButtonRelease>", lambda event:
                            mouseWrapper(leftReleased, event, canvas, data))
    root.bind("<B3-ButtonRelease>", lambda event:
                            mouseWrapper(rightReleased, event, canvas, data))

    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(600, 300)
