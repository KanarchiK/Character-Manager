import tkinter as tk
import sys
import os
sys.path.insert(0, 'classes')
sys.path.insert(0, 'functions')
from f_Functions import createFrame, defineWindow, createLabel, generateImage
from f_Setup import newSetup, loadSetup
from c_Frames import *
from f_Test import *
# from f_generateFrames import *

"""
fr   -> Frame
dict -> dictionnary
lb   -> Label
btn  -> Button
lbtn -> label-button
en   -> Entry
tx   -> Text
"""

dir = os.path.dirname(__file__) # Definition du chemin d'accès au dossier principal (Character Manager/)

root = defineWindow(1280, 720, title = 'Character Manager', icon = dir + "/resources/images/icons/CM.ico")

fr_top    = createFrame(root, '1280', '100', bg = '#252A29', x = '0', y = '0', pk = 1, pp = 1) 
fr_left   = createFrame(root, '150', '418', bg = '#252A29', x = '0', y = '102', pk = 1, pp = 1)
fr_right  = createFrame(root, '250', '618', bg = '#252A29', x = '1030', y = '102', pk = 1, pp = 1)
fr_bottom = createFrame(root, '1028', '198', bg = '#252A29', x = '0', y = '522', pk = 1, pp = 1)
fr_center = createFrame(root, '876', '418', bg = '#252A29', x = '152', y = '102', pk = 1, pp = 1)

fr_new_setup = createFrame(fr_left, '145', '72', bg = '#A9011D', x = '2', y = '20', pk = 1, pp = 1)
lbtn_new_setup = createLabel(fr_new_setup, w = 19, h = 4, txt = 'NOUVEAU SETUP', bg = '#252A29', fg = '#A9011D', cur = 'hand2', x = '3', y = '3', btn = 1, pp = 1)
lbtn_new_setup.bind('<Button-1>', lambda event : newSetup(dir, allFrames))

fr_load_setup = createFrame(fr_left, '145', '72', bg = '#A9011D', x = '2', y = '122', pk = 1, pp = 1)
lbtn_load_setup = createLabel(fr_load_setup, w = 19, h = 4, txt = 'CHARGER SETUP', bg = '#252A29', fg = '#A9011D', cur = 'hand2', x = '3', y = '3', btn = 1, pp = 1)
lbtn_load_setup.bind('<Button-1>', lambda event : loadSetup(dir, allFrames))

dictAll = dict([ 
	('root', root),
	('topBase', fr_top),
	('leftBase', fr_left),
	('rightBase', fr_right),
	('bottomBase', fr_bottom),
	('centerBase', fr_center)
])

allFrames  = Frames(dictAll)

# print(fr_bottom + "\n")
