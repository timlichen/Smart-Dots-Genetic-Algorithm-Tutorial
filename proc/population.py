from dot import Dot

class Population():
    
    def __init__(self, size):
        self.dots = []
        self.fitnessSum = 0
        self.gen = 1
        self.bestDot = 0
        self.minStep = 1000
        
        for i in range(size):
            self.dots.append(Dot())
    
    def show(self):
        for dot in self.dots:
            dot.show()
    
    def update(self):
        for dot in self.dots:
            if dot.brain.step > self.minStep:
                dot.dead = True
            else:
                dot.update()
            
        
        
