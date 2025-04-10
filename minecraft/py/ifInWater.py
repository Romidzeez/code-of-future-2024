from mcpi.minecraft import Minecraft
import time


mc=Minecraft.create()

pos=mc.player.getTilePos()

if mc.getBlock(pos.x,pos.y,pos.z)==9:
    mc.postToChat("True")
elif mc.getBlock(pos.x,pos.y,pos.z)==8:
    mc.postToChat("True")
else:
    mc.postToChat("False")








#Height=mc.getHeight(pos.x,pos.z)
#mc.postToChat(Height)










#for i in range(10):
#    pos=mc.player.getTilePos()
#    x=pos.x
#    y=pos.y
#    z=pos.z
#    mc.postToChat(pos)
#    time.sleep(30)
    

