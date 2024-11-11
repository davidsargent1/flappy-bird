import pygame

pygame.init()
screen = pygame.display.set_mode((900, 504))
clock = pygame.time.Clock()
running = True
background = pygame.Surface.convert(pygame.image.load('flappybirdbg.png'))
player_position = pygame.Vector2(250,100)
falling = True
jump_counter = 0  

class Bird:
    '''
    The character controls the bird.
    pos: Position (x,y) tuple
    alive: bool (T/F)
    radius: size of the bird
    flap_height: Height bird flaps
    '''
    
    def __init__(self, pos=(0,0), alive=True):
        self.pos = pos
        self.alive = alive
        self.radius = 20
        self.flap_height = 80
    
    def flap(self):
        global falling
        global jump_counter
        if jump_counter < 15:   
            self.pos.y -= 5
            jump_counter +=1
            return falling
        jump_counter = 0
        falling = True
        return falling, jump_counter

            

    

    

class Pipe:
     def __init__(self, height = 10, color = '2CB01A', width = 5):
        self.height = height
        self.color = color
        self.width = width
    #pygame.draw.rect(surface = screen, color = self.color, center = bird.pos, radius = bird.radius)
    
class Enemy:
    pass

    
class Weapon:
    pass


bird = Bird(player_position, True)
pipe = Pipe()
# Game Loop
while running:
    
    if falling:
        bird.pos.y += 5 # Constantly makes bird fall
    else:
        bird.flap()
    
    # Detect quit and terminate
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                falling = False
                
                
    screen.blit(background, (0,0)) # Resets background (removes player trail)
    pygame.draw.circle(surface = screen, color = '#665a2c', center = bird.pos, radius = bird.radius)
    
    
    
    
     # Key detections
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
       bird.flap() 
    
    
    # .flip() updates to screen
    pygame.display.flip()
    clock.tick(60) # 60 FPS max
    