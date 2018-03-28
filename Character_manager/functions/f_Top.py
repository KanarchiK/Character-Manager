import sys
sys.path.insert(0, '../classes')
import tkinter as tk
import PIL.Image
import PIL.ImageTk
from c_Frames import *
from f_frames import createFrame


def topBase(dir, root) :
	img_loc = dir + "/resources/images/buttons/"
	fr_top = createFrame(root, '1280', '100', bg = '#252A29')
	# fr_top.pos(0, 0)


# def loaded(dir, root, setup_name) :
# 	points = [0, 130, 199, 130, 265, 0, 66, 0]

# 	lb_setup_name = tk.Label(fr_top, text = setup_name, fg = "white", bg = "#252A29")
# 	lb_setup_name.pack()
# 	lb_setup_name.place(x = 5, y = 30)
# 	lb_setup_name.config(font = ("Arial", 44, 'italic'))

# 	lb_players = Functions.generateImage(dir + "/resources/images/buttons/players.png", 265, 130, fr_top)
# 	lb_enemies = Functions.generateImage(dir + "/resources/images/buttons/enemies.png", 265, 130, fr_top)
# 	lb_npcs = Functions.generateImage(dir + "/resources/images/buttons/npcs.png", 265, 130, fr_top)

# 	lb_npcs.place(x = 1004, y = 0)
# 	lb_npcs.config(cursor = "hand2")

# 	lb_enemies.place(x = 729, y = 0)
# 	lb_enemies.config(cursor = "hand2")

# 	lb_players.place(x = 454, y = 0)
# 	lb_players.config(cursor = "hand2")

# 	lb_npcs.bind("<Enter>", lambda event : Functions.changeImage(img_loc + "npcs_hover.png", lb_npcs, 265, 130))
# 	lb_npcs.bind("<Leave>", lambda event : Functions.changeImage(img_loc + "npcs.png", lb_npcs, 265, 130))
# 	lb_npcs.bind("<Button-1>", lambda event : Functions.changeBtnPic(buttons, pics, pics_hover, 265, 130, event))

# 	lb_enemies.bind("<Enter>", lambda event : Functions.changeImage(img_loc + "enemies_hover.png", lb_enemies, 265, 130))
# 	lb_enemies.bind("<Leave>", lambda event : Functions.changeImage(img_loc + "enemies.png", lb_enemies, 265, 130))
# 	lb_enemies.bind("<Button-1>", lambda event : Functions.changeBtnPic(buttons, pics, pics_hover, 265, 130, event))

# 	lb_players.bind("<Enter>", lambda event : Functions.changeImage(img_loc + "players_hover.png", lb_players, 265, 130))
# 	lb_players.bind("<Leave>", lambda event : Functions.changeImage(img_loc + "players.png", lb_players, 265, 130))
# 	lb_players.bind("<Button-1>", lambda event : Functions.changeBtnPic(buttons, pics, pics_hover, 265, 130, event))

# 	buttons    = [lb_players, lb_enemies, lb_npcs]
# 	pics       = [img_loc + "players.png", img_loc + "enemies.png", img_loc + "npcs.png"]
# 	pics_hover = [img_loc + "players_hover.png", img_loc + "enemies_hover.png", img_loc + "npcs_hover.png"]

# 	return(fr_top)