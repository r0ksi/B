class Kwadrat():
    def __init__(self, bok): 
        self.bok = bok
    def sketch(self, x, y):
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)
        
        
class Domek(Kwadrat):
    def sketchDomek(self, x, y): #po co przekazywać argumenty, z którymi nic isę dalej wewnątrz metody nie robi?
        fill(255, 221, 153)
        Kwadrat.sketch(self, x, y)
        _x1_ = 0
        fill(128, 0, 0)
        komin = rect(self.x+self.bok, self.y-self.bok/3, -self.bok/5, self.bok/3)
        fill(0, 51, 0)
        drzewo = ellipse(self.x, self.y, self.bok, self.bok)
        strokeWeight(5)
        stroke(115, 77, 38)
        pien = line(x+_x1_, y, x+_x1_, y+self.bok)
        strokeWeight(1)
        stroke(0)
        
def setup():
    size(400, 400)
    background(153, 153, 255)
    malyDomek = Domek(50.0)
    malyDomek.sketchDomek(250, 260)
    duzyDomek = Domek(80.0)
    duzyDomek.sketchDomek(90, 140)
        
# plus do aktywności za pomysł
# 1,75pkt
