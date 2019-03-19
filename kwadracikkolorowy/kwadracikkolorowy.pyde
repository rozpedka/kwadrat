global pos1
pos1=0
global pos2
pos2=250  #tu dałam takie, bo jeszcze nie jest ustalony size okienka, więc nie może być podzielony height przez dwa, bo jeszcze tego height nie ma 
def setup():
    rectMode(CENTER)
    size(500,500)
    global pos1
    pos1=0
    global pos2
    pos2=height/2
    noStroke()

def draw():
    background(0)
    kolor1=(255,0,100,120,19,199,149,50) 
    liczba1=int(random(7)) 
    kolor2=(60,200,0,125,180,130,100,72)
    liczba2=int(random(7))
    kolor3=(0,255,70,155,199,1,100,70)
    liczba3=int(random(7)) #z kazdej listy wylosuje jedna liczbe 
    fill(kolor1[liczba1],kolor2[liczba2],kolor3[liczba3]) #wylosowane liczby z list stworza jakis losowy kolor RGB 
    global pos1
    global pos2
    rect(pos1,pos2,50,50)
    pos1+=1
    pos2+=1
    if (pos2 > height): #w ten sposob bedzie to bardziej manualne, bo bez roznicy jaka bedzie wielkosc okienka bedzie sie zatrzymywac
        noLoop()
