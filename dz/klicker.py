from tkinter import *
import time
click = 0
a = 962020
b = '#'+ str(a)
def clicker():
    global click
    click += 1
    button.configure(text=click)
window = Tk()
window.title('clicker')
window.configure(bg = b)
window.geometry('1920x1080')
button = Button(text='0', command = clicker,
                bg = '#9bb828' , fg = '#2b2b12',
                activebackground= '#1d7a6b', activeforeground= '#12242b',
                font='New 40')
button.place(h=101, w=101, x=960, y=540)
while click == click:
    a+=100
    if a > 999999:
        a = 111111
    window.configure(bg = b)
    time.sleep(0.5)
window.mainloop()
