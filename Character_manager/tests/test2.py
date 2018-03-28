from tkinter import *

root = Tk()
root.geometry('1280x720')
root.resizable(0,0)

fr_root = Frame(root, width = '1280', height = '720', bg = 'black')
fr_root.pack()
fr_root.pack_propagate(0)
fr_main = Frame(fr_root, width = '878', height = '418', bg = '#252A29')
fr_main.pack()
fr_main.pack_propagate(0)
fr_center = Frame(fr_main, width = '778', height = '418', bg = '#252A29')
fr_center.pack()
fr_center.pack_propagate(0)
fr_center.place(x = 0, y = 0)

cpt = 0

with open('test.txt', 'r', newline = '') as file :
	for row in file :
		cpt += 1
	print(cpt)
file.close()

x = 10

can = Canvas(fr_center, bg = '#252A29', highlightthickness = 0, width = cpt*220)

with open('test.txt', 'r', newline = '') as file :
	for row in file :
		fr_char = Frame(can, width = '200', height = '375', bg = 'green')
		fr_char.pack()
		fr_char.pack_propagate(0)
		fr_char.place(x = x, y = 10)

		x += 220

scrl = Scrollbar(fr_center, orient = "horizontal", command = can.xview)
can.configure(xscrollcommand = scrl.set)
scrl.pack(side="bottom", fill="x")
can.pack(side = "left", fill="both", expand = True)


fr_add = Frame(fr_main, width = '100', height = '418', bg = '#A9011D')
fr_add.pack()
fr_add.pack_propagate(0)
fr_add.place(x = 778, y = 0)