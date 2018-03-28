import tkinter as tk
import sys
sys.path.insert(0, '../classes')
from c_Frames import *
from f_Functions import createFrame, createLabel, generateImage, changeImage, changeBtnPic, combineFuncs, changeBg
from f_delSetup import deleteSetup
from d_loadMenu import loadMenu
from d_menus import equipment
from functools import partial

def loadedSetup(dir, allFrames, setup_name) :


	fr_left = allFrames.getFrame('leftBase')
	fr_del_setup = createFrame(fr_left, '145', '72', bg = '#A9011D', x = '2', y = '224', pk = 1, pp = 1)
	lbtn_del_setup = createLabel(fr_del_setup, w = 19, h = 4, txt = 'SUPPRIMER SETUP', bg = '#252A29', fg = '#A9011D', cur = 'hand2', x = '3', y = '3', btn = 1, pp = 1)
	lbtn_del_setup.bind('<Button-1>', lambda event : deleteSetup(dir, setup_name, allFrames))

	fr_fight = createFrame(fr_left, '145', '72', bg = '#A9011D', x = '2', y = '326', pk = 1, pp = 1)
	lbtn_fight = generateImage(dir + '/resources/images/buttons/fight.png', 135, 62, fr_fight, bg = '#252A29', x = '3', y = '3', cur = 'hand2')
	lbtn_fight.bind("<Enter>", partial(changeImage, dir + "/resources/images/buttons/fight_hover.png", lbtn_fight, 135, 62, bg = 'white'))
	lbtn_fight.bind("<Leave>", partial(changeImage, dir + "/resources/images/buttons/fight.png", lbtn_fight, 135, 62, bg = '#252A29'))


	fr_top = allFrames.getFrame('topBase')
	fr_setup_name = createFrame(fr_top, '600', '100', bg = '#252A29', pk = 1, pp = 1, x = '0', y = '0')
	lb_setup_name = createLabel(fr_top, txt = setup_name, bg = '#252A29', fg = 'white', x = '10', y = '25')
	lb_setup_name.config(font = ('Arial', 30, 'italic'))

	lbtn_npcs    = generateImage(dir + '/resources/images/buttons/npcs.png', 204, 100, fr_top,  bg = '#252A29', x = '1054', y = '0', cur = 'hand2')
	lbtn_enemies = generateImage(dir + '/resources/images/buttons/enemies.png', 204, 100, fr_top,  bg = '#252A29', x = '830', y = '0', cur = 'hand2')
	lbtn_players = generateImage(dir + '/resources/images/buttons/players.png', 204, 100, fr_top,  bg = '#252A29', x = '606', y = '0', cur = 'hand2')

	lbtn_npcs.bind("<Enter>", partial(changeImage, dir + "/resources/images/buttons/npcs_hover.png", lbtn_npcs, 204, 100))
	lbtn_npcs.bind("<Leave>", partial(changeImage, dir + "/resources/images/buttons/npcs.png", lbtn_npcs, 204, 100))
	# lbtn_npcs.bind("<Button-1>", lambda event : combineFuncs(changeBtnPic(buttons_top, pics, pics_hover, 204, 100, event, 0), loadMenu(dir, allFrames, setup_name, 'Npcs')))

	lbtn_enemies.bind("<Enter>", partial(changeImage, dir + "/resources/images/buttons/enemies_hover.png", lbtn_enemies, 204, 100))
	lbtn_enemies.bind("<Leave>", partial(changeImage, dir + "/resources/images/buttons/enemies.png", lbtn_enemies, 204, 100))
	# lbtn_enemies.bind("<Button-1>", lambda event : combineFuncs(changeBtnPic(buttons_top, pics, pics_hover, 204, 100, event, 0), loadMenu(dir, allFrames, setup_name, 'Enemies')))


	lbtn_players.bind("<Enter>", partial(changeImage, dir + "/resources/images/buttons/players_hover.png", lbtn_players, 204, 100))
	lbtn_players.bind("<Leave>", partial(changeImage, dir + "/resources/images/buttons/players.png", lbtn_players, 204, 100))
	lbtn_players.bind("<Button-1>", lambda event : combineFuncs(changeBtnPic(buttons_top, pics, pics_hover, 204, 100, event, 0), loadMenu(dir, allFrames, setup_name, 'Players')))

	buttons_top = [lbtn_npcs, lbtn_enemies, lbtn_players]
	pics        = [dir + "/resources/images/buttons/npcs.png", dir + "/resources/images/buttons/enemies.png", dir + "/resources/images/buttons/players.png"]
	pics_hover  = [dir + "/resources/images/buttons/npcs_hover.png", dir + "/resources/images/buttons/enemies_hover.png", dir + "/resources/images/buttons/players_hover.png"]


	fr_bottom = allFrames.getFrame('bottomBase')

	lbtn_effects  = createLabel(fr_bottom, w = '28', h = '1', bg = '#A6ABAA', fg = '#A9011D', txt = 'EFFETS', x = '0', y = '0', btn = 2, pp = 1)
	lbtn_effects.bind('<Button-1>', lambda event : combineFuncs(changeBg(buttons_bot, event), equipment(dir, setup_name, allFrames, 'EFFECTS')))
	lbtn_skills   = createLabel(fr_bottom, w = '28', h = '1', bg = '#A6ABAA', fg = '#A9011D', txt = 'COMPÉTENCES', x = '210', y = '0', btn = 2, pp = 1)
	lbtn_weapons  = createLabel(fr_bottom, w = '28', h = '1', bg = '#A6ABAA', fg = '#A9011D', txt = 'ARMES', x = '420', y = '0', btn = 2, pp = 1)
	lbtn_armors   = createLabel(fr_bottom, w = '28', h = '1', bg = '#A6ABAA', fg = '#A9011D', txt = 'ARMURES', x = '630', y = '0', btn = 2, pp = 1)
	lbtn_trinkets = createLabel(fr_bottom, w = '28', h = '1', bg = '#A6ABAA', fg = '#A9011D', txt = 'ACCESSOIRES', x = '840', y = '0', btn = 2, pp = 1)

	buttons_bot = [lbtn_effects, lbtn_skills, lbtn_weapons, lbtn_armors, lbtn_trinkets]

	dictAll = allFrames.getAllFrames()
	dictAll['frDelSetup']   = fr_del_setup
	dictAll['frFight']      = fr_fight
	dictAll['frSetupName']  = fr_setup_name
	dictAll['lbtnNPCS']     = lbtn_npcs
	dictAll['lbtnENEMIES']  = lbtn_enemies
	dictAll['lbtnPLAYERS']  = lbtn_players
	dictAll['lbtnEffects']  = lbtn_effects
	dictAll['lbtnSkills']   = lbtn_skills
	dictAll['lbtnWeapons']  = lbtn_weapons
	dictAll['lbtnArmors']   = lbtn_armors
	dictAll['lbtnTrinkets'] = lbtn_trinkets

	allFrames.setAllFrames(dictAll)