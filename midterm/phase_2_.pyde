def setup():
    size(400, 400) # Set the size of canvas
    noStroke() # Disable drawing the stroke

def drawObject(x,y,s):
    push()
    translate(x,y)
    scale(s)
    fill(0) # Fill in with black color
    ellipse(60, 60, 30, 20) # Draw ellipses
    ellipse(90, 60, 30, 20)
    triangle(75, 105, 45, 60, 105,60)
    pop()

def draw():
    drawObject(0,0,1)
