from tkinter import *
window = Tk()
color='black'
widtth=3
mmenu=Menu(window)
window.config(menu=mmenu)
click_test=False

def motion(event):
    global click_test
    х,y = window.winfo_pointerxy()
    widget = window.winfo_containing(х,y)
    x = event.x
    y = event.y
    window.title(str(x) + " : " + str(y))
    if click_test:    
        canV.create_oval(x-1,y-1, x+1, y+1 ,fill=color, outline=color, width=widtth)

def keyPress(event):
    global click_test
    if (event.keysym == "space"):
        click_test = True
def keyRelease(event):
    global click_test
    if (event.keysym == "space"):
        click_test = False

def stir():
    global color
    global widtth
    color='white'
    widtth=90
def stir1():
    global widtth
    widtth+=2
def stir2():
    global widtth
    widtth-=2

def pencil():
    global color
    global widtth
    color='black'
    widtth=3

def pencil1():
    global widtth
    widtth+=1

def pencil2():
    global widtth
    widtth-=1

pencilmenu = Menu(mmenu, tearoff=0)
pencilmenu.add_command(label="Включить", command=pencil)
pencilmenu.add_command(label="Увеличить толщину", command=pencil1)
pencilmenu.add_command(label="Уменьшить толщину", command=pencil2)

stirmenu = Menu(mmenu, tearoff=0)
stirmenu.add_command(label="Включить", command=stir)
stirmenu.add_command(label="Увеличить толщину", command=stir1)
stirmenu.add_command(label="Уменьшить толщину", command=stir2)

mmenu.add_cascade(label='Карандаш', menu=pencilmenu)
mmenu.add_cascade(label='Ластик', menu=stirmenu)

canV = Canvas(width=700, height=500, bg='white')
# canV.create_oval(9,9, 11, 11 ,fill='black')
canV.pack()  





window.title("mouse")
window.geometry('700x500')
window.resizable(False, False)

window.bind("<Motion>" , motion)
window.bind("<KeyPress>" , keyPress)
window.bind("<KeyRelease>" , keyRelease)

window.mainloop()