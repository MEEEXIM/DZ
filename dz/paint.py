from tkinter import *
window = Tk()
color='black'
widtth=3

def motion(event):
    х,y = window.winfo_pointerxy()
    widget = window.winfo_containing(х,y)
    x = event.x
    y = event.y
    window.title(str(x) + " : " + str(y))
    canV.create_oval(x-1,y-1, x+1, y+1 ,fill=color, outline=color, width=widtth)

def butL(event):
    global color
    color='white'

def butR(event):
    global color
    color='black'

def Up(event):
    global widtth
    widtth+=2

def Down(event):
    global widtth
    widtth-=2

canV = Canvas(width=700, height=500, bg='white')
# canV.create_oval(9,9, 11, 11 ,fill='black')
canV.pack()  





window.title("mouse")
window.geometry('700x500')
window.resizable(False, False)

window.bind("<Motion>" , motion)
window.bind("<Button-1>" , butL)
window.bind("<Button-3>" , butR)
window.bind("<Button-4>" , Up)
window.bind("<Button-5>" , Down)

window.mainloop()