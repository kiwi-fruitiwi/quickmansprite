
# Coding Challenge #111: animated sprite
# 2021.07.27
# We're planning to animate Quick Man from Mega Man 2
# see https://www.youtube.com/watch?v=8s_00b0stJU for mm2 gameplay
# 
# v0.01 animate quick man boss intro sequence with custom spritesheet
# v0.02 cut and animate walking sequence
# v0.03 draw walking quickman and use WASD to initiate walking animation
# v0.04 cut and animate jumping sequence » W to jump
# v0.05 cut and animate block
# v0.06 shoot + boomerangs


class Sprite:
    def __init__(self, animation, x, y, speed, move): # move is a boolean. should it move?
        # animation is simply a list of image objects
        self.x = x
        self.y = y
        self.animation = animation
        self.frames = len(self.animation)
        self.w = self.animation[0].width
        # self.l = self.animation[0].length
        self.speed = speed
        self.index = 0
        self.move = move # the sprite always animates, but if this is False, it doesn't move
    
    
    def show(self):
        # our sprite can have a speed below 1!
        # this floor and modulo lets us have decimal indices!
        index = floor(self.index) % self.frames
        image(self.animation[index], self.x, self.y)
        
    
    # This is Daniel Shiffman's code for his animated horse.
    # Animate from left to right, with a modifier for frame speed
    def animate(self):
        ANIMATION_RATE = 80 * self.speed
        
        self.index += self.speed
        
        if self.move:
            self.x -= self.speed * ANIMATION_RATE
            
            if self.x < -self.w:
                self.x = width  # supposed to be negative self.width


def setup():
    global sprites
        
    colorMode(HSB, 360, 100, 100, 100)
    spritesheet = loadImage("quickman-run-shoot-boomerangs.png")
    size(700, 300)
    # frameRate(10)
    
    delay(100)  # with no delay we never get to see the 1st frame
    
    ichi = spritesheet.get(0, 32, 32, 32)
    ni = spritesheet.get(32, 32, 32, 32)
    san = spritesheet.get(64, 32, 32, 32)
    
    imgs = [ni, ichi, ni, san] 
    sprites = []   
    
    for i in range(9):
        sprites.append(Sprite(imgs, 10, 10 + i * 32, random(0.15, 0.25), move=True))
        
        
    sprites.append(sprite_quickman_intro())
    

def draw():
    global sprites
    background(209, 95, 33)
    
    for sprite in sprites:
        sprite.show()
        sprite.animate()
    
    
# returns a quick man intro sprite sequence
def sprite_quickman_intro():
    spritesheet = loadImage("quickman-intro.png")
    SPRITE_DIMENSIONS = 32
    s = 3 * SPRITE_DIMENSIONS # desired sprite size scale factor
    # put each frame in an imgs list starting with []
    imgs = []
    for i in range(8):
        img = spritesheet.get(i*SPRITE_DIMENSIONS, 0, 32, 32)
        img.resize(s, s)
        imgs.append(img)        
    
        # for i in range(9):
        # sprites.append(Sprite(imgs, 10, 10 + i * 32, random(0.15, 0.25)))
        
    # quick man intro sequence
    intro = Sprite(imgs, width/2 - s/2, height/2 - s/2, 0.15, move=False)
    return intro
    

# this code displays quick man's 8-frame intro animation
def spriteless_quickman_intro():
    spritesheet = loadImage("quickman-intro.png")
    
    # allows us to select the position of the sprite in the sprite sheet
    # as a function of the framecount
    x = frameCount % 8 * 32
    
    # All robot master sprites in mega man 2 are 32x32.
    #
    # The original spritesheet had too little space between each quickman,
    # I edited the file and fixed this.
    #
    # The boss intro sprites start at 0,0 and are 32x32 across 8 sprites
    SPRITE_DIMENSIONS = 32
    img = spritesheet.get(x, 0, 32, 32)
    
    s = SPRITE_DIMENSIONS * 3  # s is the side length of a square sprite
    img.resize(s, s)  # let's make it easier to see and debug    
    
    # center the sprite on the canvas using its side length, s
    image(img, width/2 - s/2, height/2 - s/2)


# our original code without using our Sprite object        
def objectless_sprite():   
    spritesheet = loadImage("quickman-run-shoot-boomerangs.png")
     
    ichi = spritesheet.get(0, 32, 32, 32)
    ni = spritesheet.get(32, 32, 32, 32)
    san = spritesheet.get(64, 32, 32, 32)
    
    imgs = [ni, ichi, ni, san]
    SPRITE_DIMENSIONS = 32
    s = SPRITE_DIMENSIONS * 3  # s is the side length of a square sprite
    for img in imgs:
        img.resize(s, s)  # let's make it easier to see and debug    

    image(imgs[frameCount % len(imgs)], width/2-s/2, height/2 - s/2)
