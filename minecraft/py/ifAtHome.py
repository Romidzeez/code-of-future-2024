from mcpi.minecraft import Minecraft
import time


mc=Minecraft.create()

pos=mc.player.getTilePos()

if pos.x>=24 and pos.x<=28 and pos.z>=-40 and pos.z<=-37 and pos.y>=68 and pos.y<=71:
	mc.postToChat("HOME! SWEET HOME!")
else:
	mc.postToChat("NOT AT HOME!")