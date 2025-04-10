from mcpi.minecraft import Minecraft



mc=Minecraft.create()
pos=mc.player.getTilePos()
while True:
        mc.setBlock(pos.x,pos.y,pos.z, 41)
        
