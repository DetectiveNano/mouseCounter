## By REAL NAME REDACTED aka LightKilt aka DetectiveNano ##
# last modified 5/6/20 20:57
# counts clicks will eventually show start time and have a window

from pynput import mouse
import tkinter as tk
import datetime

datetime_object = datetime.datetime.now()
dateTime = str(datetime_object)
root = tk.Tk()

## Define different mouse buttons
leftClick = 0
midClick = 0
rightClick = 0

## parameter shit
screen_width = 400
screen_height = 400

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
            ##printClicks()
            ## commented out so it doesnt print clicks
            once +=1 

def printClicks(): ## print the clicks in console
    print("Left Clicks : " + str(leftClick))
    print("Middle Clicks : " + str(midClick))
    print("Right Clicks : " + str(rightClick))

def startup(v,w,x,y,z): ## function to create labels
    canvas.create_window(screen_width/2, screen_height/2 - 80, window = w)
    canvas.create_window(screen_width/2, screen_height/2 - 40, window = x)
    canvas.create_window(screen_width/2, screen_height/2 , window = y)
    canvas.create_window(screen_width/2, screen_height/2 + 40, window = z)
    canvas.create_window(screen_width/2, screen_height/2 + 80, window = v)

def create(): ## make each label and then run startup(x,y,z) and then update it every 100 ms
    global LCLabel
    global MCLabel
    global RCLabel
    dateTimeLabel = tk.Label(root,
        text  = 'Started : ' + dateTime,
        bg = bgColor,
        fg = textColor,
        font=('helvetica', 14, 'bold'))
    LCLabel = tk.Label(root,
        text= 'Left Clicks : ' + str(leftClick),
        bg = bgColor,              
        fg = textColor,
        font=('helvetica', 14, 'bold'))
    MCLabel = tk.Label(root,
        text= 'Middle Clicks : ' + str(midClick),
        bg = bgColor,               
        fg = textColor,
        font=('helvetica', 14, 'bold'))
    RCLabel = tk.Label(root,
        text= 'Right Clicks : ' + str(rightClick),
        bg = bgColor,
        fg = textColor,
        font=('helvetica', 14, 'bold'))
    creditLabel = tk.Label(root,
        text= 'Written by DetectiveNano ',
        bg = bgColor,
        fg = 'white',
        font=('helvetica', 16, 'bold'))
    startup(creditLabel,dateTimeLabel,LCLabel,MCLabel,RCLabel)
    updateClicks()
    
def updateClicks():
    global LCLabel
    global MCLabel
    global RCLabel
    LCLabel['text'] = str("Left Clicks : " + str(leftClick))
    MCLabel['text'] = 'Middle Clicks : ' + str(midClick)
    RCLabel['text'] = 'Right Clicks : ' + str(rightClick)
    root.after(100,updateClicks)

    
while running:
    root.title('Clicks')
    listener = mouse.Listener(on_click=on_click)
    listener.start()
    create()
    root.mainloop()
