from mcpi.minecraft import Minecraft

import time as t

mc=Minecraft.create()

class tree(object):
	def __init__(self, x,y,z):
		self.x=x
		self.y=y
		self.z=z
	def build(self):
		mc.setBlocks(self.x-2,self.y+3,self.z-2,
								 self.x+2,self.y+5,self.z+2,18)
		mc.setBlocks(self.x,self.y,self.z,
								 self.x,self.y+4,self.z,17)
	def clear(self):
		mc.setBlocks(self.x-2,self.y,self.z-2,
								 self.x+2,self.y+5,self.z+2,0)


pos=mc.player.getTilePos()
x=pos.x
y=pos.y
z=pos.z


while True:
	pos=mc.player.getTilePos()
	x=pos.x
	z=pos.z
	y=mc.getHeight(x,z)
	Dub=tree(x+4,y,z)
	Dub.build()
	t.sleep(3)
	Dub.clear()
	t.sleep(3)