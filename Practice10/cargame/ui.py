import pygame
import json
import os
from cargame import run_game

# Инициализация
pygame.init()
player_name = "Player"
WIDTH, HEIGHT = 1200, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Game Menu")
pygame.mixer.Sound("files/music.mp3").play()
# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (50, 150, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)

# Шрифты
font = pygame.font.SysFont('Arial', 40)
small_font = pygame.font.SysFont('Arial', 30)

# Настройки игры (состояние)
settings = {
    "sound_on": True,
    "car_color": RED,
    "difficulty": "Easy"
}

class Button:
    def __init__(self, x, y, width, height, text, color, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.action = action

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=10)
        text_surf = font.render(self.text, True, WHITE)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

def main_menu():
    buttons = [
        Button(450, 200, 300, 60, "Play", BLUE, "name"),
        Button(450, 300, 300, 60, "Leaderboard", BLUE, "leaderboard"),
        Button(450, 400, 300, 60, "Settings", BLUE, "settings"),
        Button(450, 500, 300, 60, "Quit", RED, "quit")
    ]
    
    running = True
    while running:
        screen.fill(BLACK)
        title = font.render("MAIN MENU", True, WHITE)
        screen.blit(title, (WIDTH//2 - 100, 80))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                for btn in buttons:
                    if btn.is_clicked(event.pos):
                        return btn.action

        for btn in buttons:
            btn.draw(screen)
        
        pygame.display.flip()

def settings_screen():
    running = True
    while running:
        screen.fill(BLACK)
        
        # Заголовки
        title = font.render("SETTINGS", True, WHITE)
        screen.blit(title, (WIDTH//2 - 80, 50))

        # Отрисовка текущих настроек
        sound_text = f"Sound: {'ON' if settings['sound_on'] else 'OFF'}"
        diff_text = f"Difficulty: {settings['difficulty']}"
        
        # Кнопки настроек
        btn_sound = Button(450, 150, 300, 50, sound_text, GRAY)
        btn_color = Button(450, 250, 300, 50, "Change Color", settings['car_color'])
        btn_diff = Button(450, 350, 300, 50, diff_text, GRAY)
        btn_back = Button(450, 550, 300, 50, "Back to Menu", BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_sound.is_clicked(event.pos):
                    settings['sound_on'] = not settings['sound_on']
                if btn_color.is_clicked(event.pos):
                    # Переключение между Красным, Зеленым и Синим
                    colors = [RED, GREEN, BLUE]
                    current_idx = colors.index(settings['car_color'])
                    settings['car_color'] = colors[(current_idx + 1) % 3]
                if btn_diff.is_clicked(event.pos):
                    diffs = ["Easy", "Medium", "Hard"]
                    current_idx = diffs.index(settings['difficulty'])
                    settings['difficulty'] = diffs[(current_idx + 1) % 3]
                if btn_back.is_clicked(event.pos):
                    return "menu"

        btn_sound.draw(screen)
        btn_color.draw(screen)
        btn_diff.draw(screen)
        btn_back.draw(screen)
        
        pygame.display.flip()

def name_screen():
    global player_name

    input_text = ""
    running = True

    while running:
        screen.fill(BLACK)

        title = font.render("Enter Name", True, WHITE)
        screen.blit(title, (480, 150))

        box = pygame.Rect(400, 280, 400, 60)
        pygame.draw.rect(screen, WHITE, box, 2)

        txt = font.render(input_text, True, WHITE)
        screen.blit(txt, (box.x + 10, box.y + 10))

        info = small_font.render("Press ENTER to start", True, WHITE)
        screen.blit(info, (470, 380))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    player_name = input_text if input_text else "Player"
                    return "game"

                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]

                else:
                    if len(input_text) < 12:
                        input_text += event.unicode

        pygame.display.flip()


def leaderboard_screen():
    while True:
        screen.fill(BLACK)

        title = font.render("TOP 10", True, WHITE)
        screen.blit(title, (520, 50))

        if os.path.exists("leaderboard.json"):
            with open("leaderboard.json", "r") as f:
                data = json.load(f)
        else:
            data = []

        y = 150

        for i, row in enumerate(data):
            text = f"{i+1}. {row['name']} | Score: {row['score']} | {row['distance']}m"
            line = small_font.render(text, True, WHITE)
            screen.blit(line, (250, y))
            y += 40

        back = small_font.render("ESC = Back", True, WHITE)
        screen.blit(back, (20, 680))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "menu"

        pygame.display.flip()


# Основной цикл переключения экранов
current_state = "menu"
while current_state != "quit":
    if current_state == "menu":
        current_state = main_menu()
    elif current_state == "settings":
        current_state = settings_screen()
    elif current_state == "game":
        run_game(settings, player_name)
        current_state = "menu"
    elif current_state == "name":
        current_state = name_screen()
    elif current_state == "leaderboard":
        current_state = leaderboard_screen()


pygame.quit()