from brain import Brain

class Dot():
    
    def __init__(self):
        self.dead = False
        self.reachedGoal = False
        self.isBest = False
        self.pos = PVector(width / 2, height - 10)
        self.vel = PVector(0, 0)
        self.acc = PVector(0, 0)
        self.brain = Brain(1000)
        self.fitness = 0
        
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
        if not self.dead and not self.reachedGoal:
            self.move()
            if self.pos.x < 2 or self.pos.y < 2 or self.pos.x > width - 2  or self.pos.y > height - 2:
                self.dead = True
            elif dist(self.pos.x, self.pos.y, 400.0, 10.0) < 5:
                self.reachedGoal = True
            elif self.pos.x < 600 and self.pos.y < 510 and self.pos.x > 0 and self.pos.y > 500:
                self.dead = True
            elif self.pos.x < 800 and self.pos.y < 210 and self.pos.x > 200 and self.pos.y > 200:
                self.dead = True
                      
   
    def calculateFitness(self):
        """ not entirely sure about the math behind the fitness """
        if self.reachedGoal:
            self.fitness = 1.0 / 16.0 + 10000.0 / (self.brain.step * self.brain.step)
        else:
            distanceToGoal = dist(self.pos.x, self.pos.y, 400.0, 10.0)
            self.fitness = 1.0 / (distanceToGoal * distanceToGoal)
           
    def cloneABaby(self):
        baby = Dot()
        baby.brain = self.brain.clone()
        return baby
    
