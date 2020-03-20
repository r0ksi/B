def setup():
    size(600, 600)
    point(50, 50)
    rectMode(CORNER)
def draw():
    if mousePressed:
        rect(mouseX, mouseY, height/3, width/3) # lepiej używać zależnych wielkości
    else:
        line(height, width, mouseX, mouseY)
        
# 2 pkt
