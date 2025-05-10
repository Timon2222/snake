from pygame import *
window = display.set_mode((700, 500))
display.set_caption('snake')
background = transform.scale(image.load('background.png'), (700, 500))



clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image,  player_x, player_y,  size_x, size_y, player_speed):
         super().__init__()
         self.image = transform.scale(image.load(player_image), (size_x, size_y))
         self.speed = player_speed
         self.rect = self.image.get_rect()
         self.rect.x = player_x
         self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))



class Tail(GameSprite):
    def __init__(self, player_image,  player_x, player_y,  size_x, size_y, player_speed):
        super().__init__(player_image,  player_x, player_y,  size_x, size_y, player_speed)
        self.timer = timer

    

        
    def update(self):
        self.rect.y = self.speed_y
        self.rect.x = self.speed_x

        keys_pressed = key.get_pressed()
            if keys_pressed[K_LEFT]  
                self.rect.x -= self.speed

            if keys_pressed[K_RIGHT]  
                self.rect.x += self.speed

            if keys_pressed[K_UP]  
                self.rect.y -= self.speed

            if keys_pressed[K_DOWN]  
                self.rect.y += self.speed



snake('snake.png',300, 400, 50, 50, 50)
food('apple.png', 250, 250, 50, 50, 50)
game = True
finish = False


tails = sprite.Group()
score = 0

while game:
    if finish != True:
        window.blit(background,(0, 0))
        snake.update()
        snake.reset()
        if player.colliderect(food):
            score += 1
            food.rect.x = randint(0, 23) * 30
            food.rect.y = randint(0, 16) * 30
        t = Tail('snake.png', player.rect.x-player.speed_x, player.rect.y-player.speed_y, 29, 29, 0, score)
        tails.add(t)
        tails.update()
        tails.draw(window)
        wait = 30

        keys= key.get_pressed()
        if keys_pressed[K_LEFT]
            player.speed_x = -player_speed
            player_speed_y = 0
        if keys_pressed[K_RIGHT]  
            player.speed_x = player_speed
            player_speed_y = 0

        if keys_pressed[K_UP]  
            player.speed_y = -player_speed
            player_speed_x = 0

        if keys_pressed[K_DOWN]  
            player.speed_y = player_speed
            player_speed_x = 0

        for e in event.get():
            if e.type == QUIT:
                game = False    

    clock.tick(FPS)
    display.update()