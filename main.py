import pygame, sys, selecao_personagem

pygame.init()
WIDTH, HEIGHT = 800, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Street Fighter ‑ Menu")

# Fundo
bg = pygame.image.load("assets/bg.png")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

# Estilo de botão
FONT = pygame.font.SysFont("Arial", 40)
GRAY, RED, BLACK = (200, 200, 200), (255, 0, 0), (0, 0, 0)

def draw_button(text, rect, mouse):
    color = RED if rect.collidepoint(mouse) else GRAY
    pygame.draw.rect(win, color, rect)
    pygame.draw.rect(win, BLACK, rect, 2)
    label = FONT.render(text, True, BLACK)
    win.blit(label, (rect.x + (rect.w - label.get_width()) // 2,
                     rect.y + (rect.h - label.get_height()) // 2))

def main_menu():
    play_rect = pygame.Rect(300, 150, 200, 60)
    exit_rect = pygame.Rect(300, 250, 200, 60)

    while True:
        mouse = pygame.mouse.get_pos()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(mouse):
                    pygame.mixer.music.stop()
                    selecao_personagem.start_selection()   # → vai para seleção
                if exit_rect.collidepoint(mouse):
                    pygame.quit(); sys.exit()

        win.blit(bg, (0, 0))
        title = FONT.render("Street Fighter", True, BLACK)
        win.blit(title, (WIDTH//2 - title.get_width()//2, 40))

        draw_button("Jogar", play_rect, mouse)
        draw_button("Sair",  exit_rect, mouse)
        pygame.display.update()

if __name__ == "__main__":
    main_menu()
