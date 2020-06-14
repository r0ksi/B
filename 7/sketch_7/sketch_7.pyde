from abc import ABCMeta, abstractmethod 
class Pet():
    __metaclass__=ABCMeta 
    @abstractmethod 
    def speak(self): 
        super().__init__()
        return 'no sound'
class Cat(Pet): 
    def __init__(self, name):
        self.name = name
    def speak(self): 
        text('meow', random(50, width-70), random(50, height-50))
        return 'meow'
class Dog(Pet):
    def __init__(self, name):
        self.name = name
    def speak(self):
        text('woof', random(50, width-70), random(50, height-50))
        return 'woof'
    def gimmePaw(self):
        image(loadImage("lapa.png"), random(50, width-70), random(50, height-100))
    def __add__(self, other): 
        return self.name[0]+ ' i ' + other.name[0]
class KotyRoksi(Pet):
    def __init__(self, name):
        self.name = name
    def speak(self):
        text('mrrrr', random(50, width-70), random(50, height-50))
    def Kotki(self):
         image(loadImage("kotki.png"), random(50, width-70), random(50, height-100))
    def __add__(self, other): # miało być nadpisane odejmowanie, czyli metoda __sub__
        return self.name[0]+ ' i ' + other.name[0]
def setup():
    background(204, 153, 255)
    size(400,400)
    textSize(18)
    Rex = Dog('Rex') 
    Benio = Dog('Benio')
    Skrypcik = Cat('Skrypcik') 
    Maniek = KotyRoksi('Maniek')
    Zenka = KotyRoksi('Zenka') # to od Zenka disco polo? ;D
    global list_of_pets
    list_of_pets = [Rex, Benio, Skrypcik, Maniek, Zenka] 
    print(Maniek+Zenka) 
    print(isinstance(Maniek, Pet))
    print(isinstance(Zenka, Pet))
def draw(): 
    pass
    
def mouseClicked():
    for pet in list_of_pets:
        pet.speak() 
        if isinstance(pet, Dog): 
            pet.gimmePaw()
        if isinstance(pet, KotyRoksi):
            pet.Kotki()
# 1,75 pkt
