#simple class to hold position data of a player or non player character

class npc:
    def __init__(self,image,x,y):
        self.image=image
        self.x = x
        self.y = y
	self.pos=x,y

    def move(self,x,y):#move in vector x,y
        self.x+=x
        self.y+=y
        self.pos=self.x,self.y
        
    def moveto(self,x,y):
        x=x
        self.y=y
	self.pos=x,y

    def getimage():
        return self.image
