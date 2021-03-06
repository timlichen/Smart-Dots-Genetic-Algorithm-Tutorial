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
        clone = Brain(1000)
        clone.directions = [x for x in self.directions]  # new list must be established here since the reference to the self.directions array 
                                                         # might be used multiple times when the parent selection and fitness algorithm are run
                                                         # i.e. multiple clones reference the same list, when the mutation occurs, they all get the same set of mutations and their direction set will all be the same.
        return clone
    
    def mutate(self):
        mutationRate = 0.01
        for i in range(len(self.directions)):   
            rand = random(1)
            if rand < mutationRate:
                randomAngle = random(2*math.pi)
                self.directions[i] = PVector.fromAngle(randomAngle)
                           
                
        
        
                   
