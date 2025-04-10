from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
class Location(object):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.height = height
        self.depth = depth
    def build(self):
        mc.setBlocks(self.x,self.y,self.z,self.x,self.y+4,self.z,18)
        mc.setBlocks(self.x-2,self.y+4,self.z-2,self.x+2,self.y+4,self.z+2,18)

    def clear(self):
        mc.setBlocks(self.x,self.y,self.z,self.x+self.width,self.y+self.height,self.z+self.depth,0)
        mc.setBlocks(self.x-2,self.y+4,self.z-2,self.x+2,self.y+4,self.z+2,18)
while True:
    tree = Location(-443,94,-79,)
    tree.build()
    time.sleep(3)
    tree.clear()
    time.sleep(3)