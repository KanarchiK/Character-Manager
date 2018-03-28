import tkinter as tkinter
import sys
sys.path.insert(0, '../classes')
from c_Frames import *
import os
from f_Functions import createFrame, createLabel, generateImage, changeImage, defineWindow, combineFuncs

def deleteSetup(dir, setup_name, allFrames) :
	root = allFrames.getFrame('root')
	win_ask  = defineWindow(250, 50, title = setup_name, icon = dir + '/resources/images/icons/CM.ico', toplevel = root, grab = 1)
	fr_ask   = createFrame(win_ask, '250', '50', bg = "#252A29", pk = 1, pp = 1)
	lb_ask   = createLabel(fr_ask, txt = 'Voulez-vous supprimer le setup \'' + setup_name + '\' ?', bg  = '#252A29', fg = 'white')
	lbtn_yes = createLabel(fr_ask, bg = '#A6ABAA', fg = '#A9011D', txt = 'Oui', w = '8', h = '1', pp = 1, btn = 2, x = '61', y = '25')
	lbtn_cancel = createLabel(fr_ask, bg = '#A6ABAA', fg = '#A9011D', txt = 'Annuler', w = '8', h = '1', pp = 1, btn = 2, x = '127', y = '25')

	lbtn_yes.bind('<Button-1>', lambda event : combineFuncs(suppression(dir, setup_name, allFrames), win_ask.destroy()))
	lbtn_cancel.bind('<Button-1>', lambda event : win_ask.destroy())

def suppression(dir, setup_name, allFrames) :
	os.remove(dir + "/setups/" + setup_name + ".setup")
	root = allFrames.getFrame('root')
	win_success  = defineWindow(250, 50, title = 'Setup supprimé', icon = dir + '/resources/images/icons/CM.ico', toplevel = root, grab = 1)
	fr_success   = createFrame(win_success, '250', '50', bg = '#252A29', pk = 1, pp = 1)
	lb_success   = createLabel(fr_success, txt = 'Le setup \'' + setup_name + '\' a été supprimé avec succès.', bg = '#252A29', fg = 'white', pp = 1)
	lbtn_success = createLabel(fr_success, txt = 'RIP petit setup', bg = '#A6ABAA', fg = '#A9011D', w = '25', h = '1', pp = 1, x = '35', y = '25', btn = 2) 
	reloadFrames(allFrames)
	lbtn_success.bind('<Button-1>', lambda event : win_success.destroy())

def reloadFrames(allFrames) :
	root = allFrames.getFrame('root')
	fr_left   = allFrames.getFrame('leftBase')
	fr_left.pack()
	fr_left.place(x = 0, y = 102)
	fr_top    = createFrame(root, '1280', '100', bg = '#252A29', x = '0', y = '0', pk = 1, pp = 1) 
	fr_right  = createFrame(root, '250', '618', bg = '#252A29', x = '1030', y = '102', pk = 1, pp = 1)
	fr_bottom = createFrame(root, '1028', '200', bg = '#252A29', x = '0', y = '520', pk = 1, pp = 1)
	fr_center = createFrame(root, '876', '416', bg = '#252A29', x = '152', y = '102', pk = 1, pp = 1)