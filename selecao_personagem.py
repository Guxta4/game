import pygame, sys, json, game

def start_selection():
    pygame.init()
    WIDTH, HEIGHT = 800, 400
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Seleção de Personagens")

    # Fundo
    bg = pygame.image.load("assets/bg.png")
    bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

    # Lista de lutadores (adicione mais se quiser)
    chars = [
        {"idle": "assets/player1_idle.png", "punch": "assets/player1_punch.png"},
        {"idle": "assets/player2_idle.png", "punch": "assets/player2_punch.png"},
        {"idle": "assets/player3_idle.png", "punch": "assets/player3_punch.png"},
        {"idle": "assets/player4_idle.png", "punch": "assets/player4_punch.png"},
    ]

    # Carregar imagens reduzidas (cards 100×100)
    cards = [pygame.transform.scale(pygame.image.load(c["idle"]), (100,100))
             for c in chars]
    card_rects = [cards[i].get_rect(topleft=(150 + i*200, 200))
                  for i in range(len(cards))]

    FONT = pygame.font.SysFont("Arial", 28)
    turn, p1, p2 = 1, None, None
    clock = pygame.time.Clock()

    selecting = True
    while selecting:
        clock.tick(60)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                for i, r in enumerate(card_rects):
                    if r.collidepoint(e.pos):
                        if turn == 1:
                            p1 = i
                            turn = 2
                        elif turn == 2 and i != p1:
                            p2 = i
                            selecting = False

        win.blit(bg, (0,0))
        title = FONT.render("Selecione seu personagem", True, (0,0,0))
        win.blit(title, (WIDTH//2 - title.get_width()//2, 40))
        info  = FONT.render(f"Vez do Player {turn}", True, (0,0,0))
        win.blit(info, (WIDTH//2 - info.get_width()//2, 80))

        for i, r in enumerate(card_rects):
            win.blit(cards[i], r.topleft)
            pygame.draw.rect(win, (0,0,0), r, 2)
        pygame.display.update()

    # Salvar escolhas em memória e iniciar o jogo
    pygame.mixer.music.stop()
    choices = {"p1": chars[p1], "p2": chars[p2]}
    game.start_fight(choices)
