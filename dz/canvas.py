from tkinter import *
 
risunok = Tk()
risunok.geometry('1920x1080')

treug=Canvas(width=1920, height=1080, bg='light blue')
treug.pack()

treug.create_polygon(800, 100, 1550, 850, 100, 850, fill='green', outline='black')
treug.create_polygon(1175, 475, 825, 850, 450, 475, fill='red', outline='blue')
treug.create_polygon(1000, 662.5, 637.5, 662.5, 812.5, 475, fill='yellow', outline='black')

risunok.mainloop()