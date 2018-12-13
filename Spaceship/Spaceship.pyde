import time
import random

path = os.getcwd()

number = 21
numberchange = 1


class Spaceship:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.keyHandler={LEFT:False, RIGHT:False}
        self.img = loadImage(path+"/Images/"+'spaceship.png')
        self.shots = []

    def distance (self,e):
        return ((self.x-e.x)**2+(self.y-e.y)**2)**0.5
    
    def spaceshiplives(self):
        for a in g.asteroids:
            if self.distance(a)<=50:
                g.asteroids.remove(a)
                g.lives-=1
        for a in g.enemy1:
            if self.distance(a)<=50:
                g.enemy1.remove(a)
                g.lives-=1
        for a in g.enemy1:
            for x in g.enemy1[g.enemy1.index(a)].shots:
                if self.distance(x)<=50:
                    g.enemy1[g.enemy1.index(a)].shots.remove(x)
                    g.lives-=1
        for a in g.enemy2:
            if self.distance(a)<=50:
                g.enemy2.remove(a)
                g.lives-=1
        for a in g.enemy2:
            for x in g.enemy2[g.enemy2.index(a)].shots:
                if self.distance(x)<=50:
                    g.enemy2[g.enemy2.index(a)].shots.remove(x)
                    g.lives-=1
        for a in g.enemy3:
            if self.distance(a)<=50:
                g.enemy3.remove(a)
                g.lives-=1
        for a in g.enemy3:
            for x in g.enemy3[g.enemy3.index(a)].shots:
                if self.distance(x)<=5:
                    g.enemy3[g.enemy3.index(a)].shots.remove(x)
                    g.lives-=1
        
    
    def display(self):
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
        self.xdirection = True
        self.ydirection = True
        self.shots = []
    
    def display(self):
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
        self.xdirection = True
        self.ydirection = True
        self.shots = []
    
    def display(self):
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
        self.shots = []
    
    def display(self):
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
        
    def display(self):
        
        if self.y > g.h+50 :
            g.asteroids.remove(self)
            del self
            return
        
        image(self.img, self.x, self.y, 50, 50)
        self.y += self.vy
            
        
class Shotforenemy1:
    def __init__(self, x, y,vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.img = loadImage(path+"/Images/"+'Shot.png')
        
    def display(self):
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
        self.vx = vx
        self.vy = vy
        self.img = loadImage(path+"/Images/"+'Shot.png')
        self.keyHandler = {UP:False}
        
    def display(self):
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
        self.w = w
        self.h = h
        self.vy = +1
        self.img = loadImage(path+"/Images/"+'space.jpg')
    
    def display(self):
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
        #print(startTime)                                                            #line 88 to 94 adds Asteroids to the asteroids array
        
    
        self.backimage = []
        for x in range(2):
            self.backimage.append(Background(0,-x*self.h,self.w,self.h))
        self.ship=Spaceship(self.w/2, self.h - 75)
        self.menuimg=loadImage(path+"/Images/"+'menu.jpg')
        self.logo=loadImage(path+"/Images/"+'spaceinvaders.png')
    
    def display(self):
        if self.state=="menu":
           image(self.menuimg,0,0,self.w,self.h)
        else:
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
            text("Score: "+str(gametime), 20, 20)
            text("     Lives:" +str(self.lives), 110, 20)
            
        
      
    def makeasteroids(self):
        if (number%20) == 0:
            for x in range(1):
                randomy = random.randint(-50,0) 
                randomx = random.randint(0,self.w) 
                if randomx == self.w:
                    randomx += -50                                                                                                                                        
                self.asteroids.append(Asteroid(randomx, randomy, 0, 10))
                
    def makeenemy1(self):
        if (number%150) == 0:
            for x in range(1):                                                                                                                                        
                self.enemy1.append(Alien(0,0,5,2))
                
    def makeenemy2(self):
        if (number%400) == 0:
            for x in range(1):                                                                                                                                        
                self.enemy2.append(creature(g.w/2-75,0,5,2))
    def makeenemy3(self):
        if (number%700) == 0:
            for x in range(1):                                                                                                                                        
                self.enemy3.append(enemy3(0,0,5,5))
    
                

                    



g=Game(800,600)
def setup():
    size(g.w, g.h)
    
def draw():      
    if g.state == "menu":
        g.display()
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
            
    elif g.state == "gameover":
        textSize(50)
        fill (255,0,0)
        text("GAME OVER", g.w//2.5, g.h//3+140)
        g.display()
    
    global number    
    number += numberchange
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
    



def mouseClicked():
    if g.w//2.5 < mouseX < g.w//2.5 + 200 and g.h//3 < mouseY < g.h//3 + 50:
        g.state="play"  
        g.startTime = time.time()
    
def keyPressed():
    global shotcount
    if keyCode == LEFT:
        g.ship.keyHandler[LEFT] = True
    elif keyCode == RIGHT:
        g.ship.keyHandler[RIGHT] = True
    #elif keyCode == UP:
        #g.ship.shots.append(Shot(g.ship.x +23,g.ship.y, 0, -15))
    
        
def keyReleased():
    if keyCode == LEFT:
        g.ship.keyHandler[LEFT] = False
    elif keyCode == RIGHT:
        g.ship.keyHandler[RIGHT] = False
    elif keyCode == UP:
        g.ship.shots.append(Shot(g.ship.x +23,g.ship.y, 0, -15))


    
