from brain import Brain


class Dot():
    
    def __init__(self):
        self.dead = False
        self.reachedGoal = False
        self.isBest = False
        self.pos = PVector(width / 2, height - 10)
        self.vel = PVector(0, 0)
        self.acc = PVector(0, 0)
        self.brain = Brain(100)
        
    def show(self):
        if self.isBest:
            fill(0, 255, 0)
            ellipse(self.pos.x, self.pos.y, 8, 8)
        else:
            fill(0)
            ellipse(self.pos.x, self.pos.y, 4, 4)
    
    def move(self):
        if len(self.brain.directions) > self.brain.step:
            self.acc = self.brain.directions[self.brain.step]
            self.brain.step += 1
        else:
            self.dead = True
        
        self.vel.add(self.acc)
        self.vel.limit(5)
        self.pos.add(self.vel)
            
    def update(self):
        self.move()
        
        
    
