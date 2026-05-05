from connect import *
from pygame.locals import *
import random, pygame, sys, pygame_menu

pygame.init()
FPS = 8
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 20
assert WINDOWWIDTH % CELLSIZE == 0
assert WINDOWHEIGHT % CELLSIZE == 0
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (236,   114,   114)
GREEN     = ( 40,  153,  76)
DARKGREEN = (  0, 102,   51)
DARKGRAY  = ( 32,  32,  32)
POISONCOLOR = (120, 0, 0)
BLUE = (80, 170, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BGCOLOR = BLACK
APPLECOLORES = {1:(113, 235, 52),2:(235, 226, 52),3:(235, 83, 52)}

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0

def start_the_game():
    global player_name, PERSONAL_BEST
    player_name = name_input.get_value()
    PERSONAL_BEST = get_personal_best(player_name)
    main() 
    return


def draw_best():
    bestSurf = BASICFONT.render(f'Best: {PERSONAL_BEST}', True, WHITE)
    bestRect = bestSurf.get_rect()
    bestRect.topleft = (250, 10)
    DISPLAYSURF.blit(bestSurf, bestRect)


def name_menu():
    surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    menu = pygame_menu.Menu('Enter', 400, 300)

    global name_input
    name_input = menu.add.text_input('Login: ', default='Iliyas')
    menu.add.button('Play', start_the_game)
    menu.add.button('Exit', pygame_menu.events.EXIT)

    menu.mainloop(surface)

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Snake')

    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()
        showLeaderboard()

def drawPoison(poison):
    x = poison["pos"]["x"] * CELLSIZE
    y = poison["pos"]["y"] * CELLSIZE

    rect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, POISONCOLOR, rect)

def increse_speed(fps, score):
    fps = fps + int(score/3*2)
    return fps

def runGame():
    # Set a random start point.
    startx = random.randint(5, CELLWIDTH - 6)
    starty = random.randint(5, CELLHEIGHT - 6)
    snakeCoords = [{'x': startx,     'y': starty},
                  {'x': startx - 1, 'y': starty},
                  {'x': startx - 2, 'y': starty}]
    direction = RIGHT

    # Start the apple in a random place.
    apple = getSafeLocation(snakeCoords)

    food = {
        "pos": apple,
        "weight": random.choice([1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3]),
        "ttl_ms": random.choice([4000, 7000, 10000]),
        "spawn_time": pygame.time.get_ticks()
    }
    poison = {
        "pos": getSafeLocation(snakeCoords),
        "spawn_time": pygame.time.get_ticks(),
        "ttl_ms": 6000
    }
    powerup = None
    active_effect = None
    effect_end_time = 0
    shield = False

    while True: # main game loop
        global SCORE, LEVEL
        SCORE =  len(snakeCoords) - 3
        LEVEL = int((len(snakeCoords) - 3)/4)+1
        now = pygame.time.get_ticks()

        # spawn power-up
        if powerup is None and random.randint(1, 180) == 1:
            powerup = {
                "type": random.choice(["speed", "slow", "shield"]),
                "pos": getSafeLocation(snakeCoords),
                "spawn_time": now
            }

        # del after 8 sec
        if powerup and now - powerup["spawn_time"] > 8000:
            powerup = None
            
        if now - poison["spawn_time"] > poison["ttl_ms"]:
            poison = {
                "pos": getSafeLocation(snakeCoords),
                "spawn_time": pygame.time.get_ticks(),
                "ttl_ms": random.choice([5000, 7000, 9000])
            }

        if powerup:
            if snakeCoords[HEAD]['x'] == powerup['pos']['x'] and snakeCoords[HEAD]['y'] == powerup['pos']['y']:

                if powerup["type"] == "speed":
                    active_effect = "speed"
                    effect_end_time = now + 5000

                elif powerup["type"] == "slow":
                    active_effect = "slow"
                    effect_end_time = now + 5000

                elif powerup["type"] == "shield":
                    shield = True

                powerup = None

        if active_effect and now > effect_end_time:
            active_effect = None

        if now - food["spawn_time"] > food["ttl_ms"]:
            apple = getSafeLocation(snakeCoords)

            food = {
                "pos": apple,
                "weight": random.choice([1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3]),
                "ttl_ms": random.choice([4000, 7000, 10000]),
                "spawn_time": pygame.time.get_ticks()
            }

        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    terminate()

        # check if the worm has hit itself or the edge
        hit_wall = (
            snakeCoords[HEAD]['x'] == -1 or
            snakeCoords[HEAD]['x'] == CELLWIDTH or
            snakeCoords[HEAD]['y'] == -1 or
            snakeCoords[HEAD]['y'] == CELLHEIGHT
        )

        if hit_wall:
            if shield:
                shield = False

                if snakeCoords[HEAD]['x'] < 0:
                    snakeCoords[HEAD]['x'] = 0
                if snakeCoords[HEAD]['x'] >= CELLWIDTH:
                    snakeCoords[HEAD]['x'] = CELLWIDTH - 1
                if snakeCoords[HEAD]['y'] < 0:
                    snakeCoords[HEAD]['y'] = 0
                if snakeCoords[HEAD]['y'] >= CELLHEIGHT:
                    snakeCoords[HEAD]['y'] = CELLHEIGHT - 1
            else:
                save_or_update(player_name, SCORE, LEVEL)
                return
        
        if snakeCoords[HEAD]['x'] == poison['pos']['x'] and snakeCoords[HEAD]['y'] == poison['pos']['y']:

            for _ in range(2):
                if len(snakeCoords) > 1:
                    snakeCoords.pop()

            if len(snakeCoords) <= 1:
                save_or_update(player_name, SCORE, LEVEL)
                return

            poison = {
                "pos": getSafeLocation(snakeCoords),
                "spawn_time": pygame.time.get_ticks(),
                "ttl_ms": random.choice([5000, 7000, 9000])
            }

        for wormBody in snakeCoords[1:]:
            if wormBody['x'] == snakeCoords[HEAD]['x'] and wormBody['y'] == snakeCoords[HEAD]['y']:

                if shield:
                    shield = False
                    break
                else:
                    save_or_update(player_name, SCORE, LEVEL)
                    return

        # check if worm has eaten an apply
        if snakeCoords[HEAD]['x'] == apple['x'] and snakeCoords[HEAD]['y'] == apple['y']:
            # don't remove worm's tail segment
            apple = getSafeLocation(snakeCoords) # set a new apple somewhere
            grow = food['weight'] - 1
            for _ in range(grow):
                snakeCoords.append(snakeCoords[-1].copy())
            food = {
                    "pos": apple,
                    "weight": random.choice([1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3]),
                    "ttl_ms": random.choice([4000, 7000, 10000]),
                    "spawn_time": pygame.time.get_ticks()
                }

        else:
            del snakeCoords[-1] # remove worm's tail segment

        # move the worm by adding a segment in the direction it is moving
        if direction == UP:
            newHead = {'x': snakeCoords[HEAD]['x'], 'y': snakeCoords[HEAD]['y'] - 1}
        elif direction == DOWN:
            newHead = {'x': snakeCoords[HEAD]['x'], 'y': snakeCoords[HEAD]['y'] + 1}
        elif direction == LEFT:
            newHead = {'x': snakeCoords[HEAD]['x'] - 1, 'y': snakeCoords[HEAD]['y']}
        elif direction == RIGHT:
            newHead = {'x': snakeCoords[HEAD]['x'] + 1, 'y': snakeCoords[HEAD]['y']}
        snakeCoords.insert(0, newHead)
        DISPLAYSURF.fill(BGCOLOR)
        drawGrid()
        drawWorm(snakeCoords)
        drawApple(food)
        drawPoison(poison)
        drawPowerup(powerup)
        drawScore(SCORE)
        draw_level(LEVEL)
        draw_best()
        pygame.display.update()
        speed = increse_speed(FPS, SCORE)

        if active_effect == "speed":
            speed += 5

        elif active_effect == "slow":
            speed = max(4, speed - 4)

        FPSCLOCK.tick(speed)


def drawPowerup(powerup):
    if not powerup:
        return

    x = powerup["pos"]["x"] * CELLSIZE
    y = powerup["pos"]["y"] * CELLSIZE

    rect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)

    if powerup["type"] == "speed":
        color = BLUE
    elif powerup["type"] == "slow":
        color = YELLOW
    else:
        color = CYAN

    pygame.draw.rect(DISPLAYSURF, color, rect)


def getSafeLocation(snakeCoords):
    while True:
        loc = getRandomLocation()

        if loc not in snakeCoords:
            return loc

def showLeaderboard():
    leaders = get_top_10_scores()

    while True:
        DISPLAYSURF.fill(BGCOLOR)

        title = BASICFONT.render("TOP 10 SCORES", True, WHITE)
        DISPLAYSURF.blit(title, (220, 30))

        y = 80
        rank = 1

        for name, score in leaders:
            text = BASICFONT.render(f"{rank}. {name} - {score}", True, WHITE)
            DISPLAYSURF.blit(text, (180, y))
            y += 30
            rank += 1

        drawPressKeyMsg()

        if checkForKeyPress():
            pygame.event.get()
            return

        pygame.display.update()
        FPSCLOCK.tick(15)


def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press a key to play.', True, DARKGRAY)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)


def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key


def showStartScreen():
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    titleSurf1 = titleFont.render(f'HELLO {player_name}!', True, WHITE, DARKGREEN)

    degrees1 = 0
    degrees2 = 0
    while True:
        DISPLAYSURF.fill(BGCOLOR)
        Rect1 = titleSurf1.get_rect()
        Rect1.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(titleSurf1, Rect1)

        drawPressKeyMsg()

        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return
        pygame.display.update()
        FPSCLOCK.tick(15)
        degrees1 += 3 # rotate by 3 degrees each frame
        degrees2 += 7 # rotate by 7 degrees each frame


def terminate():
    save_or_update(player_name, SCORE, LEVEL)
    pygame.quit()
    sys.exit()


def getRandomLocation():
    return {'x': random.randint(0, CELLWIDTH - 1), 'y': random.randint(0, CELLHEIGHT - 1)}


def showGameOverScreen():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
    gameSurf = gameOverFont.render('Game', True, WHITE)
    overSurf = gameOverFont.render('Over', True, WHITE)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH / 2, 10)
    overRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 10 + 25)

    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress() # clear out any key presses in the event queue

    while True:
        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return

def draw_level(level):
    levelSurf = BASICFONT.render('Level: %s' % (level), True, WHITE)
    levelRect = levelSurf.get_rect()
    levelRect.topleft = (50,10)
    DISPLAYSURF.blit(levelSurf, levelRect)

def drawScore(score):
    scoreSurf = BASICFONT.render('Score: %s' % (score), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 120, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)


def drawWorm(wormCoords):
    for coord in wormCoords:
        x = coord['x'] * CELLSIZE
        y = coord['y'] * CELLSIZE
        wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, DARKGREEN, wormSegmentRect)
        wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
        pygame.draw.rect(DISPLAYSURF, GREEN, wormInnerSegmentRect)


def drawApple(food):
    x = food["pos"]["x"] * CELLSIZE
    y = food["pos"]["y"] * CELLSIZE
    appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, APPLECOLORES[food["weight"]], appleRect)


def drawGrid():
    for x in range(0, WINDOWWIDTH, CELLSIZE): # draw vertical lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, CELLSIZE): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))


if __name__ == '__main__':
    name_menu()