import sys, os, tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinterDnD
instance, root, stringvar = None, None, None
tframe = [] # list of frames
current = None # size of ring currently being dragged
orig = None # info on ring being dragged
class Game():
    def __init__(self, rings, scr, l):
        self.board = l
        self.rings = rings
        self.moves = 0
        self.completeScreen = scr
        self.map = [[],[],[]]
        self.towers = [[],[],[]]
        for x in range(1,rings+1):
            self.towers[0].append(Ring(x, 0, self.rings).create()) # init rings
            self.map[0].append(self.rings-x)
        updateBoard()
    def reset(self): # clears rings and stuff
        for x in root.winfo_children():
            print(x)
            if str(x) in str(self.towers):
                x.destroy()
        Label(root, text="Moves: 0 | Min Moves: 0 | Rings: 0", foreground="darkblue", width=500, font=("Arial", 15)).pack()
    def moveRing(): # forceably moves
        return
    def solve(self): # gives instructions on how to solve
        return
    def completed(self):
        pass
def dragging(event):
    global orig
    orig = event.widget
    return (tkinterDnD.COPY, "DND_Text", "Some nice dropped text!")
def drop(event, tower):
    global orig, tframe
    size = int(orig.winfo_name())
    newRing = Ring(int(size), tower, 1)
    orig.destroy()
    print(newRing.__dict__)
    if len(instance.map[tower]) > 0:
        if instance.map[tower][0] > size:
            instance.moves+=1
            newRing.create()
        else:
            return
    else:
        instance.moves+=1
        newRing.create()
    return
class Ring():
    def __init__(self, size, tower, rings):
        self.rings = rings
        self.size = size
        self.tower = tower
        self.towerOffset = 170
        self.ringColors = ['green','red','blue', 'yellow', 'lime', 'purple', 'magenta', 'orange',  'gold']
        self.color = self.ringColors[size-1]
        self.dx = 18
        self.dy = 18
        self.width = self.dx * ((self.size + 1)) + 40
        self.height = self.dy * (self.rings - (self.size-1)) + 120
    def create(self):
        print('HEY')
        x = ttk.Label(root, background=self.color,ondrop=drop, ondragstart=dragging, name=str(self.size))
        x.bind("<<DragInitCmd>>", dragging)
        print("x" + str(35+(self.dx + (-10 * self.size)) + (self.tower * self.towerOffset)))
        print("y" + str((540-self.height)))
        x.place(x=35+(self.dx + (-10 * (self.size-1))) + (self.tower * self.towerOffset),y=(540-self.height),width=self.width, height=15)
        return x
def updateBoard():
    pass
def init():
    global instance, tframe, root, stringvar
    root = tkinterDnD.Tk()
    root.geometry("520x560+10+10")
    root.configure(background="springgreen")
    root.title("Tower of Hanoi Puzzle")
    menubar = Menu(root)
    stringvar = tk.StringVar()
    stringvar.set('test')
    editmenu = Menu(menubar, tearoff=0)
    game = Menu(menubar, tearoff=0)
    helpmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Edit", menu=editmenu)
    menubar.add_cascade(label="Game", menu=game)
    menubar.add_cascade(label="Help", menu=helpmenu)
    l = Label(root, text="Moves: 0 | Min Moves: 0 | Rings: 0", foreground="darkblue", width=500, font=("Arial", 15))
    l.pack()
    frm1 = tk.Frame(root,width=166, height=280, background="seagreen")
    frm2 = tk.Frame(root , width=166, height=280,background="seagreen")
    frm3 = tk.Frame(root, width=166, height=280,background="seagreen")
    frm1.place(x=0, y=300)
    frm2.place(x=170, y=300)
    frm3.place(x=340, y=300)




   
    tower1 = Frame(root, background="brown", width=20, height=280)
    tower2 = Frame(root, background="brown", width=20, height=280)
    tower3 = Frame(root, background="brown", width=20, height=280)
    tower1.place(x=75, y=300)
    tower2.place(x=250, y=300)
    tower3.place(x=400, y=300)

    tower1.register_drag_source("*")

    tower1.register_drop_target("*")
    tower2.register_drop_target("*")
    tower2.register_drag_source("*")
    tower3.register_drop_target("*")
    tower3.register_drag_source("*")

    tower1.bind("<<Drop>>", lambda event, arg=0: drop(event, 0))
    tower2.bind("<<Drop>>", lambda event, arg=1: drop(event, 1))
    tower3.bind("<<Drop>>", lambda event, arg=2: drop(event, 2))
  

   
    root.config(menu=menubar)
    tframe.extend([str(tower1), str(tower2), str(tower3)])
    instance = Game(3, 0, l)
    root.mainloop()
if __name__ == '__main__':
    init()