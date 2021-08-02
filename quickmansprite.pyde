
# Coding Challenge #111: animated sprite
# 2021.07.27
# We're planning to animate Quick Man from Mega Man 2
# 
# v0.01 animate quick man boss intro sequence with custom spritesheet
# v0.02 cut and animate walking sequence
# v0.03 draw walking quickman and use WASD to initiate walking animation
# v0.04 cut and animate jumping sequence » W to jump
# v0.05 cut and animate block
# v0.06 shoot + boomerangs


def setup():
    global spritesheet
    
    spritesheet = loadImage("revised-quicksheet.png")
    size(700, 300)
    frameRate(12)
    delay(1000)  # with no delay we never get to see the 1st frame  
      

def draw():
    global spritesheet
    
    colorMode(HSB, 360, 100, 100, 100)
    background(209, 95, 33)
    
    x = frameCount % 8 * 32
    
    # All robot master sprites in mega man 2 are 32x32.
    #
    # The original spritesheet had too little space between each quickman,
    # I edited the file and fixed this.
    #
    # The boss intro sprites start at 0,0 and are 32x32 across 8 sprites
    SPRITE_DIMENSIONS = 32
    img = spritesheet.get(x, 0, 32, 32)
    
    s = SPRITE_DIMENSIONS * 8  # s is the side length of a square sprite
    img.resize(s, s)  # let's make it easier to see and debug    
    
    # center the sprite on the canvas using its side length, s
    image(img, width/2 - s/2, height/2 - s/2)
