import math

class Brain():
    
    def __init__(self, size):
        self.step = 0
        self.directions = []
        self.size = size
        self.randomize();
    
    def randomize(self):
        for i in range(self.size):
            randomAngle = random(2*math.pi)
            self.directions.append(PVector.fromAngle(randomAngle))
    
    def clone(self):
        clone = Brain(self.size)
        clone.directions = self.directions
        return clone
    
    def mutate(self):
        mutationRate = 0.01
        for i in range(self.size):
            rand = random(1)
            if rand < mutationRate:
                randomAngle = random(2*math.pi)
                directions[i] = PVector.fromAngle(randomAngle)
                
        
        
            
