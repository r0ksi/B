import random
add_library('pdf')

def setup():
    global img
    size(400, 400)
    img = loadImage("image.png") #zdjęcie wygenerowane z https://thispersondoesnotexist.com/ :)
    beginRecord(PDF, "outimage.pdf")
    
    print(random.random())
    print(type(img))
    
def draw():
    global img
    image(img, 0,0, height, width)
    
    if keyPressed:
        if key == "1": #możliwość przeskakiwania między opcjami elementów graficznych za pomocą 1, 2, 3
            beginShape()
            noStroke()
            fill(255, 80, 8, 150)
            ellipse(150,190,70,60)
            ellipse(250,190,70,60)
            fill(255, 51, 119, 200)
            rect(115,190,-35,10)
            rect(320,190,-35,10)
            rect(217,190,-35,10)
            endShape()
            
        if key == "2":  
            noStroke()
            smooth()
            translate(220, 90)
            scale(2.0)
            fill(255, 204, 255)
            beginShape()
            vertex(50, 15)
            bezierVertex(50, -5, 75, 5, 50, 45)
            vertex(50, 15)
            bezierVertex(50, -5, 25, 5, 50, 45)
            endShape()
    
        if key == "3":
            beginShape()
            fill(255, 153, 153)
            arc(200, 130, 260, 280, PI, TWO_PI)
            arc(130, 60, 170, 30, PI, TWO_PI)
            arc(270, 60, 170, 30, PI, TWO_PI)
            fill(255, 0, 85)
            arc(200, 130, 260, 180, PI, TWO_PI)
            fill(179, 0, 59)
            arc(200, 130, 260, 80, PI, TWO_PI)
            fill(255, 255, 255)
            circle(260, 100, 50)
            circle(140, 100, 50)
            fill(0, 0, 0)
            circle(260, 100, 20)
            circle(140, 100, 20)
            endShape()
            
            beginShape()
            fill(255, 204, 221, 200)
            circle(200, 300, 100)
            fill(255, 255, 255, 100)
            circle(230, 300, 20)
            circle(230, 280, 7)
            endShape()
            
            beginShape()
            fill(204, 0, 0)
            ellipse(200, 100, 20, 30)
            endShape()
            
            
    endRecord()
    
def mousePressed():
    exit()
          
