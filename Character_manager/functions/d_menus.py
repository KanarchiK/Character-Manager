import tkinter as tk
import sys
sys.path.insert(0, '../classes')
from c_Frames import *
from f_Functions import createFrame, createLabel, generateImage, changeImage, defineWindow, combineFuncs
from d_CreateEquip import createEffect


def equipment(dir, setup_name, allFrames, menu ) :
	if allFrames.getFrame('equip') :
		allFrames.getFrame('equip').destroy()

	fr_bottom = allFrames.getFrame('bottomBase')

	fr_equip = createFrame(fr_bottom, 1208, 173, bg = 'red', pk = 1, pp = 1, x = '0', y = '25')

	fr_add = createFrame(fr_equip, 100, 173, bg = '#A9011D', pk = 1, pp = 1, x = '928', y = '0')

	lbtn_add = generateImage(dir + '/resources/images/buttons/add_equip.png', 90, 162, fr_add, bg = '#252A29', x = '3', y = '3', cur = 'hand2')
	lbtn_add.bind("<Enter>", lambda event : changeImage(dir + "/resources/images/buttons/add_equip_hover.png", lbtn_add, 90, 162, 0, bg = 'white'))
	lbtn_add.bind("<Leave>", lambda event : changeImage(dir + "/resources/images/buttons/add_equip.png", lbtn_add, 90, 162, 0, bg = '#252A29'))
	lbtn_add.bind("<Button-1>", lambda event : createEffect(dir, setup_name, 'effect', allFrames))

	allDict = allFrames.getAllFrames()
	allDict['equip'] = fr_equip
	allFrames.setAllFrames(allDict)