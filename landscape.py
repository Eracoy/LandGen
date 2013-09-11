
import pygame, sys, math, os, random
from perlinalgs import *
from npc import *
pygame.init() #load pygame modules
size = width, height = 1200, 800 #size of window
screen = pygame.display.set_mode(size) #make window
clock=pygame.time.Clock() #make a clock
worldimage=pygame.Surface((1000,1000))

running=True

tilex,tiley=20,20
worldx,worldy=90,90

zoomlevel=1.8

playerspeed=.5

water=pygame.image.load(os.path.join("water.png"))
grass=pygame.image.load(os.path.join("grass.png"))
sand=pygame.image.load(os.path.join("sand.png"))
stone=pygame.image.load(os.path.join("stone.png"))
tree=pygame.image.load(os.path.join("tree.png"))
playerImage=pygame.image.load(os.path.join("player.png"))
tileimages=(water,grass,sand,stone,tree)
# 0 Water
# 1 Grass
# 2 Sand
# 3 Mountain
# 4 Stone

#Return a random selection from a set with weights
def randblock(weight):
    rnd = random.random() * sum(weight)
    for i, w in enumerate(weight):
        rnd -= w
        if rnd < 0:
            return i

#generates a new map with random surface at each point. No smoothing, but beaches are applied
def newworld(sizex,sizey):
    world=[[0 for a in range(sizey)] for b in range(sizex)]
    for a in range(worldy):
        for b in range(worldx):
            #print("Generating row",a,b)
            world[a][b]=randblock((1,10))
    world2=makebeaches(world)
    return world2

def perlinworld(sizex,sizey):
    oct1=perlin(16,255)
    oct2=perlin(8,128)
    world2=[[0 for a in range(sizey)] for b in range(sizex)]
    for a in range(sizey):
        for b in range(sizex):
            height=oct1[a%128][b%128]+oct2[a%64][b%64]+50
            if height>10:
                world2[a%128][b%128]=2
            if height>30:
                world2[a%128][b%128]=1
            if height>200:
                world2[a%128][b%128]=3
    return world2

#Smooth out the transition between land and water by adding beaches
#if land is touching water on a side, make it sand
def makebeaches(world):
    y=len(world) #worldx size
    x=len(world[0]) #worldy size
    for a in range(1,worldy-1):
        #print("Sanding row ",a)
        for b in range(1,worldx-1):
            if(world[a][b]==1):
                if(world[(a-1)%y][b%x]==0 or world[(a+1)%y][b%x]==0 or world[(a)%y][(b-1)%x]==0 or world[(a)%y][(b+1)%x]==0):
                    world[a][b]=2
    return world
                    
def drawworld(screen,world,tileimages):
    for a in range(worldx):
        for b in range(worldy):
            tilesizex,tilesizey=int(tilex/zoomlevel),int(tiley/zoomlevel)
            screen.blit(tileimages[world[a][b]],(a*tilesizex,b*tilesizey))
            
def drawnpcs(screen, npclist):
    a=npclist
    screen.blit(a.image,a.pos)
    
def main():
    world=perlinworld(worldx,worldy)
    world=makebeaches(world)
    player=npc(playerImage,92,92)
    player.moveto(52,52)
    print(world)
    drawworld(worldimage,world,tileimages)#render world
    running=True
    while running:
        clock.tick(300) #limit framerate to 30 FPS
        mpos=pygame.mouse.get_pos()
        m=pygame.mouse.get_pressed()
        k=pygame.key.get_pressed()
        for event in pygame.event.get(): #if something clicked
                if event.type == pygame.QUIT: #if EXIT clicked
                        running=False
                        
        if k[pygame.K_UP]:#up
            player.move(0,-playerspeed)
            print("up")
        if k[pygame.K_DOWN]:#down
            player.move(0,playerspeed)
            print("down")
        if k[pygame.K_LEFT]:#left
            player.move(-playerspeed,0)
            print("left")
        if k[pygame.K_RIGHT]:#right
            player.move(playerspeed,0)
            print("right")
            
        if m[0]:
            world=perlinworld(worldx,worldy)
            world=makebeaches(world)
            drawworld(worldimage,world,tileimages)#render world            


        screen.fill((0,0,0)) #make redraw background black
        screen.blit(worldimage,(0,0))
        drawnpcs(screen,player)
        pygame.display.flip() #update the screen    

if __name__=="__main__":
    
    
    main()
    pygame.quit()
