from population import Population

def setup():
    global goal
    global test
    
    size(800, 800)
    frameRate(100)
    
    goal = PVector(400, 10)
    test = Population(500)

    
def draw():
    background(255)
    fill(255, 0, 0)
    ellipseMode(CENTER)
    ellipse(goal.x, goal.y, 10, 10);
    fill(50);
    text("GENERATION: " + str(test.gen), 15, 15, 100, 100)
    
    fill(0, 0, 255);
    rect(0, 500, 600, 10);
    
    fill(0, 0, 255);
    rect(800, 200, -600, 10);
    
    if test.allDotsDead():
        test.calculateFitness()
        test.naturalSelection()
    else:
        test.update()
        test.show()
    
