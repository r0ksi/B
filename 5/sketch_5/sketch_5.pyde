class WskazowkaZegara(): 
    godzina = 0
    def __init__(self, arg_x, arg_y, arg_r): 
        self.obrot =+ 0
        self.x = arg_x 
        self.y = arg_y
        self.r = arg_r 
        
    def rysuj(self): 
        fill(0, 0, 0)
        arc(self.x, self.y, self.r, self.r, 0+radians(self.obrot+265), PI+ radians(self.obrot+90), PIE)

    def obroc(self, stopnie): 
        self.obrot += stopnie
        WskazowkaZegara.godzina += 1
        
def setup():
    size(400, 400)
    global wskazoweczka, wskazowka
    global img
    wskazoweczka = WskazowkaZegara(width/2, height/2, 140)
    wskazowka = WskazowkaZegara(width/2, height/2, 140) # miały być dwa obiekty
    img = loadImage("img.png")

    print(type(img))
    
def mouseWheel(event): 
    wskazoweczka.obroc(30)
    wskazowka.obroc(1)
    print(WskazowkaZegara.godzina)
    
def draw(): 
    image(img, 0,0, 400, 400)
    wskazoweczka.rysuj()
    wskazowka.rysuj()

# bardzo mocno wzorowane na moim kodzie, to ważny temat, spróbuj jeszcze go pozgłębiać
# zwróć uwagę, jak niewiele kodu trzeba obecnie dodać, aby otrzymać kolejny obiekt o tak 'skomplikowanej' już funkcjonalności
# 1,25pkt, głównie za małą oryginalność w stosunku do atrybutów i metody (zostały bez zmian z moimi)
