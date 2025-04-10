from mcpi.minecraft import Minecraft

import random as rand
import time as t

mc=Minecraft.create()


pos=mc.player.getTilePos()

# mc.postToChat(pos)
def createHouse():
    pos=mc.player.getTilePos()
    mc.setBlocks(pos.x+1,pos.y-1,pos.z-2,pos.x+7,pos.y+4,pos.z+3, 2)
    mc.setBlocks(pos.x+2,pos.y,pos.z-1,pos.x+6,pos.y+3,pos.z+2, 0)
    t.sleep(1)

def createRoad():
    pos=mc.player.getTilePos()
    mc.setBlocks(pos.x,pos.y-1,pos.z-2,pos.x+100,pos.y-1,pos.z, 2)



def clear():
    posForClear=mc.player.getTilePos()
    mc.setBlocks(posForClear.x-100,posForClear.y,posForClear.z-100,posForClear.x+100,posForClear.y+40,posForClear.z+100, 0)
    mc.setBlocks(posForClear.x-100,posForClear.y-1,posForClear.z-100,posForClear.x+100,posForClear.y-1,posForClear.z+100, 1)
clear()
#createHouse()
#createRoad()





#for i in range(1,6,1):
#    t.sleep(30)
#    x=rand.randint(-50,50)
#    y=rand.randint(60,100)
#    z=rand.randint(-50,50)
#    mc.player.setPos(x,y,z)
#    t.sleep(200)
#    print(f"Телепортация {i} в координаты ,x={x}, y={y},z={z}")
#    
