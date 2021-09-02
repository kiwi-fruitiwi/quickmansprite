class Sprite:
    def __init__(self, animation, x, y, speed, move): # move is a boolean. should it move?
        self.pos = PVector(x, y)
        self.vel = PVector(random(-1,1), random(-1,1))
        self.acc = PVector(0, 0)        
        
        # animation is simply a list of image objects
        self.animation = animation
        self.frames = len(self.animation)
        self.w = self.animation[0].width
        self.r = self.w
        
        self.speed = speed
        self.move = move # the sprite always animates, but if this is False, it doesn't move
        self.index = 0
        
    
    def show(self):
        if self.vel.x > 0:
            self.show_mirror()
        else:
            # our sprite can have a speed below 1!
            # this floor and modulo lets us have decimal indices
            index = floor(self.index) % self.frames        
            frame = self.animation[index]
            image(frame, self.pos.x, self.pos.y)   
     
    
    def show_mirror(self):
        index = floor(self.index) % self.frames
        
        frame = self.animation[index]        
        pushMatrix()
        translate(self.pos.x + self.w, self.pos.y);
        scale(-1, 1)
        image(frame, 0, 0)
        popMatrix()
           
    
    # updates the velocity and position
    def update(self):
        self.vel.add(self.acc)
        self.pos.add(self.vel)
        self.acc.mult(0)
    
    
    def apply_force(self, force):
        # F=ma, but assume m=1 so F=a
        self.acc.add(force)
        
    
    def animate(self):
        ANIMATION_RATE = 80 * self.speed        
        self.index += self.speed
    
    
    # check to make sure our sprite is constrained within the edges
    # of the canvas. invert velocity if it goes past an edge to give a
    # "bounce" effect. 
    def edges(self):
        if self.pos.x + self.r >= width:
            self.vel.x *= -1
            
            # this extra line is needed to constrain our particle's position
            # within the canvas
            self.pos.x = width - self.r
            
        if self.pos.x - self.r <= 0:
            self.vel.x *= -1
            self.pos.x = self.r
        
        if self.pos.y + self.r >= height:
            self.vel.y *= -1
            self.pos.y = height - self.r
            
        if self.pos.y - self.r <= 0:
            self.vel.y *= -1
            self.pos.y = self.r
                    
                                    
    # This is Daniel Shiffman's code for his animated horse.
    # Animate from left to right, with a modifier for frame speed
    # not compatible with update()
    def animate_move(self):
        ANIMATION_RATE = 80 * self.speed
        
        self.index += self.speed
        
        if self.move:
            self.x -= self.speed * ANIMATION_RATE
            
            if self.x < -self.w:
                self.x = width  # supposed to be negative self.width
