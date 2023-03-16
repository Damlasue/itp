def setup():
    size(400, 400) # Set the size of canvas
    noStroke() # Disable drawing the stroke
    
def drawObject(x,y,s):
    push()
    translate(x,y)
    scale(s)
    fill(0) # Fill in with black color
    ellipse(25, 20, 30, 20) # Draw ellipses
    ellipse(55, 20, 30, 20)
    triangle(40, 65, 10, 20, 70, 20)
    pop()

def drawGrid(gridSize):
    size = width / gridSize
    cellScale = 5 / float(gridSize)
    for y in range(gridSize):
        for x in range(gridSize):
            drawObject(x * size, y * size, cellScale)
    
def draw():
    drawGrid(10)
