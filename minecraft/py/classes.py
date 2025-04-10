from mcpi.minecraft import Minecraft

mc=Minecraft.create()

class cat():
	def __init__(self, name,  weight):
		self.name=name
		self.weight=weight

fluff= cat("Пушок",4,5)

def eat(self,food):
	self.weight = self.weight + 0.2
	print(self.name)

fluff.eat("Fish")

def GetWeightInGrams(self):
	return self.weight*1000

print(fluff.GetWeightInGrams())

class Location(object):
	def __init__(self, x,y,z):
		self.x=x
		self.y=y
		self.z=z

class NamedBuilding(object):
	def __init__(self, x,y,z, width, height, depth, name):
		self.x=x
		self.y=y
		self.z=z
		self.weight=weight
		self.height=height
		self.depth=depth

		self.name=name

def build(self):
	mc.setBlocks(self.x,self.y,self.z,
							 self.x+self.weight,self.y+self.height,
							 self.z+self.depth, 4)
							 mc.setBlocks(self.x+1,self.y+1,self.z+1,
							 self.x+self.weight-1,self.y+self.height-1,
							 self.z+self.depth-1, 0)
def clear(self):
	mc.setBlocks(self.x, self.y, self.z,
							 self.x+self.weight, self.y+self.height, 
							 self.z+self.depth, 0)

def getInfo():
	return x,y,z

bedroom = Location(64,52,-8)
mc.player.setPos(bedroom.x,bedroom.y,bedroom.z)

pos= mc.getTilePos()
x=pos.x
y=pos.y
z=pos.z
ghostCastle=NamedBuilding(x,y,z,10,16,16,"Замок-призрак")
ghostCastle.build()
mc.postToChat(ghostCastle.getInfo())


t.sleep(5)

ghostCastle.clear()

gray=cat("черныш",4.9)


print(fluff.name)
print(gray.name)

class cat():
	owner="крейг"
	def __init__(self,name,weight):
		self.name=name
		self.weight=weight

gray.owner="Мэтью"
print(gray.owner)
print(fluff.owner)