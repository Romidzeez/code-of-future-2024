from mcpi.minecraft import Minecraft
import random as rand
mc=Minecraft.create()
blockType=(input("enter type of block (type of block isn`t a number): "))
pos=mc.player.getTilePos()
x=pos.x
y=pos.y
z=pos.z
weight=rand.randint(1,6)
lens=rand.randint(1,6)
high=rand.randint(1,6)
mc.setBlock(x,y,z,x+weight,y+high,y+lens, blockType)
