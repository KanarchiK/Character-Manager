import tkinter as tk
import sys
sys.path.insert(0, '../classes')
from c_Frames import *
from f_Functions import createFrame, createLabel, combineFuncs, createEntry, changeBg, createText

def getInfos(dir, setup_name, frames, char_list, allFrames, widget) :
	for i in frames :
		if i == widget :
			print(i, widget)
			name = widget.winfo_children()[0].cget('text')
	for i in char_list :
		if name == i.split(';;')[1] :
			char = i.split(';;')


	fr_right = allFrames.getFrame('rightBase')

	if allFrames.getFrame('infos') :
		allFrames.getFrame('infos').destroy()

	fr_infos = createFrame(fr_right, '250', '618', bg = '#252A29', x = '0', y = '0', pk = 1, pp = 1)

	lb_name = createLabel(fr_infos, txt = name, bg = '#252A29', fg = 'white', pp = 1)
	lb_name.config(font = ('Arial', 15))

	fr_desc = createFrame(fr_infos, 239, 200, bg = 'white', x = '6', y = '30')
	txt_desc = createText(fr_desc, bg = "#252A29", fg = 'white', fnt = ('Arial', 10), bw = 0, h = 12, w = 33, x = '2', y = '2')
	txt_desc.insert(1.0, char[32])
	txt_desc.config(state = 'disabled')

	fr_buttons_up = createFrame(fr_infos, 250, 20, bg = '#252A29', x = '0', y = '235')
	lb_weapons  = createLabel(fr_buttons_up, w = '11', h = '1', txt = 'Armes', bg = '#A6ABAA', fg = '#A9011D', btn = 2, x = '0', y = '0')
	lb_weapons.bind('<Button-1>', lambda event : combineFuncs(changeBg(buttons, event), display(dir, char, allFrames, 'WEAPONS')))
	lb_armor    = createLabel(fr_buttons_up, w = '11', h = '1', txt = 'Armure', bg = '#A6ABAA', fg = '#A9011D', btn = 2, x = '86', y = '0')
	lb_armor.bind('<Button-1>', lambda event : combineFuncs(changeBg(buttons, event)))
	lb_trinkets = createLabel(fr_buttons_up, w = '11', h = '1', txt = 'Accessoires', bg = '#A6ABAA', fg = '#A9011D', btn = 2, x = '172', y = '0')
	lb_trinkets.bind('<Button-1>', lambda event : combineFuncs(changeBg(buttons, event)))

	fr_buttons_bot = createFrame(fr_infos, 250, 20, bg = '#252A29', x = '0', y = '257')
	lb_effects = createLabel(fr_buttons_bot, w = '16', h = '1', txt = 'Effets', bg = '#A6ABAA', fg = '#A9011D', btn = 2, x = '5', y = '0')
	lb_effects.bind('<Button-1>', lambda event : combineFuncs(changeBg(buttons, event)))
	lb_skills  = createLabel(fr_buttons_bot, w = '16', h = '1', txt = 'Compétences', bg = '#A6ABAA', fg = '#A9011D', btn = 2, x = '127', y = '0')
	lb_skills.bind('<Button-1>', lambda event : combineFuncs(changeBg(buttons, event)))

	dictAll = allFrames.getAllFrames()
	dictAll['infos'] = fr_infos
	allFrames.setAllFrames(dictAll)

	buttons = [lb_weapons, lb_armor, lb_trinkets, lb_effects, lb_skills]

def display(dir, char, allFrames, menu) :
	if allFrames.getFrame('infosMenu') :
		allFrames.getFrame('infoMenu').destroy()

	fr_infos = allFrames.getFrame('infos')

	fr_infos_menu = createFrame(fr_infos, 250, 300, bg = 'red', x = '0', y = '317')

	toInsert = []

	with open(dir + '/setups/' + setup_name + '.setup', 'r', newline = '') as file :
		for row in file :
			if menu in row and menu != 'SKILLS' and menu != 'EFFECTS' :
				toInsert.append(row.split(';;')[1] + ' - ' + row.split())