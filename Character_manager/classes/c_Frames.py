import tkinter as tk

class Frames :

	def __init__(self, frames) :
		self.frames = frames


	### GETTER ###

	def getAllFrames(self) :
		return self.frames

	### SETTER ###

	def setAllFrames(self, frames) :
		self.frames = frames


	def getFrame(self, frame) :
		return(self.getAllFrames().get(frame))

	def kill(self, frame) :
		self.getFrame(frame).destroy()
		return(self.frames)

	def setFrame(self, key, value) :
		self.getAllFrames()[key] = value
		return(self.frames)

	def addNew(self, **kwargs) :
		self.getAllFrames().update
		return(self.frames)





	def __del__(self) :
		deletion = self.getAllFrames()
		for i in deletion :
			del i
		print("Object ", self, " was successfully removed.")
		