path = os.getcwd()

class Spaceship:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = loadImage(path+"/Images/"+'spaceship.png')
        
    def display(self):
        image(self.img, 300, 500, 50, 50)
        
ship = Spaceship(50, 50)

def setup():
    size(600, 600)
    
def draw():
    ship.display()
    
