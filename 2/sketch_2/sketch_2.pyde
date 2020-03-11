def setup():
    size(400, 400)
    ellipseMode(CENTER)
    frameRate(90)
    global slownik
    slownik = {"czerwony":(255, 0, 0), "fioletowy":(204, 0, 255), "rozowy":(255, 204, 204)}
    global x
    global y
    global x1
    global y1
    x = 10
    y = 200
    x1 = 1
    y1 = 1
def draw():
    background(20, 0, 26)
    global x
    global y
    global x1
    global y1
    ellipse(x, y, 50, 50)
    x = x + x1
    y = y + y1
    
    if(x > height-10):
        fill(*slownik["czerwony"])
        x1 = x1 * -1
        
    if(y > width-10):
        fill(*slownik["fioletowy"])
        y1 = y1 * -1
        
    if(y < 10):
        fill(*slownik["rozowy"])
        y1 = y1 * -1
        
    if mousePressed:
        exit()

    if(x == 10):
        exit()
