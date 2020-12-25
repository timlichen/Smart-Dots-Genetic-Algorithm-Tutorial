from population import Population


def setup():
    size(800, 800)
    frameRate(100)
    global goal
    goal = PVector(400, 10)
    
    global test
    test = Population(1000)

    
def draw():
    background(255)
    
    fill(255, 0, 0)
    ellipseMode(CENTER)
    ellipse(goal.x, goal.y, 10, 10);
    test.update()
    test.show()
    
