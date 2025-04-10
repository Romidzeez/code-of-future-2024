from mcpi.minecraft import Minecraft

import random as rand
import time as t

mc=Minecraft.create()



def calculateMove():
	pos=mc.player.getTilePos()
	x=pos.x
	z=pos.z
	y=pos.y
	forwardHeight= mc.getHeight(x+1,z)
	rightHeight = mc.getHeight (x,z+1)
	backwardHeight = mc.getHeight(x-1,z)
	leftHeight = mc.getHeight(x, z-1)

	currentHeight=mc.getHeight(x,z)-1

	# if forwardHeight - currentHeight < 3:
	# 	x+=1
	# elif rightHeight - currentHeight < 3:
	# 	z+=1
	# elif leftHeight - currentHeight < 3:
	# 	z-=1
	# elif backwardHeight - currentHeight < 3:
	# 	x-=1
	y=mc.getHeight(x,z)
while True:
	pos=mc.player.getTilePos()
	x=pos.x 
	z=pos.z
	y=mc.getHeight(x,z)
	calculateMove()
	mc.setBlock(x,y,z, 57)
	mc.setBlock(x,y+1,z, 57)
	mc.setBlock(x+1,y+1,z, 57)
	mc.setBlock(x-1,y+1,z, 57)
	mc.setBlock(x,y+2,z, 86)
	t.sleep(0.1)
	mc.setBlock(x,y,z, 0)
	mc.setBlock(x,y+1,z, 0)
	mc.setBlock(x+1,y+1,z, 0)
	mc.setBlock(x-1,y+1,z, 0)
	mc.setBlock(x,y+2,z, 0)

