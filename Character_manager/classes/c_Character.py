class Character :

	def __init__ (self, menu, name, race, char_class, cur_str, max_str, cur_con, max_con, cur_dex, max_dex, cur_int, max_int, cur_per, max_per, cur_cha, max_cha, max_stats, cur_hea, max_hea, cur_man, max_man, cur_arm, max_arm, weapons, trinkets, helm, chest, hands, feet, desc) :
		self.menu       = menu
		self.name       = name
		self.race       = race
		self.char_class = char_class
		self.cur_str    = cur_str
		self.max_str    = max_str
		self.cur_con    = cur_con
		self.max_con    = max_con
		self.cur_dex    = cur_dex
		self.max_dex    = max_dex
		self.cur_int    = cur_int
		self.max_int    = max_int
		self.cur_per    = cur_per
		self.max_per    = max_per
		self.cur_cha    = cur_cha
		self.max_cha    = max_cha
		self.max_stats  = max_stats
		self.cur_hea    = cur_hea
		self.max_hea    = max_hea
		self.cur_man    = cur_man
		self.max_man    = max_man
		self.cur_arm    = cur_arm
		self.max_arm    = max_arm
		self.weapons    = weapons
		self.trinkets   = trinkets
		self.helm       = helm
		self.chest      = chest
		self.hands      = hands
		self.feet       = feet
		self.desc       = desc

	### GETTER ###

	def getMenu(self) :
		return self.menu

	def getName(self) :
		return self.name

	def getRace(self) :
		return self.race

	def getCharClass(self) :
		return self.char_class

	def getCurStr(self) :
		return self.cur_str

	def getMaxStr(self) :
		return self.max_str

	def getCurCon(self) :
		return self.cur_con

	def getMaxCon(self) :
		return self.max_con

	def getCurDex(self) :
		return self.cur_dex

	def getMaxDex(self) :
		return self.max_dex

	def getCurInt(self) :
		return self.cur_int

	def getMaxInt(self) :
		return self.max_int

	def getCurPer(self) :
		return self.cur_per

	def getMaxPer(self) :
		return self.max_per

	def getCurCha(self) :
		return self.cur_cha

	def getMaxCha(self) :
		return self.max_cha

	def getMaxStats(self) :
		return self.max_stats

	def getCurHea(self) :
		return self.cur_hea

	def getMaxHea(self) :
		return self.max_hea

	def getCurMan(self) :
		return self.cur_man

	def getMaxMan(self) :
		return self.max_man

	def getCurArm(self) :
		return self.cur_arm

	def getMaxArm(self) :
		return self.max_arm

	def getWeapons(self) :
		return self.weapons

	def getTrinkets(self) :
		return self.trinkets

	def getHelm(self) :
		return self.helm

	def getChest(self) :
		return self.chest

	def getHands(self) :
		return self.hands

	def getFeet(self) :
		return self.feet

	def getDesc(self) :
		return self.desc


	### SETTER ###

	def setMenu(self, menu):
		self.menu = menu