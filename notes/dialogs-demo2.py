# dialogs-demo2.py
# modal dialog, text input field, and hidden password

from tkinter import *
from tkinter import messagebox, simpledialog

####################################
# customize these functions
####################################

class MyDialog(simpledialog.Dialog):
    def body(self, master):
        self.modalResult = None
        Label(master, text="User:").grid(row=0)
        Label(master, text="Password:").grid(row=1)
        self.e1 = Entry(master)
        self.e2 = Entry(master, show="*")
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        return self.e1 # initial focus

    def apply(self):
        first = self.e1.get()
        second = self.e2.get()
        self.modalResult = (first, second)

def showDialog(data):
    dialog = MyDialog(data.root)
    return dialog.modalResult

def button1Pressed(data):
    message = "Result = " + str(showDialog(data))
    data.message = message
    data.count += 1
    
def redrawAll(canvas, data):
    # background (fill canvas)
    canvas.create_rectangle(0,0,300,300,fill="cyan")
    # print message
    msg = "message: " + str(data.message)
    canvas.create_text(150,130,text=msg)
    msg = "count: " + str(data.count)
    canvas.create_text(150,170,text=msg)

def onButton(data, buttonId):
    if (buttonId == 1): button1Pressed(data)

def init(data):
    data.message = "none"
    data.count = 0
    buttonFrame = Frame(data.root)
    b1 = Button(buttonFrame, text="Click me!", command=lambda:onButton(data,1))
    b1.grid(row=0,column=0)
    buttonFrame.pack(side=TOP)

def mousePressed(event, data): pass
def keyPressed(event, data): pass
def timerFired(event): pass

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

    # Store root in data so buttons can access
    data.root = root

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

run(300, 300)
