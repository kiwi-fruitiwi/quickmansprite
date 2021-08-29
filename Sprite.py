class Sprite:
    def __init__(self, animation, x, y, speed, move): # move is a boolean. should it move?
        self.x = x
        self.y = y
        
        # animation is simply a list of image objects
        self.animation = animation
        self.frames = len(self.animation)
        self.w = self.animation[0].width
        
        self.speed = speed
        self.move = move # the sprite always animates, but if this is False, it doesn't move
        self.index = 0
        
    
    def show(self):
        # our sprite can have a speed below 1!
        # this floor and modulo lets us have decimal indices
        index = floor(self.index) % self.frames        
        frame = self.animation[index]
        image(frame, self.x, self.y)   
     
    
    def show_mirror(self):
        index = floor(self.index) % self.frames
        
        frame = self.animation[index]        
        pushMatrix()
        translate(self.x + self.w, self.y);
        scale(-1, 1)
        image(frame, 0, 0)
        popMatrix()
           
    
    # This is Daniel Shiffman's code for his animated horse.
    # Animate from left to right, with a modifier for frame speed
    def animate(self):
        ANIMATION_RATE = 80 * self.speed
        
        self.index += self.speed
        
        if self.move:
            self.x -= self.speed * ANIMATION_RATE
            
            if self.x < -self.w:
                self.x = width  # supposed to be negative self.width
