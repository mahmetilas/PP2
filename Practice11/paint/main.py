import pygame, datetime
from functions import *
from general import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((1200, 720))
    canvas = pygame.Surface((1200,600))
    canvas.fill((96,96,96))

    clock = pygame.time.Clock()

    current_color_name = 'blue'
    mode = 'rectangle'

    drawing = False
    end_pos = None
    last_pos = None
    start_pos = None
    brush_size = 1

    # TEXT TOOL
    font = pygame.font.SysFont(None, 32)
    typing = False
    text_string = ""
    text_pos = (0,0)

    while True:
        current_color = color_change(current_color_name)
        pressed = pygame.key.get_pressed()

        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    for entity in all_colores:
                        if entity.rect.collidepoint(event.pos):
                            current_color_name = entity.name

                    for entity in all_objects:
                        if entity.rect.collidepoint(event.pos):

                            if entity == rectangle:
                                mode = rectangle.name
                            elif entity == ellipse:
                                mode = ellipse.name
                            elif entity == square:
                                mode = square.name
                            elif entity == equilateral_triangle:
                                mode = equilateral_triangle.name
                            elif entity == rhombus:
                                mode = rhombus.name
                            elif entity == triangle:
                                mode = triangle.name
                            elif entity == pencil:
                                mode = pencil.name
                            elif entity == line:
                                mode = line.name
                            elif entity == flood_fill_tool:
                                mode = flood_fill_tool.name
                            elif entity == text_tool:
                                mode = text_tool.name
                            elif entity == plus:
                                brush_size += 1
                            elif entity == minus and brush_size > 1:
                                brush_size -= 1

                    # flood fill
                    if mode == "flood_fill":
                        flood_fill(canvas, event.pos, current_color)

                    # text
                    elif mode == "text":
                        typing = True
                        text_string = ""
                        text_pos = event.pos

                    else:
                        last_pos = event.pos
                        start_pos = event.pos
                        drawing = True

            if event.type == pygame.MOUSEMOTION:
                if drawing and mode == "pencil":
                    current_pos = event.pos
                    draw_brush(canvas, current_color, last_pos, current_pos, brush_size)
                    last_pos = current_pos

            if event.type == pygame.MOUSEBUTTONUP and start_pos:
                if drawing:
                    end_pos = event.pos

                    if mode == "rectangle":
                        draw_rectangle(canvas, current_color, start_pos, end_pos, brush_size)

                    elif mode == "square":
                        draw_square(canvas, current_color, start_pos, end_pos, brush_size)

                    elif mode == "ellipse":
                        draw_ellipse(canvas, current_color, start_pos, end_pos, brush_size)

                    elif mode == "equilateral_triangle":
                        draw_equilateral_triangle(canvas, current_color, start_pos, end_pos, brush_size)

                    elif mode == "rhombus":
                        draw_rhombus(canvas, current_color, start_pos, end_pos, brush_size)

                    elif mode == "triangle":
                        draw_triangle(canvas, current_color, start_pos, end_pos, brush_size)

                    elif mode == "line":
                        draw_line(canvas, current_color, start_pos, end_pos, brush_size)

                start_pos = None
                drawing = False
                end_pos = None
                last_pos = None

            if event.type == pygame.KEYDOWN:

                if typing:
                    if event.key == pygame.K_RETURN:
                        txt = font.render(text_string, True, current_color)
                        canvas.blit(txt, text_pos)
                        typing = False

                    elif event.key == pygame.K_ESCAPE:
                        typing = False

                    elif event.key == pygame.K_BACKSPACE:
                        text_string = text_string[:-1]

                    else:
                        text_string += event.unicode

                else:
                    if event.key == pygame.K_s and ctrl_held:
                        filename = datetime.datetime.now().strftime('%d.%m.%Y_%H-%M-%S')
                        pygame.image.save(canvas, f"{filename}.png")

                    if event.key == pygame.K_w and ctrl_held:
                        return

                    if event.key == pygame.K_F4 and alt_held:
                        return

                    if event.key == pygame.K_ESCAPE:
                        return

            if event.type == pygame.QUIT:
                return

        screen.fill((80,80,80))
        screen.blit(canvas, (0,0))

        if drawing and mode == "line" and start_pos:
            mouse_pos = pygame.mouse.get_pos()
            pygame.draw.line(screen, current_color, start_pos, mouse_pos, brush_size * 2)

        for entity in all_sprites:
            screen.blit(entity.image, entity.rect)

        if typing:
            preview = font.render(text_string, True, current_color)
            screen.blit(preview, text_pos)

        pygame.display.flip()
        clock.tick(60)

main()