from mcpi.minecraft import Minecraft

import random as rand
import time as t

mc=Minecraft.create()


cube = [[[5, 5, 5, 5],
					[5, 5, 5, 5],
					[5, 5, 5, 5],
					[5, 5, 5, 5]],
					# 
					[[5, 5, 5, 5],
					[5, 0, 0, 0],
					[5, 0, 0, 0],
					[5, 5, 5, 5]],
					#
					[[5, 5, 5, 5],
					[0, 0, 0, 5],
					[5, 0, 0, 5],
					[5, 5, 5, 5]],
					#
					[[5, 5, 5, 5],
					[5, 5, 5, 5],
					[5, 5, 5, 5],
					[5, 5, 5, 5]]]

def createHouse():
	pos = mc.player.getTilePos()
	x = pos.x
	y = pos.y
	z = pos.z

	startingX = x
	startingY = y

	for depth in cube:
		for height in reversed(depth):
			for block in height:
				mc.setBlock(x, y, z, block)
				x += 1
			y+=1
			x = startingX
		z+=1
		y = startingY
createHouse()