## By REAL NAME REDACTED aka LightKilt aka DetectiveNano ##
# last modified 5/5/20 20:57
# counts clicks will eventually show start time and have a window

from pynput import mouse
import tkinter as tk
import time as tm  ## will be used in future

root = tk.Tk()

## Define different mouse buttons
leftClick = 0
midClick = 0
rightClick = 0

## parameter shit
screen_width = 300
screen_height = 300

textColor = str('lime')
bgColor = str('black')

canvas = tk.Canvas(root,bg = bgColor, width = screen_width, height = screen_height)
canvas.pack()

## I dont know if this has any utility but it works so im not deleting it

LCLabel = 0
RCLabel = 0
MCLabel = 0



running = True

def on_click(x, y, button, pressed):
    global leftClick
    global midClick
    global rightClick
    global running
    if pressed:
        once = 0 ## update click variables
        if str(button) == "Button.left" :
            leftClick += 1
        elif str(button) == "Button.middle":
            midClick += 1
            running = False
        elif str(button) == "Button.right":
            rightClick += 1
        if once == 0:
            printClicks()
            once +=1 

def printClicks(): ## print the clicks in console
    print("Left Clicks : " + str(leftClick))
    print("Middle Clicks : " + str(midClick))
    print("Right Clicks : " + str(rightClick))

def startup(x,y,z): ## function to create labels
    canvas.create_window(screen_width/2, screen_height/2 - 40, window = x)
    canvas.create_window(screen_width/2, screen_height/2 , window = y)
    canvas.create_window(screen_width/2, screen_height/2 + 40, window = z)    

def create(): ## make each label and then run startup(x,y,z) and then update it every 100 ms
    global LCLabel
    global MCLabel
    global RCLabel
    LCLabel = tk.Label(root,
        text= 'Left Clicks : ' + str(leftClick),
        bg = bgColor,              
        fg = textColor,
        font=('helvetica', 12, 'bold'))
    MCLabel = tk.Label(root,
        text= 'Middle Clicks : ' + str(midClick),
        bg = bgColor,               
        fg = textColor,
        font=('helvetica', 12, 'bold'))
    RCLabel = tk.Label(root,
        text= 'Right Clicks : ' + str(rightClick),
        bg = bgColor,
        fg = textColor,
        font=('helvetica', 12, 'bold'))
    startup(LCLabel,MCLabel,RCLabel)
    update()
    
def update():
    global LCLabel
    global MCLabel
    global RCLabel
    LCLabel['text'] = str("Left Clicks : " + str(leftClick))
    MCLabel['text'] = 'Middle Clicks : ' + str(midClick)
    RCLabel['text'] = 'Right Clicks : ' + str(rightClick)
    root.after(100,update)

    
while running:
    listener = mouse.Listener(on_click=on_click)
    listener.start()
    create()
    root.mainloop()
