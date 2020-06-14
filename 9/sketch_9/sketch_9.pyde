def setup():
    global img
    global img2
    size(600, 600)
    strokeWeight(15)
    textSize(40)
    noFill()
    img = loadImage("lato.png") 
    img2 = loadImage("basenik.jpg")

def draw():
    clear()
    background (255, 204, 221) 
    if key == CODED:
        if keyCode== UP:
            try:
                image(img, 200, 200, 300, 300)
            except:
                stroke(204, 0, 0)
                text("Brak pliku :(", 250, 150)
            else:
                stroke(179, 179, 255)
            finally:
                rect(200, 200, 300, 300)
                
        if keyCode== DOWN:
            try:
                image(img2, 200, 200, 300, 300)
            except:
                stroke(204, 0, 0)
                text("Brak pliku :(", 250, 150)
            else:
                stroke(179, 179, 255)
            finally:
                rect(200, 200, 300, 300)
                
# 1,5pkt
