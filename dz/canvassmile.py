from tkinter import *
 
risunok = Tk()
risunok.geometry('1920x1080')

smile=Canvas(width=1920, height=1080, bg='light blue')
smile.pack()

smile.create_oval(200, 200, 1720, 880, fill='yellow', outline='black', width=3)
smile.create_oval(500, 300, 700, 500, fill='white', outline='black', width=3)
smile.create_oval(1420, 300, 1220, 500, fill='white', outline='black', width=3)

smile.create_arc(500, 600, 1420, 800, start=180, extent=180, fill='white', outline='black', width=3, style='pieslice')

smile.create_oval(575, 375, 625, 425, fill='black', outline='black', width=3)
smile.create_oval(1345, 375, 1295, 425, fill='black', outline='black', width=3)

smile.create_line(960, 200, 100, 300, 960, 200, 110, 320, 960, 200, 320, 380, 
                  960, 200, 1700, 300, 960, 200, 1670, 360, 960, 200, 1685, 330, 
                    960, 200, 780, 400, 960, 200, 1120, 387, fill='brown', width=5)

risunok.mainloop()