def setup():
    size(600, 600)
    point(50, 50)
    rectMode(CORNER)
def draw():
    if mousePressed:
        rect(mouseX, mouseY, 200, 200)
    else:
        line(height, width, mouseX, mouseY)
