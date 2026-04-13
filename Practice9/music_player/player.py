import pygame
import os
from mutagen.mp3 import MP3

pygame.mixer.init()
pygame.init()

music_folder = r'C:\Users\mahme\.vscode\PP2\Practice9\music_player\music'
songs = [os.path.join(music_folder, f) for f in os.listdir(music_folder) 
         if f.endswith(('.mp3', '.wav'))]

if not songs:
    print("No .mp3 or .wav files found in", music_folder)
    pygame.quit()
    exit()

screen = pygame.display.set_mode((1440, 720))
clock = pygame.time.Clock()
done = True

font = pygame.font.SysFont("comicsansms", 72)

count = 0

def next_s(count, songs):
    if count + 1 == len(songs):
        count = 0
    else: count+=1
    return count
def prev_s(count, songs):
    if count == 0:
        count = len(songs) - 1
    else: count-=1
    return count
def get_duration(path):
    return MP3(path).info.length
while done:
    pos = pygame.mixer.music.get_pos()
    length = get_duration(songs[count])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                pygame.mixer.music.pause()
            if event.key == pygame.K_p:
                if pos>=0:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.load(songs[count])
                    pygame.mixer.music.play()
            if event.key == pygame.K_n:
                count = next_s(count, songs)
                pygame.mixer.music.load(songs[count])
                pygame.mixer.music.play()
            if event.key == pygame.K_b:
                if pos > 3000:
                    pygame.mixer.music.load(songs[count])
                    pygame.mixer.music.play()
                else:
                    count = prev_s(count, songs)
                    pygame.mixer.music.load(songs[count])
                    pygame.mixer.music.play()

    text = font.render(f"{(songs[count])[56:-4]}", True, (188, 86, 86))
    screen.fill((255, 242, 242))
    screen.blit(text,
        (720 - text.get_width() // 2, 360 - text.get_height() // 2))
    pygame.draw.line(screen, (240, 220, 220), (40, 600), (1400, 600), 20)
    pygame.draw.circle(screen, (94,52,52), (40+13.6*(pos/length)*0.1,600), 15)

    pygame.display.flip()
    clock.tick(10)