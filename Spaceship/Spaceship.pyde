add_library('minim')
import time
import random

path = os.getcwd()
player = Minim(this)

number = 21
numberchange = 1                                   #number is increased by number change in the draw function, which is continuesly ran

if number > 2000:
    numberchange = 5                              # this block increases difficulty as the game runs
elif number > 1200:
    numberchange = 2


class Spaceship:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.keyHandler={LEFT:False, RIGHT:False}
        self.img = loadImage(path+"/Images/"+'spaceship.png')
        self.shots = []
        self.explosion=player.loadFile(path+"/sound/explosion.mp3")
        self.music=player.loadFile(path+"/sound/music.mp3")
    def distance (self,e):
        return (((self.x+25)-e.x)**2+((self.y+25)-e.y)**2)**0.5
    def distanceshots (self,e):
        return (((self.x+25)-(e.x+2.5))**2+((self.y+25)-(e.y+10))**2)**0.5
    def distanceenemy1 (self,e):
        return (((self.x+25)-(e.x+50))**2+((self.y+25)-(e.y+50))**2)**0.5               #lines 28 to 96 are for collisions
    def distanceenemy2 (self,e):
        return (((self.x+25)-(e.x+37.5))**2+((self.y+25)-(e.y+60))**2)**0.5 
    def distanceenemy3 (self,e):
        return (((self.x+25)-(e.x+50))**2+((self.y+25)-(e.y+50))**2)**0.5      
    def spaceshiplives(self):
        for a in g.asteroids:
            if self.distance(a)<=50:
                g.asteroids.remove(a)
                self.explosion.play()
                g.lives-=1
        for a in g.enemy1:
            if self.distanceenemy1(a)<=40:
                g.enemy1.remove(a)
                g.lives-=1
                self.explosion.play()
        for a in g.enemy1:
            for x in g.enemy1[g.enemy1.index(a)].shots:
                if self.distanceshots(x)<=40:
                    g.enemy1[g.enemy1.index(a)].shots.remove(x)
                    g.lives-=1
                    self.explosion.play()
        for a in g.enemy2:
            if self.distanceenemy2(a)<=50:
                g.enemy2.remove(a)
                g.lives-=1
                self.explosion.play()
        for a in g.enemy2:
            for x in g.enemy2[g.enemy2.index(a)].shots:
                if self.distanceshots(x)<=50:
                    g.enemy2[g.enemy2.index(a)].shots.remove(x)
                    g.lives-=1
                    self.explosion.play()
        for a in g.enemy3:
            if self.distanceenemy3(a)<=50:
                g.enemy3.remove(a)
                g.lives-=1
                self.explosion.play()
        for a in g.enemy3:
            for x in g.enemy3[g.enemy3.index(a)].shots:
                if self.distanceshots(x)<=5:
                    g.enemy3[g.enemy3.index(a)].shots.remove(x)
                    g.lives-=1
                    self.explosion.play()
        
    
    def display(self):
        if g.state=="play":
            self.spaceshiplives()
            image(self.img, self.x, self.y, 50, 50)
            
            if self.keyHandler[LEFT]:
                if self.x != 0:
                    self.vx = -10
                else:
                    self.vx = 0
            elif self.keyHandler[RIGHT]:
                if self.x != g.w -50:
                    self.vx = 10
                else:
                    self.vx = 0
            else:
                self.vx = 0        
            self.x += self.vx
    

        

class Enemies:
    def __init__ (self,x,y,vx,vy):
        self.x=x
        self.y=y                                                 #general enemy class
        self.vx=vx
        self.vy=vy
    
class Alien(Enemies):
    def __init__(self,x,y,vx, vy):
        Enemies.__init__(self,x,y,vx,vy)
        self.img = loadImage(path+"/Images/"+'Enemy1.png') 
        self.imgstatus = 1
        self.xdirection = True                                     #first enemy class
        self.ydirection = True
        self.shots = []
    def distance (self,e):
        return ((self.x-e.x)**2+(self.y-e.y)**2)**0.5
 
    def shipshots(self):
        for x in g.ship.shots:
            if self.distance(x)<=30:                
                g.enemy1.remove(self)
                del self 
                g.ship.explosion.play()
                return
    
    def display(self):
        if g.state=="play":
            self.shipshots()
            image(self.img, self.x, self.y, 100, 100, 64*self.imgstatus, 0, 64+64*self.imgstatus, 64)
            if self.imgstatus == 4:
                self.imgstatus += -4 
            else:
                self.imgstatus += 1
                
            if self.x == 0:
                self.xdirection = True
            if self.x == g.w - 100:
                self.xdirection = False
            if self.y == 0:
                self.ydirection = True
            if self.y == g.h - 100:
                self.ydirection = False
            
            
            if self.xdirection:
                self.x += self.vx
            else:
                self.x -= self.vx
            if self.ydirection:
                self.y += self.vy
            else:
                self.y -= self.vy
                
            for x in self.shots:
                x.display()
            
    def shotmaker(self):
        if (number%20) == 0:
            for x in range(1):                                                                                                                                        
                self.shots.append(Shotforenemy1(self.x+50, self.y+50, 0, 5))        

        
        

class creature(Enemies):
    def __init__(self,x,y,vx, vy):
        Enemies.__init__(self,x,y,vx,vy)
        self.img = loadImage(path+"/Images/"+'Enemy2.png') 
        self.imgstatus = 1
        self.xdirection = True                                   #second enemy class
        self.ydirection = True
        self.shots = []
    def distance (self,e):
        return ((self.x-e.x)**2+(self.y-e.y)**2)**0.5
 
    def shipshots(self):
        for x in g.ship.shots:
            if self.distance(x)<=30:
                self.rs=True
                g.enemy2.remove(self)
                g.ship.explosion.play()
                del self 
                return
    
    def display(self):
        if g.state=="play":
            self.shipshots()
            image(self.img, self.x, self.y, 75, 120, self.imgstatus*64, 0, 64+64*self.imgstatus, 159)
            if self.imgstatus == 7:
                self.imgstatus += -7 
            else:
                self.imgstatus += 1
                
            if self.x == 0:
                self.xdirection = True
            if self.x == g.w - 100:
                self.xdirection = False
            if self.y == 0:
                self.ydirection = True
            if self.y == g.h - (g.h/2):
                self.ydirection = False
            
            
            if self.xdirection:
                self.x += self.vx
            else:
                self.x -= self.vx
            if self.ydirection:
                self.y += self.vy
            else:
                self.y -= self.vy
                
            for x in self.shots:
                x.display()
            
    def shotmaker(self):
        if (number%20) == 0:
            for x in range(1):                                                                                                                                        
                self.shots.append(Shotforenemy1(self.x+50, self.y+50, -7, 7))
                self.shots.append(Shotforenemy1(self.x+50, self.y+50, 7, 7))
                
                
class enemy3(Enemies):
    def __init__(self,x,y,vx, vy):
        Enemies.__init__(self,x,y,vx,vy)
        self.img = loadImage(path+"/Images/"+'Enemy3.png') 
        self.imgstatus = 0
        self.direction = 1
        self.shots = []                                                 #enemy 3 class
    def distance (self,e):
        return ((self.x-e.x)**2+(self.y-e.y)**2)**0.5
 
    def shipshots(self):
        for x in g.ship.shots:
            if self.distance(x)<=30:
                g.enemy3.remove(self)
                g.ship.explosion.play()
                del self 
                return

    
    def display(self):
        if g.state=="play":
            self.shipshots()
            image(self.img, self.x, self.y, 100, 100, 64*self.imgstatus, 0, 64+64*self.imgstatus, 64)
            
            if self.imgstatus == 7:
                self.imgstatus += -7 
            else:
                self.imgstatus += 1
                
            if self.x == 0 or self.y == 0:
                self.direction = 1
            if self.x == g.w - 100:
                self.direction = 2
            if self.y ==  g.h - 100:
                self.direction = 3
                
            if self.direction == 1:
                self.vx = 5
                self.vy = 0
                self.x += self.vx
                self.y += self.vy
            if self.direction == 2:
                self.vx = -10
                self.vy = 10
                self.x += self.vx
                self.y += self.vy
            if self.direction == 3:
                self.vx = -10
                self.vy = -10
                self.x += self.vx
                self.y += self.vy
            
            
        
                
            for x in self.shots:
                x.display()
            
    def shotmaker(self):
        if (number%20) == 0:
            for x in range(1):                                                                                                                                        
                self.shots.append(Shotforenemy1(self.x+50, self.y+50, -10, 10))
                self.shots.append(Shotforenemy1(self.x+50, self.y+50, 10, 10))
                self.shots.append(Shotforenemy1(self.x+50, self.y+50, 0, 10))
        
              
        
        
class Asteroid(Enemies):
    def __init__(self,x,y,vx, vy):
        Enemies.__init__(self,x,y,vx,vy)
        self.img = loadImage(path+"/Images/"+'meteor.png')                #asteroids class
    def distance (self,e):
        return ((self.x-e.x)**2+(self.y-e.y)**2)**0.5
 
    def shipshots(self):
        for x in g.ship.shots:
            if self.distance(x)<=30:
                g.asteroids.remove(self)
                del self 
                return

                        
    def display(self):
        if g.state=="play":
            self.shipshots()
            
            if self.y > g.h+50 :
                g.asteroids.remove(self)
                g.ship.explosion.play()
                del self
                return
            image(self.img, self.x, self.y, 50, 50)
            self.y += self.vy
            
        
class Shotforenemy1:
    def __init__(self, x, y,vx, vy):                          #shots for the enemies
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.img = loadImage(path+"/Images/"+'Shot.png')
        
    def display(self):
        if g.state=="play":
            if self.y > g.w + 100:
                for x in g.enemy1:
                    for y in x.shots:
                        if self == y:
                            x.shots.remove(self)
                            del self
                            return
                for x in g.enemy2:
                    for y in x.shots:
                        if self == y:
                            x.shots.remove(self)
                            del self
                            return
                for x in g.enemy3:
                    for y in x.shots:
                        if self == y:
                            x.shots.remove(self)
                            del self
                            return
            
        image(self.img, self.x, self.y, 5, 20)
        self.y += self.vy
        self.x += self.vx

class Shot:
    def __init__(self, x, y,vx, vy):
        self.x = x
        self.y = y
        self.vx = vx                                             #shots for ship
        self.vy = vy
        self.img = loadImage(path+"/Images/"+'Shot.png')
        self.shotmusic=player.loadFile(path+"/sound/shot.wav")
        self.keyHandler = {UP:False}
        
    def display(self):
        if g.state=="play":
            if self.y < -50:
                g.ship.shots.remove(self)
                del self
                return
                
            # if self.keyHandler[UP] == True:
            image(self.img, self.x, self.y, 5, 20)
            self.y += self.vy
            self.x += self.vx
 
class Background:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w                                            #background class
        self.h = h
        self.vy = +1
        self.img = loadImage(path+"/Images/"+'space.jpg')
    
    def display(self):
        if g.state=="play":
            image(self.img, 0, self.y+self.vy, self.w, self.h)
            self.vy = (self.vy+1)%g.h


class Game:
    def __init__(self,w,h):
        self.w=w
        self.h=h
        self.lives = 3
        self.state="menu"
        self.asteroids = [] 
        self.enemy1 = []
        self.enemy2 = []
        self.enemy3 = []
        self.startTime = 0
        self.score=0
        #print(startTime)
        self.music=player.loadFile(path+"/sound/music.mp3")
        # self.music = player.loadFile(path+"/sounds/music.mp3")
    
        self.backimage = []
        for x in range(2):
            self.backimage.append(Background(0,-x*self.h,self.w,self.h))
        self.ship=Spaceship(self.w/2, self.h - 75)
        self.menuimg=loadImage(path+"/Images/"+'menu.jpg')
        self.logo=loadImage(path+"/Images/"+'spaceinvaders.png')
        self.instructions=loadImage(path+"/Images/"+'ins.png')
        
    def lifechecker(self):
        if self.lives==0 and self.state=="play":
            self.state="gameover"
            self.lives=3
    def display(self):
        self.music
        self.lifechecker()
        if self.state=="play":
            for x in range(len(self.backimage)):
                self.backimage[x].display()
            self.ship.display()
            for s in self.ship.shots:
                s.display()
            for z in self.asteroids:                                       #displays asteroids
                z.display()
            for p in self.enemy1:                                       #displays asteroids
                p.display()
            for r in self.enemy2:                                       #displays asteroids
                r.display()
            for t in self.enemy3:                                       #displays asteroids
                t.display()            
            textSize(20)
            fill(255)
            gametime=int(time.time()-g.startTime)
            self.score=gametime
            text("Score: "+str(gametime), 20, 20)
            text("     Lives:" +str(self.lives), 110, 20)
        elif self.state=="menu":
           image(self.menuimg,0,0,self.w,self.h)
           global number
           number = 21
        elif self.state=="instructions":
           image(self.instructions,0,0,self.w,self.h)  
        elif self.state=="gameover":
           image(self.menuimg,0,0,self.w,self.h)
        
        
      
    def makeasteroids(self):
        if (number%20) == 0 and self.state=="play":
            for x in range(1):
                randomy = random.randint(-50,0) 
                randomx = random.randint(0,self.w) 
                if randomx == self.w:
                    randomx += -50                                                                                                                                        
                self.asteroids.append(Asteroid(randomx, randomy, 0, 10))
                
    def makeenemy1(self):
        if (number%150) == 0 and self.state=="play":
            for x in range(1):                                                                                                                                        
                self.enemy1.append(Alien(0,0,5,2))
                
    def makeenemy2(self):
        if (number%400) == 0 and self.state=="play":
            for x in range(1):                                                                                                                                        
                self.enemy2.append(creature(g.w/2-75,0,5,2))
    def makeenemy3(self):
        if (number%700) == 0 and self.state=="play":
            for x in range(1):                                                                                                                                        
                self.enemy3.append(enemy3(0,0,5,5))
    
                

                    



g=Game(800,600)
def setup():
    size(g.w, g.h)
    
def draw():      
    if g.state == "menu":
        g.display()
        g.music.play()
        textSize(34)
        image(g.logo,0,0,g.w,g.h//3)
        
        if g.w//2.5 < mouseX < g.w//2.5 + 200 and g.h//3 < mouseY < g.h//3 + 50:
            fill(255,0,0)
        else:
            fill(255,255,0)
        text("Play Game", g.w//2.5, g.h//3+40)
        if g.w//2.5 < mouseX < g.w//2.5 + 200 and g.h//3+100 < mouseY < g.h//3 + 150:
            fill(255,0,0)
        else:
            fill(255,255,0)
        text("Instructions", g.w//2.5, g.h//3+140)
        
    elif g.state == "play":
        background(0)
        g.display()
        g.music.play()
            
    elif g.state == "gameover":
        g.display()
        g.music.play()
        textSize(50)
        fill (255,0,0)
        text("GAME OVER", g.w//3, g.h//2)
        textSize(30)
        fill(255,0,0)
        text("Your Score is:"+ str(g.score),g.w//3+280,g.h//2+250)
        textSize(30)
        if g.w//3-250 < mouseX < g.w//3-50 and g.h//2+230 < mouseY < g.h//2 + 250:
            fill(255,0,0)
        else:
            fill(255)
        text("Main Menu",g.w//3-250,g.h//2+250)
    elif g.state=="instructions":
        g.display()
        textSize(30)
        if g.w//3-250 < mouseX < g.w//3-50 and g.h//2+230 < mouseY < g.h//2 + 250:
            fill(255,0,0)
        else:
            fill(255)
        text("Main Menu",g.w//3-250,g.h//2+250)
       
            
    
    global number    
    number += numberchange                                 #lines 537 to 546 checks to create enemies and asteroids and shots
    g.makeasteroids()
    g.makeenemy1()
    g.makeenemy2()
    g.makeenemy3()
    for x in g.enemy1:
        x.shotmaker()
    for x in g.enemy2:
        x.shotmaker()
    for x in g.enemy3:
        x.shotmaker()
    
    print(number)

def mouseClicked():
    if g.w//3-250 < mouseX < g.w//3-50 and g.h//2+230 < mouseY < g.h//2 + 250:
        g.state="menu"
        g.music.play()
        # g.lives=3
        g.__init__(800,600) 
    if g.w//2.5 < mouseX < g.w//2.5 + 200 and g.h//3+100 < mouseY < g.h//3 + 150:
        g.state="instructions"
        g.music.play()
    if g.w//2.5 < mouseX < g.w//2.5 + 200 and g.h//3 < mouseY < g.h//3 + 50:
        g.state="play"
        g.music.play()  
        g.startTime = time.time()
    # if g.state=="gameover":
        # if g.w//3+370 < mouseX < g.w//3+600 and g.h//2+230 < mouseY < g.h//2 + 300:
        #     g.state="play"
        #     g.startTime = time.time()

def keyPressed():
    global shotcount
    if keyCode == LEFT:
        g.ship.keyHandler[LEFT] = True
    elif keyCode == RIGHT:                          #for movement of ship
        g.ship.keyHandler[RIGHT] = True
    elif keyCode == UP:
        return
        
def keyReleased():
    if keyCode == LEFT:
        g.ship.keyHandler[LEFT] = False
    elif keyCode == RIGHT:
        g.ship.keyHandler[RIGHT] = False
    elif keyCode == UP:                                                #for movement of ship and creates shots in class
        g.ship.shots.append(Shot(g.ship.x +23,g.ship.y, 0, -15))
        g.ship.shots[0].shotmusic.play()
        


    
