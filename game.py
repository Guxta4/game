def start_fight(choice_dict):
    import pygame
    import sys

    pygame.init()
    WIDTH, HEIGHT = 800, 400
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Luta de quem é pior!")

    bg = pygame.image.load("assets/bg.png")
    bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

    font = pygame.font.SysFont("Arial", 24)
    clock = pygame.time.Clock()

    # Carrega sprites
    p1_idle = pygame.transform.scale(pygame.image.load(choice_dict["p1"]["idle"]), (100, 100))
    p1_punch = pygame.transform.scale(pygame.image.load(choice_dict["p1"]["punch"]), (100, 100))
    p2_idle = pygame.transform.scale(pygame.image.load(choice_dict["p2"]["idle"]), (100, 100))
    p2_punch = pygame.transform.scale(pygame.image.load(choice_dict["p2"]["punch"]), (100, 100))

    nome_p1 = choice_dict["p1"].get("nome", "Player 1")
    nome_p2 = choice_dict["p2"].get("nome", "Player 2")

    # Placar
    placar1 = 0
    placar2 = 0
    round_num = 1

    while placar1 < 2 and placar2 < 2:
        # Mostrar número do round
        win.blit(bg, (0, 0))
        texto_round = font.render(f"Round {round_num}", True, (0, 0, 0))
        win.blit(texto_round, (WIDTH // 2 - texto_round.get_width() // 2, HEIGHT // 2))
        pygame.display.update()
        pygame.time.delay(1500)

        # Reset de posições e vidas
        p1 = pygame.Rect(100, 250, 100, 100)
        p2 = pygame.Rect(600, 250, 100, 100)
        vida1 = 100
        vida2 = 100
        is_p1_hit = False
        is_p2_hit = False
        punch_timer = 0

        round_ativo = True

        while round_ativo:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Controles
            keys = pygame.key.get_pressed()
            vel = 5
            if keys[pygame.K_a]: p1.x -= vel
            if keys[pygame.K_d]: p1.x += vel
            if keys[pygame.K_w]:
                is_p1_hit = True
                punch_timer = 10
                if p1.colliderect(p2): vida2 -= 1

            if keys[pygame.K_LEFT]: p2.x -= vel
            if keys[pygame.K_RIGHT]: p2.x += vel
            if keys[pygame.K_UP]:
                is_p2_hit = True
                punch_timer = 10
                if p2.colliderect(p1): vida1 -= 1

            # Limites
            p1.x = max(0, min(p1.x, WIDTH - p1.width))
            p2.x = max(0, min(p2.x, WIDTH - p2.width))

            win.blit(bg, (0, 0))

            # Desenhar personagens
            win.blit(p1_punch if is_p1_hit else p1_idle, (p1.x, p1.y))
            win.blit(p2_punch if is_p2_hit else p2_idle, (p2.x, p2.y))

            # Nomes
            nome1_texto = font.render(nome_p1, True, (0, 0, 0))
            nome2_texto = font.render(nome_p2, True, (0, 0, 0))
            win.blit(nome1_texto, (p1.x + 50 - nome1_texto.get_width() // 2, p1.y - 25))
            win.blit(nome2_texto, (p2.x + 50 - nome2_texto.get_width() // 2, p2.y - 25))

            # Vidas
            pygame.draw.rect(win, (255, 0, 0), (50, 30, vida1 * 2, 20))
            pygame.draw.rect(win, (0, 0, 255), (WIDTH - 250, 30, vida2 * 2, 20))

            # Placar
            placar_texto = font.render(f"{placar1} x {placar2}", True, (0, 0, 0))
            win.blit(placar_texto, (WIDTH // 2 - placar_texto.get_width() // 2, 10))

            # Ataque temporizado
            if punch_timer > 0:
                punch_timer -= 1
            else:
                is_p1_hit = False
                is_p2_hit = False

            # Vitória no round
            if vida1 <= 0 or vida2 <= 0:
                round_ativo = False
                vencedor_round = "Player 1 venceu o round!" if vida2 <= 0 else "Player 2 venceu o round!"
                if vida2 <= 0: placar1 += 1
                else: placar2 += 1
                texto = font.render(vencedor_round, True, (0, 0, 0))
                win.blit(texto, (WIDTH // 2 - texto.get_width() // 2, HEIGHT // 2))
                pygame.display.update()
                pygame.time.delay(2000)

            pygame.display.update()

        round_num += 1

    # Vitória final
    win.blit(bg, (0, 0))
    vencedor = "Player 1 venceu a luta!" if placar1 == 2 else "Player 2 venceu a luta!"
    texto = font.render(vencedor, True, (0, 0, 0))
    win.blit(texto, (WIDTH // 2 - texto.get_width() // 2, HEIGHT // 2))
    pygame.display.update()
    pygame.time.delay(3000)
    pygame.quit()
    sys.exit()
