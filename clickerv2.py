from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("Clicker v2")

global counter
counter = 0
currentColor = ''

def up():
    global counter
    counter += 1
    cButton2.config(text = counter)
    main()

def down():
    global counter
    counter -= 1
    cButton2.config(text = counter)
    main()

def hoverEnter(event):
    root['bg'] = 'yellow'

def hoverLeave(event):
    main()

cButton1 = Button(text = 'Up', command = up, fg = "darkgreen", bg = "white")
cButton1.pack()

cButton2 = Button(text = counter, command = counter, fg = "darkgreen", bg = "white", state = DISABLED)
cButton2.pack()
cButton2.bind('<Enter>', hoverEnter) # enter the widget
cButton2.bind('<Leave>', hoverLeave)

cButton3 = Button(text = 'Down', command = down, fg = "darkgreen", bg = "white")
cButton3.pack()

def main():
    if counter == 0:
        root['bg'] = 'grey'
    elif counter < 0:
      root['bg'] = 'red'  
    elif counter > 0:
        root['bg'] = 'green'

main()

root.mainloop()