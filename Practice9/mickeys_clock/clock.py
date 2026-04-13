import pygame
import datetime
import os

pygame.init()
screen = pygame.display.set_mode((1200, 700))
WHITE = (255, 255, 255)

images = r'C:\Users\mahme\.vscode\PP2\Practice9\mickeys_clock\images'

clock_img = pygame.image.load(os.path.join(images, 'clck.png')).convert_alpha()
hand_l = pygame.image.load(os.path.join(images, 'hnd.png')).convert_alpha()  # seconds
hand_r = pygame.image.load(os.path.join(images, 'hnd.png')).convert_alpha()  # minutes

clock_img = pygame.transform.scale(clock_img, (800, 600))
hand_l_base = pygame.transform.scale(hand_l, (120, 240))
hand_r_base = pygame.transform.scale(hand_r, (100, 200))

CENTER = (600, 340)

clock = pygame.time.Clock()
done = False

last_second = -1  # чтобы обновлять раз в секунду

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    now = datetime.datetime.now()
    m = now.minute
    s = now.second

    # обнова только если секунда изменилась
    if s != last_second:
        last_second = s

        # углы
        seconds_angle = -s * 6
        minutes_angle = -(m * 6 + s * 0.1)  # плавное движение минут

        rotated_seconds = pygame.transform.rotate(hand_l_base, seconds_angle)
        rotated_minutes = pygame.transform.rotate(hand_r_base, minutes_angle)

        seconds_rect = rotated_seconds.get_rect(center=CENTER)
        minutes_rect = rotated_minutes.get_rect(center=CENTER)

    screen.fill(WHITE)

    clock_rect = clock_img.get_rect(center=CENTER)
    screen.blit(clock_img, clock_rect)

    screen.blit(rotated_minutes, minutes_rect)   # правая рука = минуты
    screen.blit(rotated_seconds, seconds_rect)   # левая рука = секунды

    pygame.display.flip()
    clock.tick(60)

pygame.quit()