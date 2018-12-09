path = os.getcwd()

shotcount = 0

class Spaceship:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.keyHandler={LEFT:False, RIGHT:False}
        self.img = loadImage(path+"/Images/"+'spaceship.png')
        self.shots = []
        for x in range(1000):
            self.shots.append(Shot(3000,self.y-20))
        
    def display(self):
        global shotcount
        image(self.img, self.x, self.y, 50, 50)
        
        if self.keyHandler[LEFT]:
            if self.x != 0:
                self.vx = -5
            else:
                self.vx = 0
        elif self.keyHandler[RIGHT]:
            if self.x != 750:
                self.vx = 5
            else:
                self.vx = 0
        else:
            self.vx = 0
            
        self.x += self.vx
        
        
class Shot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vy = -15
        self.img = loadImage(path+"/Images/"+'Shot.png')
        self.keyHandler = {UP:False}
        
    def display(self):
        if self.keyHandler[UP] == True:
            image(self.img, self.x +23, self.y, 5, 20)
            self.y += self.vy
 
class Game:
    def __init__(self,w,h):
        self.w=w
        self.h=h
        self.state="menu"
        self.backimage=loadImage(path+"/Images/"+'space.jpg')
        self.menuimg=loadImage(path+"/Images/"+'menu.jpg')
        self.ship=Spaceship(390, 500)
    def display(self):
        if self.state=="menu":
           image(self.menuimg,0,0,self.w,self.h)
        else:
            image(self.backimage,0,0,self.w,self.h)
            self.ship.display()
                    
        
        

g=Game(800,600)
def setup():
    size(g.w, g.h)
    
def draw():
      
    if g.state == "menu":
        g.display()
        textSize(34)
        
        logo=loadImage(path+"/Images/"+'spaceinvaders.png')
        image(logo,0,0,g.w,g.h//3)
        
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
        # g.__init__(1280,720,585)
        g.display()

    for x in range(len(g.ship.shots)):
        g.ship.shots[x].display()

def mouseClicked():
    if g.w//2.5 < mouseX < g.w//2.5 + 200 and g.h//3 < mouseY < g.h//3 + 50:
        g.state="play"    

def keyPressed():
    global shotcount
    if keyCode == LEFT:
        g.ship.keyHandler[LEFT] = True
    elif keyCode == RIGHT:
        g.ship.keyHandler[RIGHT] = True
    elif keyCode == UP:
        g.ship.shots[shotcount].x = g.ship.x
        g.ship.shots[shotcount].keyHandler[UP] = True
        shotcount += 1
    
        
def keyReleased():
    if keyCode == LEFT:
        g.ship.keyHandler[LEFT] = False
    elif keyCode == RIGHT:
        g.ship.keyHandler[RIGHT] = False


    
