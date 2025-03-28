import pygame
import random

pygame.init()

HEIGHT = 600
WIDTH = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

road = pygame.image.load("AnimatedStreet.png")
coin_i = pygame.image.load("Coin.png")
coin_im = pygame.transform.scale(coin_i, (50, 50))
player_im = pygame.image.load("Player.png")
enemy_im = pygame.image.load("enemy.png")

pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(-1)
coin_sound = pygame.mixer.Sound('Coin.mp3')
crash_sound = pygame.mixer.Sound('crash.wav')

font = pygame.font.SysFont("Verdana", 30)
count = 0

def reset_game():
    global player, coin, enemy, count
    player = Player()
    coin = Coin()
    enemy = Enemy()
    all_sprites.empty()
    all_sprites.add(player, coin, enemy)
    coin_sprites.empty()
    coin_sprites.add(coin)
    enemy_sprites.empty()
    enemy_sprites.add(enemy)
    count = 0

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_im
        self.speed = 5
        self.rect = self.image.get_rect()
        self.rect.midbottom = (WIDTH // 2, HEIGHT)
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_im
        self.speed = 5
        self.rect = self.image.get_rect()
        self.generate()
    
    def generate(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.width)
        self.rect.bottom = 0
    
    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.generate()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_im
        self.speed = 7
        self.rect = self.image.get_rect()
        self.generate()
    
    def generate(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.width)
        self.rect.bottom = 0
    
    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.generate()

player = Player()
coin = Coin()
enemy = Enemy()

all_sprites = pygame.sprite.Group(player, coin, enemy)
coin_sprites = pygame.sprite.Group(coin)
enemy_sprites = pygame.sprite.Group(enemy)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.move()
    coin.move()
    enemy.move()
    
    if pygame.sprite.spritecollideany(player, coin_sprites):
        coin_sound.play()
        count += 1
        coin.generate()
    
    if pygame.sprite.spritecollideany(player, enemy_sprites):
        crash_sound.play()
        pygame.time.delay(1000)
        reset_game()
    
    screen.blit(road, (0, 0))
    all_sprites.draw(screen)
    
    score_text = font.render(f"Score: {count}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
