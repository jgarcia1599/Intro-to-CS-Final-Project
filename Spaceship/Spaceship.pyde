path = os.getcwd()

class Spaceship:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.keyHandler={LEFT:False, RIGHT:False}
        self.img = loadImage(path+"/Images/"+'spaceship.png')
        
    def display(self):
        image(self.img, self.x, self.y, 50, 50)
        
        if self.keyHandler[LEFT]:
            self.vx = -5
        elif self.keyHandler[RIGHT]:
            self.vx = 5
        else:
            self.vx = 0
            
        self.x += self.vx
        
   
        
ship = Spaceship(390, 500)

def setup():
    size(800, 600)
    
def draw():
    ship.display()
    
def keyPressed():
    if keyCode == LEFT:
        ship.keyHandler[LEFT] = True
    elif keyCode == RIGHT:
        ship.keyHandler[RIGHT] = True

def keyReleased():
    if keyCode == LEFT:
        ship.keyHandler[LEFT] = False
    elif keyCode == RIGHT:
        ship.keyHandler[RIGHT] = False
    
