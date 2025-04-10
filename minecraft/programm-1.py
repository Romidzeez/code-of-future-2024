from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
for i in range(10):
    pos=mc.player.getTilePos()
    x=pos.x
    y=pos.y
    z=pos.z
    mc.postToChat(pos)
    time.sleep(30)
    

