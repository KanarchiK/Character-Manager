import tkinter as tk
import sys
sys.path.insert(0, '../classes')
from c_Frames import *
from f_Functions import selectListValues

def createChar(dir, setup_name, allFrames, lst_weapons, lst_trinkets, lst_effects, lst_spells, lst_helm, lst_chest, lst_hands, lst_boots, dictStats) :

	def toStr(listParam) :
		string = ''
		if listParam :
			for i in listParam :
				string += '||' + i
		return(string)

	weapons    = toStr(selectListValues(lst_weapons))
	trinkets   = toStr(selectListValues(lst_trinkets))
	effects    = toStr(selectListValues(lst_effects))
	spells     = toStr(selectListValues(lst_spells))
	helm       = selectListValues(lst_helm)
	helm       = helm[0] if helm else ''
	chest      = selectListValues(lst_chest)
	chest      = chest[0] if chest else ''
	hands      = selectListValues(lst_hands)
	hands      = hands[0] if hands else ''
	boots      = selectListValues(lst_boots)
	boots      = boots[0] if boots else ''

	print(weapons)
  
	name          = dictStats.get('name')
	race	      = dictStats.get('race')
	char_class    = dictStats.get('class')
	stre          = dictStats.get('str')
	con           = dictStats.get('con')
	dex           = dictStats.get('dex')
	inte          = dictStats.get('int')
	per           = dictStats.get('per')
	cha           = dictStats.get('cha')
	hea           = dictStats.get('hea')
	man           = dictStats.get('man')
	phyArm        = dictStats.get('phyArm')
	magArm        = dictStats.get('magArm')
	menu          = dictStats.get('menu')
	desc          = dictStats.get('desc')



	with open(dir + '/setups/' + setup_name + '.setup', 'a', newline = '') as file :
		file.write('\n' +
			menu.upper() + 
			';;' + name +
			';;' + race +
			';;' + char_class +
			';;' + stre +
			';;' + stre +
			';;' + con +
			';;' + con +
			';;' + dex +
			';;' + dex +
			';;' + inte +
			';;' + inte + 
			';;' + per + 
			';;' + per +
			';;' + cha +
			';;' + cha +
			';;' + hea +
			';;' + hea +
			';;' + man +
			';;' + man +
			';;' + phyArm +
			';;' + phyArm +
			';;' + magArm +
			';;' + magArm +
			';;' + weapons +
			';;' + trinkets +
			';;' + effects +
			';;' + spells +
			';;' + helm +
			';;' + chest +
			';;' + hands +
			';;' + boots +
			';;' + desc +
			';;'
			)
	file.close()

	fr_menu = allFrames.getFrame('createChar')
	if fr_menu :
		fr_menu.destroy()
