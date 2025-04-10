from mcpi.minecraft import Minecraft

import random as rand
import time as t

mc=Minecraft.create()

pos=mc.player.getTilePos()

def createPool(posOfPool):
    pos=mc.player.getTilePos()
    mc.setBlocks(pos.x+posOfPool+(8*posOfPool),pos.y-5,pos.z-4,pos.x+6+posOfPool+(8*posOfPool+1),pos.y-1,pos.z+4, 8)
    t.sleep(3)

for i in range(5):
    createPool(i)
    t.sleep(1)
