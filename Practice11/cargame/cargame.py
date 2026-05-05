#cargame.py
import pygame, sys
import json
import os
from pygame.locals import *
import random, time

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()
        self.image0 = pygame.image.load(f"files/Car_Red_2.png").convert_alpha()
        self.image = pygame.transform.scale(self.image0, (68, 120))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40),0)

        old_center = self.rect.center
        self.rect = self.rect.inflate(-20, -10)
        self.rect.center = old_center
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED + int(coin_counter/3))
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        self.active = False
        self.image0 = pygame.image.load(f"files/{image}.png").convert_alpha()
        self.image = pygame.transform.scale(self.image0, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40),0)

        old_center = self.rect.center
        self.rect = self.rect.inflate(-30, -30)
        self.rect.center = old_center
        self.type = image
        self.spawn()

    def spawn(self):
        while True:
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -180)

            blocked_rects = []

            for enemy in enemies:
                blocked_rects.append(enemy.rect)

            for coin in coins:
                blocked_rects.append(coin.rect)

            if self.rect.collidelist(blocked_rects) == -1:
                break

    def move(self):
        self.rect.move_ip(0, SPEED)

        if self.rect.top > 600:
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -10000)
 
class Player(pygame.sprite.Sprite):
    def __init__(self, settings):
        super().__init__()
        if settings["car_color"] == (200,0,0):
            img = "files/Car_Red.png"
        elif settings["car_color"] == (0,200,0):
            img = "files/Car_Green.png"
        else:
            img = "files/Car_Blue.png"

        self.image0 = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image0, (68, 120))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

        old_center = self.rect.center
        self.rect = self.rect.inflate(-20, -10)
        self.rect.center = old_center
 
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
                self.rect.move_ip(0, -P_SPEED)
        if pressed_keys[K_DOWN]:
                self.rect.move_ip(0,P_SPEED)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-P_SPEED, 0)
        if self.rect.right < SCREEN_WIDTH-25:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(P_SPEED, 0)


# coin
class Coin(pygame.sprite.Sprite):
    def __init__(self, image, score):
        super().__init__()
        self.active = False
        self.score = score
        self.coin = pygame.image.load(f"files/{image}.png").convert_alpha()
        self.image = pygame.transform.scale(self.coin, (50, 50))
        self.rect = self.image.get_rect()

        old = self.rect.center
        self.rect = self.rect.inflate(-15, -15)
        self.rect.center = old

        self.spawn()

    def spawn(self):
        while True:
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

            if not self.rect.colliderect(E1.rect):
                break

    def move(self):
        self.rect.move_ip(0, SPEED)

        if self.rect.top > 600:
            self.rect.top = 0
            self.spawn()


def save_score(name, score, distance):
    file = "leaderboard.json"

    if os.path.exists(file):
        with open(file, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append({
        "name": name,
        "score": score,
        "distance": int(distance)
    })

    data = sorted(data, key=lambda x: x["score"], reverse=True)[:10]

    with open(file, "w") as f:
        json.dump(data, f, indent=4)



def get_best_score():
    if not os.path.exists("leaderboard.json"):
        return 0

    with open("leaderboard.json", "r") as f:
        data = json.load(f)

    return data[0]["score"] if data else 0



def run_game(settings, player_name):
    pygame.init()
    best_score = get_best_score()
    distance_traveled = 0
    power_ups = 0

    #Setting up FPS 
    FPS = 60
    FramePerSec = pygame.time.Clock()

    #Creating colors
    RED   = (255, 0, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    last_hit_time = 0
    last_hit_time_repair = 0
    damage_cooldown = 1000
    slow_until = 0

    global SPEED,SCORE,COIN_SCORE,P_SPEED
    #Other Variables for use in the program
    if settings["difficulty"] == "Easy":
        SPEED = 5
    elif settings["difficulty"] == "Medium":
        SPEED = 7
    else:
        SPEED = 9
    SCORE = 0
    COIN_SCORE = 0
    P_SPEED = 5
    HP = 3
    HP_s = 0

    heart = pygame.image.load("files/heart.png")
    heart = pygame.transform.scale(heart, (10, 10))
    #Values about road
    road = pygame.image.load("files/AnimatedStreet.png")
    road = pygame.transform.scale(road, (400, 600))

    y1 = 0
    y2 = -600
    #Setting up Fonts
    font = pygame.font.SysFont("Verdana", 60)
    font_small = pygame.font.SysFont("Verdana", 20)
    game_over = font.render("Game Over", True, BLACK)

    coins_images = ('bronze','silver','gold')
    obstacles_images = ("oil_spill","obstacle", "nitro", "repair", "shield")

    #Create a white screen 
    DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    DISPLAYSURF.fill(WHITE)
    pygame.display.set_caption("Game")

    #Setting up Sprites
    global E1, coins, enemies
    P1 = Player(settings)
    E1 = Enemy()

    Bronze = Coin(coins_images[0],1)
    Silver = Coin(coins_images[1],2)
    Gold = Coin(coins_images[2],3)

    coins = pygame.sprite.Group()
    coins.add(Bronze, Silver, Gold)

    enemies = pygame.sprite.Group()
    enemies.add(E1)

    oil_spill = Obstacle(obstacles_images[0])
    obstacle = Obstacle(obstacles_images[1])
    nitro = Obstacle(obstacles_images[2])
    repair = Obstacle(obstacles_images[3])
    shield = Obstacle(obstacles_images[4])

    obstacles = pygame.sprite.Group()
    obstacles.add(oil_spill, obstacle, nitro, repair, shield)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(P1,E1,Bronze, Silver, Gold,oil_spill, obstacle, nitro, repair, shield)


    Silver.active = True
    oil_spill.active = False
    obstacle.active = False
    nitro.active = False
    repair.active = False
    shield.active = False
    #Adding a new User event 
    INC_SPEED = pygame.USEREVENT + 1
    pygame.time.set_timer(INC_SPEED, 1000)
    SPAWN_OBSTACLE = pygame.USEREVENT + 2
    pygame.time.set_timer(SPAWN_OBSTACLE, 3000)

    #Game Loop
    while True:
        distance_traveled += SPEED / 60
        if COIN_SCORE == 0:
            global coin_counter
            coin_counter = 0

        y1 += SPEED
        y2 += SPEED
        if y1 >= 600:
            y1 = -600

        if y2 >= 600:
            y2 = -600

        DISPLAYSURF.blit(road, (0, y1))
        DISPLAYSURF.blit(road, (0, y2))
        #Cycles through all events occurring  
        for event in pygame.event.get():
            if event.type == INC_SPEED:
                SPEED += 0.5
            if event.type == SPAWN_OBSTACLE:
                new_obstacle = random.choice([obstacle, oil_spill, nitro, repair, shield])

                if not new_obstacle.active:
                    new_obstacle.active = True
                    new_obstacle.spawn()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        scores = font_small.render(str(SCORE), True, WHITE)
        coin_scores = font_small.render(str(COIN_SCORE), True, WHITE)
        DISPLAYSURF.blit(scores, (10,10))
        DISPLAYSURF.blit(coin_scores, (370,10))
        dist_text = font_small.render(f"{int(distance_traveled)} m", True, WHITE)
        DISPLAYSURF.blit(dist_text, (150, 10))
        remain = max(0, best_score - int(distance_traveled))
        rec_text = font_small.render(f"To Record: {remain}", True, WHITE)
        DISPLAYSURF.blit(rec_text, (100, 35))

        #Moves and Re-draws all Sprites
        for entity in all_sprites:
            if entity in coins:
                if entity.active == True:
                    DISPLAYSURF.blit(entity.image, entity.rect)
                    entity.move()
            elif entity in obstacles:
                if entity.active == True:
                    DISPLAYSURF.blit(entity.image, entity.rect)
                    entity.move()
            else:
                DISPLAYSURF.blit(entity.image, entity.rect)
                entity.move()
            # pygame.draw.rect(DISPLAYSURF, RED, entity.rect, 2)

        #To be run if collision occurs between Player and Enemy
        now = pygame.time.get_ticks()

        if pygame.sprite.spritecollideany(P1, enemies):
            if now - last_hit_time > damage_cooldown:
                if HP_s:
                    HP_s-=1
                else:
                    HP -= 1
                last_hit_time = now

                if settings["sound_on"]:
                    pygame.mixer.Sound('files/damage.mp3').play()

        if HP <= 0:
            if settings["sound_on"]:
                pygame.mixer.Sound('files/crash.mp3').play()
            time.sleep(0.5)

            final_score = int(COIN_SCORE * 10 + distance_traveled + power_ups)
            save_score(player_name, final_score, distance_traveled)
                        
            DISPLAYSURF.fill(RED)
            DISPLAYSURF.blit(game_over, (30,250))
            
            pygame.display.update()
            for entity in all_sprites:
                    entity.kill() 
            time.sleep(2)
            pygame.quit()
            sys.exit()

        if pygame.time.get_ticks() > slow_until:
            P_SPEED = 5
        hit_obstacle = pygame.sprite.spritecollideany(P1, obstacles)
        if hit_obstacle and hit_obstacle.active:
            if hit_obstacle.type == "obstacle":
                if settings["sound_on"]:
                    pygame.mixer.Sound('files/damage.mp3').play()
                if HP_s:
                    HP_s-=1
                else:
                    HP -= 1
            elif hit_obstacle.type == "oil_spill":
                if settings["sound_on"]:
                    pygame.mixer.Sound('files/slow_down.mp3').play()
                P_SPEED = 2
                slow_until = pygame.time.get_ticks() + 3000
            elif hit_obstacle.type == "nitro":
                power_ups += 10
                if settings["sound_on"]:
                    pygame.mixer.Sound('files/nitro_sound.mp3').play()
                P_SPEED = 8
                slow_until = pygame.time.get_ticks() + 3000
            elif hit_obstacle.type == "repair":
                power_ups += 10
                if now - last_hit_time_repair > damage_cooldown:
                    HP += 1
                    last_hit_time_repair = now

                    if settings["sound_on"]:
                        pygame.mixer.Sound('files/nitro_sound.mp3').play()
            elif hit_obstacle.type == "shield":
                power_ups += 10
                if now - last_hit_time_repair > damage_cooldown:
                    HP_s += 1
                    last_hit_time_repair = now

                    if settings["sound_on"]:
                        pygame.mixer.Sound('files/nitro_sound.mp3').play()

            hit_obstacle.active = False
            hit_obstacle.rect.center = (-200, -200)

        hit_coin = pygame.sprite.spritecollideany(P1, coins)
        if hit_coin and hit_coin.active:
            if settings["sound_on"]:
                pygame.mixer.Sound('files/coinsound.mp3').play()

            COIN_SCORE += hit_coin.score
            coin_counter += 1

            hit_coin.active = False
            hit_coin.rect.center = (-300,-300)

            new_coin = random.choice(
                [Bronze,Bronze,Bronze,Bronze,Bronze,Bronze,Bronze,
                Silver,Silver,Silver,
                Gold]
            )

            new_coin.active = True
            new_coin.spawn()

        # blit hearts
        for i in range(HP):
            DISPLAYSURF.blit(heart, (10*i,0))

        pygame.display.update()
        FramePerSec.tick(FPS)