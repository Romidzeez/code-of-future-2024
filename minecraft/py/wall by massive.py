from mcpi.minecraft import Minecraft

import random as rand
import time as t

mc=Minecraft.create()

one = [0, 1, 2, 3, 4, 5]

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
for color in one:
	mc.setBlock(x, y, z, 35, color)
	y += 1


two=[[0, 0, 0],
		 [1, 1, 1],
		 [2, 2, 2],
	 	 [3, 3, 3],
	 	 [4, 4, 4],
		 [5, 5, 5]]
def createWall():
	pos = mc.player.getTilePos()
	x = pos.x
	y = pos.y
	z = pos.z
	starting = x
	for row in two:
		for color in row:
			mc.setBlock(x, y, z, 35, color)
			x += 1
			t.sleep(2)
		y +=1
		x=starting

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

def createCube():
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
				t.sleep(0.01)
				x += 1
			y+=1
			x = startingX
		z+=1
		y = startingY
createCube()
# createWall()
