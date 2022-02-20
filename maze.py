#создай игру "Лабиринт"!
from pygame import *


#создай окно игры
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Maze')

#задай фон сцены
background = transform.scale(image.load('background.jpg'), (win_width, win_height))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (60,60))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x> 5:
            self.rect.x-= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x< 595:
            self.rect.x += self.speed
        if keys_pressed[K_DOWN] and self.rect.y<430:
            self.rect.y += self.speed
        if keys_pressed[K_UP] and self.rect.y>5:
            self.rect.y -= self.speed
class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 425:
            self.direction = "right"
        if self.rect.x >= win_width - 85:
            self.direction = 'left'

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

wall1 = Wall(35,46,67, 100, 0, 20, 350)
wall2 = Wall(35,46,67, 200, 300, 20, 350)
wall3 = Wall(35,46,67, 200, 300, 350, 20)
wall4 = Wall(35,46,67, 400, 100, 20, 325)
wall5 = Wall(35,46,67, 250, 0, 20, 200)
wall6 = Wall(35,46,67, 500, 200, 350, 20)
treasure = GameSprite('treasure.png',275, 375, 0)
hero = Player('hero.png', 50, 365, 3)
enemy = Enemy("cyborg.png", 450, 365, 3)

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
money = mixer.Sound("money.ogg")
kick = mixer.Sound("kick.ogg")

game = True
clock = time.Clock()
FPS = 60
finish = False

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render("YOU LOSE", True, (180, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))
        hero.reset()
        enemy.reset()
        
        hero.update()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()
        enemy.update()
        treasure.reset()
    
        if sprite.collide_rect(hero, enemy) or sprite.collide_rect(hero, wall1) or sprite.collide_rect(hero, wall2) or sprite.collide_rect(hero, wall3) or sprite.collide_rect(hero, wall4) or sprite.collide_rect(hero, wall5) or sprite.collide_rect(hero, wall6):
            finish = True
            window.blit(lose, (200, 200))
            kick.play()
            mixer.music.stop()
            
            

        if sprite.collide_rect(hero, treasure):
            finish = True
            window.blit(win, (200,200))
            money.play()
            mixer.music.stop()
            
            

        
        
        
        display.update()
        clock.tick(FPS)