from pygame import *

wind = display.set_mode((700,500))
display.set_caption('Пинг понг')
background = transform.scale(image.load('back.jpg'),(700,500))

class GameSprite(sprite.Sprite):
    def __init__(self,p_image,speed,x,y,size1,size2):
        super().__init__()
        #self.size1 = size1
        #self.size2 = size2
        self.image = transform.scale(image.load(p_image),(size1,size2))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        wind.blit(self.image,(self.rect.x,self.rect.y))        

class Player(GameSprite):
    def update(self):
        keys_p = key.get_pressed()
        if keys_p[K_UP] or self.rect.y>500-150:
            self.rect.y -= self.speed
        if keys_p[K_DOWN] or self.rect.y<0:
            self.rect.y += self.speed

class Player1(GameSprite):
    def update(self):
        keys_p = key.get_pressed()
        if keys_p[K_w] or self.rect.y>500-150:
            self.rect.y -= self.speed
        if keys_p[K_s] or self.rect.y<0:
            self.rect.y += self.speed

font.init()
font = font.SysFont('Arial',70)


hero = Player('racket.jpg',15,630,300,70,170)
hero1 = Player1('racket.jpg',15,0,300,70,170)
ball = Player('ball.png',0,350,300,50,50)

speed_x = 5
speed_y = 5
clock = time.Clock()
FPS = 60
game = True
finish = False
while game == True:
    for i in event.get():
        if i.type == QUIT:
            game = False

    if not finish:
        wind.blit(background,(0,0))
        hero.reset()
        hero.update()
        hero1.reset()
        hero1.update()
        ball.reset()
        ball.update()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(hero,ball) or sprite.collide_rect(hero1,ball):
            speed_x *= -1
            speed_y *= 1

        lose = font.render('YOU LOSE!',True,(255,215,0))    

        if ball.rect.x > 649:
            speed_x *= -1
            finish = True
            wind.blit(lose,(325,200))
        if ball.rect.x < 0:
            speed_x *= -1
            finish = True
            wind.blit(lose,(200,200))
        if ball.rect.y > 449:
            speed_y *= -1
            
        if ball.rect.y < 0:
            speed_y *= -1
            


        

        
        display.update()
        clock.tick(FPS)


