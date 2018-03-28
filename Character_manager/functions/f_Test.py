import sys
sys.path.insert(0, '../classes')
from c_Frames import *
from f_Functions import createFrame

def test(allFrames, root) :
	fr_top    = createFrame(root, '1280', '100', bg = '#A9011D', x = '0', y = '0', pk = 0) 
	print(allFrames.getAllFrames())
	baseFrames = allFrames.getFrame('base')
	print(baseFrames)
	print('TOP1 : ', baseFrames.getFrame('top'), '\n')
	baseFrames.kill('top')
	fr_top.pack()
	fr_top.pack_propagate(0)

	baseFrames.setFrame('top', fr_top)
	allFrames.setFrame('baseFrames', baseFrames)
	print(baseFrames.getFrame('top'))