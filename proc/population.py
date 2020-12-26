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
    
    def allDotsDead(self):
        for dot in self.dots:
            if not dot.dead and not dot.reachedGoal:
                return False
        
        return True
    
    def calculateFitnessSum(self):
        self.fitnessSum = 0;
        for dot in self.dots:
            self.fitnessSum += dot.fitness
                    
    def calculateFitness(self):
        for dot in self.dots:
            dot.calculateFitness()
    
    def selectParent(self):
        rand = random(self.fitnessSum)
        runningSum = 0
        for dot in self.dots:
            runningSum += dot.fitness
            if runningSum > rand:
                return dot
            
        print("I should not be called")
                            
    def naturalSelection(self):
        best_baby = self.getCloneOfBestDot()
        best_baby.isBest = True
        newDots = [best_baby]
        self.calculateFitnessSum()
        
        for count in range(len(self.dots) - 1):
            cloned_baby = self.selectParent().cloneABaby()
            cloned_baby.brain.mutate()
            newDots.append(cloned_baby)
            
        self.dots = newDots
        self.gen += 1
                        
    def getCloneOfBestDot(self):
        max = 0
        bestDot = None
        for dot in self.dots:
            if dot.fitness > max:
                max = dot.fitness
                bestDot = dot
        
        if bestDot.reachedGoal:
            self.minStep = bestDot.brain.step
            print("min_step", self.minStep)
            
        return bestDot.cloneABaby()
    
        
