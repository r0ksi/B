def setup():
    global img
    global img2
    size(600, 600)
    img = loadImage("lato.png") 
    img2 = loadImage("basenik.jpg")

def draw():
    clear()
    background (255, 204, 221) 
    rect(200, 200, 300, 300)
    if key == CODED:
        if keyCode== UP:
            try:
                strokeWeight(15)
                stroke(179, 179, 255)
                image(img, 200, 200, 300, 300)
        
            except:
                stroke(204, 0, 0)
                text("Brak pliku :(", 250, 150)
                textSize(40)
        if key == CODED:
            if keyCode== DOWN:
                try:
                    strokeWeight(15)
                    stroke(179, 179, 255)
                    image(img2, 200, 200, 300, 300)
        
                except:
                    stroke(204, 0, 0)
                    text("Brak pliku :(", 250, 150)
                    textSize(40)
