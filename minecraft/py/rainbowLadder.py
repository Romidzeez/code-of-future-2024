from mcpi.minecraft import Minecraft

import random as rand
import time as t

mc=Minecraft.create()

pos=mc.player.getTilePos()
tryStop=int(input())

while True:
	for num in range(50):
		mc.setBlock(pos.x+num,pos.y+num,pos.z, 35, rand.randint(1,15))
	t.sleep(1)
