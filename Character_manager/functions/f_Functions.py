import tkinter as tk
from PIL import Image
import PIL.Image
import PIL.ImageTk
from functools import partial

"""
Cree une frame selon les parametres passes
	container -> widget contenant la frame
	width 
"""
def createFrame(container, width, height, **kwargs) :
	fr = tk.Frame(container, width = width, height = height)

	x  = kwargs.get('x')
	y  = kwargs.get('y')
	bg = kwargs.get('bg')
	pk = kwargs.get('pk')
	pp = kwargs.get('pp')

	if pk :
		fr.pack()
	if pp :
		fr.pack_propagate(0)
	if x and y :
		fr.place(x = int(x), y = int(y))
	if bg :
		fr.config(bg = bg)

	return(fr)

def defineWindow(win_width, win_height, **kwargs) :

	title    = kwargs.get('title')
	icon     = kwargs.get('icon')
	toplevel = kwargs.get('toplevel')
	grab     = kwargs.get('grab')

	if toplevel :
		win = tk.Toplevel(toplevel)
		width = int((toplevel.geometry()).split('x')[0]) # Largeur de la fenetre 'root'
		height = int((toplevel.geometry()).split('x')[1].split('+')[0]) # Hauteur de la fenetre 'root'
		x = int((toplevel.geometry()).split('x')[1].split('+')[1]) # Position 'x' de la fenetre root
		y = int((toplevel.geometry()).split('x')[1].split('+')[2])# Position 'y' de la fenetre 'root'

		y += (height/2) - (win_height/2)    # Definition des position du coin superieur gauche de la fenetre dans l'ecran
		x += (width/2) - (win_width/2)  # //

	else :
		win = tk.Tk()
		screen_width = win.winfo_screenwidth() # Largeur de l'ecran
		screen_height = win.winfo_screenheight() # Hauteur de l'ecran

		x = (screen_width/2) - (win_width/2)    # Definition des position du coin superieur gauche de la fenetre dans l'ecran
		y = (screen_height/2) - (win_height/2)  # //

	if grab :
		win.grab_set()

	if title :
		win.title(title) # Titre de la fenêtre

	if icon :
		win.iconbitmap(icon)


	win.geometry('%dx%d+%d+%d' % (win_width, win_height, x, y)) # Placement de la fenetre
	win.resizable(0,0) # Suppression du redimensionnage de la fenetre

	return(win)

def createLabel(container, **kwargs) :

	w      = kwargs.get('w')
	h      = kwargs.get('h')
	bg     = kwargs.get('bg')
	fg     = kwargs.get('fg')
	x      = kwargs.get('x')
	y	   = kwargs.get('y')
	cur    = kwargs.get('cur')
	pp     = kwargs.get('pp')
	txt	   = kwargs.get('txt')
	btn	   = kwargs.get('btn')
	anc    = kwargs.get('anc')


	lb = tk.Label(container)
	lb.pack()
	if pp :
		lb.pack_propagate(0)
	if w :
		lb.config(width = w)
	if h :
		lb.config(height = h)
	if bg :
		lb.config(bg = bg)
	if fg :
		lb.config(fg = fg)
	if x and y :
		lb.place(x = int(x), y = int(y))
	if cur :
		lb.config(cursor = cur)
	if txt :
		lb.config(text = txt)
	if anc :
		lb.config(anchor = anc)
	if btn == 1 and bg and fg :
		lb.bind('<Enter>', lambda event : event.widget.config(bg = '#A6ABAA', fg = 'white'))
		lb.bind('<Leave>', lambda event : event.widget.config(bg = bg, fg = fg))
	elif btn == 2 :
		lb.bind('<Enter>', lambda event : event.widget.config(relief = 'sunken'))
		lb.bind('<Leave>', lambda event : event.widget.config(relief = 'flat'))
	elif btn == 3 :
		lb.bind('<Enter>', lambda event : event.widget.config(bg = '#252A29'))
		lb.bind('<Leave>', lambda event : event.widget.config(bg = bg))
	return(lb)

def createEntry(container, **kwargs) :

	w      = kwargs.get('w')
	h      = kwargs.get('h')
	bg     = kwargs.get('bg')
	fg     = kwargs.get('fg')
	x      = kwargs.get('x')
	y	   = kwargs.get('y')

	en = tk.Entry(container)

	if w :
		en.config(width = w)
	if h :
		en.config(height = h)
	if bg :
		en.config(bg = bg)
	if fg :
		en.config(fg = fg)
	en.pack()
	en.pack_propagate(0)

	if x and y :
		en.place(x = int(x), y = int(y))

	return(en)

"""
Permet d'executer plusieurs fonctions avec un seul event
	*funcs            -> fonctions a executer 
	*args / **kwargs  -> arguments des fonctions
"""
def combineFuncs(*funcs):
	def combined_func(*args, **kwargs):
		for f in funcs: # Pour chaque element presente dans combinedFuncs()...
			f(*args, **kwargs) # ...on lui applique ses arguments
		return combined_func


"""
Generation d'une image avec PILLOW
	img_loc   -> chemin d'acces vers l'image a afficher
	width     -> largeur de l'image
	height    -> hauteur de l'image
	container -> widget contenant le LABEL qui contient l'image

	return    -> le LABEL contenant l'image
"""
def generateImage(img_loc, width, height, container, **kwargs) :

	bg  = kwargs.get('bg')
	x   = kwargs.get('x')
	y   = kwargs.get('y')
	cur = kwargs.get('cur')

	img = PIL.Image.open(img_loc) # Ouverture de l'image avec PILLOW
	img = img.resize((width, height), PIL.Image.ANTIALIAS) # Redimensionnage de l'image et application de l'anti-aliasing
	img = PIL.ImageTk.PhotoImage(img)  # Conversion de l'image PILLOW vers l'image Tkinter
	
	lb_img = tk.Label(container, image = img, bg = "#252A29") # Création du container pour l'image
	if bg :
		lb_img.config(bg = bg)
	lb_img.image = img # Attribution de l'image au container
	lb_img.pack()

	if x and y :
		lb_img.place(x = int(x), y = int(y))

	if cur :
		lb_img.config(cursor = cur)
	return(lb_img)


def changeImage(img_loc, container, width, height, temp1, **kwargs) :

	bg = kwargs.get('bg')

	img = PIL.Image.open(img_loc) # Ouverture de l'image avec PILLOW
	img = img.resize((width, height), PIL.Image.ANTIALIAS) # Redimensionnage de l'image et application de l'anti-aliasing
	img = PIL.ImageTk.PhotoImage(img) #Conversion de l'image PILLOW vers l'image Tkinter

	container.config(image = img) # Application de la nouvelle image au container 
	container.image = img
	if bg :
		container.config(bg = bg)



def changeBtnPic(buttons, pics, pics_hover, width, height, event, temp1) :
	for i in range (0, len(buttons)) : # Pour chaque objet a l'index i dans le tableau buttons...
		clicked_frame = event.widget # ...attribution du widget qui a declenche l'event a la variable clicked_frame 
		if clicked_frame == buttons[i] : # Si le widget a declenche l'event est le meme que celui parcouru dans le tableau
			# print("=========CLICKED FRAME=========\nCLICKED FRAME : ", clicked_frame, ".\nBUTTONS[i] : ", buttons[i], "\nEVENT.WIDGET : ", event.widget, '\n===============================')
			changeImage(pics_hover[i], buttons[i], width, height, 0) # Redirection vers la fonctions Functions.changeImage() pour appliquer l'image '_hover'
			buttons[i].unbind('<Leave>') # Suppression de l'evenement <Leave> du widget pour eviter le changement d'image lors du survol

		elif clicked_frame != buttons[i] :
			# print("============FRAMES=============\nCLICKED FRAME : ", clicked_frame, ".\nBUTTONS[i] : ", buttons[i], "\nEVENT.WIDGET : ", event.widget, '\n===============================')
			changeImage(pics[i], buttons[i], width, height, 0)
			buttons[i].bind('<Leave>', partial(changeImage, pics[i], buttons[i], width, height))

	# print('\n\n\n')

def createText(container, **kwargs) :

	bg   = kwargs.get('bg')
	fg   = kwargs.get('fg')
	h    = kwargs.get('h')
	w    = kwargs.get('w')
	x    = kwargs.get('x')
	y    = kwargs.get('y')
	fnt  = kwargs.get('fnt')
	bw   = kwargs.get('bw')
	hb   = kwargs.get('hb')
	ib   = kwargs.get('ib')

	txt = tk.Text(container, wrap = 'word')
	txt.pack()
	txt.pack_propagate(0)

	if bg : 
		txt.config(bg = bg)

	if ib :
		txt.config(insertbackground = ib)

	if fg :
		txt.config(fg = fg)

	if h :
		txt.config(height = h)

	if w :
		txt.config(width = w)

	if fnt :
		txt.config(font = fnt)

	if bw :
		txt.config(borderwidth = int(bw))

	if hb :
		txt.config(highlightbackground = hb)
	if x and y :
		txt.place(x = int(x), y = int(y))		
	
	return(txt)

def createListBox(container, **kwargs) :

	bg  = kwargs.get('bg')
	cur = kwargs.get('cur')
	fg  = kwargs.get('fg')
	hb  = kwargs.get('hb')
	hc  = kwargs.get('hc')
	sf  = kwargs.get('sf')
	sb  = kwargs.get('sb')
	sm  = kwargs.get('sm')
	sf  = kwargs.get('sf')
	w   = kwargs.get('w')
	h   = kwargs.get('h')
	x   = kwargs.get('x')
	y   = kwargs.get('y')
	es  = kwargs.get('es')

	lb = tk.Listbox(container)
	lb.pack()
	lb.pack_propagate(0)

	if bg :
		lb.config(bg = bg)
	if cur :
		lb.config(cursor = cur)
	if fg :
		lb.confg(fg = fg)
	if hb : 
		lb.config(highlightbackground = hb)
	if not es : 
		lb.config(exportselection = 0)
	if sb :
		lb.config(selectbackground = sb)
	if hc :
		lb.config(highlightcolor = hc)
	if sf :
		lb.config(selectforeground = sf)
	if sm :
		lb.config(selectmode = sm)
	if w :
		lb.config(width = w)
	if h :
		lb.config(height = h)
	if x and y :
		lb.place(x = x, y = y)

	return(lb)

def getRows(loc, menu) :
	rows = []
	with open(loc, 'r', newline = '') as file :
		for row in file :
			if menu in row :
				rows.append(row)
	file.close()
	return(rows)

def selectListValues(lstbox):
	values = []
	reslist = list()
	selection = lstbox.curselection()
	for i in selection:
		entry = lstbox.get(i)
		reslist.append(entry)
	for i in reslist:
		values.append(i)
	return(values)

def changeBg(frames, event) :
	for i in frames :
		if i == event.widget :
			i.config(bg = '#252A29')
		else :
			i.config(bg = '#A6ABAA')
			print(i)