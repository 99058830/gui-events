from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("Clicker v2")

global counter
global lastButton
counter = 0
lastButton = True

def up():
    global counter, lastButton
    counter += 1
    cButton2.config(text = counter)
    print(counter)
    main()
    lastButton = True

def down():
    global counter, lastButton
    counter -= 1
    cButton2.config(text = counter)
    main()
    lastButton = False

def hoverEnter(event):
    root['bg'] = 'yellow'

def hoverLeave(event):
    main()

def upDouble(event):
    global counter
    counter = counter * 3
    cButton2.config(text = counter)
    print(counter)

def downDouble(event):
    global counter
    counter = counter / 3
    cButton2.config(text = counter)
    print(counter)

def main():
    global lastButton
    if counter == 0:
        root['bg'] = 'grey'
    elif counter < 0:
      root['bg'] = 'red'  
    elif counter > 0:
        root['bg'] = 'green'
    if lastButton == True:
        cButton2.bind('<Double-Button-1>', upDouble)
    elif lastButton == False:
        cButton2.bind('<Double-Button-1>', downDouble)

cButton2 = Button(text = counter, command = counter, fg = "darkgreen", bg = "white", state = DISABLED)
cButton2.pack()
cButton2.bind('<Enter>', hoverEnter)
cButton2.bind('<Leave>', hoverLeave)
cButton1 = Button(text = 'Up', command = up, fg = "darkgreen", bg = "white")
cButton1.pack()
cButton3 = Button(text = 'Down', command = down, fg = "darkgreen", bg = "white")
cButton3.pack()

main()

root.mainloop()