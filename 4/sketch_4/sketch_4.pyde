import random
add_library('pdf')

def setup():
    global img
    size(492, 633)
    img = loadImage("image.png") #zdjęcie wygenerowane z https://thispersondoesnotexist.com/ :)
    beginRecord(PDF, "outimage.pdf")
    
    #print(random.random())
    #print(type(img))
    
def draw():
    global img
    image(img, 0,0, 492, 633)
    
    if keyPressed: # poniższy komentarz powinien być zawarty dla użytkownika w mini UI asmego programu, a nie tylko dla programisty w kodzie :)
        if key == "1": #możliwość przeskakiwania między opcjami elementów graficznych za pomocą 1, 2, 3
            beginShape()
            noStroke()
            fill(255, 80, 8, 150)
            circle(190, 300, 90)
            circle(300, 300, 90)
            fill(255, 51, 119, 200)
            rect(150,300,-40,10)
            rect(380,300,-45,10)
            rect(260,300,-30,10)
            endShape()
        
        if key == "2":  
            noStroke()
            smooth()
            translate(280, 200)
            scale(2.5)
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
            arc(243, 150, 320, 320, PI, TWO_PI)
            arc(150, 60, 170, 40, PI, TWO_PI)
            arc(340, 60, 170, 40, PI, TWO_PI)
            fill(255, 0, 85)
            arc(243, 150, 320, 220, PI, TWO_PI)
            fill(179, 0, 59)
            arc(243, 150, 320, 90, PI, TWO_PI)
            fill(255, 255, 255)
            circle(300, 90, 50)
            circle(190, 90, 50)
            fill(0, 0, 0)
            circle(300, 90, 20)
            circle(190, 90, 20)
            endShape()
            
            beginShape()
            fill(255, 204, 221, 200)
            circle(243, 470, 120)
            fill(255, 255, 255, 100)
            circle(280, 490, 20)
            circle(290, 470, 7)
            endShape()
            
            beginShape()
            fill(204, 0, 0)
            ellipse(246, 100, 20, 30)
            endShape()
            # namęczyłaś się z rysunkami
            
        endRecord() # teraz będzie zamykać zapis pliku dopiero po wcinięciu jakiegoś klawisza, wczęśniej zamykało w pierwszej klatce nie zdążając zarejestrować dodatków
    
def mousePressed():
    exit()
    
# 1,75p

          
