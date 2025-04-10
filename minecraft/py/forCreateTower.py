from mcpi.minecraft import Minecraft

import random as rand
import time as t

mc=Minecraft.create()

pos=mc.player.getTilePos()

for i in range(rand.randint(1,10)):
	mc.setBlock(pos.x+1,pos.y+i,pos.z, 57)
	t.sleep(1)
	mc.postToChat(i)
