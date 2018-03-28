import tkinter as tk
import sys
sys.path.insert(0, '../classes')
from c_Frames import *
from f_Functions import createFrame, createLabel, generateImage, changeImage, defineWindow, combineFuncs

def createEffect(dir, setup_name, menu, allFrames) :
	allFrames.getFrame('equip').destroy()

	fr_bottom = allFrames.getFrame('baseBottom')
	fr_create = createFrame(fr_bottom, 1208, 173, bg = 'red', pk = 1, pp = 1, x = '0', y = '25')

