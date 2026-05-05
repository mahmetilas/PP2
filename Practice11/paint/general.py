import pygame
from coloures import *
n = 30
class Objects(pygame.sprite.Sprite):
        def __init__(self, pos, name):
            super().__init__()
            self.image0 = pygame.image.load(f"images/{name}.png")
            self.image = pygame.transform.scale(self.image0, (60, 60))
            self.rect = self.image.get_rect()
            self.rect.center = pos
            self.name = name
# =================================
eraseri = Objects((n*10, 660),'eraser')
plus = Objects((n*13, 660),'plus')
minus = Objects((n*15, 660),'minus')
rectangle = Objects((n*18, 660),'rectangle')
square = Objects((n*20, 660),'square')
ellipse = Objects((n*22, 660),'ellipse')
rhombus = Objects((n*24, 660),'rhombus')
triangle = Objects((n*26, 660),'triangle')
equilateral_triangle = Objects((n*28, 660),'equilateral_triangle')
pencil = Objects((n*30, 660),'pencil')
line = Objects((n*32, 660),'line')
flood_fill_tool = Objects((n*34, 660), 'flood_fill')
text_tool = Objects((n*36, 660), 'text')
# =================================
all_objects = pygame.sprite.Group()
all_objects.add(flood_fill_tool)
all_objects.add(text_tool)
all_objects.add(pencil)
all_objects.add(line)
all_objects.add(eraseri)
all_objects.add(plus)
all_objects.add(minus)
all_objects.add(rectangle)
all_objects.add(square)
all_objects.add(ellipse)
all_objects.add(rhombus)
all_objects.add(triangle)
all_objects.add(equilateral_triangle)
# =================================
class Colour(pygame.sprite.Sprite):
    def __init__(self, pos, colour, name):
        super().__init__()
        self.image = pygame.Surface((30,30))
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.name = name
#==================================
red = Colour((n,650), RED, 'red')

orange = Colour((n*2,650), ORANGE,'orange')
yellow = Colour((n*3,650), YELLOW,'yellow')
light_green = Colour((n*4,650), LIGHT_GREEN,'light_green')

green = Colour((n*5,650), GREEN,'green')

neon_green = Colour((n*6,650), NEON_GREEN,'neon_green')
cyan = Colour((n*7,650), CYAN,'cyan')
light_blue = Colour((n,680),LIGHT_BLUE,'light_blue')

blue = Colour((n*2,680), BLUE,'blue')

violet = Colour((n*3,680), VIOLET,'violet')
pink = Colour((n*4,680), PINK,'pink')
magnenta = Colour((n*5,680), MAGENTA,'magnenta')

white = Colour((n*6,680), WHITE,'white')
black = Colour((n*7,680), BLACK,'black')
eraser = Colour((n*10, 680), (96,96,96),'eraser')
#==================================
all_colores = pygame.sprite.Group()
all_colores.add(red)
all_colores.add(orange)
all_colores.add(yellow)
all_colores.add(light_green)
all_colores.add(green)
all_colores.add(neon_green)
all_colores.add(cyan)
all_colores.add(light_blue)
all_colores.add(blue)
all_colores.add(violet)
all_colores.add(pink)
all_colores.add(magnenta)
all_colores.add(white)
all_colores.add(black)
all_colores.add(eraser)
all_sprites = pygame.sprite.Group()
all_sprites.add(red)
all_sprites.add(orange)
all_sprites.add(yellow)
all_sprites.add(light_green)
all_sprites.add(green)
all_sprites.add(neon_green)
all_sprites.add(cyan)
all_sprites.add(light_blue)
all_sprites.add(blue)
all_sprites.add(violet)
all_sprites.add(pink)
all_sprites.add(magnenta)
all_sprites.add(white)
all_sprites.add(black)
# =================================
all_sprites.add(pencil)
all_sprites.add(line)
all_sprites.add(eraser)
all_sprites.add(eraseri)
all_sprites.add(plus)
all_sprites.add(minus)
all_sprites.add(rectangle)
all_sprites.add(square)
all_sprites.add(ellipse)
all_sprites.add(rhombus)
all_sprites.add(triangle)
all_sprites.add(equilateral_triangle)
all_sprites.add(flood_fill_tool)
all_sprites.add(text_tool)