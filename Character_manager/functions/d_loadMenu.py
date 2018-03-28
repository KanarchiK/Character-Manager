import tkinter as tk
import sys
sys.path.insert(0, '../classes')
from c_Frames import *
from f_Functions import createFrame, createLabel, generateImage, changeImage, changeBtnPic, combineFuncs, createEntry, changeBg
from d_createChar import newChar
from d_Infos import getInfos


def loadMenu(dir, allFrames, setup_name, menu) :
	def compare(cur, max, lb) :
		if int(cur) < int(max) :
			lb.config(fg = '#FE0101')
		elif int(cur) > int(max) :
			lb.config(fg = '#379E1D')
	dictAll = allFrames.getAllFrames()

	fr_create = allFrames.getFrame('createChar')
	if fr_create :
		fr_create.destroy()

	fr_center = allFrames.getFrame('centerBase')
	fr_center.config(width = '878')

	fr_main = createFrame(fr_center, '778', '418', bg = '#252A29', x = '0', y = '0', pk = 1, pp = 1)


	cpt = 0
	x = '10'
	char_list = []
	with open(dir + '/setups/' + setup_name + '.setup', 'r', newline = '') as file :
		for row in file :
			if menu.upper() in row :
				cpt += 1
		print(cpt) 
	file.close()

	frames = []
	with open(dir + '/setups/' + setup_name + '.setup', 'r', newline = '') as file :
		# for row in file :
		# 	if menu.upper() in row :
		# 		cpt += 1
		# print(cpt) 
		for row in file :
			if menu.upper() in row :
				s = row.split(';;')
				name           = s[1]
				race           = s[2]
				char_class     = s[3]
				cur_str        = s[4]
				max_str        = s[5]
				cur_con        = s[6]
				max_con        = s[7]
				cur_dex        = s[8]
				max_dex        = s[9]
				cur_int        = s[10]
				max_int        = s[11]
				cur_per        = s[12]
				max_per        = s[13]
				cur_cha        = s[14]
				max_cha        = s[15]
				cur_hea        = s[16]
				max_hea        = s[17]
				cur_man        = s[18]
				max_man        = s[19]
				cur_phy_arm    = s[20]
				max_phy_arm    = s[21]
				cur_mag_arm    = s[22]
				max_mag_arm    = s[23]
				weapons        = s[24]
				trinkets       = s[25]
				effects        = s[26]
				spells         = s[27]
				helm           = s[28]
				chest          = s[29]
				hands          = s[30]
				boots          = s[31]
				desc           = s[32]

				char_list.append(row)

				can_chars = tk.Canvas(fr_main, bg = '#252A29', highlightthickness = 0, width = cpt*220)

				scrl = tk.Scrollbar(fr_main, orient = "horizontal", command = can_chars.xview)
				# can_chars.configure(xscrollcommand = scrl.set)
				# scrl.pack(side="bottom", fill="x")
				can_chars.pack(side = "left", fill="both", expand = True)

				fr_char = createFrame(fr_center, '200', '375	', bg = '#CCCCCC', x = x, y = '10', pk = 1, pp = 1, btn = 2)
				fr_char.bind('<Enter>', lambda event : event.widget.config(highlightthickness = 2, highlightbackground = '#A9011D'))
				fr_char.bind('<Leave>', lambda event : event.widget.config(highlightthickness = 0))
				fr_char.bind('<Button-1>', lambda event : getInfos(dir, setup_name, frames, char_list, allFrames, event.widget))

				lb_name = createLabel(fr_char, txt = name, bg = '#CCCCCC', x = '2', y = '2', w = '11', h = '1', pp = 1)
				lb_name.config(font = ('Arial', 20))

				lb_rc = createLabel(fr_char, txt = race + ' ' + char_class, bg = '#CCCCCC', w = '22', x = '2', y = '32')
				lb_rc.config(font = ('Arial', 10, 'italic'))


				lb_mag_arm = createLabel(fr_char, txt = 'Armure  Magique', bg = '#CCCCCC', x = '2', y = '348', w = '14', h = '1', pp = 1, anc = 'w')
				lb_mag_arm.config(font = ('Arial', 10, 'bold'))
				lb_cur_mag_arm = createLabel(fr_char, txt = cur_mag_arm, bg = '#CCCCCC', x = '140', y = '348', w = '2', h = '1',  pp = 1, anc = 'e')
				compare(cur_mag_arm, max_mag_arm, lb_cur_mag_arm)
				lb_max_mag_arm = createLabel(fr_char, txt = '/ ' + max_mag_arm, bg = '#CCCCCC', x = '160', y = '348', w = '4', h = '1', pp = 1)

				lb_phy_arm = createLabel(fr_char, txt = 'Armure  Physique', bg = '#CCCCCC', x = '2', y = '323', w = '14', h = '1', pp = 1, anc = 'w')
				lb_phy_arm.config(font = ('Arial', 10, 'bold'))
				lb_cur_phy_arm = createLabel(fr_char, txt = cur_phy_arm, bg = '#CCCCCC', x = '140', y = '323', w = '2', h = '1',  pp = 1, anc = 'e')
				compare(cur_phy_arm, max_phy_arm, lb_cur_phy_arm)
				lb_max_phy_arm = createLabel(fr_char, txt = '/ ' + max_phy_arm, bg = '#CCCCCC', x = '160', y = '323', w = '4', h = '1', pp = 1)

				lb_man = createLabel(fr_char, txt = 'Mana', bg = '#CCCCCC', x = '2', y = '298', w = '10', h = '1', pp = 1 , anc = 'w')
				lb_man.config(font = ('Arial', 10, 'bold'))
				lb_cur_man = createLabel(fr_char, txt = cur_man, bg = '#CCCCCC', x = '140', y = '398', w = '2', h = '1', pp = 1, anc = 'e')
				compare(cur_man, max_man, lb_cur_man)
				lb_max_man = createLabel(fr_char, txt = '/ ' + max_man, bg = '#CCCCCC', x = '160', y = '298', w = '4', h = '1', pp = 1)

				lb_hea = createLabel(fr_char, txt = 'Santé', bg = '#CCCCCC', x = '2', y = '250', w = '10', h = '1', pp = 1 , anc = 'w')
				lb_hea.config(font = ('Arial', 10, 'bold'))
				lb_cur_hea = createLabel(fr_char, txt = cur_hea, bg = '#CCCCCC', x = '140', y = '250', w = '2', h = '1', pp = 1, anc = 'e')
				compare(cur_hea, max_hea, lb_cur_hea)
				lb_max_hea = createLabel(fr_char, txt = '/ ' + max_hea, bg = '#CCCCCC', x = '160', y = '250', w = '4', h = '1', pp = 1)

				lb_cha = createLabel(fr_char, txt = 'Charisme', bg = '#CCCCCC', x = '2', y = '225', w = '10', h = '1', pp = 1 , anc = 'w')
				lb_cha.config(font = ('Arial', 10, 'bold'))
				lb_cur_cha = createLabel(fr_char, txt = cur_cha, bg = '#CCCCCC', x = '140', y = '225', w = '2', h = '1', pp = 1, anc = 'e')
				compare(cur_cha, max_cha, lb_cur_cha)
				lb_max_cha = createLabel(fr_char, txt = '/ ' + max_cha, bg = '#CCCCCC', x = '160', y = '225', w = '4', h = '1', pp = 1)

				lb_per = createLabel(fr_char, txt = 'Perception', bg = '#CCCCCC', x = '2', y = '200', w = '10', h = '1', pp = 1 , anc = 'w')
				lb_per.config(font = ('Arial', 10, 'bold'))
				lb_cur_per = createLabel(fr_char, txt = cur_per, bg = '#CCCCCC', x = '140', y = '200', w = '2', h = '1', pp = 1, anc = 'e')
				compare(cur_per, max_per, lb_cur_per)
				lb_max_per = createLabel(fr_char, txt = '/ ' + max_per, bg = '#CCCCCC', x = '160', y = '200', w = '4', h = '1', pp = 1)

				lb_int = createLabel(fr_char, txt = 'Intelligence', bg = '#CCCCCC', x = '2', y = '175', w = '10', h = '1', pp = 1 , anc = 'w')
				lb_int.config(font = ('Arial', 10, 'bold'))
				lb_cur_int = createLabel(fr_char, txt = cur_int, bg = '#CCCCCC', x = '140', y = '175', w = '2', h = '1', pp = 1, anc = 'e')
				compare(cur_int, max_int, lb_cur_int)
				lb_max_int = createLabel(fr_char, txt = '/ ' + max_int, bg = '#CCCCCC', x = '160', y = '175', w = '4', h = '1', pp = 1)

				lb_dex = createLabel(fr_char, txt = 'Dextérité', bg = '#CCCCCC', x = '2', y = '150', w = '10', h = '1', pp = 1 , anc = 'w')
				lb_dex.config(font = ('Arial', 10, 'bold'))
				lb_cur_dex = createLabel(fr_char, txt = cur_dex, bg = '#CCCCCC', x = '140', y = '150', w = '2', h = '1', pp = 1, anc = 'e')
				compare(cur_dex, max_dex, lb_cur_dex)
				lb_max_dex = createLabel(fr_char, txt = '/ ' + max_dex, bg = '#CCCCCC', x = '160', y = '150', w = '4', h = '1', pp = 1)

				lb_con = createLabel(fr_char, txt = 'Constitution', bg = '#CCCCCC', x = '2', y = '125', w = '10', h = '1', pp = 1 , anc = 'w')
				lb_con.config(font = ('Arial', 10, 'bold'))
				lb_cur_con = createLabel(fr_char, txt = cur_con, bg = '#CCCCCC', x = '140', y = '125', w = '2', h = '1', pp = 1, anc = 'e')
				compare(cur_con, max_con, lb_cur_con)
				lb_max_con = createLabel(fr_char, txt = '/ ' + max_con, bg = '#CCCCCC', x = '160', y = '125', w = '4', h = '1', pp = 1)

				lb_str = createLabel(fr_char, txt = 'Force', bg = '#CCCCCC', x = '2', y = '100', w = '10', h = '1', pp = 1 , anc = 'w')
				lb_str.config(font = ('Arial', 10, 'bold'))
				lb_cur_str = createLabel(fr_char, txt = cur_str, bg = '#CCCCCC', x = '140', y = '100', w = '2', h = '1', pp = 1, anc = 'e')
				compare(cur_str, max_str, lb_cur_str)
				lb_max_str = createLabel(fr_char, txt = '/ ' + max_str, bg = '#CCCCCC', x = '160', y = '100', w = '4', h = '1', pp = 1)


				labels = [
						fr_char,
						lb_name,
						lb_rc,
						lb_phy_arm,
						lb_cur_phy_arm,
						lb_max_phy_arm,
						lb_mag_arm,
						lb_cur_mag_arm,
						lb_max_mag_arm,
						lb_man,
						lb_cur_man,
						lb_max_man,
						lb_hea,
						lb_cur_hea,
						lb_max_hea,
						lb_cha,
						lb_cur_cha,
						lb_max_cha,
						lb_per,
						lb_cur_per,
						lb_max_per,
						lb_int,
						lb_cur_int,
						lb_max_int,
						lb_dex,
						lb_cur_dex,
						lb_max_dex,
						lb_con,
						lb_cur_con,
						lb_max_con,
						lb_str,
						lb_cur_con,
						lb_max_str
						]


				frames.append(fr_char)
				x = int(x)
				x += 220
				str(x)
				print(x)
				dictAll[name] = fr_char

	fr_add_char = createFrame(fr_center, '100', '418', bg = '#A9011D', x = '776', y = '0', pk = 1, pp = 1, btn = 2)
	lbtn_add_char = generateImage(dir + '/resources/images/buttons/add_char.png', 87, 405, fr_add_char,  bg = '#252A29', x = '5', y = '5', cur = 'hand2')

	lbtn_add_char.bind("<Enter>", lambda event : changeImage(dir + "/resources/images/buttons/add_char_hover.png", lbtn_add_char, 87, 405, 0, bg = "white"))
	lbtn_add_char.bind("<Leave>", lambda event : changeImage(dir + "/resources/images/buttons/add_char.png", lbtn_add_char, 87, 405, 0, bg = "#252A29"))
	lbtn_add_char.bind('<Button-1>', lambda event : newChar(dir, setup_name, allFrames, menu))


	dictAll['addChar'] = fr_add_char			
	allFrames.setAllFrames(dictAll)