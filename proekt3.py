from pygame import*

okno = display.set_mode((1000,600))
bkgd = transform.scale(image.load('подводный мир.jpg'),(1000,600))
gm = True
FPS = 80
clock = time.Clock()   
mixer.init()
mixer.music.load('phonky.mp3' )
mixer.music.play()

class sprit(sprite.Sprite):
    def __init__(self, imag, x, y,speed):
        super().__init__()
        self.image = transform.scale(image.load(imag),(60,60))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def self (self):
        okno.blit(self.image,(self.rect.x, self.rect.y))

class wall(sprite.Sprite):
    def __init__(self,  x, y):
        super().__init__()
        self.image = Surface((70,30))
        self.image.fill((0,50,200))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def selff (self):
        okno.blit(self.image,(self.rect.x, self.rect.y))
    def update(self):
            keys_pressed = key.get_pressed()
            if keys_pressed[K_d]:
                self.rect.x -= 5
            if keys_pressed[K_w]:
                self.rect.y +=5
            if keys_pressed[K_a]:
                self.rect.x +=5
            if keys_pressed[K_s]:
                self.rect.y -=5
  
ochki = 0
health = 10
font.init()
font1 = font.Font(None, 80)
font2 = font.Font(None, 80)
h1 = sprit("ball.png",280,340,4)
#los = font.render('you lose', True, (200,200,0))

level = [
"-------------------------",
"-                       -",
"-                       -",
"-    -----              -",
"-            --         -",
"-                -      -",
"--                 -    -",
"-                       -",
"-                   --- -",
"-   -           -       -",
"-            -          -",
"-      ---              -",
"-                       -",
"-  ------------         -",
"-                       -",
"-                -      -",
"-       ---         --  -",
"-  ----                 -",
"-                       -",
"-------------------------"]

grsten=sprite.Group()
steni=[]
x = 280
y = 340
for y1 in range(len(level)):
    y2=y1*61
    for x1 in range(len(level[y1])):
        x2 = x1*61
        if level[y1][x1]=="-":
            w = wall(x2,y2)
            steni.append(w)
            grsten.add(w)

while gm:
    okno.blit(bkgd,(0,0))
    for i in event.get():
        if i.type == QUIT:
            gm = False
    #txt = 'очки '+ str(ochki)
    #txt2 = 'здоровье' + str(health)
    h1.self()

    h1.self()
    for i in steni:
        i.selff()
        i.update()
        i.rect.y-=3
    if sprite.spritecollideany(h1,grsten):
        for i in grsten:
            i.rect.y+=3.5
    #text = font1.render(txt,1,(230,40,230))
    #text2 = font2.render(txt2,2,(40,115,235))
    #okno.blit(text,(5,200))
    #okno.blit(text2,(10,300))
    #if health <= 1:
        #print(los)
        #gm = False
    display.update()
    clock.tick(FPS)