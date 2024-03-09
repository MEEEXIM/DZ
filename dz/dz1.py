from tkinter import *

def clicer():
    if (lang.get() == "a"):
        text.config(fg = '#FFFF00', bg = '#808000')
        a_btn.config(fg = '#FFFF00', bg = '#808000')
        b_btn.config(fg = '#FFFF00', bg = '#808000')
        c_btn.config(fg = '#FFFF00', bg = '#808000')
    if (lang.get() == "b"):
        text.config(fg = '#000080', bg = '#4169E1')
        a_btn.config(fg = '#000080', bg = '#4169E1')
        b_btn.config(fg = '#000080', bg = '#4169E1')
        c_btn.config(fg = '#000080', bg = '#4169E1')
    if (lang.get() == "c"):
        text.config(fg = '#FF0000', bg = '#800000')
        a_btn.config(fg = '#FF0000', bg = '#800000')
        b_btn.config(fg = '#FF0000', bg = '#800000')
        c_btn.config(fg = '#FF0000', bg = '#800000')
        
window = Tk()
window.title("okno")
mainmenu = Menu(window)
window.configure(bg = '#33c5ff')
window.config(menu = mainmenu)
window.geometry('400x250')

def butt1():
    window.config(bg ='#FFFFFF')
def butt2():
    window.config(bg = '#C0C0C0')
def butt3():
    window.config(bg = '#000000')


men = Menu(mainmenu, tearoff=0)
men.add_command(label="белый",command=butt1)
men.add_command(label="серый",command=butt2)
men.add_command(label="черный",command=butt3)

mainmenu.add_cascade(label="фон", menu=men)

lang = StringVar(value="aT")

text = Label(text = 'YUYBYYIGNTBFUIB')
text.place(h=111 , x=100 , y = 140)
text.config(fg = '#FFFFFF', bg = '#000000', font = 'Times 20')



a_btn = Radiobutton(window , text="желтый текст" , value="a" , variable=lang, command=clicer)
a_btn.place(x=0 , y = 0)

b_btn = Radiobutton(text="синий текст", value="b", variable=lang, command=clicer)
b_btn.place(x=0 , y = 40)

c_btn = Radiobutton(text='красный текст', value="c", variable=lang, command=clicer)
c_btn.place(x=0 , y = 80)

window.mainloop()