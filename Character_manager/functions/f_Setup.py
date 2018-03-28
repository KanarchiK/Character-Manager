import sys
sys.path.insert(0, '../classes')
import re
import c_Frames
import os
from pathlib import Path
from f_Functions import createFrame, defineWindow, createLabel, createEntry, combineFuncs
from d_Setup import loadedSetup
from tkinter.filedialog import askopenfilename

def newSetup(dir, allFrames) :
	root = allFrames.getFrame('root')
	win_prompt = defineWindow(301, 100, title = 'Nouveau Setup', icon = dir + "/resources/images/icons/CM.ico", toplevel = root, grab = 1)
	fr_prompt  = createFrame(win_prompt, '301', '100', bg = '#252A29', pk = 1, x = '0', y = '0', pp = 1)
	lb_enter_name = createLabel(fr_prompt, txt = "NOM DU SETUP", bg = "#252A29", fg = 'white')
	en_name    = createEntry(fr_prompt, w = 40, x = '30', y = '40')
	en_name.focus_set()

	lbtn_ok = createLabel(fr_prompt, w = '8', h = '1', txt = 'Ok', bg = '#A6ABAA', fg = '#A9011D', pp = 1, btn = 2, x = '86', y = '75')
	lbtn_cancel = createLabel(fr_prompt, w = '8', h = '1', txt = 'Annuler', bg = '#A6ABAA', fg = '#A9011D', pp = 1, btn = 2, x = '153', y = '75')

	lbtn_ok.bind('<Button-1>', lambda event : checkEntry(dir, allFrames, en_name.get(), win_prompt))
	lbtn_cancel.bind('<Button-1>', lambda event : win_prompt.destroy())

def checkEntry(dir, allFrames, entry, window) :
	regex = r"^[A-Za-z0-9]{1,}$" # Definition d'une regex de vérification : on autorise que les lettres, les chiffres et les '.' avec un minimum de 1

	if not re.match(regex, entry) or entry == '': # Si le texte entre ne match pas la regex OU si le champ d'entree est vide ...
		win_error = defineWindow(200, 50, title = 'Erreur', icon = dir + '/resources/images/icons/CM.ico', toplevel = window, grab = 1)
		fr_error  = createFrame(win_error, '200', '50', bg = '#252A29', pk = 1, pp = 1)
		lb_error  = createLabel(fr_error, bg = '#252A29', fg = 'white', txt = 'Nom invalide !')
		lbtn_ok   = createLabel(fr_error, bg = '#A6ABAA', fg = '#A9011D', txt = 'Ok', w = '8', h = '1', pp = 1, btn = 2, x = '69', y = '25')
		lbtn_ok.bind('<Button-1>', lambda event : win_error.destroy())

	else :
		setup_file = Path(dir + '/setups/' + entry + '.setup') 
		if setup_file.is_file() : # Si le fichier '.setup' existe deja...
			win_error 	= defineWindow(200, 50, title = 'Fichier existant', icon = dir + '/resources/images/icons/CM.ico', toplevel = window, grab = 1)
			fr_error  	= createFrame(win_error, '200', '50', bg = '#252A29', pk = 1, pp = 1)
			lb_error  	= createLabel(fr_error, bg = '#252A29', fg = 'white', txt = 'Setup déjà existant. L\'écraser ?')
			lbtn_ok   	= createLabel(fr_error, bg = '#A6ABAA', fg = '#A9011D', txt = 'Ok', w = '8', h = '1', pp = 1, btn = 2, x = '36', y = '25')
			lbtn_cancel = createLabel(fr_error, bg = '#A6ABAA', fg = '#A9011D', txt = 'Annuler', w = '8', h = '1', pp = 1, btn = 2, x = '102', y = '25')
			lbtn_ok.bind('<Button-1>', lambda event : combineFuncs(os.remove(dir + "/setups/" + entry + ".setup"), addSetup(dir, entry, allFrames), window.destroy(), win_error.destroy()))
			lbtn_cancel.bind('<Button-1>', lambda event : win_error.destroy())

		else :
			window.destroy()
			addSetup(dir, entry, allFrames)

def addSetup(dir, setup_name, allFrames) :
	open(dir + '/setups/' + setup_name + '.setup', 'w')
	root = allFrames.getFrame('root')
	win_success  = defineWindow(250, 50, title = 'Setup créé !', icon = dir + '/resources/images/icons/CM.ico', toplevel = root, grab = 1)
	fr_success   = createFrame(win_success, '250', '50', bg = '#252A29', pk = 1, pp = 1)
	lb_success   = createLabel(fr_success, txt = 'Le setup \'' + setup_name + '\' a été crée avec succès !', bg = '#252A29', fg = 'white', pp = 1)
	lbtn_success = createLabel(fr_success, txt = 'Excellent, laisse-moi continuer.', bg = '#A6ABAA', fg = '#A9011D', w = '25', h = '1', pp = 1, x = '35', y = '25', btn = 2) 
	lbtn_success.bind('<Button-1>', lambda event : combineFuncs(loadedSetup(dir, allFrames, setup_name), win_success.destroy()))


def loadSetup(dir, allFrames) :
	fname = askopenfilename(initialdir = dir + "/setups", title = "Sélectioner un setup", filetypes = (("Setup files", "*.setup"), ("All files", "*.*")))
	if fname.split(".")[-1] != 'setup' :
		root = allFrames.getFrame('root')
		win_error = defineWindow(200, 50, title = 'Erreur', icon = dir + '/resources/images/icons/CM.ico', toplevel = root, grab = 1)
		fr_error  = createFrame(win_error, '200', '50', bg = '#252A29', pk = 1, pp = 1)
		lb_error  = createLabel(fr_error, bg = '#252A29', fg = 'white', txt = 'Le fichier sélectionné n\'est pas valide')
		lbtn_ok   = createLabel(fr_error, bg = '#A6ABAA', fg = '#A9011D', txt = 'Ok', w = '8', h = '1', pp = 1, btn = 2, x = '69', y = '25')
		lbtn_ok.bind('<Button-1>', lambda event : combineFuncs(win_error.destroy()))

	else :
		print(fname)
		setup_name = fname.split("/")[-1].split(".")[0]
		loadedSetup(dir, allFrames, setup_name)