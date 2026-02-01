import pygame
import sys

# REUSABLE BUTTON CLASS
class Button:
    def __init__(self, x, y, width, height, text, target, color=(167, 215, 232)):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.target = target
        self.base_color = color
        self.font = pygame.font.SysFont("Arial", 30)

    def draw(self, screen):
        # Hover Effect
        mouse_pos = pygame.mouse.get_pos()
        color = (184, 213, 179) if self.rect.collidepoint(mouse_pos) else self.base_color
        
        pygame.draw.rect(screen, color, self.rect, border_radius=12)
        pygame.draw.rect(screen, (99, 66, 46), self.rect, 3, border_radius=12)
        
        txt_surface = self.font.render(self.text, True, (99, 66, 46))
        txt_rect = txt_surface.get_rect(center=self.rect.center)
        screen.blit(txt_surface, txt_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.rect.collidepoint(event.pos)
        return False

# --- GAME STATES ---

class MainMenu:
    def __init__(self):
        # Main buttons
        self.btn_start = Button(300, 200, 200, 60, "START", "SELECTOR")
        self.btn_exit = Button(300, 300, 200, 60, "EXIT", "EXIT", color=(242, 177, 177))

    def handle_events(self, events):
        for e in events:
            if self.btn_start.is_clicked(e): return "SELECTOR"
            if self.btn_exit.is_clicked(e): return "EXIT"
        return "MAIN_MENU"

    def draw(self, screen):
        screen.fill((212, 241, 244)) 
        self.btn_start.draw(screen)
        self.btn_exit.draw(screen)

class LevelSelector:
    def __init__(self):
        self.buttons = []
        for i in range(5):
            x = 100 + (i * 125)
            self.buttons.append(Button(x, 250, 100, 100, f"{i+1}", f"LEVEL {i+1}"))
        self.btn_back = Button(20, 20, 100, 40, "Back", "MAIN_MENU")

    def handle_events(self, events):
        for e in events:
            if self.btn_back.is_clicked(e): return "MAIN_MENU"
            for b in self.buttons:
                if b.is_clicked(e): return b.target
        return "SELECTOR"

    def draw(self, screen):
        screen.fill((225, 238, 221))
        self.btn_back.draw(screen)
        for b in self.buttons:
            b.draw(screen)

class Level:
    def __init__(self, num):
        self.num = num
        self.font = pygame.font.SysFont("Arial", 40)

    def handle_events(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_m: return "SELECTOR"
                if e.key == pygame.K_p: return "GAME_OVER" 
        return f"LEVEL {self.num}"

    def draw(self, screen):
        screen.fill((255, 255, 255))
        txt = self.font.render(f"PLAYING LEVEL {self.num}", True, (50, 50, 50))
        hint = self.font.render("'P' to Finish | 'M' to Go Back", True, (150, 150, 150))
        screen.blit(txt, (250, 200))
        screen.blit(hint, (180, 300))

class GameOver:
    def __init__(self):
        self.btn_restart = Button(300, 300, 200, 60, "MENU", "MAIN_MENU")

    def handle_events(self, events):
        for e in events:
            if self.btn_restart.is_clicked(e): return "MAIN_MENU"
        return "GAME_OVER"

    def draw(self, screen):
        screen.fill((242, 177, 177))
        font = pygame.font.SysFont("Arial", 50)
        txt = font.render("LEVEL COMPLETED!", True, (99, 66, 46))
        screen.blit(txt, (200, 150))
        self.btn_restart.draw(screen)

# --- CENTRAL MANAGER ---

class Manager:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Level System")
        self.states = {
            "MAIN_MENU": MainMenu(),
            "SELECTOR": LevelSelector(),
            "LEVEL 1": Level(1),
            "LEVEL 2": Level(2),
            "LEVEL 3": Level(3),
            "LEVEL 4": Level(4),
            "LEVEL 5": Level(5),
            "GAME_OVER": GameOver()
        }
        self.current_state = "MAIN_MENU"

    def run(self):
        clock = pygame.time.Clock()
        while True:
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            new_state = self.states[self.current_state].handle_events(events)
            
            if new_state == "EXIT":
                pygame.quit()
                sys.exit()
                
            self.current_state = new_state
            self.states[self.current_state].draw(self.screen)
            pygame.display.flip()
            clock.tick(60)

if __name__ == "__main__":
    Manager().run()