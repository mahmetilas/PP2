from coloures import *
from collections import deque
import pygame
import math

def color_change(color_mode):
    if color_mode == 'red':
        color = RED
    elif color_mode == 'orange':
        color = ORANGE
    elif color_mode == 'yellow':
        color = YELLOW
    elif color_mode == 'light_green':
        color = LIGHT_GREEN
    elif color_mode == 'green':
        color = GREEN
    elif color_mode == 'neon_green':
        color = NEON_GREEN
    elif color_mode == 'cyan':
        color = CYAN
    elif color_mode == 'light_blue':
        color = LIGHT_BLUE
    elif color_mode == 'blue':
        color = BLUE
    elif color_mode == 'violet':
        color = VIOLET
    elif color_mode == 'pink':
        color = PINK
    elif color_mode == 'magnenta':
        color = MAGENTA
    elif color_mode == 'white':
        color = WHITE
    elif color_mode == 'black':
        color = BLACK
    elif color_mode == 'eraser':
        color = (96,96,96)
    return color

def draw_brush(surface, color, start, end, size):
    pygame.draw.line(surface, color, start, end, size *2)
    pygame.draw.circle(surface, color, end, size)

def draw_line(surface, color, start, end, size):
    pygame.draw.line(surface, color, start, end, size *2)

def draw_rectangle(surface, current_color, start_pos, end_pos, width=2):
    x1, y1 = start_pos
    x2, y2 = end_pos

    x = min(x1, x2)
    y = min(y1, y2)
    w = abs(x2 - x1)
    h = abs(y2 - y1)

    pygame.draw.rect(surface, current_color, (x, y, w, h), width*2)

def draw_square(surface, color, start, end, width=2):
    x1, y1 = start
    x2, y2 = end
    side = min(abs(x2 - x1), abs(y2 - y1))
    rect = pygame.Rect(x1, y1, side if x2 >= x1 else -side, side if y2 >= y1 else -side)
    pygame.draw.rect(surface, color, rect, width)

def draw_ellipse(surface, color, start, end, width=2):
    x = min(start[0], end[0])
    y = min(start[1], end[1])
    w = abs(start[0] - end[0])
    h = abs(start[1] - end[1])

    if w > 0 and h > 0:
        pygame.draw.ellipse(surface, color, (x, y, w, h), width*2)

def draw_equilateral_triangle(screen, color, start, end, width=2):
    x1, y1 = start
    side = abs(end[0] - x1)
    height = side * math.sqrt(3) / 2
    points = [(x1, y1), (x1 + side, y1), (x1 + side / 2, y1 - height)]
    pygame.draw.polygon(screen, color, points, width*2)

def draw_rhombus(screen, color, start, end, width=2):
    x1, y1 = start
    x2, y2 = end
    cx, cy = (x1 + x2) / 2, (y1 + y2) / 2
    points = [(cx, y1), (x2, cy), (cx, y2), (x1, cy)]
    pygame.draw.polygon(screen, color, points, width*2)

def draw_triangle(screen, color, start, end, width=2):
    pygame.draw.polygon(screen, color,[(start[0], start[1]),(start[0],end[1]),(end[0],end[1])], width*2)

def flood_fill(surface, start_pos, fill_color):
    w, h = surface.get_size()
    x, y = start_pos

    if not (0 <= x < w and 0 <= y < h):
        return

    target_color = surface.get_at((x, y))
    fill_color = pygame.Color(*fill_color)

    if target_color == fill_color:
        return

    queue = deque()
    queue.append((x, y))

    while queue:
        px, py = queue.popleft()

        if not (0 <= px < w and 0 <= py < h):
            continue

        if surface.get_at((px, py)) != target_color:
            continue

        surface.set_at((px, py), fill_color)

        queue.append((px + 1, py))
        queue.append((px - 1, py))
        queue.append((px, py + 1))
        queue.append((px, py - 1))