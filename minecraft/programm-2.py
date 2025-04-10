from mcpi.minecraft import Minecraft
import random as rand
import time as t
mc=Minecraft.create()
for i in range(1,6,1):
    t.sleep(30)
    x=rand.randint(-50,50)
    y=rand.randint(60,100)
    z=rand.randint(-50,50)
    mc.player.setPos(x,y,z)
    t.sleep(200)
    print("Телепортация ",+i,"в координаты ","x=",+x," y=",+y," z=",+z)
    
