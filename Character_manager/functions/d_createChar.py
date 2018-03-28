import sys
sys.path.insert(0, '../classes')
from c_Frames import *
import tkinter as tk
from f_Functions import createLabel, createFrame, createEntry, changeImage, createText, createListBox, getRows
from functools import partial
from f_createChar import createChar

def newChar(dir, setup_name, allFrames, menu) :
	if allFrames.getFrame('char') :
		allFrames.getFrame('char').destroy()

	lbtn_npcs    = allFrames.getFrame('lbtnNPCS')
	lbtn_enemies = allFrames.getFrame('lbtnENEMIES')
	lbtn_players = allFrames.getFrame('lbtnPLAYERS')

	changeImage(dir + "/resources/images/buttons/npcs.png", lbtn_npcs, 204, 100, 0)
	changeImage(dir + "/resources/images/buttons/enemies.png", lbtn_enemies, 204, 100, 0)
	changeImage(dir + "/resources/images/buttons/players.png", lbtn_players, 204, 100, 0)
	lbtn_npcs.bind("<Leave>", partial(changeImage, dir + "/resources/images/buttons/npcs.png", lbtn_npcs, 204, 100))
	lbtn_enemies.bind("<Leave>", partial(changeImage, dir + "/resources/images/buttons/enemies.png", lbtn_enemies, 204, 100))
	lbtn_players.bind("<Leave>", partial(changeImage, dir + "/resources/images/buttons/players.png", lbtn_players, 204, 100))

	allFrames.kill('addChar')
	fr_center = allFrames.getFrame('centerBase')
	fr_center.config(width = '876')

	fr_menu = createFrame(fr_center, '876', '418', bg = '#252A29', x = '0', y = '0', pk = 1, pp = 1)

	lb_name = createLabel(fr_menu, w = 9, h = 1, txt = 'Nom', bg = '#252A29', fg = 'white', x = '0', y = '2', anc = 'e', pp = 1)
	en_name = createEntry(fr_menu, w = 30, x = '70', y = '2')

	lb_race = createLabel(fr_menu, w = 9, h = 1, txt = 'Race', bg = '#252A29', fg = 'white', x = '0', y = '35', anc = 'e', pp = 1)
	en_race = createEntry(fr_menu, w = 30, x = '70', y = '35')

	lb_class = createLabel(fr_menu, w = 9, h = 1, txt = 'Classe', bg = '#252A29', fg = 'white', x = '0', y = '70', anc = 'e', pp = 1)
	en_class = createEntry(fr_menu, w = 30, x = '70', y = '70')

	lb_str     = createLabel(fr_menu, w = 9, h = 1, txt = 'Force', bg = '#252A29', fg = 'white', x = '0', y = '140', anc = 'e', pp = 1)
	en_str 	   = createEntry(fr_menu, w = 3, x = '70', y = '140')
	lb_str_max = createLabel(fr_menu, txt = '/ 100', bg = '#252A29', fg = 'white', x = '90', y = '140', pp = 1)


	lb_con = createLabel(fr_menu, w = 9, h = 1, txt = 'Constitution', bg = '#252A29', fg = 'white', x = '0', y = '175', anc = 'e', pp = 1)
	en_con = createEntry(fr_menu, w = 3, x = '70', y = '175')
	lb_con_max = createLabel(fr_menu, txt = '/ 100', bg = '#252A29', fg = 'white', x = '90', y = '175', pp = 1)


	lb_dex = createLabel(fr_menu, w = 9, h = 1, txt = 'Dextérité', bg = '#252A29', fg = 'white', x = '0', y = '210', anc = 'e', pp = 1)
	en_dex = createEntry(fr_menu, w = 3, x = '70', y = '210')
	lb_dex_max = createLabel(fr_menu, txt = '/ 100', bg = '#252A29', fg = 'white', x = '90', y = '210', pp = 1)


	lb_int = createLabel(fr_menu, w = 9, h = 1, txt = 'Intelligence', bg = '#252A29', fg = 'white', x = '0', y = '245', anc = 'e', pp = 1)
	en_int = createEntry(fr_menu, w = 3, x = '70', y = '245')
	lb_int_max = createLabel(fr_menu, txt = '/ 100', bg = '#252A29', fg = 'white', x = '90', y = '245', pp = 1)


	lb_per = createLabel(fr_menu, w = 9, h = 1, txt = 'Perception', bg = '#252A29', fg = 'white', x = '0', y = '280', anc = 'e', pp = 1)
	en_per = createEntry(fr_menu, w = 3, x = '70', y = '280')
	lb_per_max = createLabel(fr_menu, txt = '/ 100', bg = '#252A29', fg = 'white', x = '90', y = '280', pp = 1)


	lb_cha = createLabel(fr_menu, w = 9, h = 1, txt = 'Charisme', bg = '#252A29', fg = 'white', x = '0', y = '315', anc = 'e', pp = 1)
	en_cha = createEntry(fr_menu, w = 3, x = '70', y = '315')
	lb_cha_max = createLabel(fr_menu, txt = '/ 100', bg = '#252A29', fg = 'white', x = '90', y = '315', pp = 1)

	fr_create = createFrame(fr_menu, '248', '65', bg = '#A9011D', x = '7', y = '345', pk = 1, pp = 1)
	lbtn_create = createLabel(fr_create, w = 9, h = 1, bg = '#252A29', txt = 'CRÉER', fg = '#A9011D', x = '4', y = '4', pp = 1, btn = 1, cur = 'hand2')
	lbtn_create.config(font = ('Arial', 33 ))


	lb_hea = createLabel(fr_menu, w = 15, h = 1, txt = 'Santé', bg = '#252A29', fg = 'white', x = '120', y = '140', anc = 'e', pp = 1)
	en_hea = createEntry(fr_menu, w = 3, x = '230', y = '140')


	lb_man = createLabel(fr_menu, w = 15, h = 1, txt = 'Mana', bg = '#252A29', fg = 'white', x = '120', y = '175', anc = 'e', pp = 1)
	en_man = createEntry(fr_menu, w = 3, x = '230', y = '175')


	lb_phy_arm = createLabel(fr_menu, w = 15, h = 1, txt = 'Armure physique', bg = '#252A29', fg = 'white', x = '120', y = '210', anc = 'e', pp = 1)
	en_phy_arm = createEntry(fr_menu, w = 3, x = '230', y = '210')

	lb_mag_arm = createLabel(fr_menu, w = 15, h = 1, txt = 'Armure magique', bg = '#252A29', fg = 'white', x = '120', y = '245', anc = 'e', pp = 1)
	en_mag_arm = createEntry(fr_menu, w = 3, x = '230', y = '245')

	OPTIONS = [
		('Joueur', 'Players'),
		('Ennemi', 'Enemies'),
		('PNJ',    'Npcs')
	]
	rbValue = tk.StringVar()
	rbValue.set(menu)
	fr_rb = createFrame(fr_menu, '93', '90', bg = '#252A29', x = '160', y = '270')
	for text, mode in OPTIONS :
		rb_char = tk.Radiobutton(fr_rb, bg = '#252A29', cursor = 'hand2', fg = '#A9011D', text = text, value = mode, variable = rbValue)
		rb_char.pack(anchor = 'w')



	fr_desc  = createFrame(fr_menu, '555', '88', bg = 'white', x = '300', y = '19', pk = 1, pp = 1)
	txt_desc = createText(fr_desc, bg = "#252A29", fg = 'white', fnt = ('Arial', 10), bw = 0, x = '2', y = '2', h = 5, w = 78, ib = '#A9011D')
	lb_desc  = createLabel(fr_menu, w = 8, h = 1, txt = 'Description', bg = '#252A29', fg = 'white', x = '320', y = '6', pp = 1)

	lb_weapons  = createLabel(fr_menu, txt = 'Armes (2 max)', bg = '#252A29', fg = 'white', x = '290', y = '120', pp = 1, w = 20, h = 1)
	lst_weapons = createListBox(fr_menu, cur = 'hand2', sb = '#A9011D', sf = "white", sm = 'multiple', h = 7, w = 20, x = '300', y = '140', es = 0)

	lb_trinkets  = createLabel(fr_menu,  txt = 'Accessoires', bg = '#252A29', fg = 'white', x = '430', y = '120', pp = 1, w = 20, h = 1)
	lst_trinkets = createListBox(fr_menu, cur = 'hand2', sb = '#A9011D', sf = 'white', sm = 'multiple', h = 7, w = 20, x = '443', y = '140', es = 0)

	lb_effects   = createLabel(fr_menu, txt = 'Effets', bg = '#252A29', fg = 'white', x = '575', y = '120', pp = 1, w = 20, h = 1)
	lst_effects  = createListBox(fr_menu, cur = 'hand2', sb = '#A9011D', sf = 'white', sm = 'multiple', h = 7, w = 20, x = '586', y = '140', es = 0)

	lb_spells   = createLabel(fr_menu, txt = 'Sorts / Compétences', bg = '#252A29', fg = 'white', x = '715', y = '120', pp = 1, w = 20, h = 1)
	lst_spells  = createListBox(fr_menu, cur = 'hand2', sb = '#A9011D', sf = 'white', sm = 'multiple', h = 7, w = 20, x = '728', y = '140', es = 0)



	lb_helm   = createLabel(fr_menu, txt = 'Casque', bg = '#252A29', fg = 'white', x = '335', y = '263', pp = 1)
	lst_helm  = createListBox(fr_menu, cur = 'hand2', sb = '#A9011D', sf = 'white', h = 7, w = 20, x = '300', y = '282', es = 0)

	lb_chest  = createLabel(fr_menu, txt = 'Plastron', bg = '#252A29', fg = 'white', x = '480', y = '263', pp = 1)
	lst_chest = createListBox(fr_menu, cur = 'hand2', sb = '#A9011D', sf = 'white', h = 7, w = 20, x = '443', y = '282', es = 0)

	lb_hands  = createLabel(fr_menu, txt = 'Gants', bg = '#252A29', fg = 'white', x = '625', y = '263', pp = 1)
	lst_hands = createListBox(fr_menu, cur = 'hand2', sb = '#A9011D', sf = 'white', h = 7, w = 20, x = '586', y = '282', es = 0)

	lb_boots  = createLabel(fr_menu, txt = 'Bottes', bg = '#252A29', fg = 'white', x = '770', y = '263', pp = 1)
	lst_boots = createListBox(fr_menu, cur = 'hand2', sb = '#A9011D', sf = 'white', h = 7, w = 20, x = '728', y = '282', es = 0)

	weapons = getRows(dir + '/setups/' + setup_name + '.setup', 'WEAPONS')
	for i in weapons :
		lst_weapons.insert('end', i.split(';')[2])

	trinkets = getRows(dir + '/setups/' + setup_name + '.setup', 'TRINKETS')
	for i in trinkets :
		lst_trinkets.insert('end', i.split(';')[2])

	effects = getRows(dir + '/setups/' + setup_name + '.setup', 'EFFECTS')
	for i in effects :
		lst_effects.insert('end', i.split(';')[2])

	spells = getRows(dir + '/setups/' + setup_name + '.setup', 'SPELLS')
	for i in spells :
		lst_spells.insert('end', i.split(';')[2])

	skills = getRows(dir + '/setups/' + setup_name + '.setup', 'SKILLS')
	for i in skills :
		lst_skills.insert('end', i.split(';')[2])

	helm = getRows(dir + '/setups/' + setup_name + '.setup', 'HELM')
	for i in helm :
		lst_helm.insert('end', i.split(';')[2])

	chest = getRows(dir + '/setups/' + setup_name + '.setup', 'CHEST')
	for i in chest :
		lst_chest.insert('end', i.split(';')[2])

	hands = getRows(dir + '/setups/' + setup_name + '.setup', 'HANDS')
	for i in hands :
		lst_hands.insert('end', i.split(';')[2])

	boots = getRows(dir + '/setups/' + setup_name + '.setup', 'BOOTS')
	for i in boots :
		lst_boots.insert('end', i.split(';')[2])

	lbtn_create.bind('<Button-1>', lambda event : createChar(dir, setup_name, allFrames, lst_weapons, lst_trinkets, lst_effects, lst_spells, lst_helm, lst_chest, lst_hands, lst_boots, dict([
		('name', en_name.get()),
		('race', en_race.get()),
		('class', en_class.get()),
		('str', en_str.get()),
		('con', en_con.get()), 
		('dex', en_dex.get()),
		('int', en_int.get()),
		('per', en_per.get()),
		('cha', en_cha.get()),
		('desc', txt_desc.get(1.0, 'end'+'-1c')),
		('hea', en_hea.get()),
		('man', en_man.get()),
		('phyArm', en_phy_arm.get()),
		('magArm', en_mag_arm.get()),
		('menu', rbValue.get()),
	])))
	
	alldict = allFrames.getAllFrames()
	alldict['createChar'] = fr_menu
	allFrames.setAllFrames(alldict)