# импортируем библиотеку tkinter
from tkinter import *

# функция которая должна вызываться при нажатии на кнопку
# def click():
#     # изменяем текст Label
#     # inp.get() берём текст из Entry (input)
#     text.configure(text=inp.get())

# def printGeometry():
    # text.configure(text=window.geometry())

click = 1
def clicer():
    global click
    click+=1
    button.configure(text=click)

# создаём окно 
window = Tk()
# меняем название окна
window.title("12345")
# меняем ширину и высоту окна 
window.geometry('400x250')

# создаём текст
# text = Label(text=window.geometry(), padx=60, pady=30)
# text.pack(anchor="center")


# создаём ввод (input)
# inp = Entry(width=10)
# inp.pack(anchor="s", padx=100, pady=100)
# inp.pack(fill=X)
# inp.pack(fill=BOTH, expand=True)
# inp.pack(side=BOTTOM)
a = 100000
button = Button(text="0", command=clicer, highlightcolor=a)
button.pack(expand=True)
# метод mainloop() оставляет окно открытым
window.mainloop()

# создаём кнопку                     command вызывает функцию
while True:
    a+= 1
    if a == 1000000:
        a=100000
    