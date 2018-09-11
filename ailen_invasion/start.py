from tkinter import Tk, Button, Frame
from os import system
# from settings import Settings


def q(ev):
    global root
    root.destroy()


def start_game(ev):
    global root
    root.destroy()
    system('python ailen_invasion.py')


# close = Settings()

# if not close.Q:
#     exit()

root = Tk()
root.geometry('600x400')
root.minsize(600, 400)
root.maxsize(600, 400)
root.title('Alien invasion')

panelFrame = Frame(root, width=600, height=400, bg='gray')

panelFrame.pack(fill='both')

startBtn = Button(panelFrame, text='Alien invasion', font='arial 22')
quitBtn = Button(panelFrame, text='Выход', font='arial 22')

# loadBtn.bind('<Button-1>', load_file)
# saveBtn.bind('<Button-1>', save_file)
quitBtn.bind('<Button-1>', q)
startBtn.bind('<Button-1>', start_game)

w = 200 / 4
h = 100
y = 400
startBtn.place(x=w, y=y / 2 - h - 30, width=w * 10, height=h)
quitBtn.place(x=w, y=y / 2 + h - 60, width=w * 10, height=h)

root.update_idletasks()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
size = tuple(int(_) for _ in root.geometry().split('+')[0].split('x'))
x = w / 2 - size[0] / 2
y = h / 2 - size[1] / 2
root.geometry("%dx%d+%d+%d" % (size + (x, y)))

root.mainloop()
